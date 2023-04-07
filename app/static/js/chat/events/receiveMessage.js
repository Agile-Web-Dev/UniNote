export const receiveMessage = (message) => {

  $("#chat-container").append(`<p>${message.msg}</p>`);
};
