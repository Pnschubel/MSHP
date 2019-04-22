#Payton Schubel
#Automotive Website Database Manager
#Sprint 3 Clean Up

import sqlite3, click, os
from flask import current_app, g
from flask.cli import with_appcontext

#A method to return the members of the database as dictionaries.
#It will return the row as key-value pairs. (column_Name:column_Value)
#0 is the index of the actual name of the column.
def make_dicts(cursor, row):
     return dict((cursor.description[idx][0], value,)
                 for idx, value in enumerate(row))

#how to open the database in the first place
def get_db():
    if "db" not in g:
         g.db = sqlite3.connect(
             #So, when we defined a database in __init__.py? It's here.
             #We use the path stored in the DATABASE key to retrieve the
             #location.
             current_app.config["DATABASE"],
             
             #This next bit means we get all of our data back as Python-operable
             #objects (instead of SQL types)
             detect_types = sqlite3.PARSE_DECLTYPES
        )
    #Now we make everything into a dictionary for ease
    g.db.row_factory = make_dicts
    
    return g.db


#THE GOD FUNCTION
def query_db(query, args=(), one=False):

    #Two things:
    #1) Call get_db() to get conncetion to DB
    #2) Execute the query within given arguments
    #Fancry wrapper for regular get_db().execute()
    db = get_db()
    cursor = db.execute(query, args)
    
    #Returns 'all remaining' results from query. Typically have to move
    #One by by one with cursor, but fetchall loads everything into a list
    #and returns it. 
    queryList = cursor.fetchall()
    
    #closes database connection
    cursor.close()
    db.commit()
    
    #If 'One' is true, will return top value of list. (For only one result.)
    #If 'one' is false, it'll return the entire list.
    return (queryList[0] if queryList else()) if one else queryList

def close_db(exception=None):
    #Checks if db exists in g and grabs it if so.
    db = g.pop("db", None)
    
    #If db is open, closes it
    if db is not None:
        db.close()
        

def init_db():
    #Gets the database
    db = get_db()
    
    #Iterates over the schema.sql file & executes as SQL
    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf8"))
        
def init_app(myApp):
    #When called init __init__, close_connection gets teardown_appcontext
    #decorater, so "initdb" becomes usable command to invoke
    #init_db_command()
    
    #Could replace it by decorating closer with teardown, but I'm doing this.
    myApp.teardown_appcontext(close_db)
    myApp.cli.add_command(initdb_command)
    
#Registers command with the flask script
@click.command("initdb")
@with_appcontext
def initdb_command():
    #Initializes the database
    init_db()
    #for troubleshooting
    click.echo('Initialized the Database')
    