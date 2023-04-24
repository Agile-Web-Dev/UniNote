import { cacheAvatar } from "../../user.js";

export const join = (message) => {
  $("#chat-scroll-window").append(`<p>${message.name} joined the chatroom</p>`);
  cacheAvatar(message.name);
  cacheAvatar("UniNote Bot")
};
