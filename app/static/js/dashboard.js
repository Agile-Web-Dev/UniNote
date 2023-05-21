const addClassEl = $(".add-class");

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

  console.log(ancestor);
  ancestor.remove();

  const enrolledClassesEl = $("#enrolled-classes");
  enrolledClassesEl.empty();
  console.log(enrolledClasses.classes);
  for (const enrolledClass of enrolledClasses.classes) {
    const newClassEl = $(`
<div class="g-4 col-sm-6 col-md-4 col-lg-3 d-flex justify-content-center text-center align-self-center">
  <a class="class-cell d-flex flex-column justify-content-center rounded p-2 text-decoration-none"
    href="/${enrolledClass.class_id}/chatroom">
    <h3>${enrolledClass.name}</h3>
    <p class="m-0">${enrolledClass.class_id}</p>
  </a>
</div>`);
    enrolledClassesEl.append(newClassEl);
  }
});
