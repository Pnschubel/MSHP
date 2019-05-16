import os
from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from flask_mail import Mail, Message
from app import create_app
from app import validation
from app import toolkit

#This NEEDS to Stay at TOP of This File. If You Move it, I Will be VERY MAD AT YOU! Be Warned...
app = create_app()
app.config['SECRET_KEY'] = 'superSecretGlobalKey'




#Change the template directory for render_template
template_dir = os.path.abspath("./app/templates")




#Mailing
#--------------------------------------------------------------------------------------------

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
#----------------------------------------------------------------------------------------------
@app.route('/')
def form():
    return render_template('login.html')

@app.route('/result', methods = ['POST','GET' ])
def result():
    if request.method == 'POST':
        result = request.form.to_dict()
#----------------------------------------------------------------------------------------------




#Validation
#----------------------------------------------------------------------------------------------
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
            
            if validation.hasData(result['vin']) == 1:
                ## if vin number is entered incorrerctly
                if validation.vinNumber(result['vin']) == 0: 
                    flash("vin number is invalid")
                    ok = "False"
                
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

            if ok == "True":
                toolkit.publish(result)
                render_template("success.html")
            
    return render_template("login.html")
#----------------------------------------------------------------------------------------------

#Test Mailing
#----------------------------------------------------------------------------------------------
@app.route("/test_sendEmail")
def test_sendEmail():
    #email template can be found at app/templates/testEmail.html
    sendEmail("This is a test email!", render_template("testEmail.html"), "spkudrna@gmail.com")
    return("email test succefully fired, check target inbox.")
#----------------------------------------------------------------------------------------------




#Admin Console
#----------------------------------------------------------------------------------------------
@app.route("/admin")
def adminConsole():
    return(render_template("console.html", compliedData=toolkit.compileRequestData()))

@app.route("/admin", methods=['POST'])
def processAdminRequest():
    if request.form['side'] == 'L':
        pass
    if request.form['side'] == 'R':
        pass

@app.route("/admin/L/<repairID>")
def sinistra(repairID):
    if getRepairAccepted(repairID) == True:
        pass
        #printForm(repairID)
    else:
        setRepairAccepted(repairID, True)
        #sendAcceptEmail()
    return(render_template("console.html", compliedData=toolkit.compileRequestData()))

@app.route("/admin/R/<repairID>")
def destra(repairID):
    if getRepairAccepted(repairID) == True:
        setRepairCompleted(repairID, True)
    else:
        setRepairCompleted(repairID, True)
        #sendRejectEmail()
    return(render_template("console.html", compliedData=toolkit.compileRequestData()))
#----------------------------------------------------------------------------------------------

#Route to purge the database... smart idea
@app.route("/purge/database/<secretKey>")
def seanThinksThisIsInsaneAndHeIsCorrect(secretKey):
    if secretKey == app.config['SECRET_KEY']:
        toolkit.BIG_RED_BUTTON()
        return("bye bye...")
    else:
        return("nope.")


#This NEEDS to Stay at BOTTOM of This File. If You Move it, I Will be VERY MAD AT YOU! Be Warned...
if __name__ == "__main__":
    app.run(debug=True) #this should probably be False in a productoin environent...
