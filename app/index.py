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
    
    getId = query_db("SELECT vehicleId FROM vehicles ORDER BY vehicleId DESC", one = True)
    print (getId)


    #I'm going to create a new customer with bare minimum.
    EZ.createCustomer(customerName = "Boring Betty",
                        customerEmail = "bb@boring.com")
    EZ.createVehicle(vin = "00011122233344")
    EZ.createRepair(repairType = "Oil Change")

    #This is a customer with everything
    EZ.createCustomer(customerName = "Kool Kyle",
                        customerEmail = "koolaidkid@swag.com",
                        customerPhoneNum = "347-347-9345")
    EZ.createVehicle(make = "Kardial", model = "Roadster",
                        year = "3402", vin = "54321543214321")
    EZ.createRepair(repairType = "Flight Drive Alignment",
                    repairDescription = "Needs accents")
    
    # for entry in entries:
        #This is where we can put the tests to make
        #sure that Sean's things actually work.
    #    print ("Repair Type:", entry["repairType"])
    #    print ("Repair ID:", entry["repairId"])

    myIds = EZ.getRepairIds()

   
    #Setting repairTypes with setters.
    # for myId in myIds:
    #     if (myId % 2 == 0):
    #         EZ.setRepairType(myId, "YOLO")
    #     else:
    #         EZ.setRepairType(myId, "SWAG")
    
    #Getting repair Types with the getter. 
    for repairId in myIds:
        print (repairId)
        print("Repair ID:",repairId, "\nRepair Type:",EZ.getRepairType(repairId))

    return render_template("index.html")


