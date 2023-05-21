const populateNote = (noteRef) => {
  const note = $(noteRef);
  const title = note.data("bs-title");
  const content = note.data("bs-content");
  note
    .html("")
    .append($("<h4></h4>").text(title))
    .append($("<p></p>").text(content));

  return note;
};

// Notes page
jQuery(async () => {
  const currentPath = window.location.pathname;
  const className = currentPath.split("/");
  const response = await fetch("/api/notes/" + className[1].toUpperCase());
  const data = await response.json();
  const noteList = $("#notes-list");
  noteList.html(data.map(NoteItem).join(""));

  $(".note-item").each(function () {
    populateNote(this);
  });

  $("#notes-searchbar-form").on("submit", (e) => {
    e.preventDefault();

    const searchQuery = $("#notes-searchbar").val();
    const results = data.filter(
      (note) =>
        note.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
        note.content.toLowerCase().includes(searchQuery.toLowerCase())
    );
    console.log(results);
    noteList.html(results.map(NoteItem).join(""));
  });

  noteList.on("click", ".note-item", function () {
    const title = $(this).data("bs-title");
    const content = $(this).data("bs-content");
    var myModal = $("#notes-modal");
    myModal.find(".modal-title").text(title);
    myModal.find(".modal-body").html(content);
    myModal.modal("show");
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
    ${content}
    </article>
  `;
};

// Note menu actions
jQuery(async () => {
  const currentPath = window.location.pathname;
  const className = currentPath.split("/");
  const fetchUser = await fetch("/api/user");
  const userData = await fetchUser.json();
  const noteMenuBtn = $("#note-menu-button");
  const noteMenuPopover = $("#note-menu");
  const noteHeader = $("#note-header");
  const noteContent = $("#note-content");

  const postNote = async () => {
    noteHeader.prop("disabled", true);
    noteContent.prop("disabled", true);
    try {
      await fetch("/api/notes", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          createdBy: userData.user_id,
          classId: className[1].toUpperCase(),
          title: noteHeader.val(),
          content: noteContent.val(),
        }),
      });

      const newNote = NoteItem({
        title: noteHeader.val(),
        content: noteContent.val(),
      });

      $("#notes-list").prepend(populateNote(newNote));
      notearr.push(newNote);
      clearNote();
    } catch (error) {
      console.error(error);
    }

    noteHeader.prop("disabled", false);
    noteContent.prop("disabled", false);
    console.log("Note posted");
  };

  const clearNote = () => {
    noteHeader.val("");
    noteContent.val("");
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
    if (noteHeader.val() === "" || noteContent.val() === "") return;
    await postNote();
    clearNote();
  });
});
