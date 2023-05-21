//log in functionality on login page
const loginFormHandler = async (event) => {
  event.preventDefault();

  let errors = [];

  const username = $("#username").val();
  const password = $("#password").val();
  const remember = $("#remember").is(":checked");

  if (!username || !password) {
    errors.push("Please fill in all fields.");
  }

  if (errors.length > 0) {
    $("#alert").text(errors.join("\n"));
    $("#alert").removeClass("d-none");
    return;
  }

  // loading animation
  $("#submit").html(
    '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Loading...'
  );

  try {
    await $.ajax({
      type: "POST",
      dataType: "json",
      url: "/api/auth/login",
      contentType: "application/json",
      data: JSON.stringify({ username, password, remember }),
    });
  } catch (err) {
    // We only need to show Login button again if the request failed
    $("#submit").text("Login");
    if (err.responseJSON) {
      $("#alert").text(err.responseJSON.msg);
    } else {
      $("#alert").text("Unexpected error. Please try again later.");
    }
    $("#alert").removeClass("d-none");
    return;
  }
  document.location.replace("/");
};
