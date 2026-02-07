import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

# Load environment variables from .env
load_dotenv()

# Get database credentials from environment variables
db_host = os.getenv('DB_HOST', 'localhost')
db_user = os.getenv('DB_USER', 'root')
db_password = os.getenv('DB_PASSWORD', 'root')

try:
    # Connect to MySQL server without specifying a database
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password
    )
    
    cursor = conn.cursor()
    
    # Drop the database if it exists
    cursor.execute("DROP DATABASE IF EXISTS student_management;")
    conn.commit()
    
    print("Database deleted. Run python app.py to recreate it.")
    
    cursor.close()
    conn.close()
    
except Error as e:
    print(f"Error: {e}")
