from flask import Flask, render_template, redirect, url_for

from . import app
from .forms import EmailPasswordForm 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('DumbyPage.html')

def login():
    form = LoginForm()
    if form.validate_on_submit():
        
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0")