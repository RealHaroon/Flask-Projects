from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app=Flask(__name__)
app.config['SECRET_KEY'] = 'haroon-secret-key'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

from Components import routes