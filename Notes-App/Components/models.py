from Components import db

from datetime import datetime

class Note(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    content=db.Column(db.Text,nullable=False)
    created_at=db.Column(db.DateTime,default=datetime.now)
    updated_at=db.Column(db.DateTime,default=datetime.now,onupdate=datetime.now)



    def __repr__(self):
      return f'Item {self.name}'
    