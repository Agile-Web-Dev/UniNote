const noteData = [
  { title: "Note 1", content: "This is note 1" },
  { title: "Note 2", content: "This is note 2" },
  { title: "Note 3", content: "This is note 3" },
  { title: "Note 4", content: "This is note 4" },
  { title: "Note 5", content: "This is note 5" },
];

jQuery(async () => {
  const currentPath = window.location.pathname;
  const className = currentPath.split("/")
  const response = await fetch("/api/notes/" + className[1].toUpperCase());
  const data = await response.json();
  const noteList = $("#notes-list");
  noteList.html(data.map(NoteItem).join(""));
  $("#notes-searchbar-form").on("submit", (e) => {
    e.preventDefault();

    const searchQuery = $("#notes-searchbar").val();
    const results = data.filter(note => note.title.toLowerCase().includes(searchQuery.toLowerCase()) || note.content.toLowerCase().includes(searchQuery.toLowerCase()));
    console.log(results)
    noteList.html(results.map(NoteItem).join(""));
  });

  $(".note-item").on("click", function () {
    const title = $(this).data("bs-title");
    const content = $(this).data("bs-content");
    var myModal = $('#notes-modal');
    myModal.find('.modal-title').text(title);
    myModal.find('.modal-body').html(content);
    myModal.modal('show');
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
