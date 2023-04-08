import { connect } from "./connect.js";
import { join } from "./join.js";
import { receiveMessage } from "./receiveMessage.js";
import { sendMessage } from "./sendMessage.js";

export let socket;

export const setupSocketIO = () => {
  socket = io.connect(`${document.location.host}/chat`);
  socket.on("connect", connect);
  socket.on("join", join);
  socket.on("receiveMessage", receiveMessage);    

  $("#chatbox").on("keypress", (e) => {
    const message = $("#chatbox").val().trim();
    if (e.key === "Enter" && message.length > 0) {
      sendMessage(message);
      $("#chatbox").val("");
    }
  });
};