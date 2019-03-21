import os
from flask import Flask
myApp = Flask(__name__)

#Don't forget to register your files with the app (this is why we needed workarounds)
from app import routes
from app import database
from app import CarDB

#Justas's version of this file is signficantly more complicated
#and probably better so if a) we're getting a lot of errors we can't
#explain or b) we have the time, we should maybe go back to that.