// User test
const USER = { username: "admin", password: "123456" };

// Khi submit form
document.getElementById("loginForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const username = document.getElementById("username").value.trim();
  const password = document.getElementById("password").value.trim();
  const message = document.getElementById("message");

  if (username === USER.username && password === USER.password) {
    message.style.color = "green";
    message.textContent = "Đăng nhập thành công!";
  } else {
    message.style.color = "red";
    message.textContent = "Sai tên đăng nhập hoặc mật khẩu!";
  }
});

// Nút hiện/ẩn mật khẩu
document.getElementById("togglePassword").addEventListener("click", function () {
  const passInput = document.getElementById("password");
  const type = passInput.getAttribute("type") === "password" ? "text" : "password";
  passInput.setAttribute("type", type);
  this.textContent = type === "password" ? "👁" : "🙈";
});
