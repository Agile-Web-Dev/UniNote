import { cacheAvatar } from "../../user.js";
import { socket } from "./index.js";

//connecting chatGPT bot to server
export const connect = () => {
  socket.emit("join", {});
  cacheAvatar("UniNote Bot");
};
