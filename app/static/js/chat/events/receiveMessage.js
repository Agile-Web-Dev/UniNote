import { getAvatar } from "../../user.js";

const messageHtml = `
<div class="message">
  <div class="avatar-holder"></div>
  <p class="name"></p>
  <div class="message-content"></div>
</div>`;

let lastParentMessage;
let lastAuthor = "";
export const receiveMessage = async (message) => {
  if (lastAuthor !== message.name) {
    const messageElement = $(messageHtml).appendTo("#chat-container");
    messageElement.children(".avatar-holder").append(await getAvatar(message.name));
    messageElement.children(".name").text(message.name);
    messageElement.children(".message-content").text(message.msg);
    lastParentMessage = messageElement;
  }
  else {
    lastParentMessage.children(".message-content").append(`<br>${message.msg}`);
  }
  lastAuthor = message.name;

};
