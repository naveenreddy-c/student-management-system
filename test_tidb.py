
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

def test_connection():
    print("Testing connection to TiDB...")
    db_config = {
        'host': os.getenv('DB_HOST'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'port': int(os.getenv('DB_PORT', 4000)),
        'database': os.getenv('DB_NAME')
    }
    
    # Mask password for printing
    print_config = db_config.copy()
    print_config['password'] = '******'
    print(f"Configuration: {print_config}")
    
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            print("Successfully connected to TiDB via MySQL Protocol!")
            cursor = conn.cursor()
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone()
            print(f"Database/TiDB Version: {version[0]}")
                
            conn.close()
        else:
            print("Connected but connection object says not connected.")

    except Error as e:
        print(f"Error connecting to TiDB: {e}")

if __name__ == "__main__":
    test_connection()
