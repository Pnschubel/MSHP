from wtforms import Form, BooleanField, StringField, PasswordField, validators 

class myForm(form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', [validators.DataRequired()])

