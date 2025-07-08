from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY']='ed1b23547159b7b11c3cac01'
db=SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager=LoginManager(app) # login Functionality in Flask app
login_manager.login_view = "login" # it will redirect user to login page and prevent user to got to the market page
login_manager.login_message_category= 'info'
from Components import Routes

# taskkill /F /IM python.exe