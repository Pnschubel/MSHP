#This is first attempt at using Flask Mail
from flask import Flask
from flask_mail import Mail, Message
from app import create_app

test_app = create_app()

mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com' #This sends request to google
app.config['MAIL_PORT'] = 465 #This is required for the server
app.config['MAIL_USERNAME'] = 'nchsauto@gmail.com' #Associates sender name
app.config['MAIL_PASSWORD'] = 'nchsautomail' #Validates sender with password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(test_app)

@test_app.route("/")
def index():
    msg = Message('NCHS Auto: Your Request has been viewed!', sender ='NCHS Auto', recipients = ['spkudrna@stu.naperville203.org'])

    msg.body = 'You\'re a loser!'
    mail.send(msg)
    return "Sent"

if __name__ == '__main__':
    app.run(debug = True)

index()

