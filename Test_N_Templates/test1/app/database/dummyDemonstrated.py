#Payton Schubel and Sean Kuderna
#Way to test the database & functionality.

from flask import Flask
from database import query_db

app = Flask(__name__)
with app.app_context():
    flag = True
    while flag == True:
        print("\nWelcome to the rudimentary database displayer!")
        print("\n1) Print the database")
        print("\n2) Add to the database")
        print("\n3) Exit")
        choice = input("\n\nSelect your choice: ")
        
        if choice == "1":
            customers = query_db("SELECT * FROM customers ORDER BY customerId DESC")
            print("\nCUSTOMERS:\n")
            for customer in customers:
                print(customer + "\n")
            print("\n\nVEHICLES:\n")
            vehicles = query_db("SELECT * FROM vehicles ORDER BY vehicleId DESC")
            for vehicle in vehicles:
                print(vehicle + "\n")
            print ("\n\nREPAIRS:\n")
            repairs = query_db("SELECT * FROM repairs ORDER BY repairId DESC")
            for repair in repairs:
                print (repair + "\n")
        if choice == "2":
            choice = input ("Select 1 for customers, 2 for vehicles, 3 for repairs: ")
            if choice == "1":
                print(query_db("SELECT * FROM customers ORDER BY customerId ASC"))
                print(query_db("SElECT * FROM customers WHERE customerId = ?", (0,), True))
        if choice == "3":
            flag = False
            