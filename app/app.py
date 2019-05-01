from flask import Flask, render_template, request, flash
import validation 
##from app import create_app

app = Flask(__name__)

##create_app()
app.config['SECRET_KEY'] = 'hanas password'

@app.route('/')
def form():
    return render_templater('login.html')

@app.route('/result', methods = ['POST','GET' ])
def result():
    if request.method == 'POST':
        result = request.form.to_dict()
       
        ##the validation!:(
        ok = "True"
        
        if ok == "True":
            ##if required fields arent filled out
            if validation.hasData(result['customerName']) == 0:
                print("required name")
                flash("required name")

                ok = "False"

            if  validation.hasData(result['customerEmail'])  == 0:
                print("required email")
                flash("required email")
                ok = "False"

            if validation.hasData(result['repairType'])  == 0:
                print("required fields aint filled out")
                flash("required repairType")
                ok = "False"

            ##require repairDescription if repair type is other
            if result['repairType'] == "other":
                if validation.hasData(result['repairDescription']) == 0: 
                    print("require repair description")
                    flash("required email")
                    ok = "False"

            ##require vin if year,make,model is null
            if validation.hasData(result['make']) == 0 and validation.hasData(result['model']) == 0 and validation.hasData(result['year']) == 0:
                ##if vin is empty incorrect
                if validation.hasData(result['vin']) == 0:
                    flash("vehicle vin or vehicle make,model and year")
                    ok = "False"
                else:
                    ## if vin number is entered incorrectly
                    if validation.vinNumber(result['vin']) == 0: 
                        flash("vin number is incorrect")
                        ok = "False"

            ##check year,make,model if vn is empty
            if validation.hasData(result['vin']) == 0:
                
                ##check make
                if validation.hasData(result['make']) == 0:
                    flash("Vehicle make is required")
                    ok = "False" 
                if validation.hasData(result['model']) == 0: 
                    flash("Vehicle model is required")
                    ok = "False" 
                if validation.hasData(result['year']) == 0: 
                        flash("Vehicle year is required")
                        ok = "False" 

            ##check if the email is correct
            if validation.hasData(result['customerEmail']) == 0 and validation.emailChecker(result['customerEmail']) == 0:
                    flash("Email is invalid")
                    print ("this email is WRONG")


            
    return render_template("login.html")
  
if __name__ == '__main__':
    app.run(debug = True)
    
