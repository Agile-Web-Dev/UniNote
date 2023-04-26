const getMessages = () => {
  const messageItems = document.getElementsByClassName("message-item");


  const messages = Array.from(messageItems).map((messageEl) => {
    const message = {
      id: messageEl.id,
      // created_by:
      content: messageEl.textContent.trim(),
    };
    return message;
  });

  console.log(messages)
  return messages;
};

const getUserMessages = () => {
    const userItems = document.getElementsByClassName("sender");

    const userMessages = Array.from(userItems).map((messageEl) => {
      const userMessage = {
        id: messageEl.id,
        // created_by:
        content: messageEl.textContent.trim(),
      };
      return userMessage;
    });
  
    console.log(userMessages)
    return userMessages;
  };

let index = 0;
const searchResults = [];
const searchInput = document.getElementById("search-chat-input");
const searchOption = document.getElementById("form-select");
searchInput.addEventListener("keyup", function (event) {
  if (
    event.key === "Enter" &&
    searchInput.value.trim() !== "" &&
    searchOption.value === "Content:"
  ) {
    const messages = getMessages()
    const userMessages = getUserMessages();
    console.log(userMessages)
    const searchQuery = searchInput.value.trim();
    for (let i = messages.length - 1; i >= 0; i--) {
      const message = messages[i];
      if (message.content.toLowerCase().includes(searchQuery.toLowerCase())) {
        searchResults.push(message);
      }
    }
    searchInput.value = "";
    const searchResultBar = document.getElementById("search-results");
    searchResultBar.style.display = "flex";
    const resultString = document.getElementById("result-string");
    resultString.textContent = `found ${searchResults.length} results for "${searchQuery}"`;
    scrollToMessage(searchResults[index].id);
  }

  if (
    event.key === "Enter" &&
    searchInput.value.trim() !== "" &&
    searchOption.value == "From:"
  ) {
    const searchQuery = searchInput.value.trim();

    for (let i = messages.length - 1; i >= 0; i--) {
      const message = messages[i];
      if (
        message.created_by.toLowerCase().includes(searchQuery.toLowerCase())
      ) {
        searchResults.push(message);
      }
    }
    searchInput.value = "";
    const searchResultBar = document.getElementById("search-results");
    searchResultBar.style.display = "flex";
    const resultString = document.getElementById("result-string");
    resultString.textContent = `found ${searchResults.length} results for "${searchQuery}"`;
    scrollToMessage(searchResults[index].id);
  }
});

const scrollToMessage = (messageId) => {
  const messageEl = document.getElementById(messageId);
  messageEl.scrollIntoView();
  messageEl.style.backgroundColor = "var(--app-grey-800)";
};

const clearSearchHighlights = (current) => {
  if (current) {
    current.style.background = "transparent";
  }
};

const buttonNext = document.getElementById("iterate-up");
buttonNext.addEventListener("click", function () {
  const curr = document.getElementById(searchResults[index].id);
  if (index + 1 < searchResults.length) {
    index = index + 1;
    clearSearchHighlights(curr);
    scrollToMessage(searchResults[index].id);
  }
});

const buttonPrev = document.getElementById("iterate-down");
buttonPrev.addEventListener("click", function () {
  const curr = document.getElementById(searchResults[index].id);
  if (index - 1 >= 0) {
    index--;
    clearSearchHighlights(curr);
    scrollToMessage(searchResults[index].id);
  }
});

const buttonClose = document.getElementById("close-search-results");
buttonClose.addEventListener("click", function () {
  const curr = document.getElementById(searchResults[index].id);
  clearSearchHighlights(curr);
  const searchResultBar = document.getElementById("search-results");
  searchResultBar.style.display = "none";
});
