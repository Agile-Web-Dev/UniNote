import { cacheAvatar } from "../../user.js";
import { socket } from "./index.js";

export const connect = () => {
  socket.emit("join", {});
  cacheAvatar("UniNote Bot")
};
