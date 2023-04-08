import { cacheAvatar } from "../../user.js";

export const join = (message) => {
  $("#chat-container").append(`<p>${message.name}</p>`);
  cacheAvatar(message.name);
};
