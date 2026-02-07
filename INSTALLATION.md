# 🚀 Student Management System - Complete Installation Guide

## Prerequisites Checklist

- ✅ Python 3.7 or higher installed
- ✅ MySQL Server 5.7 or higher installed and running
- ✅ pip (Python package manager)
- ✅ Text editor or IDE (VS Code recommended)

---

## Step 1: Verify Prerequisites

### Check Python Installation
```bash
python --version
# or
python3 --version
```
**Expected Output**: Python 3.7.0 or higher

### Check MySQL Installation
```bash
mysql --version
```
**Expected Output**: MySQL version 5.7.0 or higher

---

## Step 2: Install Python Dependencies

Navigate to the project directory:
```bash
cd d:\naveen\Java\student-management-system
```

Install all required packages:
```bash
pip install -r requirements.txt
```

**Packages that will be installed:**
- Flask 2.3.0 - Web framework
- Flask-CORS 4.0.0 - Cross-origin requests support
- mysql-connector-python 8.0.33 - MySQL database connector
- python-dotenv 1.0.0 - Environment variable management
- Werkzeug 2.3.0 - WSGI utilities

Verify installation:
```bash
pip list
```

---

## Step 3: Configure Database Connection

### 3.1 Start MySQL Server

**Windows:**
```bash
# Option 1: Using Services
# Open Services app and start "MySQL80" or similar

# Option 2: Command line
mysql -u root -p
# Enter your password when prompted
```

**Mac:**
```bash
brew services start mysql
```

**Linux:**
```bash
sudo service mysql start
```

### 3.2 Configure `.env` File

Edit the `.env` file in the project root directory:

```env
# Database Configuration
DB_HOST=localhost           # MySQL server address
DB_USER=root               # MySQL username
DB_PASSWORD=root               # Your MySQL password (if any)
DB_NAME=student_management # Database name

# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True
```

**Common scenarios:**

**Scenario A: MySQL with no password (default)**
```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=root
DB_NAME=student_management
```

**Scenario B: MySQL with password**
```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=root
DB_NAME=student_management
```

**Scenario C: Remote MySQL server**
```env
DB_HOST=192.168.1.100
DB_USER=root
DB_PASSWORD=root
DB_NAME=student_management
```

---

## Step 4: Create Database (Two Options)

### Option A: Automatic (Recommended)
The Flask app will automatically create the database when you run it for the first time.

### Option B: Manual Setup
If you prefer to create the database manually:

```bash
# Start MySQL
mysql -u root -p

# Run the setup script inside MySQL
mysql> source database_setup.sql;

# Or run from command line
mysql -u root -p < database_setup.sql
```

---

## Step 5: Run the Application

Start the Flask development server:

```bash
python app.py
```

**Expected output:**
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

If port 5000 is busy, you can use a different port:
```bash
# Edit app.py and change the port:
app.run(debug=True, host='0.0.0.0', port=5001)
```

---

## Step 6: Access the Application

Open your web browser and go to:
```
http://localhost:5000
```

You should see the Student Management System interface!

---

## Directory Structure

After installation, your project should look like this:

```
student-management-system/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── .env                     # Configuration file
├── database_setup.sql       # Database setup script
├── README.md                # Project documentation
├── DATABASE_SETUP.md        # Database guide
├── INSTALLATION.md          # This file
├── templates/
│   └── index.html           # Main HTML template
└── static/
    ├── style.css            # Styling
    └── script.js            # JavaScript functionality
```

---

## Testing the Installation

### 1. Test Database Connection

The app will test the connection on startup. You should see:
```
Database 'student_management' created or already exists
Students table created or already exists
```

### 2. Test CRUD Operations

1. **Create**: Fill the form and click "Add Student"
2. **Read**: View students in the table
3. **Update**: Click "Edit" button to modify a student
4. **Delete**: Click "Delete" button to remove a student
5. **Search**: Use the search bar to find students

---

## Troubleshooting

### Problem: ModuleNotFoundError: No module named 'flask'

**Solution**: Reinstall dependencies
```bash
pip install -r requirements.txt --force-reinstall
```

### Problem: "Can't connect to MySQL server on 'localhost'"

**Solutions:**
1. Verify MySQL is running
2. Check username and password in `.env`
3. Verify `DB_HOST` is correct (usually `localhost`)
4. Try creating a manual connection:
   ```bash
   mysql -u root -p -h localhost
   ```

### Problem: "Error creating database: Access denied"

**Solutions:**
1. Check MySQL user permissions
2. Use a user with database creation privileges
3. Create database manually:
   ```bash
   mysql -u root -p
   > CREATE DATABASE student_management;
   ```

### Problem: "Port 5000 already in use"

**Solutions:**
1. Find what's using port 5000:
   ```bash
   # Windows
   netstat -ano | findstr :5000
   
   # Mac/Linux
   lsof -i :5000
   ```
2. Change port in `app.py`
3. Or kill the process using the port

### Problem: "No module named 'dotenv'"

**Solution**:
```bash
pip install python-dotenv
```

### Problem: Form validation errors

**Check:**
1. Email format (must contain @ and .)
2. Phone number (must be 10-15 digits only)
3. All fields are filled
4. Enrollment date is not in the future

---

## Development vs Production

### Development Mode (Current Setup)
```python
FLASK_DEBUG=True      # Auto-reload on code changes
FLASK_ENV=development # Shows detailed error messages
```

### Production Mode
```python
FLASK_DEBUG=False     # No auto-reload
FLASK_ENV=production  # Minimal error messages
```

To switch to production, update `.env`:
```env
FLASK_ENV=production
FLASK_DEBUG=False
```

---

## Next Steps

1. ✅ Install dependencies
2. ✅ Configure MySQL connection
3. ✅ Create database
4. ✅ Run the application
5. 🚀 Start using the system!

## Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [Python Documentation](https://docs.python.org/)

## Support

If you encounter any issues:
1. Check the error message in the terminal
2. Review the Troubleshooting section above
3. Verify all prerequisites are installed
4. Check the `.env` configuration

---

**Version**: 1.0.0  
**Last Updated**: 2026-02-05  
**Status**: Ready to use! 🎉
