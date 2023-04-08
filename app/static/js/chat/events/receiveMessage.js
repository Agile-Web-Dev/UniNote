import { getAvatar } from "../../user.js";

const messageHtml = `
<div class="message d-flex gap-3">
  <div class="avatar-holder"></div>
  <div class="d-flex flex-column">
    <p class="name fw-bold mb-1"></p>
    <div class="message-content"></div>
  </div>
</div>`;

let lastParentMessage;
let lastAuthor = "";

export const receiveMessage = async (message) => {
  if (lastAuthor !== message.name) {
    const messageElement = $(messageHtml).appendTo("#chat-container");
    messageElement
      .children("div.avatar-holder")
      .append(await getAvatar(message.name));
    messageElement.children("div").children(".name").text(message.name);
    messageElement.children("div").children(".message-content").text(message.msg);
    lastParentMessage = messageElement;
  } else {
    lastParentMessage.children("div").children("div.message-content").append(`<br>${message.msg}`);
  }
  lastAuthor = message.name;
};
