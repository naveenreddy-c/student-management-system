# 🗄️ DATABASE SETUP GUIDE

## Quick Start

The application automatically creates the database and tables on first run. However, here are manual setup options if needed.

## Option 1: Automatic Setup (Recommended)

1. Ensure MySQL is running
2. Configure `.env` file with your MySQL credentials:
   ```env
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=root
   DB_NAME=student_management
   ```
3. Run the Flask app - it will automatically create the database and tables
4. Done! The system is ready to use

## Option 2: Manual Setup with SQL Script

### Step 1: Start MySQL
```bash
# On Windows
mysql -u root -p

# On Mac/Linux
mysql -u root -p
```

### Step 2: Run the SQL Setup Script
```bash
# Option A: From command line
mysql -u root -p < database_setup.sql

# Option B: From within MySQL
mysql> source database_setup.sql;
```

### Step 3: Verify Installation
```sql
-- Check if database exists
SHOW DATABASES;

-- Switch to the database
USE student_management;

-- Check the table structure
DESCRIBE students;

-- View all students (should be empty initially)
SELECT * FROM students;
```

## Option 3: Manual SQL Commands

If you prefer to run commands individually:

```sql
-- Create the database
CREATE DATABASE IF NOT EXISTS student_management;

-- Switch to database
USE student_management;

-- Create the students table
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(15) NOT NULL,
    course VARCHAR(100) NOT NULL,
    enrollment_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email),
    INDEX idx_name (name),
    INDEX idx_course (course)
);
```

## MySQL Configuration (`.env` file)

Edit the `.env` file in the project root:

```env
# Database Configuration
DB_HOST=localhost              # MySQL server address
DB_USER=root                   # MySQL username
DB_PASSWORD=root                   # MySQL password (empty by default)
DB_NAME=student_management     # Database name

# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True
```

### Common Configurations

**Local Setup (Default)**
```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=root
DB_NAME=student_management
```

**With Password**
```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=root
DB_NAME=student_management
```

**Remote Database**
```env
DB_HOST=192.168.1.100
DB_USER=student_user
DB_PASSWORD=root
DB_NAME=student_management
```

## Database Schema Details

### Table: students

| Field | Type | Constraints | Description |
|-------|------|-----------|-------------|
| id | INT | PRIMARY KEY, AUTO_INCREMENT | Unique student identifier |
| name | VARCHAR(100) | NOT NULL | Student's full name |
| email | VARCHAR(100) | NOT NULL, UNIQUE | Student's email (must be unique) |
| phone | VARCHAR(15) | NOT NULL | Student's phone number |
| course | VARCHAR(100) | NOT NULL | Course name |
| enrollment_date | DATE | NOT NULL | Date of enrollment |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation time |
| updated_at | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Record update time |

### Indexes for Performance
- `idx_email`: Fast lookups by email
- `idx_name`: Fast searches by name
- `idx_course`: Fast filtering by course

## Adding Sample Data

To populate the database with sample students:

```sql
USE student_management;

INSERT INTO students (name, email, phone, course, enrollment_date) VALUES
('John Doe', 'john.doe@example.com', '9876543210', 'Computer Science', '2024-01-15'),
('Jane Smith', 'jane.smith@example.com', '9876543211', 'Information Technology', '2024-01-20'),
('Mike Johnson', 'mike.johnson@example.com', '9876543212', 'Business Administration', '2024-02-01'),
('Sarah Williams', 'sarah.williams@example.com', '9876543213', 'Mechanical Engineering', '2024-02-05'),
('Tom Brown', 'tom.brown@example.com', '9876543214', 'Civil Engineering', '2024-02-10');
```

## Verify Your Setup

Run these commands to verify everything is working:

```sql
-- Check database exists
SHOW DATABASES LIKE 'student_management';

-- Check table exists
USE student_management;
SHOW TABLES;

-- Check table structure
DESCRIBE students;

-- Count records
SELECT COUNT(*) as total_students FROM students;

-- View all records
SELECT * FROM students;
```

## Troubleshooting

### "ERROR 1045: Access denied"
- **Problem**: Wrong username or password
- **Solution**: Check MySQL credentials in `.env` file
- **Try**: `mysql -u root -p` and enter your password

### "ERROR 1049: Unknown database"
- **Problem**: Database doesn't exist
- **Solution**: Run the SQL setup script or let the app create it automatically

### "ERROR 1064: Syntax error"
- **Problem**: SQL syntax error
- **Solution**: Check the SQL script syntax
- **Try**: Run commands one by one to find the issue

### "ERROR 1062: Duplicate entry"
- **Problem**: Email already exists
- **Solution**: Use a different email address (must be unique)

### "Can't connect to MySQL server"
- **Problem**: MySQL service is not running
- **Solution**: 
  - Windows: Start MySQL service from Services
  - Mac: `brew services start mysql`
  - Linux: `sudo service mysql start`

## Backup & Restore

### Backup Database
```bash
mysqldump -u root -p student_management > backup.sql
```

### Restore Database
```bash
mysql -u root -p student_management < backup.sql
```

## Performance Tips

1. **Indexes**: Already created for common queries (email, name, course)
2. **Connection Pooling**: Consider implementing for production
3. **Query Optimization**: The app uses parameterized queries to prevent SQL injection
4. **Regular Backups**: Schedule periodic database backups

## Next Steps

1. ✅ Ensure MySQL is running
2. ✅ Configure `.env` with your credentials
3. ✅ Run the Flask app - database will be created automatically
4. ✅ Access the web interface at `http://localhost:5000`
5. ✅ Start adding student records!

---

**Note**: The Flask application handles database creation automatically on startup. You only need to ensure MySQL is running and the credentials are correct.
