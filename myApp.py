import os
from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from flask_mail import Mail, Message
from app import create_app

#This NEEDS to Stay at TOP of This File. If You Move it, I Will be VERY MAD AT YOU! Be Warned...
app = create_app()
app.config['SECRET_KEY'] = 'superSecretGlobalKey'

#Change the template directory for render_template
template_dir = os.path.abspath("./app/templates")

#Mailing
#----------------------------------------------------------------------------------

#Config SMTP with App
with app.app_context():
    mail = Mail(app)
    app.config['MAIL_SERVER'] = 'smtp.gmail.com' #This sends requst to google
    app.config['MAIL_PORT'] = 465 #This is required for the server
    app.config['MAIL_USERNAME'] = 'nchsauto@gmail.com' #Associates sender address
    app.config['MAIL_PASSWORD'] = 'nchsautomail' #Validates sender with password
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    mail = Mail(app)
    print("See")
    
#Create Mailing Function
def sendEmail(title, html_code, target):
    msg = Message(title, sender = 'NCHS Auto Shop', recipients = [target])
    msg.html = html_code
    mail.send(msg)

    
#Routing
#----------------------------------------------------------------------------------
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
            if validation.emailChecker(result['customerEmail']) == "False":
                    flash("Email is invalid")
                    print ("this email is WRONG")
            
    return render_template("login.html")

#Test Mailing
@app.route("/test_sendEmail")
def test_sendEmail():
    htmlCode = ('<p style="background-color: #ff00ff;"> ...Hello i am a pink rectangle... </p>')
    sendEmail("Test W/Parameters", render_template("EmailTemplate.html"), "spkudrna@gmail.com")
    return("...Email Sent...")

#This NEEDS to Stay at BOTTOM of This File. If You Move it, I Will be VERY MAD AT YOU! Be Warned...
if __name__ == "__main__":
    app.run(debug=True)
