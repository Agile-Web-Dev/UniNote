const registerFormHandler = async (event) => {
    event.preventDefault();

    let errors = [];
  
    const studentNumber = $("#student-number").val();
    const name = $("#name").val();
    const email = $("#email").val();
    const password = $("#password").val();
    const confirmPassword = $("#confirm-password").val();

    if (!studentNumber || !name || !email || !password || !confirmPassword) {
      errors.push("Please fill in all fields.");
    }

    if (!email.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)) {
      errors.push("Please enter a valid email address.");
    }

    if (password.length < 8) {
      errors.push("Password must be at least 8 characters long.");
    }

    if (password !== confirmPassword) {
      errors.push("Passwords do not match.");
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
        url: "/api/auth/register",
        contentType: "application/json",
        data: JSON.stringify({ userId: studentNumber, name, email, password }),
      });
    } catch (err) {
      // We only need to show Register button again if the request failed
      $("#submit").text("Register");
      if (err.responseJSON) {
        $("#alert").text(err.responseJSON.msg);
      } else {
        $("#alert").text("Unexpected error. Please try again later.");
      }
      $("#alert").removeClass("d-none");
      return;
    }

    try {
      await $.ajax({
        type: "POST",
        dataType: "json",
        url: "/api/auth/login",
        contentType: "application/json",
        data: JSON.stringify({ username: studentNumber, password }),
      });
    } catch (err) {
      console.log(err);
      // We only need to show Register button again if the request failed
      $("#submit").text("Register");
      if (err.responseJSON.msg) {
        $("#alert").text(err.responseJSON.msg);
      } else {
        $("#alert").text("Unexpected error. Please try again later.");
      }
      $("#alert").removeClass("d-none");
      return;
    }

    document.location.replace("/");
  };
  