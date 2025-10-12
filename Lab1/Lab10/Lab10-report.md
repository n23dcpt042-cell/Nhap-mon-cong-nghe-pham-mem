# LAB 10 REPORT – PHÂN TÍCH & THIẾT KẾ ỨNG DỤNG CHUỖI TRUYỀN THÔNG CÀ PHÊ

## 1. Thông tin chung

**Môn học:** Nhập môn Công nghệ phần mềm  
**Tên bài lab:** Phân tích & thiết kế hệ thống chuỗi truyền thông cà phê  
**Sinh viên thực hiện:** Nhóm 16  
- Bùi Kim Vân Anh - N23DCPT002  
- Nguyễn Thị Kiều Anh - N23DCPT003  
- Ro Phi Ni - N23DCPT042  

---

## 2. Mục tiêu bài lab

- Vận dụng kiến thức về phân tích và thiết kế hệ thống phần mềm vào bài toán thực tế.  
- Thực hành xây dựng Use Case Diagram, Sequence Diagram và ERD để mô hình hóa hệ thống.  
- Hiểu rõ vai trò các actor, chức năng, dữ liệu và mối quan hệ giữa các thành phần trong hệ thống truyền thông.

---

## 3. Giới thiệu hệ thống

Hệ thống truyền thông số cho chuỗi cà phê giúp doanh nghiệp quản lý và xuất bản nội dung marketing trên nhiều nền tảng (Facebook, YouTube, TikTok, Zalo, Website).  
Hệ thống hỗ trợ tạo chiến dịch, lên lịch bài đăng, thống kê hiệu quả, và phân quyền người dùng.

**Đối tượng sử dụng chính:**  
- **Admin:** Quản lý toàn bộ hệ thống, phân quyền người dùng.  
- **Marketer:** Tạo chiến dịch, đăng bài, theo dõi hiệu quả.  
- **Editor:** Soạn nội dung, thiết kế hình ảnh/video.  
- **Social Platform:** Các nền tảng mạng xã hội (Facebook, YouTube, TikTok) tương tác qua API.

---

## 4. Phân tích Use Case

### Use Case chính:
1. Đăng nhập hệ thống  
2. Quản lý người dùng  
3. Tạo chiến dịch truyền thông  
4. Quản lý bài đăng  
5. Nhúng video đa nền tảng  
6. Đăng bài lên đa nền tảng  
7. Theo dõi hiệu quả  

### Quan hệ Include / Extend:
- “Đăng bài lên đa nền tảng” *include* “Xác thực API nền tảng”  
- “Tạo chiến dịch” *include* “Quản lý bài đăng”  
- “Nhúng video đa nền tảng” *extend* “Kiểm tra liên kết video hợp lệ”  
- “Theo dõi hiệu quả” *extend* “Xuất báo cáo thống kê”

---

## 5. Thiết kế cơ sở dữ liệu (ERD)

### Các bảng chính:
- **User**(UserID, Username, PasswordHash, Role)  
- **Chiendich**(ChiendichID, TenChiendich, MucTieu, NgayBatDau, NgayKetThuc, TrangThai, UserID)  
- **Baidang**(BaidangID, ChiendichID, TieuDe, NoiDung, NgayDang, NenTangID, TrangThai)  
- **NenTang**(NenTangID, TenNenTang, APIKey, MoTa)  
- **PhanHoi**(PhanHoiID, BaiDangID, LuotXem, LuotThich, LuotBinhLuan, NgayCapNhat)  

### Quan hệ chính:
- 1 **User** → N **Chiendich**  
- 1 **Chiendich** → N **Baidang**  
- 1 **NenTang** → N **Baidang**  
- 1 **BaiDang** → N **PhanHoi**  

---

## 6. Sequence Diagram – Đăng bài đa nền tảng

1. Marketer đăng nhập hệ thống  
2. Tạo chiến dịch và bài đăng mới  
3. Hệ thống gọi API từng nền tảng (Facebook, TikTok, YouTube)  
4. Nền tảng phản hồi trạng thái thành công/thất bại  
5. Hệ thống lưu ID bài viết và cập nhật kết quả  
6. Marketer nhận thông báo kết quả đăng bài  

---

## 7. Kết luận

- Hệ thống giúp số hóa quy trình marketing của chuỗi cà phê, tiết kiệm thời gian quản lý chiến dịch.  
- Việc thiết kế mô hình UML (Use Case, Sequence, ERD) giúp xác định rõ vai trò, chức năng và luồng dữ liệu trong ứng dụng.  
- Đây là bước quan trọng trong giai đoạn phân tích yêu cầu và thiết kế hệ thống của quy trình phát triển phần mềm (SDLC).  
- **Hướng phát triển:** mở rộng quản lý quảng cáo trả phí, chatbot chăm sóc khách hàng, phân tích AI.
