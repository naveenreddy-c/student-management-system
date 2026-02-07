from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from app import db
from app.models import Student

bp = Blueprint('students', __name__)

@bp.route('/students')
@login_required
def list():
    students = Student.query.order_by(Student.created_at.desc()).all()
    return render_template('students/list.html', students=students)

@bp.route('/students/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        course = request.form['course']
        
        if Student.query.filter_by(email=email).first():
            flash('Email already registered for another student')
            return redirect(url_for('students.add'))
            
        student = Student(name=name, email=email, course=course)
        db.session.add(student)
        db.session.commit()
        flash('Student added successfully')
        return redirect(url_for('students.list'))
        
    return render_template('students/add.html')

@bp.route('/students/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    student = Student.query.get_or_404(id)
    if request.method == 'POST':
        student.name = request.form['name']
        original_email = student.email
        student.email = request.form['email']
        student.course = request.form['course']
        
        if student.email != original_email and Student.query.filter_by(email=student.email).first():
            flash('Email already registered for another student')
            return redirect(url_for('students.edit', id=id))

        db.session.commit()
        flash('Student details updated')
        return redirect(url_for('students.list'))
        
    return render_template('students/edit.html', student=student)

@bp.route('/students/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash('Student deleted')
    return redirect(url_for('students.list'))
