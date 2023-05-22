let leftOpen = false;
let rightOpen = false;

jQuery(() => {
  $(".drawer-button").on("click", function () {
    const parentContainer = $(this).parent();
    const parentId = parentContainer.attr("id");

    if (parentId.includes("left")) {
      leftOpen = !leftOpen;

      if (leftOpen) {
        $("#nav-bar").css({ "min-width": "120px", "max-width": "120px" });
        $(this).css("transform", "rotate(180deg)");
        $(this).css("left", "114px");
      } else {
        $("#nav-bar").css({ "min-width": "0", "max-width": "0" });
        $(this).css("transform", "rotate(0deg)");
        $(this).css("left", "6px");
      }
    } else if (parentId.includes("right")) {
      rightOpen = !rightOpen;

      if (rightOpen) {
        $("#note-bar").css({ "min-width": "300px", "max-width": "300px" });
        $(this).css("transform", "rotate(180deg)");
        $(this).css("right", "294px");
      } else {
        $("#note-bar").css({ "min-width": "0", "max-width": "0" });
        $(this).css("transform", "rotate(0deg)");
        $(this).css("right", "6px");
      }
    }
  });

  handleMediaChange();
});

const sidebarQuery = window.matchMedia("(max-width: 999.98px)");

const handleMediaChange = () => {
  if (sidebarQuery.matches) {
    leftOpen = false;
    rightOpen = false;
    $("#nav-bar").css({ "min-width": "0", "max-width": "0" });
    $("#note-bar").css({ "min-width": "0", "max-width": "0" });
  } else {
    leftOpen = true;
    rightOpen = true;
    $("#nav-bar").css({ "min-width": "250px", "max-width": "250px" });
    $("#note-bar").css({ "min-width": "400px", "max-width": "400px" });
  }
};

sidebarQuery.addEventListener("change", () => {
  handleMediaChange();
});
