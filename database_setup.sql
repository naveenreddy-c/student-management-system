CREATE DATABASE IF NOT EXISTS student_management;
USE student_management;

-- USERS TABLE
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) DEFAULT 'staff'
);

-- STUDENTS TABLE
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    course VARCHAR(100)
);

-- DEFAULT ADMIN USER
INSERT IGNORE INTO users (username, password, role)
VALUES ('admin', 'admin', 'admin');

-- DEFAULT STAFF USER
INSERT IGNORE INTO users (username, password, role)
VALUES ('staff', 'staff', 'staff');
