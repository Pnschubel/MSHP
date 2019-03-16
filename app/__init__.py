import os
from flask import Flask
#myApp = Flask(__name__)

#test_config is a configuration populated with values to make launching easy.
#pass it in during testing
def create_app(test_config=None):
    
    myApp = Flask(__name__, instance_relative_config = True)
    
    #SECRET_KEY is to keep nasty hackers from doing dum stuff.
    #DATABASE is path of our database
    myApp.config.from_mapping(SECRET_KEY="dev", DATABASE = os.path.join(myApp.instance_path, "CarDB.sqlite"))


    #I"M NOT DONE COMMENTING THIS I'MMA FIX IT LATER
    if test_config is None:
        myApp.config.from_pyfile("config.py",silent=False)
    else:
        myApp.config.from_mapping(test_config)
        
    try:
        os.makedirs(myApp.instance_path)
    except OSError:
        pass
    
    
    from . import database
    #from . import dummyTester
    
    #myApp.register_blueprint(index.bp)
    
    database.init_app(myApp)
    
    return myApp


#Justas's version of this file is signficantly more complicated
#and probably better so if a) we're getting a lot of errors we can't
#explain or b) we have the time, we should maybe go back to that.