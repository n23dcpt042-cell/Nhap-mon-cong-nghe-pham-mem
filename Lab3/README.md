# Selenium Test - Login Form

## Thông tin
- Môn học: Nhập Môn Công Nghệ Phần Mềm
- Sinh viên:
  + Bùi Kim Vân Anh - N23DCPT002
  + Nguyễn Thị Kiều Anh - N23DCPT003
  + Ro Phi Ni - N23DCPT042
- Bài tập: Lab 03- Testing software (login form) 

## Nội dung
Form `login.html` gồm:
- Ô nhập Username, Password
- Nút LOGIN
- Link Forgot password?
- Link SIGN UP
- Nút social login (Facebook, Twitter, Google)

Các test case:
1. Đăng nhập thành công
2. Sai thông tin đăng nhập
3. Bỏ trống Username
4. Bỏ trống Password
5. Link Forgot password
6. Link SIGN UP
7. Nút social login (Facebook, Twitter, Google)

## Cách chạy
### Chạy bằng Selenium IDE
1. Cài extension **Selenium IDE** trên Chrome/Firefox.
2. Mở IDE → `File > Open Project` → chọn file `login_test.side`.
3. Chạy toàn bộ suite hoặc từng test case.
4. Xem kết quả pass/fail trong log.

### Export code (tùy chọn)
Từ Selenium IDE có thể `Export` sang Python/JS rồi chạy bằng Selenium WebDriver.

## Kết quả minh họa
Ảnh chụp màn hình được lưu trong thư mục `screenshots/`.

Ví dụ:
- Đăng nhập thành công: hiện "Login success!" và chuyển trang `dashboard.html`
- Sai password: hiện "Invalid credentials."
- Trống Username/Password: hiện "Please fill all required fields."
