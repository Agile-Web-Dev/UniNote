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
    const messageElement = $(messageHtml).appendTo("#chat-scroll-window");
    messageElement
      .children("div.avatar-holder")
      .append(await getAvatar(message.name));

    messageElement.children("div").children(".name").text(message.name);
    const messageContainer = messageElement
      .children("div")
      .children(".message-content");
    $('<p class="mb-0"></p>').text(message.msg).appendTo(messageContainer);
    lastParentMessage = messageElement;
  } else {
    const messageContainer = lastParentMessage
      .children("div")
      .children(".message-content");
    $("<b></b>").appendTo(messageContainer);
    $('<p class="mb-0"></p>').text(message.msg).appendTo(messageContainer);
  }
  lastAuthor = message.name;
};
