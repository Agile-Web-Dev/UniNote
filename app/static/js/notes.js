const noteData = [
  { title: "Note 1", content: "This is note 1" },
  { title: "Note 2", content: "This is note 2" },
  { title: "Note 3", content: "This is note 3" },
  { title: "Note 4", content: "This is note 4" },
  { title: "Note 5", content: "This is note 5" },
];

jQuery(() => {
  const noteList = $("#notes-list");
  noteList.html(noteData.map(NoteItem).join(""));

  $("#notes-searchbar-form").on("submit", (e) => {
    e.preventDefault();

    const searchQuery = $("#notes-searchbar").val();
    const filteredNotes = noteData.filter(
      (note) =>
        note.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
        note.content.toLowerCase().includes(searchQuery.toLowerCase())
    );
    noteList.html(filteredNotes.map(NoteItem).join(""));
  });

  $(".note-item").on("click", function () {
    $("#notes-modal").modal("toggle");
    const title = $(this).data("bs-title");
    const content = $(this).data("bs-content");

    $("#notes-modal-title").text(title);
    $("#notes-modal-content").text(content);
  });
});

const NoteItem = ({ title, content }) => {
  return `
    <article
      class="note-item"
      data-bs-toggle="modal"
      data-bs-target="#notes-modal"
      data-bs-title="${title}"
      data-bs-content="${content}"
    >
      <h4>${title}</h4>
      <p>${content}</p>
    </article>
  `;
};
// Note updating
jQuery(() => {
  let autosaveInterval = localStorage.getItem("autosaveInterval");

  if (!autosaveInterval) {
    autosaveInterval = 3000;
    localStorage.setItem("autosaveInterval", autosaveInterval);
  }

  autosave("#notes-content", autosaveInterval);
  autosave("#note-header", autosaveInterval);
});

const autosave = (element, autosaveInterval) => {
  let saveTimeout = null;

  let oldValue = "";
  $(element).on("change keyup paste", function () {
    const currentValue = $(this).val();
    if (!oldValue || currentValue == oldValue) {
      oldValue = currentValue;
      return;
    } // prevent multiple simultaneous triggers

    clearTimeout(saveTimeout); // don't save if user is still typing
    saveTimeout = setTimeout(saveNote, autosaveInterval);
  });
};

const saveNote = async () => {
  // update note in db
  console.log("Note saved");
  return Promise.resolve();
};

// Note menu actions
jQuery(() => {
  const noteMenuBtn = $("#note-menu-button");
  const noteMenuPopover = $("#note-menu");
  Popper.createPopper(noteMenuBtn[0], noteMenuPopover[0], {
    placement: "bottom-start",
  });

  $("#note-menu-button").on("click", () => {
    noteMenuPopover.toggleClass("shown");
  });

  $(document).on("click", (e) => {
    if (
      !noteMenuPopover.is(e.target) &&
      !noteMenuBtn.is(e.target) &&
      noteMenuPopover.has(e.target).length === 0
    ) {
      noteMenuPopover.removeClass("shown");
    }
  });

  $(".note-menu-item").on("click", function () {
    const action = $(this).data("action");
    switch (action) {
      case "create":
        createNote();
      case "delete":
        deleteNote();
        break;
      case "share":
        shareNote(); // share note to forum
        break;
      default:
        break;
    }
  });

  $("#note-close-button").on("click", () => {
    $("#note-bar").css("display", "none");
    $("#main-content").addClass("col-10").removeClass("col-6");
  });
});
