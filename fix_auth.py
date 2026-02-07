from app import app, db, User
import certifi

with app.app_context():
    print("Checking users...")
    admin = User.query.filter_by(username='admin').first()
    if admin:
        print(f"Admin found. Current password length: {len(admin.password)}")
        # Reset to plain text 'admin'
        admin.password = 'admin'
        db.session.commit()
        print("Admin password reset to 'admin' (plain text).")
    else:
        print("Admin not found. Creating...")
        new_admin = User(username='admin', password='admin', role='admin')
        db.session.add(new_admin)
        db.session.commit()
        print("Admin user created with password 'admin'.")
        
    # Also check staff
    staff = User.query.filter_by(username='staff').first()
    if staff:
        staff.password = 'staff'
        db.session.commit()
        print("Staff password reset to 'staff'.")
    else:
         db.session.add(User(username='staff', password='staff', role='staff'))
         db.session.commit()
         print("Staff user created.")
