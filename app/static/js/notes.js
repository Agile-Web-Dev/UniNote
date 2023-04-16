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
