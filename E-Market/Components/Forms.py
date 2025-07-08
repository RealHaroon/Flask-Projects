from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from Components.Models  import User

class RegisterForm(FlaskForm):


    def validate_username(self,username_to_check):
        user=User.query.filter_by(userName=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username.')
    def validate_email_address(self, email_address_to_check):
     email = User.query.filter_by(email_address=email_address_to_check.data).first()
     if email:
        raise ValidationError('Email address already exists! Please try a different one.')

    username = StringField(label='User Name', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators=[Length(min=6, max=20), DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


#* Firstly Created  a form using wtforms and flask_wtf
#* created a method of feilds

#* then created a table inside database 

#* then added route with validation and actions 

class LoginForm(FlaskForm):
    username = StringField(label='User Name', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')


class PurchaseItemForm(FlaskForm):
   submit = SubmitField(label='Purchase Item')

class SellItemForm(FlaskForm):
   submit = SubmitField(label='Sell Item')