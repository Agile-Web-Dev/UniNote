const loginFormHandler = async (event) => {
  event.preventDefault();

  const username = $("#username").val();
  const password = $("#password").val();
  const remember = $("#remember").is(":checked");

  if (!username && !password) {
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
    if (err.responseJSON.msg) {
      $("#alert-login").text(err.responseJSON.msg);
    } else {
      $("#alert-login").text("Unexpected error. Please try again later.");
    }
    $("#alert-login").removeClass("d-none");
    return;
  }
  document.location.replace("/");
};

const logoutHandler = async (event) => {
  try {
    await $.ajax({
      type: "GET",
      dataType: "json",
      url: "/api/auth/logout",
    });
  } catch (err) {
    console.log(err);
  }
  document.location.replace("/login");
}