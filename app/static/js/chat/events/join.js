import { cacheAvatar } from "../../user.js";

//cache avatar of user who joined
export const join = (message) => {
  cacheAvatar(message.name);
};
