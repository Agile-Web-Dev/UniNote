//get individual messages that are already in the chat
const getMessages = () => {
  const messageItems = $(".message-item");
  const messages = messageItems.toArray().map((messageEl) => {
    const message = {
      id: messageEl.id,
      content: $(messageEl).text().trim(),
    };
    return message;
  });

  return messages;
};

//get all messages from all specific users
const getUserMessages = () => {
  const userItems = $(".sender");
  const userMessages = userItems.toArray().map((messageEl) => {
    const messageContentEl = $(messageEl).find(".message-item");
    const messageId = messageContentEl.attr("id");
    const userMessage = {
      created_by: $(messageEl).text().trim().split("\n")[0],
      id: messageId,
    };
    return userMessage;
  });

  return userMessages;
};

//auto scroll to the message that is being searched and highlight
const scrollToMessage = (messageId) => {
  const messageEl = $("#" + messageId);
  messageEl[0].scrollIntoView();
  messageEl.css("background-color", "var(--app-grey-500)");
};

//clearing all highlights if exists
const clearAllHighlights = () => {
  $(".message-item").css("background", "transparent");
};

//clear the current highlighted message
const clearSearchHighlights = (current) => {
  if (current) {
    $(current).css("background", "transparent");
  }
};

//searching for message based on query from the search bar
const searchMessages = () => {
  if (searchInput.val().trim() === "") return;

  index = 0;
  searchResults = [];
  const searchOption = $("#search-chat-filter");
  const searchQuery = searchInput.val().trim();

  clearAllHighlights();
  //search based on content
  if (searchOption.val() === "Content:") {
    const messages = getMessages();
    for (let i = messages.length - 1; i >= 0; i--) {
      const message = messages[i];
      if (message.content.toLowerCase().includes(searchQuery.toLowerCase())) {
        searchResults.push(message);
      }
    }
    searchInput.val("");
    const searchResultBar = $("#search-results");
    searchResultBar.css("display", "flex");
    const resultString = $("#result-string");

    resultString.text(
      `found ${searchResults.length} results for "${searchQuery}"`
    );
    if (searchResults.length !== 0) {
      scrollToMessage(searchResults[index].id);
    }
  }

  //search based on user
  if (searchOption.val() == "From:") {
    const userMessage = getUserMessages();
    for (let i = userMessage.length - 1; i >= 0; i--) {
      const user = userMessage[i];
      if (user.created_by.toLowerCase().includes(searchQuery.toLowerCase())) {
        searchResults.push(user);
      }
    }
    searchInput.val("");
    const searchResultBar = $("#search-results");
    searchResultBar.css("display", "flex");
    const resultString = $("#result-string");
    resultString.text(
      `found ${searchResults.length} results for "${searchQuery}"`
    );
    scrollToMessage(searchResults[index].id);
  }
};

// Event listeners
let index = 0;
let searchResults = [];

const searchInput = $("#search-chat-input");
searchInput.on("keyup", function (event) {
  if (event.key !== "Enter") return;
  searchMessages();
});

const searchButton = $("#search-button");
searchButton.on("click", searchMessages);

//next query in the search results
const buttonNext = $("#iterate-up");
buttonNext.on("click", function () {
  if (searchResults.length === 0) return;
  const curr = $("#" + searchResults[index].id)[0];
  if (index + 1 < searchResults.length) {
    index = index + 1;
    clearSearchHighlights(curr);
    scrollToMessage(searchResults[index].id);
  }
});

//previous query in the search results
const buttonPrev = $("#iterate-down");
buttonPrev.on("click", function () {
  if (searchResults.length === 0) return;
  const curr = $("#" + searchResults[index].id)[0];
  if (index - 1 >= 0) {
    index--;
    clearSearchHighlights(curr);
    scrollToMessage(searchResults[index].id);
  }
});

//quit search function
const buttonClose = $("#close-search-results");
buttonClose.on("click", function () {
  if (searchResults.length !== 0) {
    const curr = $("#" + searchResults[index].id)[0];
    clearSearchHighlights(curr);
  }
  const searchResultBar = $("#search-results");
  searchResultBar.css("display", "none");
  searchResults = [];
});
