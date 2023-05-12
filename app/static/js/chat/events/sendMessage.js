import { socket } from "./index.js";

export const sendMessage = (message, intent) => {
  socket.emit("receive_message", { msg: message, intent });
};
