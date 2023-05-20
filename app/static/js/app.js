const leftOpen = true;
const rightOpen = true;

jQuery(() => {
  $(".drawer-button").on("click", function () {
    const parentContainer = $(this).parent();
    const parentId = parentContainer.attr("id");

    if (parentId.includes("left")) {
      $("#nav-bar").toggleClass("d-none");
    } else if (parentId.includes("right")) {
      $("#note-bar").toggleClass("d-none");
    }
  });

  handleMediaChange();
});

const sidebarQuery = window.matchMedia("(max-width: 575.98px");

const handleMediaChange = () => {
  if (sidebarQuery.matches) {
    $("#nav-bar").addClass("d-none");
    $("#note-bar").addClass("d-none");
  } else {
    $("#nav-bar").removeClass("d-none");
    $("#note-bar").removeClass("d-none");
  }
};

sidebarQuery.addEventListener("change", () => {
  handleMediaChange();
});
