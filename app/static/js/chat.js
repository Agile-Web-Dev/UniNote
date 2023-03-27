
let socket;
$(document).ready(() => {
  socket = io.connect(`https://${document.location.host}/chat`);
  socket.on("connect", connect);

  socket.on("joined", joined)

  socket.on("receiveMessage", receiveMessage);

  $("#chatbox").keypress((e) => {
    if (e.which == 13) {
      sendMessage();
    }
    const container = $("#chat-container")
      container.scrollTop = container.scrollHeight;
  }
  );
});

const connect = () => {
  socket.emit("joined", {});
};

const joined = (message) => {
  $("#chat-container").append(`<p>${message.msg}</p>`);
};

const sendMessage = () => {
  const message = $("#chatbox").val();
  socket.emit("receive_message", { msg: message });
  $("#chatbox").val("");
}

const receiveMessage = (message) => {
  $("#chat-container").append(`<p>${message.msg}</p>`);
}