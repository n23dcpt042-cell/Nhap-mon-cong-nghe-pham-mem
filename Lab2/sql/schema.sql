-- schema.sql (MySQL / InnoDB)
CREATE DATABASE IF NOT EXISTS hotel_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hotel_db;

CREATE TABLE Guest (
  GuestID INT AUTO_INCREMENT PRIMARY KEY,
  Name VARCHAR(150) NOT NULL,
  Phone VARCHAR(30),
  Email VARCHAR(150),
  Address VARCHAR(255),
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE RoomType (
  TypeID INT AUTO_INCREMENT PRIMARY KEY,
  Name VARCHAR(100) NOT NULL,
  Price DECIMAL(10,2) NOT NULL,
  Capacity INT NOT NULL,
  Description TEXT,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE Room (
  RoomID INT AUTO_INCREMENT PRIMARY KEY,
  TypeID INT NOT NULL,
  RoomNumber VARCHAR(20) UNIQUE NOT NULL,
  Status ENUM('available','held','occupied','maintenance') DEFAULT 'available',
  Floor INT,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (TypeID) REFERENCES RoomType(TypeID) ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB;

CREATE TABLE Staff (
  StaffID INT AUTO_INCREMENT PRIMARY KEY,
  Name VARCHAR(150) NOT NULL,
  Role ENUM('receptionist','manager','housekeeping') DEFAULT 'receptionist',
  Username VARCHAR(100) UNIQUE,
  PasswordHash VARCHAR(255),
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE Reservation (
  ResvID INT AUTO_INCREMENT PRIMARY KEY,
  GuestID INT NOT NULL,
  RoomID INT,
  StaffID INT,
  CheckInDate DATE NOT NULL,
  CheckOutDate DATE NOT NULL,
  Status ENUM('pending','confirmed','checked_in','checked_out','cancelled') DEFAULT 'pending',
  HoldExpiresAt DATETIME DEFAULT NULL,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (GuestID) REFERENCES Guest(GuestID) ON DELETE CASCADE,
  FOREIGN KEY (RoomID) REFERENCES Room(RoomID) ON DELETE SET NULL,
  FOREIGN KEY (StaffID) REFERENCES Staff(StaffID) ON DELETE SET NULL
) ENGINE=InnoDB;

CREATE TABLE Payment (
  PaymentID INT AUTO_INCREMENT PRIMARY KEY,
  ResvID INT NOT NULL,
  Amount DECIMAL(10,2) NOT NULL,
  Method ENUM('card','paypal','cash') DEFAULT 'card',
  Status ENUM('initiated','success','failed','refunded') DEFAULT 'initiated',
  PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  TransactionRef VARCHAR(255),
  FOREIGN KEY (ResvID) REFERENCES Reservation(ResvID) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Indexes
CREATE INDEX idx_resv_guest ON Reservation(GuestID);
CREATE INDEX idx_resv_room ON Reservation(RoomID);
CREATE INDEX idx_room_type ON Room(TypeID);
