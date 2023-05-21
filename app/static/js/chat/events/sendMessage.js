import { socket } from "./index.js";

//send message to socket server for render
export const sendMessage = (message, intent) => {
  socket.emit("receive_message", { msg: message, intent });
};
