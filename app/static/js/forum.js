const noteData = [
  { title: "Note 1", content: "This is note 1" },
  { title: "Note 2", content: "This is note 2" },
  { title: "Note 3", content: "This is note 3" },
  { title: "Note 4", content: "This is note 4" },
  { title: "Note 5", content: "This is note 5" },
];

jQuery(() => {
  const noteList = $("#note-list");
  noteList.html(noteData.map(NoteItem).join(""));

  $("#note-searchbar-form").on("submit", (e) => {
    e.preventDefault();
    console.log("search");
    const searchQuery = $("#note-searchbar").val();
    const filteredNotes = noteData.filter(
      (note) =>
        note.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
        note.content.toLowerCase().includes(searchQuery.toLowerCase())
    );
    noteList.html(filteredNotes.map(NoteItem).join(""));
  });
});

const NoteItem = ({ title, content }) => {
  return `
    <article class="note-item">
      <h4>${title}</h4>
      <p>${content}</p>
    </article>
  `;
};
