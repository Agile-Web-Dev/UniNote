import { resizeChatbox } from "../index.js";
import { connect } from "./connect.js";
import { join } from "./join.js";
import { receiveMessage } from "./receiveMessage.js";
import { sendMessage } from "./sendMessage.js";

export let socket;

const handleSend = (message) => {
  if (message.trim().length > 0) {
    const isCommand = message.startsWith("/");
    const intent = isCommand ? "command" : "message";
    sendMessage(message, intent);
    $("#chatbox").val("");
    resizeChatbox();
  }
};

export const setupSocketIO = () => {
  socket = io.connect(`${document.location.host}/chat`);
  socket.on("connect", connect);
  socket.on("join", join);
  socket.on("receiveMessage", receiveMessage);

  $("#chatbox").on("keypress", (e) => {
    const message = $("#chatbox").val();
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend(message);
    }
  });

  $("#send-button").on("click", () => {
    const message = $("#chatbox").val();
    handleSend(message);
  });
};
