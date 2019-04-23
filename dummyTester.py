#Payton Schubel and Sean Kuderna
#Special thanks to Justas Stankavicius
#Way to test the database & functionality.

from app.database import query_db, close_db
from app import create_app
import random

test_app = create_app()

with test_app.app_context():
    # Data with which to populate our dummy database
    customerNames = ["Hana", "Matias", "Orrin", "Payton", "Sean"]
    customerEmail =["hana@hasan.com","matias@bonta.com","orrin@lutes.com","payton@schubel.com","sean@kuderna.com"]
    makes = ["Honda", "Motorolla", "Old", "Pontiac", "Subaru"]
    models = ["Accord", "Car", "Blue", "Pilot", "Forester"]
    types = ["oil change", "oil change", "tire rotation", "ATF Change"]

    # Clear database. Hopefully you didn't have anything too important in it.
    query_db("DELETE FROM customers;")
    query_db("DELETE FROM SQLITE_SEQUENCE WHERE name = 'customers'")
    query_db("DELETE FROM vehicles;")
    query_db("DELETE FROM SQLITE_SEQUENCE WHERE name = 'vehicles'")
    query_db("DELETE FROM repairs;")
    query_db("DELETE FROM SQLITE_SEQUENCE WHERE name = 'repairs'")

    # Presumably, "vehicles" is the top-level identity in the schema, since only one vehicle with a particular
    # ID can exist at any one time. As such, we'll list some "jobs" from the database where the vehicle and make
    # are listed first, followed up by the owner name, and finally all the repairs associated with the vehicle.
    for i, name in enumerate(customerNames):
        query_db("INSERT INTO customers (customerName, customerEmail) VALUES(?, ?)",
                 (customerNames[i], customerEmail[i]))
        query_db("INSERT INTO vehicles (make, model, customerId) VALUES(?, ?, ?)",
                 (makes[i], models[i], i + 1))
        query_db("INSERT INTO repairs (repairType, vehicleId) VALUES(?, ?)",
                 (random.choice(types), i + 1))

    # This will retrieve all values enumerated after the SELECT statement by first matching together rows from
    # 'customers' and 'vehicles' based on customerId (so that the owner is matched with their car), and then
    # matching that table with 'repairs' based on vehicleId, so that each vehicle is matched with its repairs.
    # The results are stored in 'entries.' This query will probably give weird results for multiple repairs per
    # vehicle, but that can be solved using SQL magic as well. This is just to demonstrate that your DB works.

    # You can do this the old way as well by querying 'SELECT * FROM ___ WHERE __ = __`, but this is really
    # a more elegant way of retrieving all the values in one query. I'd suggest learning more complicated SQL queries,
    # since they'll make your life substantially easier as your project becomes more complex in scope.
    entries = query_db("""
    SELECT customers.customerName, customers.customerEmail, vehicles.make, vehicles.model, repairs.repairType 
    FROM ((vehicles INNER JOIN customers ON vehicles.customerID = customers.customerID)
    INNER JOIN repairs ON vehicles.vehicleId = repairs.vehicleID)""")

    for entry in entries:
        print("Name:", entry["customerName"])
        print("Email:", entry["customerEmail"])
        print("Vehicle:", entry["make"], entry["model"])
        print("Repair type:", entry["repairType"])
        print()
