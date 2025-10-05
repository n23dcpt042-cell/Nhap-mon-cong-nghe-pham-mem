

## 🔷 **1. Class Diagram – Mô tả chi tiết**

Class Diagram thể hiện các **lớp (class)** trong hệ thống, **thuộc tính**, **hành vi (method)** của chúng, và các **mối quan hệ** giữa các lớp.



### 🧑‍💼 **User (Người dùng tổng quát)**

* **Thuộc tính**: `userID`, `username`, `password`, `email`
* **Phương thức**: `login()`, `logout()`, `updateProfile()`
* **Quan hệ**: Là lớp cha của `Viewer`, `Marketer`, và `Admin`



### 👁 **Viewer (Người xem nội dung)**

* **Phương thức**: `viewContent()`, `interact()`, `comment()`, `feedback()`, `rateProduct()`
* **Quan hệ**: kế thừa từ `User`



### 📣 **Marketer (Người làm chiến dịch tiếp thị)**

* **Thuộc tính**: `campaignList: List<Campaign>`
* **Phương thức**: `createContent()`, `schedulePublish()`, `livestream()`, `requestApproval()`, `viewPerformance()`
* **Quan hệ**: kế thừa từ `User`, tương tác với `Campaign` và `Content`



### 🔧 **Admin (Quản trị viên)**

* **Thuộc tính**: `adminID`, `permissionLevel`
* **Phương thức**: `approveContent()`, `manageCategories()`, `manageSystem()`, `viewReports()`, `restoreError()`
* **Quan hệ**: kế thừa từ `User`, quản lý các class khác như `Content`, `Report`



### 🧾 **Content (Nội dung)**

* **Thuộc tính**: `contentID`, `title`, `body`, `type`, `publishDate`, `status`
* **Phương thức**: `editContent()`, `publish()`, `embedVideo()`
* **Quan hệ**: liên kết với `Campaign`, `Platform`, `Viewer`



### 📊 **Campaign (Chiến dịch)**

* **Thuộc tính**: `campaignID`, `title`, `description`, `startDate`, `endDate`, `status`
* **Phương thức**: `addContent()`, `updateStatus()`, `getAnalytics()`
* **Quan hệ**: liên kết với `Content`, `Report`, `Marketer`



### 🧠 **AnalyticsEngine (Bộ máy phân tích)**

* **Thuộc tính**: `reportID`, `seoScore`, `coreWebVitals`
* **Phương thức**: `collectData()`, `analyzePerformance()`, `generateReport()`
* **Quan hệ**: liên kết với `Report`



### 📄 **Report (Báo cáo)**

* **Thuộc tính**: `reportID`, `campaignID`, `metrics`, `dateGenerated`
* **Phương thức**: `exportReport()`, `summarize()`
* **Quan hệ**: gắn với `Campaign`, nhận dữ liệu từ `AnalyticsEngine`



### 🌐 **Platform (Nền tảng bên ngoài)**

* **Thuộc tính**: `platformID`, `name`, `apiEndpoint`
* **Phương thức**: `postContent()`, `getInteractionData()`
* **Quan hệ**: liên kết với `Content`



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

