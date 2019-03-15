#Payton Schubel and Sean Kuderna
#Way to test the database & functionality.

from app import create_app
app = create_app()
from flask import Flask, current_app, g
from app import database
from app import myApp

from database import close_connection, query_db

#myApp.config.from_object(__name__)

with myApp.app_context():
    #Data with which to populate our dummy database
    customerNames = ["Hana","Matias","Orrin","Payton","Sean"]
    customerEmail =["hana@hasan.com","matias@bonta.com","orrin@lutes.com","payton@schubel.com","sean@kuderna.com"]

    makes = ["Honda", "Motorolla", "Old", "Pontiac","Subaru"]
    models = ["Accord", "Car","Blue","Pilot","Forester"]

    types = ["oil change","oil change","tire rotation", "ATF Change"]

    #Something to insert data into the customers table
    for count, value in enumerate (customerNames):
        query_db("INSERT INTO customers (customerId, customerName, customerEmail) VALUES(?,?,?)",
                (count, customerNames[count], customerEmail[count]))        
        

    #Something to insert data into the vehicles table
    for count, value in enumerate (makes):
        owner = query_db("SELECT * FROM customers WHERE customerId = ?", (count,), True)
        query_db("INSERT INTO vehicles (vehicleId, make, model, customerId) VALUES(?,?,?,?)",
                (count, makes[count], models[count], owner[0]))

    #Something to insert into the vehicles table
    #(I'm going to give some cars two repairs and some cars one, hence the 7)
    i = 0
    while i <= 7:
        car = query_db("SELECT * FROM customers WHERE customerId = ?", (i % 5,), True)
        query_db("INSERT INTO repairs (repairId, repairType, vehicleId) VALUES(?,?,?)",
                (i, types[i % 4], car[0]))
        i += 1

            
        customers = query_db("SELECT * FROM customers ORDER BY customerId DESC")
        print("\nCUSTOMERS:\n")
        for customer in customers:
            print(customer)
        print("\n\nVEHICLES:\n")
        vehicles = query_db("SELECT * FROM vehicles ORDER BY vehicleId DESC")
        for vehicle in vehicles:
            print(vehicle)
        print ("\n\nREPAIRS:\n")
        repairs = query_db("SELECT * FROM repairs ORDER BY repairId DESC")
        for repair in repairs:
            print (repair)
 