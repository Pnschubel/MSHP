from flask import Flask, render_template, request
import validation

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

@app.route('/result', methods = ['POST','GET' ])
def testResult():
    if request.method == 'POST':
        result = request.form.to_dict()
        for field, userinput in result.items():
            ##checks email
            if field == 'email':
                if hasData(userInput) == 0 or emailChecker(userInput) == 0:
                    ##email is wrong
            ##check vim 
            if field == 'vinNumber':
                if vinNumber(userInput) == 0 and hasData(userInput):
                    ##vin number is wrong
            if field == 'customerName' and field == 'model' and field == 'make' and field == 'repairType' and field == "repairDescription":
                if hasData(userInput) == 0: 
                    ##name, model, make, repairType, and decription is wrong
            if field == 'year': 
                if hasData(userInput) == 0 and isintance(userInput, (int)):
                    ##year is wrong
    else:
        print (field, userinput)
        return render_template("errorPage.html", result = result)

if __name__ == '__main__':
    app.run(debug = True)
