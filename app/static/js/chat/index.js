import { setupSocketIO } from "./events/index.js";

// resize chatbox upwards
export const resizeChatbox = () => {
  const chatbox = $("#chatbox");
  chatbox.css("height", "0");
  chatbox.height(chatbox[0].scrollHeight - 20);
};

$("#chatbox").on("input", () => {
  resizeChatbox();
});

$(window).on("resize", () => {
  resizeChatbox();
});

const setup = () => {
  const pickerOptions = {
    theme: "dark",
    onEmojiSelect: (emoji) => {
      const chatbox = $("#chatbox");
      const cursor = chatbox.prop("selectionStart");
      const beforeCursor = chatbox.val().substring(0, cursor);
      const afterCursor = chatbox.val().substring(cursor);
      chatbox.val(`${beforeCursor}${emoji.native}${afterCursor}`);
      chatbox.prop("selectionStart", cursor + 2);
      chatbox.prop("selectionEnd", cursor + 2);
      chatbox.focus();
      emojiPopover.toggleClass("shown");
      emojiBtn.toggleClass("active-action");
    },
  };

  const picker = new EmojiMart.Picker(pickerOptions);
  $("#emoji-picker").append(picker);

  const emojiBtn = $("#emoji-picker-button");
  const emojiPopover = $("#emoji-picker");
  Popper.createPopper(emojiBtn[0], emojiPopover[0], {
    placement: "top-end",
    modifiers: [
      {
        name: "offset",
        options: {
          offset: [20, 15],
        },
      },
    ],
  });

  $("#emoji-picker-button").on("click", () => {
    emojiPopover.toggleClass("shown");
    emojiBtn.toggleClass("active-action");
  });

  $(document).on("click", (e) => {
    if (
      !emojiPopover.is(e.target) &&
      !emojiBtn.is(e.target) &&
      emojiPopover.has(e.target).length === 0
    ) {
      emojiPopover.removeClass("shown");
      emojiBtn.removeClass("active-action");
    }
  });
};

$(() => {
  resizeChatbox();
  setup();
  setupSocketIO();
});
