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
