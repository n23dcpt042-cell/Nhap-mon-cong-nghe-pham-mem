import mysql.connector

# Dùng root để tạo DB và user mới
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="398218"
)
cur = conn.cursor()

# Xóa và tạo mới database
cur.execute("DROP DATABASE IF EXISTS atm_demo")
cur.execute("CREATE DATABASE atm_demo CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
cur.execute("USE atm_demo")

# Tạo bảng
cur.execute("""
CREATE TABLE accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    balance DECIMAL(15,2)
)
""")

cur.execute("""
CREATE TABLE cards (
    card_no CHAR(16) PRIMARY KEY,
    account_id INT,
    pin_hash CHAR(64),
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
)
""")

cur.execute("""
CREATE TABLE transactions (
    tx_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT,
    card_no CHAR(16),
    atm_id INT,
    tx_type VARCHAR(20),
    amount DECIMAL(15,2),
    balance_after DECIMAL(15,2),
    tx_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Thêm dữ liệu mẫu
import hashlib

pin = "1234"
pin_hash = hashlib.sha256(pin.encode()).hexdigest()

cur.execute("INSERT INTO accounts (name, balance) VALUES ('Nguyen Van A', 5000000.00)")
account_id = cur.lastrowid
cur.execute("INSERT INTO cards (card_no, account_id, pin_hash) VALUES ('1111222233334444', %s, %s)", (account_id, pin_hash))

conn.commit()

# Tạo user riêng cho ứng dụng
try:
    cur.execute("CREATE USER 'atm_user'@'localhost' IDENTIFIED BY '123456'")
except:
    pass  # nếu user đã tồn tại thì bỏ qua

cur.execute("GRANT ALL PRIVILEGES ON atm_demo.* TO 'atm_user'@'localhost'")
cur.execute("FLUSH PRIVILEGES")

conn.commit()
conn.close()

print("✅ Database 'atm_demo' và dữ liệu mẫu đã được tạo thành công!")
