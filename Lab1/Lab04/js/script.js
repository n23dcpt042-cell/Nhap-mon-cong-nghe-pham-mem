document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('loginForm');
  const err = document.getElementById('error');
  const remember = document.getElementById('remember');
  const username = document.getElementById('username');

  // load remembered username
  const saved = localStorage.getItem('rememberedUser');
  if (saved) { username.value = saved; remember.checked = true; }

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    err.textContent = '';
    const user = username.value.trim();
    const pass = document.getElementById('password').value;

    if (!user) { err.textContent = 'Username không được để trống'; return; }
    if (pass.length < 4) { err.textContent = 'Password phải ít nhất 4 ký tự'; return; }

    if (remember.checked) localStorage.setItem('rememberedUser', user); else localStorage.removeItem('rememberedUser');

    // giả lập login success (trong lab chưa có backend)
    console.log('Đăng nhập thành công:', user);
    alert('Login thành công (demo).');
  });

  document.getElementById('cancelBtn').addEventListener('click', () => form.reset());
});
