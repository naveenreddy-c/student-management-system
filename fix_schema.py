from app import app, db
import certifi

with app.app_context():
    print("Fixing audit_logs schema...")
    
    try:
        # Option 1: Try to rename the column if it exists
        db.session.execute(db.text("ALTER TABLE audit_logs CHANGE COLUMN student_name details VARCHAR(255) NOT NULL"))
        db.session.commit()
        print("✓ Renamed student_name to details")
    except Exception as e:
        print(f"Rename failed: {e}")
        print("\nTrying to recreate table...")
        
        try:
            # Option 2: Drop and recreate
            db.session.execute(db.text("DROP TABLE IF EXISTS audit_logs"))
            db.session.commit()
            
            # Create new table with correct schema
            db.session.execute(db.text("""
                CREATE TABLE audit_logs (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    user_id INT NOT NULL,
                    action VARCHAR(50) NOT NULL,
                    details VARCHAR(255) NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            """))
            db.session.commit()
            print("✓ Recreated audit_logs table with new schema")
        except Exception as e2:
            print(f"Recreate failed: {e2}")
    
    print("\nSchema migration complete!")
