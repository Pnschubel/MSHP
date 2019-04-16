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
        ok = "True"

        if ok == "True":

            ##if required fields arent filled out
            if hasData(result[customerName]) == 0 and hasData(result[customerEmail])  == 0 and hasData(result[repairType])  == 0:
                error = error + "required data /n"
                ok = "False"

            ##require repairDescription if repair type is other
            if result[repairType] == "other":
                if hasData(result[repairDescription]) == 0: 
                    error = error + "repair description /n"
                    ok = "False"

            ##require vin if year,make,model is null
            if hasData(result[make]) == 0 and hasData(result[model]) == 0 and hasData(result[year]) == 0:
                ##if vin is empty incorrect
                if hasData(result[vin]) == 0:
                    error = error + "vehicle vin or vehicle make,model and year /n"
                    ok = "False"
                else:
                    ## if vin number is entered incorrectly
                    if vinNumber(result[vin]) == 0: 
                        error = error + "vin number is incorrect"
                        ok = "False"

            ##check year,make,model if vin is empty
            if hasData(result[vin]) == 0:
                ##check make
                if hasData(result[make]) == 0:
                    error = error + 



            

        ##see if ok variable is true false - see if you flash error or confirmation message:
        if ok == "False":
            flash("Must include: "+ error)
        else:
            flash("Your form was successfully submitted!") 




           
if __name__ == '__main__':
    app.run(debug = True)
