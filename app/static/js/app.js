let leftOpen = false;
let rightOpen = false;

jQuery(() => {
  $(".drawer-button").on("click", function () {
    const parentContainer = $(this).parent();
    const parentId = parentContainer.attr("id");

    if (parentId.includes("left")) {
      leftOpen = !leftOpen;
      $("#nav-bar").toggleClass("d-none");

      if (leftOpen) {
        $(this).css("transform", "rotate(180deg)");
        $(this).css("left", "120px");
      } else {
        $(this).css("transform", "rotate(0deg)");
        $(this).css("left", "0px");
      }
    } else if (parentId.includes("right")) {
      rightOpen = !rightOpen;
      $("#note-bar").toggleClass("d-none");

      if (rightOpen) {
        $(this).css("transform", "rotate(180deg)");
        $(this).css("right", "400px");
      } else {
        $(this).css("transform", "rotate(0deg)");
        $(this).css("right", "0px");
      }
    }
  });

  handleMediaChange();
  handleNoteMediaChange();
});

const sidebarQuery = window.matchMedia("(max-width: 575.98px)");

const handleMediaChange = () => {
  if (sidebarQuery.matches) {
    leftOpen = false;
    rightOpen = false;
    $("#nav-bar").addClass("d-none");
    $("#note-bar").addClass("d-none");
  } else {
    leftOpen = true;
    rightOpen = true;
    $("#nav-bar").removeClass("d-none");
    $("#note-bar").removeClass("d-none");
  }
};

sidebarQuery.addEventListener("change", () => {
  handleMediaChange();
});

const notebarQuery = window.matchMedia("(max-width: 991.98px)");

const handleNoteMediaChange = () => {
  if (notebarQuery.matches) {
    rightOpen = false;
    $("#note-bar").addClass("d-none");
  } else {
    rightOpen = true;
    $("#note-bar").removeClass("d-none");
  }
};

notebarQuery.addEventListener("change", () => {
  handleNoteMediaChange();
});
