//html for class enrollment
const enrolledHtml = `
<div class="g-4 col-sm-6 col-md-4 col-lg-3 d-flex justify-content-center text-center align-self-center">
  <a class="class-cell d-flex flex-column justify-content-center rounded p-2 text-decoration-none">
    <h3></h3>
    <p class="m-0"></p>
  </a>
</div>`;

const addClassEl = $(".add-class");

//functionality for user to add their class
addClassEl.on("click", async (e) => {
  const currAddClassEl = $(e.target);
  const parent = currAddClassEl.parent();
  const ancestor = parent.parent();
  const classId = ancestor.find("p").text();

  let enrolledClasses;

  try {
    currAddClassEl.replaceWith(
      '<span class="add-class add-class-spinner spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>'
    );
    await $.ajax({
      type: "POST",
      dataType: "json",
      url: "/api/user/class",
      contentType: "application/json",
      data: JSON.stringify({ classId }),
    });

    enrolledClasses = await $.ajax({
      type: "GET",
      url: "/api/user/class",
    });
  } catch (err) {
    console.log(err);
    return;
  }

  ancestor.remove();

  const enrolledClassesEl = $("#enrolled-classes");
  enrolledClassesEl.empty();
  console.log(enrolledClasses.classes);
  for (const enrolledClass of enrolledClasses.classes) {
    const newClassEl = $(enrolledHtml);
    newClassEl.find("a").attr("href", `/${enrolledClass.class_id}/chatroom`);
    newClassEl.find("h3").text(enrolledClass.name);
    newClassEl.find("p").text(enrolledClass.class_id);

    enrolledClassesEl.append(newClassEl);
  }
});
