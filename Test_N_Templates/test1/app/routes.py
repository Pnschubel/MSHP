from app import myApp

@myApp.route('/')
@myApp.route('/homepage')
def homepage():
    #Will eventually be HTML file
    return "Placeholder"