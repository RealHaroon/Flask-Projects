from flask import Flask,render_template,request,redirect,url_for,flash     #type:ignore
from Components import app,db
from Components.models import Students,Grade


@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':

        roll_no=request.form['roll_no']
        name=request.form['name']
        department=request.form['department']
        email=request.form['email']
        student=Students(roll_no=roll_no,name=name,department=department,email=email)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('index'))
    students=Students.query.all()
    return render_template('index.html',students=students)



@app.route('/delete/<int:id>')
def delete_student(id):
    student=Students.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/update/<int:id>',methods=['POST'])
def update_student(id):
    student=Students.query.get_or_404(id)
    student.roll=request.form['roll_no']
    student.name=request.form['name']
    student.department=request.form['department']
    student.email=request.form['email']
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/add_grade/<int:student_id>',methods=['POST'])
def add_grade(student_id):
    subject=request.form['subject']
    score=request.form['score']
    grade=Grade(subject=subject,score=score,student_id=student_id)
    db.session.add(grade)
    db.session.commit()
    return redirect(url_for('index'))
