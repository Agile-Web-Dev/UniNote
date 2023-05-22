//render notes list
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

// pulling notes from API and Rendering them
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

  $("#notes-searchbar-form").on("submit", async (e) => {
    e.preventDefault();
    const searchQuery = $("#notes-searchbar").val();

    const response = await fetch("/api/notes/" + className[1].toUpperCase());
    const data = await response.json();
  
    const results = data.filter(
      (note) =>
        note.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
        note.content.toLowerCase().includes(searchQuery.toLowerCase())
    );

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
    <div
      class="note-item"
      data-bs-toggle="modal"
      data-bs-target="#notes-modal"
      data-bs-title="${title}"
      data-bs-content="${content}"
    >
    <h4>${title}</h4>
    <p>${content}</p>
    </div>
  `;
};

// Note menu actions
jQuery(async () => {
  const currentPath = window.location.pathname;
  const className = currentPath.split("/");
  const fetchUser = await fetch("/api/user");
  const userData = await fetchUser.json();
  const noteHeader = $("#note-header");
  const noteContent = $("#note-content");

  const clearNote = () => {
    noteHeader.val("");
    noteContent.val("");
  };

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
      clearNote();
    } catch (error) {
      console.error(error);
    }

    noteHeader.prop("disabled", false);
    noteContent.prop("disabled", false);
  };

  $("#note-share-button").on("click", async () => {
    if (noteHeader.val() === "" || noteContent.val() === "") return;
    $(this).prop("disabled", true);
    await postNote();
    $(this).prop("disabled", false);
    clearNote();
  });
});
