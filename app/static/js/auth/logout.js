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