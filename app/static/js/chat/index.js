import { setupSocketIO } from "./events/index.js";

// resize chatbox upwards
export const resizeChatbox = (e) => {
  $(e.target).css("height", "30px");
  $(e.target).height(e.target.scrollHeight - 20);
};

$("#chatbox").on("input", (e) => {
  resizeChatbox(e);
});

const setup = () => {
  const pickerOptions = {
    theme: "dark",
    onEmojiSelect: (emoji) => {
      const cursor = $("#chatbox").prop("selectionStart");
      const beforeCursor = $("#chatbox").val().substring(0, cursor);
      const afterCursor = $("#chatbox").val().substring(cursor);
      emojiPopover.toggleClass("shown");

      $("#chatbox").val(`${beforeCursor}${emoji.native}${afterCursor}`);
      $("#chatbox").prop("selectionStart", cursor + 2);
      $("#chatbox").prop("selectionEnd", cursor + 2);
      $("#chatbox").focus();
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
  });

  $(document).on("click", (e) => {
    if (
      !emojiPopover.is(e.target) &&
      !emojiBtn.is(e.target) &&
      emojiPopover.has(e.target).length === 0
    ) {
      emojiPopover.removeClass("shown");
    }
  });
};

$(() => {
  setup();
  setupSocketIO();
});
