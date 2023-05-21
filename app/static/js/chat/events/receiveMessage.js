import { getAvatar } from "../../user.js";

const messageHtml = `
<div class="message d-flex d-none gap-3">
  <div class="avatar-holder d-flex">
    <img class="avatar" preload src="/static/images/placeholder_avatar.png"/></div>
  <div class="d-flex flex-column sender">
    <p class="d-flex mb-1">
      <span class="name fw-bold"></span>
      <span></span>
    </p>
    <div class="message-content"></div>
  </div>
</div>`;

let lastParentMessage;
let lastAuthor = "";

export const receiveMessage = async (message) => {
  if (lastAuthor !== message.created_by) {
    lastAuthor = message.created_by;
    const messageElement = $(messageHtml);
    lastParentMessage = messageElement;
    const avatar = messageElement.find(".avatar");
    avatar.prop("src", await getAvatar(message.created_by));
    avatar.on("load", () => {
      messageElement.removeClass("d-none");
    });
    $(".sender").attr("id", "sender-" + message.created_by);
    messageElement.find(".name").text(message.created_by);
    const messageContainer = messageElement.find(".message-content");
    $(`<p class="message-item mb-0" id="message-${message.message_id}"></p>`)
      .text(message.content)
      .appendTo(messageContainer);

    messageElement.appendTo("#chat-scroll-window");
  } else {
    $(".sender").attr("id", "sender-" + message.created_by);
    const messageContainer = lastParentMessage.find(".message-content");
    $("<b></b>").appendTo(messageContainer);
    $(`<p class="message-item mb-0" id="message-${message.message_id}"></p>`)
      .text(message.content)
      .appendTo(messageContainer);
  }
};
