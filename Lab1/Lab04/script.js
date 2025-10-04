function validateForm() {
  let user = document.getElementById("username").value.trim();
  let pass = document.getElementById("password").value.trim();
  let error = document.getElementById("error");

  if (user === "" || pass === "") {
    error.textContent = "Username và Password không được để trống!";
    return false;
  }
  error.textContent = "";
  alert("Login thành công (demo)");
  return true;
}
