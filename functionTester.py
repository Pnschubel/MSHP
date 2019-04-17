#Payton Schubel
#Sprint 4
#File to test Sean's EZ_Funct.py

from app.database import query_db, close_db
from app import create_app

#get the application context
test_app = create_app()

#work inside application context
with test_app.app_context():
   #Making sure the database exists.
   entries = query_db("""SELECT customers.customerName, customers.customerEmail, vehicles.make, vehicles.model, repairs.repairId, repairs.repairType FROM ((vehicles INNER JOIN customers ON vehicles.customerID = customers.customerID) INNER JOIN repairs ON vehicles.vehicleID = repairs.vehicleID)""")
   
   print("The file is running.")
   for entry in entries:
       print ("Repair ID:", entry["repairId"])
       print ("Name:", entry["customerName"])
       print()
    
    
    #Getting all of the repair IDs
#    repairIds = query_db("""SELECT repairId FROM repairs""")
#
#    print (repairIds)
#    #Just to see if the query to get repairIds actually worked
#    for repairId in repairIds:
#        print("Repair ID:", repairId["repairId"])
#        print()
