export const receiveMessage = (message) => {
  const messageElem = document.createElement("p");
  messageElem.innerText = message.msg;

  $("#chat-container").append(messageElem);
};
