from flask import Flask, render_template, request, flash
from validation import validation

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('login.html')


@app.route('/result', methods = ['POST','GET' ])
def result():
    if request.method == 'POST':
        error = None
        result = request.form.to_dict()
        print (result)
        print ("hello")
        ##the validation!:(
        ok = "True"

        if ok == "True":

            ##if required fields arent filled out
            if validation.hasData(result['customerName']) == 0 and validation.hasData(result['customerEmail'])  == 0 and validation.hasData(result['repairType'])  == 0 and validation.hasData(result[repairType]) == 0:
                error = error + "required data /n"
                ok = "False"

            ##require repairDescription if repair type is other
            if result['repairType'] == "other":
                if validation.hasData(result[repairDescription]) == 0: 
                    error = error + "repair description /n"
                    ok = "False"

            ##require vin if year,make,model is null
            if validation.hasData(result['make']) == 0 and validation.hasData(result['model']) == 0 and validation.hasData(result['year']) == 0:
                ##if vin is empty incorrect
                if validation.hasData(result['vin']) == 0:
                    error = error + "vehicle vin or vehicle make,model and year /n"
                    ok = "False"
                else:
                    ## if vin number is entered incorrectly
                    if validation.vinNumber(result['vin']) == 0: 
                        error = error + "vin number is incorrect"
                        ok = "False"

            ##check year,make,model if vn is empty
            if validation.hasData(result['vin']) == 0:
                ##check make
                if validation.hasData(result['make']) == 0:
                    error = error + "Vehicle make is required /n"
                    ok = "False" 
                if validation.hasData(result['model']) == 0: 
                    error = error + "Vehicle model is required /n"
                    ok = "False" 
                if validation.hasData(result['year']) == 0: 
                        error = error + "Vehicle year is required /n"
                        ok = "False" 

            ##check if the email is correct
            if validation.hasData(result['customerEmail']) == 0 and validation.emailChecker(result['customerEmail']) == 0:
                error = error + "Email is invalid /n"


            

        ##see if ok variable is true false - see if you flash error or confirmation message:
        if ok == "False":
            flash("Must include: "+ error)
        else:
            flash("Your form was successfully submitted!") 

    return render_template("login.html",error=error)
  
if __name__ == '__main__':
    app.run(debug = True)
