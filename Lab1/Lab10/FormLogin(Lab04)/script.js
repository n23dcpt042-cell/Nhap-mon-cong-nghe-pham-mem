document.getElementById("loginForm").addEventListener("submit", function(e) {
  e.preventDefault();
  
  const username = document.getElementById("username").value.trim();
  const password = document.getElementById("password").value.trim();
  const message = document.getElementById("message");

  if (username === "admin" && password === "123456") {
    message.style.color = "green";
    message.textContent = "Đăng nhập thành công!";
  } else {
    message.style.color = "red";
    message.textContent = "Sai tên đăng nhập hoặc mật khẩu!";
  }
});

// Hiện / ẩn mật khẩu
document.getElementById("togglePassword").addEventListener("click", function() {
  const passwordField = document.getElementById("password");
  passwordField.type = passwordField.type === "password" ? "text" : "password";
});

// Nút Hủy
document.getElementById("cancelBtn").addEventListener("click", function() {
  document.getElementById("loginForm").reset();
  document.getElementById("message").textContent = "";
});
