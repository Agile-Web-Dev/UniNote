const liItems = $(".header-tab-item");
for (var i = 0; i < liItems.length; i++) {
  liItems[i].addEventListener("click", function() {
  const current = $(".active");
  console.log(current)
  current[0].className = current[0].className.replace(" active", "");
  this.className += " active";
  });
}