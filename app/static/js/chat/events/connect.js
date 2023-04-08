import { socket } from "./index.js";

export const connect = () => {
  socket.emit("join", {});
};
