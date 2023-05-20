import { getAvatar } from "../../user.js";
import { receiveMessage } from "../events/receiveMessage.js";
const messageHtml = `
<div class="message d-flex gap-3">
  <div class="avatar-holder">
    <img class="avatar" preload src="/static/images/placeholder_avatar.png"/>
  </div>
  <div class="d-flex flex-column sender">
    <p class="name fw-bold mb-1"></p>
    <div class="message-content"></div>
  </div>
</div>`;

jQuery(async () => {
  const currentPath = window.location.pathname;
  const classCode = currentPath.split("/");
  const response = await fetch("/api/messages/" + classCode[1]);
  const data = await response.json();
  for (const message of data) {
    await receiveMessage(message);
  }
});

let lastParentMessage;
let lastAuthor = "";

export const displayMessage = async (data) => {
  if (lastAuthor !== data.created_by) {
    const messageElement = $(messageHtml).appendTo("#chat-scroll-window");
    messageElement
      .children("div.avatar-holder")
      .append(await getAvatar(data.created_by));

    $(".sender").attr("id", "sender-" + data.created_by);

    messageElement.children("div").children(".name").text(data.created_by);
    const messageContainer = messageElement
      .children("div")
      .children(".message-content");
    $(`<p class="message-item mb-0" id="message-${data.message_id}"></p>`)
      .text(data.content)
      .appendTo(messageContainer);
    lastParentMessage = messageElement;
  } else {
    const messageContainer = lastParentMessage
      .children("div")
      .children(".message-content");
    $("<b></b>").appendTo(messageContainer);
    $(`<p class="message-item mb-0" id="message-${data.message_id}"></p>`)
      .text(data.content)
      .appendTo(messageContainer);
  }
  lastAuthor = data.created_by;
};
