const noteData = [
  { title: "<h1>Note 1</h1>", content: "This is note 1" },
  { title: "Note 2", content: "This is note 2" },
  { title: "Note 3", content: "This is note 3" },
  { title: "Note 4", content: "This is note 4" },
  { title: "Note 5", content: "This is note 5" },
];

// Notes page
jQuery(() => {
  const noteList = $("#notes-list");
  noteList.html(noteData.map(NoteItem).join(""));

  $(".note-item").each(function () {
    const note = $(this);
    const title = note.data("bs-title");
    const content = note.data("bs-content");
    note
      .html("")
      .append($("<h4></h4>").text(title))
      .append($("<p></p>").text(content));
  });

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
      No XSS attack for you
    </article>
  `;
};

// Note menu actions
jQuery(() => {
  const noteMenuBtn = $("#note-menu-button");
  const noteMenuPopover = $("#note-menu");
  const noteHeader = $("#note-header");
  const noteContent = $("#note-content");

  const postNote = async () => {
    // todo update note in db
    noteHeader.prop("disabled", true);
    noteContent.prop("disabled", true);
    await new Promise((resolve) => setTimeout(resolve, 1000));
    noteHeader.prop("disabled", false);
    noteContent.prop("disabled", false);
    console.log("Note posted");
  };

  const clearNote = () => {
    noteHeader.val("");
    noteContent.val("");
    console.log("Note cleared");
  };

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
      case "post":
        postNote();
        break;
      case "discard":
        clearNote();
        break;
      default:
        break;
    }
    noteMenuPopover.removeClass("shown");
  });

  $("#note-share-button").on("click", async () => {
    await postNote();
    clearNote();
  });
});
