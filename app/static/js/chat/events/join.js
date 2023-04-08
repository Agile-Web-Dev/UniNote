import { cacheAvatar } from "../../user.js";

export const join = (message) => {
  $("#chat-container").append(`<p>${message.name} joined the chatroom</p>`);
  cacheAvatar(message.name);
};
