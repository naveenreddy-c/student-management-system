
import os
import certifi
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

# Load Env
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-random-secret')

# Database Config (TiDB / MySQL)
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Robust SSL for TiDB & Windows using certifi
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "connect_args": {
        "ssl": {
            "ca": certifi.where(),
            "check_hostname": True,
            "verify_mode": "CERT_REQUIRED"
        }
    }
}

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'error' # Shows flash as error by default if needed

# --- Models ---
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), default='staff') # 'admin' or 'staff'

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    course = db.Column(db.String(100))
    enrollment_date = db.Column(db.DateTime, default=datetime.utcnow)

class AuditLog(db.Model):
    __tablename__ = 'audit_logs'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    action = db.Column(db.String(50), nullable=False) # 'Added' / 'Deleted'
    student_name = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref=db.backref('logs', lazy=True))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# --- Routes ---
@app.route('/')
@login_required
def dashboard():
    # Only Admin sees logic. Staff sees normal list.
    students = Student.query.order_by(Student.enrollment_date.desc()).all()
    
    logs = []
    if current_user.role == 'admin':
        logs = AuditLog.query.order_by(AuditLog.timestamp.desc()).limit(20).all()
        
    return render_template('dashboard.html', students=students, logs=logs, user=current_user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            # flash('Welcome back!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'error')
            
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/add_student', methods=['POST'])
@login_required
def add_student():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    course = request.form.get('course')
    
    if not name or not email:
        flash('Name and Email are mandatory.', 'error')
        return redirect(url_for('dashboard'))
        
    if Student.query.filter_by(email=email).first():
        flash('Student email already exists.', 'error')
        return redirect(url_for('dashboard'))
        
    s = Student(name=name, email=email, phone=phone, course=course)
    db.session.add(s)
    
    # Audit
    log = AuditLog(user_id=current_user.id, action="Added", student_name=name)
    db.session.add(log)
    
    db.session.commit()
    flash('Student added successfully.', 'success')
    return redirect(url_for('dashboard'))

@app.route('/delete_student/<int:id>', methods=['POST'])
@login_required
def delete_student(id):
    s = Student.query.get_or_404(id)
    s_name = s.name
    
    db.session.delete(s)
    
    # Audit
    log = AuditLog(user_id=current_user.id, action="Deleted", student_name=s_name)
    db.session.add(log)
    
    db.session.commit()
    flash('Student deleted.', 'success')
    return redirect(url_for('dashboard'))

# --- Startup ---
def init_db():
    with app.app_context():
        try:
            db.create_all()
            # Ensure Admin
            if not User.query.filter_by(username='admin').first():
                pw = generate_password_hash('admin')
                admin = User(username='admin', password=pw, role='admin')
                db.session.add(admin)
                db.session.commit()
                print("Admin user created.")
        except Exception as e:
            print(f"DB Init Error: {e}")

if __name__ == '__main__':
    init_db()
    app.run(debug=True)