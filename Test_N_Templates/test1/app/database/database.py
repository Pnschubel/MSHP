#Payton Schubel
#Auto Tutorial Databasing
#February 8th, 2019

#import sqlite3 so we can use it
from flask import Flask
myApp = Flask(__name__)
import sqlite3

#the g stands for global; it's the same as an app context
#basically, it's a recepticle for data we want to store.
from flask import g
#the path where the database is stored
DATABASE='CarDB.db'

#how to open the database in the first place
def get_db():
    #the getattr(object, attrib, default) is the same as object.attrib
    #where you get the default if the attrib doesn't exist.
    db = getattr(g, '_database', None)
    #Need to make sure we actually got the database.
    if db is None:
        #Basically, creates the g._database attrib from where it didn't
        #exist before. Then assigns that value to a returnable variable.
        g._database = sqlite3.connect(DATABASE)
        db = g._database
    #returns database
    return db


#THIS MAY OR MAY NOT GO HERE
#This is to build the database from the schema file
def init_db():
    with app.app_context():
        #Sets the database equal to the value of get_db()
        db.get_db()
        #Builds db off of the schema sql file (opened for read)
        with app.open_resource('schema.sql', mode='r') as f: #file
            #cursor is like an iterator to read the db
            db.cursor().executescript(f.read())
        #saves db
        db.commit()
        
#Registers command with the flask script
@myApp.cli.command('initdb')
def initdb_command():
    #Initializes the database
    init_db()
    #for troubleshooting
    print ('Initialized the Database')
    
#Pretty sure this runs the module when in the right space.
if __name__ == '__main__':
    init_db()
    app.run()
    
#THE GOD FUNCTION
#Basically, can 1) Display 2) Add To 3) Remove from database
def query_db(query, args=(), one=False):

    #Two things:
    #1) Call get_db() to get conncetion to DB
    #2) Execute the query within given arguments
    #Fancry wrapper for regular get_db().execute()
    cursor = get_db().execute(query, args)
    
    #Returns 'all remaining' results from query. Typically have to move
    #One by by one with cursor, but fetchall loads everything into a list
    #and returns it. 
    queryList = cursor.fetchall()
    
    #closes database connection
    cursor.close()
    
    #If 'One' is true, will return top value of list. (For only one result.)
    #If 'one' is false, it'll return the entire list.
    return (queryList[0] if queryList else none) if one else queryList


#So, this will run (always) to close the database when done.
@myApp.teardown_appcontext
#So we're gonna close it now
def close_connection(exception):
    #sees if the database is open right now or not.
    db = getattr(g, '_database', None)
    #if the database is not closed, close it.
    if db is not None:
        #how to close the database
        db.close()
        


#EXTRA ASSORTED NOTES
#to connect on demand (if testing, open by hand first)
        #with app.app_context() //allows you to use get_db()
#to query db, should have a row factory function to convert stuff.
        #it should be in get_db()
        #example: db.row_factory = sqlite3.Row //gives you rows not queries.
#usually good practice to have a function to execute, fetch, and get cursor all at once.
        