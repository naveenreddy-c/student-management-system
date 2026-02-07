from app import app, db, AuditLog
import certifi

with app.app_context():
    print("Migrating database schema...")
    
    # Drop the old audit_logs table
    try:
        db.session.execute(db.text("DROP TABLE IF EXISTS audit_logs"))
        db.session.commit()
        print("✓ Dropped old audit_logs table")
    except Exception as e:
        print(f"Note: {e}")
    
    # Recreate all tables with new schema
    db.create_all()
    print("✓ Created tables with new schema")
    print("\nMigration complete!")
