export const join = (message) => {
  $("#chat-container").append(`<p>${message.msg}</p>`);
};
