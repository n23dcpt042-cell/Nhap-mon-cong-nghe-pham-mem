// Xử lý đăng nhập
document.getElementById("loginForm").addEventListener("submit", function(e) {
  e.preventDefault();

  const username = document.getElementById("username").value.trim();
  const password = document.getElementById("password").value.trim();
  const remember = document.getElementById("remember").checked;
  const message = document.getElementById("message");

  // user test
  const testUser = { username: "admin", password: "12345" };

  if (username === "" || password === "") {
    message.textContent = "Vui lòng nhập đầy đủ thông tin!";
    message.style.color = "orange";
    return;
  }

  if (username === testUser.username && password === testUser.password) {
    message.textContent = "Đăng nhập thành công!";
    message.style.color = "green";

    if (remember) {
      localStorage.setItem("savedUser", username);
    }
  } else {
    message.textContent = "Sai tên đăng nhập hoặc mật khẩu!";
    message.style.color = "red";
  }
});

// Nút Hủy
document.getElementById("cancelBtn").addEventListener("click", function() {
  document.getElementById("loginForm").reset();
  document.getElementById("message").textContent = "";
});

// Hiện/ẩn mật khẩu
document.getElementById("togglePassword").addEventListener("click", function() {
  const pwdField = document.getElementById("password");
  if (pwdField.type === "password") {
    pwdField.type = "text";
    this.textContent = "🙈";
  } else {
    pwdField.type = "password";
    this.textContent = "👁️";
  }
});

// Gợi nhớ người dùng
window.onload = function() {
  const savedUser = localStorage.getItem("savedUser");
  if (savedUser) {
    document.getElementById("username").value = savedUser;
    document.getElementById("remember").checked = true;
  }
};
