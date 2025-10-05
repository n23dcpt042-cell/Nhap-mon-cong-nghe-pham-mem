## 🗂️ **2. Package Diagram – Mô tả chi tiết**

Package Diagram thể hiện cách tổ chức hệ thống thành các **gói (module)** logic. Mỗi gói chứa các lớp liên quan về mặt chức năng.



### 📦 **Package: User Management**

* **Chứa các class**: `User`, `Viewer`, `Marketer`, `Admin`
* **Chức năng**: Quản lý người dùng và phân quyền. `Admin`, `Marketer`, `Viewer` là các vai trò mở rộng từ `User`.



### 📦 **Package: Content Management**

* **Chứa các class**: `Content`, `Campaign`
* **Chức năng**: Quản lý nội dung và chiến dịch quảng bá, lịch đăng bài, trạng thái nội dung, gắn nội dung với chiến dịch.



### 📦 **Package: Analytics**

* **Chứa các class**: `AnalyticsEngine`, `Report`
* **Chức năng**: Phân tích hiệu suất, tạo báo cáo từ dữ liệu thu thập được.



### 📦 **Package: Platform Integration**

* **Chứa class**: `Platform`
* **Chức năng**: Giao tiếp với nền tảng bên ngoài (như mạng xã hội, hệ thống CMS...), đăng nội dung và lấy dữ liệu tương tác.



### 🔁 **Quan hệ giữa các Package**

* `User Management` ➡ `Content Management`: Marketer và Admin tạo, kiểm duyệt nội dung.
* `Content Management` ➡ `Platform Integration`: Nội dung được đăng lên các nền tảng.
* `Content Management` ➡ `Analytics`: Nội dung và chiến dịch được phân tích hiệu quả.
* `Analytics` ↔ `Platform Integration`: Lấy dữ liệu từ nền tảng để phân tích hiệu quả nội dung.
