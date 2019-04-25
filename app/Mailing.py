#This is first attempt at using Flask Mail
from flask import Flask
from flask_mail import Mail, Message
from __init__ import create_app
test_app = create_app()

with test_app.app_context():
    mail = Mail(test_app)
    test_app.config['MAIL_SERVER'] = 'smtp.gmail.com' #This sends requst to google
    test_app.config['MAIL_PORT'] = 465 #This is required for the server
    test_app.config['MAIL_USERNAME'] = 'nchsauto@gmail.com' #Associates sender address
    test_app.config['MAIL_PASSWORD'] = 'nchsautomail' #Validates sender with password
    test_app.config['MAIL_USE_TLS'] = False
    test_app.config['MAIL_USE_SSL'] = True
    mail = Mail(test_app)

    @test_app.route("/")
    def deleteWebsite(title, html_code, target):
        msg = Message(title, sender = 'NCHS Auto Shop', recipients = [target])

       # msg.body = bodyText
        msg.html = html_code
        mail.send(msg)
        return "Email Sent"
    
