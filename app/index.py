from flask import Blueprint, render_template, session
from app.database import query_db
import app.toolkit as EZ

bp = Blueprint("index", __name__)


#Way to fake-instantiate the database
@bp.route("/functionTest", methods=["GET"])
def index():
    # Something in order troubleshoot: literally calling just about everything in the file. (May have to re-instantiate the database from dummyTester.py because no vin and things yet.
    entries = query_db("""
        SELECT customers.customerName, customers.customerEmail, vehicles.make, vehicles.model, repairs.repairType, repairs.repairId
        FROM ((vehicles INNER JOIN customers ON vehicles.customerID = customers.customerID)
        INNER JOIN repairs ON vehicles.vehicleId = repairs.vehicleID)""")
    
    getId = query_db("SELECT vehicleId FROM vehicles ORDER BY vehicleId DESC", one = True)
    print (getId)


       # for entry in entries:
        #This is where we can put the tests to make
        #sure that Sean's things actually work.
    #    print ("Repair Type:", entry["repairType"])
    #    print ("Repair ID:", entry["repairId"])

    myIds = EZ.getRepairIds()

  
    #This is me testing if the removers work -- I'm just gonna test customer.
    vehId = EZ.getAssociatedVehicle(myIds[2])
    cusId = EZ.getAssociatedCustomer(vehId)

    EZ.RemoveCustomer(cusId)
    #Setting repairTypes with setters.
    # for myId in myIds:
    #     if (myId % 2 == 0):
    #         EZ.setRepairType(myId, "YOLO")
    #     else:
    #         EZ.setRepairType(myId, "SWAG")
    
    #You have to grab the repairIds again because they've changed.
    myIds = EZ.getRepairIds()
    
    #Getting repair Types with the getter. 
    for repairId in myIds:
        print (repairId)
        print("Repair ID:",repairId, "\nRepair Type:",EZ.getRepairType(repairId))

    return render_template("index.html")


