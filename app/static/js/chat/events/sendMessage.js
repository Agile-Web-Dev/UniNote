import { socket } from "./index.js";

export const sendMessage = (message) => {
  socket.emit("receive_message", { msg: message });
};
