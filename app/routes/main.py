from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import Student

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    student_count = Student.query.count()
    return render_template('index.html', student_count=student_count)
