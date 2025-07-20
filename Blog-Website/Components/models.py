from Components import db
from datetime import datetime

class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    slug=db.Column(db.String(120),unique=True,nullable=False)
    content=db.Column(db.Text,nullable=False)
    author=db.Column(db.String(50),defualt='Admin')
    category=db.Column(db.String(50),nullable=True)
    created_at=db.Column(db.Datetime,default=datetime.now)
    updated_at=db.Column(db.Datetime,defualt=datetime.now)
    