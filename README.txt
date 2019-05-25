PROJECT OVERVIEW:
The purpose of this project is to create a functional autoshop website through which potential customers can insert their information and requested repairs, and through which the website administrator can accept and reject these repairs, mark these repairs completed or incomplete, send emails informing customers of the state of their repair requests, and print the necessary forms surrounding the repairs.


FILES AND THEIR PURPOSE:
app.py
	Mailing
		Establishes connection with google's mailing server to allow for automated emailing from the website to customers about requests.
	Routing
		How to naviate between pages on the website.
	Forms
		Using functions in validation.py, validate information given by the user by the rendered html form login.html
	Admin Console
		Where the administrator is going to be able to view the data.


EmailTemplates.txt
instance (folder)
	CarDB.sqlite
		This is the location in which the data is actually stored, and you will never really interact with this file directly beyond its creation -- you’ll be using query_db() instead
	config.py
		We’re not entirely sure what this file does, but it seemed important so we left it there to avoid errors.
app (folder)
	database.py
		This is the file in which the python methods exist that you can use to interact with the database. The imports are sqlite3, click, os, from flask import current_app, g, from flask.cli import with_appcontext. The methods are get_db(), query_db(query, args=(), one=False), close_db(exception=None), init_db(), init_app(myApp), inidb_command()
	index.py
		This is the file that was used to test the code, specifically the database code. You can write testing methods with special Flask code, but it’s kind of a pain in the butt, so it’s just easier to create a route and call that to test  your stuff. 
	__init__.py
		This has your create_app(test_config=None) function, which is really important in regards to getting the app context in the rest of your files. Be sure to include it. It’s also where you import/register blueprints.
	schema.sql
		The code that is essentially the framework for your database into which you will later insert actual data. You create CarDB.db from the schema, which has all of your tables and columns contained within. 
	toolkit.py
		Gets, sets, adds, removes, and creates data in the database using query_db() but simplified for ease of use by those who don’t understand how query_db() works
	validation.py
		All your stuff from flask 
Static (folder)
	hell.js
	stylesheet.css
		Styling file to create prettier imagery.
templates (folder)
	console.html
		The html file that generates the buttons for the admin window to view the data
	success.html
		a success message, will be rendered in app when form is entered correctly
	login.html
		the html form where user will enter in information, rendered in app.py
	testEmail.html
		Test email to demonstrate the functionality of the emailing functions.




PLATFORM REQUIREMENTS:
	None known


SEQUENTIAL INSTALLATION INSTRUCTIONS:
	General Dependencies (Install First)
		python 3 (or greater), Flask, flaskMail, pdfkit (if implementing PDF functionality)
	Dependencies for Database:
		None

INSTALL FROM GITHUB:
	Ask Mr. Hayes for the github repo url -- he should have been made owner. If not, it’s called MSHP. Good luck finding that (it stands for Magical Sparkly Handheld Polyhedrons, but that was too long.)


USING PROJECT:
	How to Configure Project:
		Project should be pre-configured on the server.
	How to Run Project:
		From the customer end…
			Launch the url: {{INSERT URL HERE}}
		From the administration end…
			Launch the url: {{INSERT URL HERE}}
		(Note: We won't know the final urls until the site gets hosted, which hasn't currently happened yet. Stay tuned.)
		
		
CHANGES FOR THE FUTURE:
- Button functionality (there is some backend for these things):
	- Pressing Deny/Accept should prompt Mr. Feid to send an email (which he should be allowed to send as default or modify)
	- Pressing Deny/Accept should update the deny/accept boolean in the database.
	- Pressing Deny and sending the email should remove the particular request from the admin console
	- Pressing Accept and sending the email should switch the button to completed and offer Mr. Feid a way to print the manual form he needs to print.
- PDF Form Functionality (theere is some backend for these things.)
	- Mr. Feid should be able to print the form (that one he needs in triplicate) or download the form.
- Additional Things (There is currently no backend created for these things):
	- Security Implementations: 
		- Login to the admin console should exist.
		- Security features should be investigated and implemented.
	
