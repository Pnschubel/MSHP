from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    firstName = StringField('firstName', validators = [DataRequired()])
    lastName = PasswordField('lastName', validators = [DataRequired()])