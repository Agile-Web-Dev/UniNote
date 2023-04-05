import { setupSocketIO } from "./events/index.js";

const setup = () => {
  const pickerOptions = {
    theme: "dark",
    onEmojiSelect: (emoji) => {
      $("#chatbox").val($("#chatbox").val() + emoji.native);
      emojiPopover.toggleClass("shown");
    },
  };
  const picker = new EmojiMart.Picker(pickerOptions);
  $("#emoji-picker").append(picker);

  const emojiBtn = $("#emoji-picker-button");
  const emojiPopover = $("#emoji-picker");
  Popper.createPopper(emojiBtn[0], emojiPopover[0], {
    placement: "top-end",
  });

  $("button").on("click", () => {
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
