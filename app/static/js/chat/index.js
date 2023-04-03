import { setupSocketIO } from "./events/index.js";

const setup = () => {
  const pickerOptions = {
    theme: "dark",
    onEmojiSelect: (emoji) => {
      $("#chatbox").val($("#chatbox").val() + emoji.native);
    },
  };
  const picker = new EmojiMart.Picker(pickerOptions);
  $(".emoji-picker").append(picker);

  const button = $("button");
  const tooltip = $(".emoji-picker");
  Popper.createPopper(button[0], tooltip[0], {
    placement: "top-end",
  });

  $("button").on("click", () => {
    tooltip.toggleClass("shown");
  });
};

$(() => {
  setup();
  setupSocketIO();
});
