from flask import render_template, request, redirect, url_for, flash
from Components import app, db
from Components.models import Students, Grade

@app.route('/', methods=['GET', 'POST'])
def index():
    students = Students.query.all()
    edit_student = None

    if request.method == 'POST':
        form_id = request.form.get('edit_id')
        roll_no = request.form['roll_no']
        name = request.form['name']
        department = request.form['department']
        email = request.form['email']

        # Check duplicates
        roll_check = Students.query.filter(Students.roll_no == roll_no, Students.id != int(form_id or 0)).first()
        email_check = Students.query.filter(Students.email == email, Students.id != int(form_id or 0)).first()

        if roll_check:
            flash("Roll Number already exists", category='danger')
        elif email_check:
            flash("Email already exists", category='danger')
        else:
            if form_id:
                student = Students.query.get_or_404(form_id)
                student.roll_no = roll_no
                student.name = name
                student.department = department
                student.email = email
                flash("Student updated successfully!", category='success')
            else:
                new_student = Students(roll_no=roll_no, name=name, department=department, email=email)
                db.session.add(new_student)
                flash("Student added successfully!", category='success')

            db.session.commit()
            return redirect(url_for('index'))

    if request.args.get('edit'):
        edit_student = Students.query.get_or_404(request.args.get('edit'))

    return render_template('index.html', students=students, edit_student=edit_student)


@app.route('/delete/<int:id>')
def delete_student(id):
    student = Students.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash("Student deleted successfully!", category='success')
    return redirect(url_for('index'))


@app.route('/add_grade/<int:student_id>', methods=['POST'])
def add_grade(student_id):
    subject = request.form['subject']
    score = request.form['score']

    grade = Grade(subject=subject, score=score, student_id=student_id)
    db.session.add(grade)
    db.session.commit()
    flash("Grade added successfully!", category='success')
    return redirect(url_for('index'))
