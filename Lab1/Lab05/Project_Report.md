# Lab 05 – Tích hợp, quản lý & báo cáo

## 1. Giới thiệu
Báo cáo này trình bày các artifacts và mô tả **quy trình làm việc** trong quá trình xây dựng **Cổng truyền thông số chuỗi cafe**.  
Các nội dung bao gồm:  
- Phân tích chức năng hệ thống  
- Use Case Diagram, Sequence Diagram  
- Source code giao diện đăng nhập (HTML, CSS, JS)  
- Mô tả Use Case chuẩn UML  
- Quy trình làm việc và quản lý project  

---

## 2. Phân tích mục tiêu hệ thống
**Hệ thống lựa chọn:** Cổng truyền thông số cho chuỗi cafe  

**Mục tiêu chính:**  
- Quản lý nội dung số (bài viết, hình ảnh, video)  
- Xuất bản đa kênh (Web/FB/Zalo/TikTok/YouTube)  
- Hỗ trợ livestream/clip ngắn  
- Tối ưu SEO và Analytics  

**Nhu cầu thực tế:**  
- Doanh nghiệp cần quản lý nội dung tập trung  
- Tiết kiệm thời gian xuất bản lên nhiều kênh  
- Theo dõi hiệu quả chiến dịch, tương tác khách hàng  
- Cải thiện trải nghiệm người dùng, tối ưu tốc độ Web  

---

## 3. Sơ đồ Use Case

### 3.1 Tổng quan hệ thống
**Actors:** Admin, Content Creator, Customer/User, System  
**Use Case chính:** Quản trị CMS, Lập lịch xuất bản, Livestream/Clip ngắn, Nhúng video YouTube/TikTok, Social login, Bình luận/duyệt, Trang chiến dịch, SEO/Core Web Vitals  

### 3.2 Use Case chi tiết
- **Quản trị CMS (Admin, Content Creator):** Tạo/sửa/xóa bài viết, hình ảnh, video; phân quyền người dùng.  
- **Lập lịch xuất bản (Admin, Content Creator):** Lên lịch tự động đăng bài trên các kênh.  
- **Livestream/Clip ngắn (Content Creator):** Phát trực tiếp và nhúng video từ YouTube/TikTok.  
- **Bình luận/duyệt (Admin, Customer/User):** Quản lý bình luận, kiểm duyệt nội dung.  
- **Theo dõi Analytics (Admin):** Thống kê lượt xem, tương tác, hiệu suất SEO.  

---

## 4. Sequence Diagram
**Ví dụ Sequence: Đăng bài viết và xuất bản đa kênh**
1. Content Creator tạo bài viết và upload hình/clip.  
2. Hệ thống kiểm tra định dạng, lưu vào CMS.  
3. Hệ thống gửi thông báo Admin duyệt bài.  
4. Sau khi duyệt, hệ thống xuất bản bài viết lên Web/FB/Zalo/TikTok/YouTube.  
5. Hệ thống ghi lại lượt xuất bản và thống kê Analytics.  



---

## 5. Quy trình làm việc

### Bước 1: Chuẩn bị artifacts
- Thu thập Use Case Diagram, Sequence Diagram, source code Form Login.  
- Kiểm tra tính đầy đủ và chính xác của từng artifact.  

### Bước 2: Phân công công việc
- Nếu nhóm: phân công rõ ai thực hiện sơ đồ, ai viết code, ai viết báo cáo.  
- Nếu cá nhân: Bảo Anh thực hiện tất cả các bước.  

### Bước 3: Tích hợp artifacts
- Gom tất cả artifacts vào folder dự án chuẩn.  
- Kiểm tra liên kết giữa sơ đồ UML và code.  

### Bước 4: Quản lý code trên GitHub
- Commit và push code lên repository chính thức.  
- Cập nhật README.md.  
- Tạo tag version `v1.0` đánh dấu hoàn thành lab.  

### Bước 5: Kiểm tra & hoàn thiện
- Kiểm tra tất cả file đã đầy đủ chưa.  
- Xem sơ đồ Use Case, Sequence có khớp với code không.  
- Ghi chú các vấn đề gặp phải và cách giải quyết.  

---

## 6. Kết quả đạt được
- Tất cả artifacts được gom vào folder chuẩn.  
- Quy trình làm việc được mô tả rõ ràng và minh bạch.  
- Code và tài liệu được quản lý tập trung, dễ theo dõi.  
- Phiên bản v1.0 đánh dấu trạng thái hoàn chỉnh của Lab 05.  
- Hệ thống cơ bản đã có khả năng: quản trị nội dung, xuất bản đa kênh, livestream, social login.  

---

