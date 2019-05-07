#Payton Schubel and Sean Kuderna
#Special thanks to Justas Stankavicius
#Way to test the database & functionality.

from app.database import query_db, close_db
from app import create_app
import random

test_app = create_app()

#THIS FILE IS JUST IF YOU NEED TO...
#   A) Tune up the website (ex: add a column to the table
#   B) Test something.
#   C) Clear the database.
with test_app.app_context():
   # Uncomment to CLEAR THE DATABASE
   # query_db("DELETE FROM customers;")
   # query_db("DELETE FROM SQLITE_SEQUENCE WHERE name = 'customers'")
   # query_db("DELETE FROM vehicles;")
   # query_db("DELETE FROM SQLITE_SEQUENCE WHERE name = 'vehicles'")
   # query_db("DELETE FROM repairs;")
   # query_db("DELETE FROM SQLITE_SEQUENCE WHERE name = 'repairs'")

    #Uncomment and modify to ALTER THE TABLE
    #query_db("ALTER TABLE table_of_choice ADD attribute TYPE")

   # Uncomment to GRAB ALMOST ALL VALUES FROM DATABASE 
   # entries = query_db("""SELECT customers.customerName, customers.customerEmail, vehicles.make, vehicles.model, repairs.repairType 
   # FROM ((vehicles INNER JOIN customers ON vehicles.customerID = customers.customerID)
   # INNER JOIN repairs ON vehicles.vehicleId = repairs.vehicleID)""")

