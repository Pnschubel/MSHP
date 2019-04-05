from flask import Flask, render_template, request, flash
import validation


app = Flask(__name__)

@app.route('/')
def form():
    return render_template('login.html')

@app.route('/result', methods = ['POST','GET'])
def result():
    if request.method == 'POST':
        result = request.form.to_dict() ##get into a dictionary
        for field,userinput in result.items(): 
            print(field, userinput)
            return render_template("result.html", result = result)


@app.route('/result', methods = ['POST','GET' ])
def testResult():
    if request.method == 'POST':
        error = None
        result = request.form.to_dict()
        ##the validation!:(

        ##see if data is entered into required fields
        if result[customerName] == 0 and result[customerEmail] == 1 and result[repairType] == 1:

            ##require repairDescription if repair type is othe
            if result[repairType] == "other":
                error = error + "

        

           
if __name__ == '__main__':
    app.run(debug = True)
