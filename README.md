# Student Management System - Setup Guide

## Project Overview

A full-stack Student Management System built with:
- **Backend**: Flask (Python)
- **Database**: MySQL
- **Frontend**: HTML, CSS, JavaScript

## Features

✨ **Complete CRUD Operations**
- Create new student records
- Read and display all students
- Update existing student information
- Delete student records

📱 **User-Friendly Interface**
- Responsive design for all devices
- Real-time search functionality
- Form validation with error messages
- Modal dialogs for editing and deletion
- Professional UI with smooth animations

🔒 **Data Management**
- Database connectivity with error handling
- Form validation (name, email, phone, date)
- Duplicate email prevention
- Unique student IDs

## Project Structure

```
student-management-system/
├── app.py                 # Flask application with routes
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   ├── style.css         # CSS styling
│   └── script.js         # JavaScript functionality
└── README.md            # This file
```

## Prerequisites

- Python 3.7 or higher
- MySQL Server 5.7 or higher
- pip (Python package manager)

## Installation & Setup

### 1. Install Python Dependencies

```bash
cd student-management-system
pip install -r requirements.txt
```

### 2. Configure MySQL Database

Ensure MySQL is running. You can configure the database connection in the `.env` file:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=student_management
```

**Note**: The application will automatically create the database and table on first run if they don't exist.

### 3. Run the Flask Application

```bash
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

### 4. Access the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

## API Endpoints

### GET All Students
```
GET /api/students
Response: { "success": true, "data": [...] }
```

### GET Single Student
```
GET /api/students/<id>
Response: { "success": true, "data": {...} }
```

### CREATE Student
```
POST /api/students
Body: {
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "1234567890",
  "course": "Computer Science",
  "enrollment_date": "2024-01-15"
}
```

### UPDATE Student
```
PUT /api/students/<id>
Body: { same as POST }
```

### DELETE Student
```
DELETE /api/students/<id>
```

### SEARCH Students
```
GET /api/students/search/<query>
Example: GET /api/students/search/john
```

## Database Schema

### Students Table

| Column | Type | Description |
|--------|------|-------------|
| id | INT | Auto-incremented primary key |
| name | VARCHAR(100) | Student's full name (required, unique) |
| email | VARCHAR(100) | Student's email (required, unique) |
| phone | VARCHAR(15) | Student's phone number (required) |
| course | VARCHAR(100) | Course enrolled in (required) |
| enrollment_date | DATE | Date of enrollment (required) |
| created_at | TIMESTAMP | Record creation timestamp |
| updated_at | TIMESTAMP | Record last update timestamp |

## Form Validation Rules

### Name
- Required field
- Minimum 2 characters
- Only letters, spaces, hyphens, and apostrophes allowed

### Email
- Required field
- Must be a valid email format (contains @ and .)
- Must be unique in database

### Phone
- Required field
- Only digits allowed
- Minimum 10 digits
- Maximum 15 digits

### Course
- Required field
- Select from predefined list or other

### Enrollment Date
- Required field
- Cannot be in the future (max date is today)

## Features in Detail

### 1. Add Student
- Fill the form on the left sidebar
- Click "Add Student" to submit
- Validation ensures data quality
- Success/error messages displayed
- Form clears after successful submission

### 2. View Students
- All students displayed in a table
- Shows: ID, Name, Email, Phone, Course, Enrollment Date
- Sorted by ID (newest first)
- Empty state message when no students exist

### 3. Search Students
- Real-time search functionality
- Search by name, email, phone, or course
- Results update instantly as you type
- Clear search to view all students

### 4. Edit Student
- Click "Edit" button in the table
- Modal opens with student details
- Modify any field
- Submit to save changes
- Validation applied to all fields

### 5. Delete Student
- Click "Delete" button in the table
- Confirmation modal appears
- Click "Delete" to confirm
- Student removed from database

## Troubleshooting

### "Error connecting to MySQL"
- Ensure MySQL server is running
- Check database credentials in `.env`
- Verify database host is correct

### "Port 5000 already in use"
- Change the port in app.py:
  ```python
  app.run(port=5001)  # Use different port
  ```

### "ModuleNotFoundError"
- Install missing dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### Database Not Created
- The app creates the database automatically
- If it fails, create manually:
  ```sql
  CREATE DATABASE student_management;
  ```

## Development Notes

- Debug mode is enabled by default (set `FLASK_DEBUG=False` in .env for production)
- CORS is enabled for cross-origin requests
- All database connections are properly closed
- Input sanitization prevents SQL injection
- Form data is validated on both client and server

## Security Considerations

✅ Input validation on frontend and backend
✅ SQL injection prevention with parameterized queries
✅ Email uniqueness constraint in database
✅ XSS prevention with HTML escaping
✅ Error messages don't expose sensitive information

## Browser Compatibility

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## License

This project is open source and available for educational purposes.

## Support

For issues or questions, please check the console logs and error messages displayed in the application.

---

**Version**: 1.0.0  
**Last Updated**: 2026-02-05
