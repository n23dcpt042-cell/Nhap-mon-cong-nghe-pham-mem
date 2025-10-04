CREATE DATABASE IF NOT EXISTS atm_demo;
USE atm_demo;

-- Bảng tài khoản
CREATE TABLE accounts (
  account_id INT PRIMARY KEY AUTO_INCREMENT,
  balance DECIMAL(15,2)
);

-- Bảng thẻ ATM
CREATE TABLE cards (
  card_no VARCHAR(20) PRIMARY KEY,
  account_id INT,
  pin_hash VARCHAR(64),
  FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

-- Bảng lịch sử giao dịch
CREATE TABLE transactions (
  id INT PRIMARY KEY AUTO_INCREMENT,
  account_id INT,
  card_no VARCHAR(20),
  atm_id INT,
  tx_type VARCHAR(20),
  amount DECIMAL(15,2),
  balance_after DECIMAL(15,2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Dữ liệu mẫu
INSERT INTO accounts(balance) VALUES (2000000);
INSERT INTO cards VALUES ('1234567890', 1, SHA2('1234', 256));
