// User test
const validUser = {
  username: "admin",
  password: "123456"
};

document.getElementById("loginForm").addEventListener("submit", function(e) {
  e.preventDefault(); // Ngăn reload trang

  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const message = document.getElementById("message");

  if (username === validUser.username && password === validUser.password) {
    message.style.color = "green";
    message.textContent = "✅ Đăng nhập thành công!";
  } else {
    message.style.color = "red";
    message.textContent = "❌ Sai tên đăng nhập hoặc mật khẩu!";
  }
});
