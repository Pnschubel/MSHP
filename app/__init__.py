import os
from flask import Flask


# test_config is a configuration populated with values to make launching easy.
# pass it in during testing
def create_app(test_config=None):
    
    myApp = Flask(__name__, instance_relative_config=True)
    
    # SECRET_KEY is to keep nasty hackers from doing dum stuff.
    # DATABASE is path of our database
    myApp.config.from_mapping(SECRET_KEY="dev", DATABASE=os.path.join(myApp.instance_path, "CarDB.sqlite"))

    if test_config is None:
        # If there is a configured instance, load it. config.py can store values
        # you don't want visible, like a real secret key.
        myApp.config.from_pyfile("config.py", silent=False)
    else:
        # otherwise, test configuration
        myApp.config.from_mapping(test_config)
        
    try:
        os.makedirs(myApp.instance_path)
    except OSError:
        pass
    
    #import your blueprints here
    from app import database
    from app import index
    # from . import dummyTester
    
    # register your blueprints here.
    # Can use flask tutorial
    # Ex: myApp.register_blueprint(index.bp)

    myApp.register_blueprint(index.bp)
    database.init_app(myApp)
    
    return myApp

# Justas's version of this file is significantly more complicated
# and probably better so if a) we're getting a lot of errors we can't
# explain or b) we have the time, we should maybe go back to that.
