from flask import render_template. redirect. url_for
from . import app
from .forms import EmailPasswordForm

@app.route('/login', methods=["GET","POST"])
def login():
    form = EmailPasswordForm()
    if form.validate_on_submit();
    