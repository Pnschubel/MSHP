import os
from flask import Flask
from flask import render_template
from flask_mail import Mail, Message
from app import create_app

#This NEEDS to Stay at TOP of This File. If You Move it, I Will be VERY MAD AT YOU! Be Warned...
app = create_app()

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




#Test Mailing
@app.route("/test_sendEmail")
def test_sendEmail():
    htmlCode = ('<p style="background-color: #ff00ff;"> ...Hello i am a pink rectangle... </p>')
    sendEmail("Test W/Parameters", render_template("EmailTemplate.html"), "spkudrna@gmail.com")
    return("...Email Sent...")

#End of Mailing
#----------------------------------------------------------------------------------




#This NEEDS to Stay at BOTTOM of This File. If You Move it, I Will be VERY MAD AT YOU! Be Warned...
if __name__ == "__main__":
    app.run(debug=True)
