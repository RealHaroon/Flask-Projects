from  Components import db

class Students(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    roll_no=db.Column(db.String(20),unique=True,nullable=False)
    name=db.Column(db.String(60),unique=True,nullable=False)
    department=db.Column(db.String(60))
    email=db.Column(db.String(100),unique=True)
    grades=db.relationship('Grade',backref='student',cascade="all,delete-orphan")

class Grade(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    subject=db.Column(db.String(50))
    score=db.Column(db.Float)
    student_id=db.Column(db.Integer,db.ForeignKey('students.id'))


    def __repr__(self):
        return f'Item {self.name}'
    