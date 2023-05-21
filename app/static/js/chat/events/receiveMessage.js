import { getAvatar } from "../../user.js";

const units = {
  year: 24 * 60 * 60 * 1000 * 365,
  month: (24 * 60 * 60 * 1000 * 365) / 12,
  day: 24 * 60 * 60 * 1000,
  hour: 60 * 60 * 1000,
  minute: 60 * 1000,
  second: 1000,
};

const rtf = new Intl.RelativeTimeFormat("en", { numeric: "auto" });

const messageHtml = `
<div class="message d-flex d-none gap-3">
  <div class="avatar-holder d-flex">
    <img class="avatar" preload src="/static/assets/placeholder_avatar.png"/></div>
  <div class="d-flex flex-column sender">
    <p class="d-flex mb-1">
      <span class="name fw-bold"></span>
      <span class="bot"></span>
      <span class="timestamp"></span>
    </p>
    <div class="message-content"></div>
  </div>
</div>`;

const formatTimestamp = (timestamp) => {
  const datetime = new Date(timestamp);
  const now = new Date();

  const timeDiff = datetime-now;

  let formattedDatetime = "";
  if (timeDiff < 24 * 60 * 60 * 1000) {
    formattedDatetime =
      "— Today at " +
      datetime.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
  } else if (timeDiff < 2 * 24 * 60 * 60 * 1000) {
    formattedDatetime =
      "— Yesterday at " +
      datetime.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
  } else {
    formattedDatetime =
      datetime.toLocaleDateString() +
      " at " +
      datetime.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
  }
  return formattedDatetime;
};

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

    if (message.is_bot) {
      const bot = messageElement.find(".bot");
      bot.text(" (verified)");
      bot.css("color", "#dead73");
    }

    messageElement
      .find(".timestamp")
      .text(` ${formatTimestamp(message.created_at)}`);

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
