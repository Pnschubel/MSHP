#Payton Schubel and Sean Kuderna
#Way to test the database & functionality.

from flask import Flask
from database import query_db

app = Flask(__name__)
with app.app_context():

    #Data with which to populate our dummy database
    ids = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    customerNames = ["Hana","Matias","Orrin","Payton","Sean"]
    customerEmail =["hana@hasan.com","matias@bonta.com","orrin@lutes.com","payton@schubel.com","sean@kuderna.com"]

    makes = ["Honda", "Motorolla", "Old", "Pontiac","Subaru"]
    models = ["Accord", "Car","Blue","Pilot","Forester"]

    types = ["oil change","oil change","tire rotation", "ATF Change"]

    #Something to insert data into the customers table
    count = 0
    for customer in customerNames:
        query_db("INSERT INTO customers (customerId, customerName, customerEmail) VALUES(?,?,?)",
                 (ids[count], customer, customerEmail[count]))
        count += 1
        
    
    #Something to insert data into the vehicles table
    #resetting count
    count = 0
    for make in makes:
        owner = query_db("SELECT * FROM customers WHERE customerId = ?", (count,), True)
        query_db("INSERT INTO vehicles (vehicleId, make, model, customerId) VALUES(?,?,?,?)"
                 ids[count], make, models[count], owner["customerId"])
        count += 1
        
