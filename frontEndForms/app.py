
from flask import Flask, render_template, request, validation

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('login.html')

##@app.route('/result', methods = ['POST','GET'])
##def result():
##    if request.method == 'POST':
##        result = request.form.to_dict() ##gets form from form()??
##        for field,userinput in result.items(): 
##            print(field, userinput)
##        return render_template("result.html", result = result)

@app.route('/testResult' methods = ['POST',"GET"])
def testResult():
    if request.method == 'POST':
        result = request.form.to_dict()
        for field, userinput in result.items():
            ##checks email
            if field == 'email':
                if emailchecker(userInput) == 0:



            print (field, userinput)
        return render_template("result.html", result = result)

if __name__ == '__main__':
    app.run(debug = True)
