from  flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Employee(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(60),nullable=False)
    email=db.Column(db.String(60),nullable=False,unique=True)
    department=db.Column(db.String(60),nullable=False)


    def __repr__(self):
        return f'<Employee {self.name}>'