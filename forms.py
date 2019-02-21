from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email

from .util.validators import Unique
from .models import User

class EmailPasswordForm(Form):
    email = StringField('Email', validators = [DataRequired(), Email(),
                            Unique(
                                User,
                                User.email,
                                message= 'There is already an account with that email.'])
    password = PasswordField('Password', validators = [DataRequired()])