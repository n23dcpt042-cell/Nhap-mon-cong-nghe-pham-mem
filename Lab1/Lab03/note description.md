1. Sơ đồ Use Case – Chuỗi truyền thông số cà phê
Các tác nhân  (Actor):
•	Analytics Engine: Công cụ phân tích dữ liệu, giúp theo dõi chỉ số, thu thập dữ liệu và tối ưu chiến dịch truyền thông.
•	Marketer: Người tạo và quản lý nội dung truyền thông.
•	Viewer: Người dùng cuối – người xem và tương tác với nội dung.
•	Admin: Người quản lý kỹ thuật và hệ thống.
•	Social Platform: Các nền tảng mạng xã hội như Facebook, TikTok, YouTube,...

Các chức năng (Use Case):
1. Đối với Analytics Engine
•	Theo dõi SEO / Core Web Vitals: Giám sát các chỉ số hiệu suất website và trải nghiệm người dùng.
•	Tổng hợp, viết báo cáo (mở rộng từ Theo dõi SEO): Phân tích và báo cáo dữ liệu hoạt động truyền thông.
•	Thu thập dữ liệu từ nền tảng MXH: Thu thập tự động dữ liệu tương tác từ các nền tảng mạng xã hội.
•	Tối ưu chiến dịch tự động: Dựa vào dữ liệu phân tích để điều chỉnh chiến dịch truyền thông cho hiệu quả hơn.
•	Khôi phục hệ thống khi có lỗi (mở rộng từ Tối ưu chiến dịch): Tự động xử lý lỗi hoặc sự cố trong quá trình truyền thông.
2. Đối với Marketer
•	Tạo nội dung, chiến dịch mới: Xây dựng nội dung truyền thông phù hợp với chiến dịch.
•	Lên lịch xuất bản: Đặt lịch cho các nội dung đăng tải lên mạng xã hội.
•	Đề xuất khung giờ, nền tảng hiệu quả (mở rộng từ Lên lịch): Gợi ý thời gian và nền tảng đăng tải hiệu quả nhất.
•	Livestream: Tổ chức các buổi phát trực tiếp nhằm tăng tương tác.
3. Đối với Viewer
•	Xem và tương tác: Xem nội dung, like, bình luận, chia sẻ...
•	Theo dõi và chia sẻ thương hiệu: Thực hiện hành động theo dõi trang và chia sẻ nội dung.
•	Góp ý, phản hồi: Gửi phản hồi, nhận xét đến hệ thống.
•	Đánh giá chất lượng sản phẩm (bao gồm trong Góp ý, phản hồi): Đánh giá mức độ hài lòng với sản phẩm hoặc dịch vụ.
4. Đối với Admin
•	Xem báo cáo thống kê: Truy cập dữ liệu thống kê từ các hoạt động truyền thông.
•	Quản trị hệ thống kỹ thuật: Quản lý và bảo trì kỹ thuật cho toàn hệ thống.
•	Quản lý chuyên mục: Tạo và quản lý danh mục nội dung truyền thông.
5. Đối với Social Platform
•	Nhúng video: Cho phép tích hợp video từ các nguồn khác.
•	Xuất bản đa nền tảng (mở rộng từ Nhúng video): Đăng nội dung đồng thời trên nhiều nền tảng mạng xã hội.

Quan hệ giữa các Use Case
•	<> (mở rộng): Một số chức năng chỉ được thực hiện khi có điều kiện kích hoạt. Ví dụ:
o	Tổng hợp, viết báo cáo mở rộng từ Theo dõi SEO.
o	Đề xuất khung giờ mở rộng từ Lên lịch xuất bản.
•	<> (bao gồm): Một số chức năng là một phần không thể thiếu của chức năng khác. Ví dụ:
o	Đánh giá chất lượng sản phẩm được bao gồm trong Góp ý, phản hồi.

2. Sơ đồ tuần tự (Sequence Diagram) – Quy trình xuất bản nội dung
Các thành phần tham gia
•	Marketer: Khởi tạo và gửi yêu cầu nội dung.
•	System: Hệ thống trung tâm xử lý các yêu cầu, gửi và nhận dữ liệu.
•	Admin: Xét duyệt nội dung.
•	Analytics Engine: Phân tích dữ liệu và gợi ý thời gian đăng tải.
•	Social Platform: Nơi xuất bản nội dung và nhận tương tác từ người dùng.

Luồng xử lý cụ thể
1.	Marketer gửi yêu cầu phê duyệt nội dung mới đến System.
2.	System gửi thông báo phê duyệt nội dung đến Admin.
3.	Admin gửi phản hồi phê duyệt về cho System.
4.	System cập nhật trạng thái chiến dịch đến Marketer.
5.	Marketer chọn khung giờ, nền tảng đăng tải, gửi thông tin đến System.
6.	System gửi yêu cầu phân tích thời gian tối ưu cho Analytics Engine.
7.	Analytics Engine trả về đề xuất thời gian đăng hiệu quả.
8.	System hiển thị gợi ý thời gian lên giao diện của Marketer.
9.	System tiến hành xuất bản đa nền tảng đến Social Platform.
10.	Social Platform phản hồi trạng thái đăng bài cho System.
11.	System thu thập dữ liệu tương tác từ Social Platform.
12.	Analytics Engine trả kết quả phân tích tương tác về System.
13.	System gửi báo cáo thống kê và phân tích cho Admin.
14.	Admin cập nhật báo cáo tổng hợp cho toàn hệ thống.
15.	System hiển thị kết quả xuất bản cho Marketer.

