from flask import Blueprint, render_template, session
from app.database import query_db
import app.EZ_Funct as EZ

bp = Blueprint("index", __name__)


#Way to fake-instantiate the database
@bp.route("/functionTest", methods=["GET"])
def index():
    # Something in order troubleshoot: literally calling just about everything in the file. (May have to re-instantiate the database from dummyTester.py because no vin and things yet.
    entries = query_db("""
        SELECT customers.customerName, customers.customerEmail, vehicles.make, vehicles.model, repairs.repairType, repairs.repairId
        FROM ((vehicles INNER JOIN customers ON vehicles.customerID = customers.customerID)
        INNER JOIN repairs ON vehicles.vehicleId = repairs.vehicleID)""")


    for entry in entries:
        #This is where we can put the tests to make
        #sure that Sean's things actually work.
        print ("Repair Type:", entry["repairType"])
        print ("Repair ID:", entry["repairId"])

    myIds = EZ.getRepairIds()

   
    #Setting repairTypes with setters.
    for myId in myIds:
        if (myId % 2 == 0):
            EZ.setRepairType(myId, "YOLO")
        else:
            EZ.setRepairType(myId, "SWAG")
    
     #Getting repair Types with the getter. 
    for repairId in myIds:
        print (repairId)
        print("Repair ID:",repairId, "\nRepair Type:",EZ.getRepairType(repairId))

    # PAYTON
    # One cause of your problem might have been the autoincrementing ID field in most of your tables.
    # Once all the table's entries are deleted, the ID is not reset. Thus, you might get a vehicleId
    # of 63 or something when the vehicle is the "first" entry in the table. This is because you
    # deleted all previous vehicles but didn't reset the increment. You can fully reset a table with
    # DELETE FROM your_table;
    # DELETE FROM SQLITE_SEQUENCE WHERE name = 'your_table';

    # As a result, the three-line query above would have failed in matching up a vehicle with its owner
    # and repairs, returning an empty list.

    # Even if this wasn't your problem, I'd strongly suggest resetting your autoincrement counter upon
    # resetting each table.

    # ~ Justas

    return render_template("index.html")


