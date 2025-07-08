from flask import Flask,render_template,request,redirect,url_for,flash
from models import db,Employee


app = Flask(__name__)
app.secret_key='haroon-secret-123'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///employee.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# create table inside database ( once )
# with app.app_context():
#     db.create_all()

    
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        department=request.form['department']

        #Basic backend Validations
        if not name or not email or not department:
            flash("All field are required.")
        if '@' not in email or '.' not in email:
            flash("Invalid Email Adress")
        existing = Employee.query.filter_by(email=email).first()
        if existing:
            flash("Email already Exists")
        


        new_employee= Employee(name=name,email=email,department=department)
        db.session.add(new_employee)
        db.session.commit()
        flash("Employee added successfully!")
        return redirect(url_for('home'))

    employees = Employee.query.all()
    return render_template('index.html',employees=employees)


@app.route('/delete/<int:id>')
def delete(id):
    emp=Employee.query.get_or_404(id)
    db.session.delete(emp)
    db.session.commit()
    flash("Employee deleted successfully!")
    return redirect(url_for('home'))


@app.route('/edit/<int:id>',methods=['GET','POST'])
def edit(id):
    emp=Employee.query.get_or_404(id)

    if request.method=='POST':
        emp.name=request.form['name']
        emp.email=request.form['email']
        emp.department=request.form['department']
        db.session.commit()
        flash("Employee updated successfully!")
        return redirect(url_for('home'))
    employees=Employee.query.all()
    return render_template('index.html',employees=employees,edit_emp=emp)
if __name__ == '__main__':
    app.run(debug=True)

