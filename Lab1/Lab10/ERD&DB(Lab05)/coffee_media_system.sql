-- Tạo database cho hệ thống truyền thông chuỗi cà phê
CREATE DATABASE IF NOT EXISTS coffee_media_system;
USE coffee_media_system;

-- Bảng User (tài khoản hệ thống)
CREATE TABLE IF NOT EXISTS User (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(50) NOT NULL UNIQUE,
    PasswordHash VARCHAR(255) NOT NULL,
    Role ENUM('Admin', 'Marketer', 'ContentEditor', 'Viewer') DEFAULT 'Marketer',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Bảng NhanVien (nhân sự trong hệ thống)
CREATE TABLE IF NOT EXISTS NhanVien (
    NhanVienID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT UNIQUE,
    HoTen VARCHAR(100) NOT NULL,
    Email VARCHAR(100),
    SoDienThoai VARCHAR(20),
    ChucVu VARCHAR(100),
    PhongBan ENUM('Marketing','Design','IT','Quản lý chuỗi','Khác') DEFAULT 'Marketing',
    NgayVaoLam DATE,
    FOREIGN KEY (UserID) REFERENCES User(UserID)
        ON DELETE SET NULL
);

-- Bảng ChuoiCaPhe (quản lý các chi nhánh hoặc thương hiệu con)
CREATE TABLE IF NOT EXISTS ChuoiCaPhe (
    ChuoiID INT AUTO_INCREMENT PRIMARY KEY,
    TenChuoi VARCHAR(100) NOT NULL,
    DiaChi VARCHAR(255),
    SoDienThoai VARCHAR(20),
    Email VARCHAR(100),
    MoTa TEXT,
    NgayTao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Bảng KenhTruyenThong (các nền tảng được kết nối: Facebook, Zalo, TikTok...)
CREATE TABLE IF NOT EXISTS KenhTruyenThong (
    KenhID INT AUTO_INCREMENT PRIMARY KEY,
    ChuoiID INT NOT NULL,
    TenKenh ENUM('Facebook','Instagram','Zalo','TikTok','YouTube','Website') NOT NULL,
    AccessToken TEXT,
    TrangThai ENUM('Hoạt động','Ngưng kết nối') DEFAULT 'Hoạt động',
    FOREIGN KEY (ChuoiID) REFERENCES ChuoiCaPhe(ChuoiID)
        ON DELETE CASCADE
);

-- Bảng ChienDich (quản lý chiến dịch truyền thông)
CREATE TABLE IF NOT EXISTS ChienDich (
    ChienDichID INT AUTO_INCREMENT PRIMARY KEY,
    ChuoiID INT NOT NULL,
    TenChienDich VARCHAR(150) NOT NULL,
    MoTa TEXT,
    NgayBatDau DATE,
    NgayKetThuc DATE,
    TrangThai ENUM('Lên kế hoạch','Đang chạy','Hoàn thành','Tạm dừng') DEFAULT 'Lên kế hoạch',
    FOREIGN KEY (ChuoiID) REFERENCES ChuoiCaPhe(ChuoiID)
        ON DELETE CASCADE
);

-- Bảng BaiDang (bài đăng, video, hình ảnh truyền thông)
CREATE TABLE IF NOT EXISTS BaiDang (
    BaiDangID INT AUTO_INCREMENT PRIMARY KEY,
    ChienDichID INT,
    KenhID INT,
    TieuDe VARCHAR(150) NOT NULL,
    NoiDung TEXT,
    LoaiNoiDung ENUM('Ảnh','Video','Bài viết','Livestream') DEFAULT 'Bài viết',
    LienKetFile VARCHAR(255),
    TrangThai ENUM('Nháp','Đã duyệt','Đã đăng','Lỗi đăng') DEFAULT 'Nháp',
    NgayDangDuKien DATETIME,
    NgayDangThucTe DATETIME,
    FOREIGN KEY (ChienDichID) REFERENCES ChienDich(ChienDichID)
        ON DELETE SET NULL,
    FOREIGN KEY (KenhID) REFERENCES KenhTruyenThong(KenhID)
        ON DELETE SET NULL
);

-- Bảng TuongTac (thống kê hiệu quả bài đăng)
CREATE TABLE IF NOT EXISTS TuongTac (
    TuongTacID INT AUTO_INCREMENT PRIMARY KEY,
    BaiDangID INT NOT NULL,
    LuotXem INT DEFAULT 0,
    LuotThich INT DEFAULT 0,
    LuotBinhLuan INT DEFAULT 0,
    LuotChiaSe INT DEFAULT 0,
    ThoiGianCapNhat TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (BaiDangID) REFERENCES BaiDang(BaiDangID)
        ON DELETE CASCADE
);

-- Bảng BaoCaoChienDich (báo cáo tổng hợp hiệu quả chiến dịch)
CREATE TABLE IF NOT EXISTS BaoCaoChienDich (
    BaoCaoID INT AUTO_INCREMENT PRIMARY KEY,
    ChienDichID INT NOT NULL,
    TongBaiDang INT DEFAULT 0,
    TongLuotXem INT DEFAULT 0,
    TongTuongTac INT DEFAULT 0,
    HieuQua ENUM('Thấp','Trung bình','Cao') DEFAULT 'Trung bình',
    GhiChu TEXT,
    FOREIGN KEY (ChienDichID) REFERENCES ChienDich(ChienDichID)
        ON DELETE CASCADE
);

-- Dữ liệu mẫu ban đầu
INSERT INTO ChuoiCaPhe (TenChuoi, DiaChi, SoDienThoai, Email, MoTa)
VALUES
('CoffeeHouse Central', '123 Nguyễn Huệ, Q.1, TP.HCM', '0901234567', 'central@coffeehouse.vn', 'Chuỗi trung tâm'),
('CoffeeHouse Hà Nội', '45 Tràng Thi, Hoàn Kiếm, Hà Nội', '0912345678', 'hanoi@coffeehouse.vn', 'Chi nhánh phía Bắc');

INSERT INTO KenhTruyenThong (ChuoiID, TenKenh, TrangThai)
VALUES
(1, 'Facebook', 'Hoạt động'),
(1, 'TikTok', 'Hoạt động'),
(2, 'Instagram', 'Hoạt động'),
(2, 'YouTube', 'Ngưng kết nối');

INSERT INTO ChienDich (ChuoiID, TenChienDich, MoTa, NgayBatDau, NgayKetThuc)
VALUES
(1, 'Chiến dịch “Cà phê buổi sáng”', 'Quảng bá combo sáng trên Facebook và TikTok', '2025-10-01', '2025-10-31'),
(2, 'Chiến dịch “Mùa đông ấm áp”', 'Ra mắt sản phẩm mới – Cà phê sữa nóng', '2025-11-01', '2025-11-30');
