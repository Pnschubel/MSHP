from flask import Blueprint, render_template, session
from app.database import query_db

bp = Blueprint("index", __name__)


#Way to fake-instantiate the database
@bp.route("/functionTest", methods=["GET"])
def index():
    # Something in order troubleshoot: literally calling just about everything in the file. (May have to re-instantiate the database from dummyTester.py because no vin and things yet.
    entries = query_db("""
        SELECT customers.customerName, customers.customerEmail, vehicles.make, vehicles.model, repairs.repairType, repairs.repairId
        FROM ((vehicles INNER JOIN customers ON vehicles.customerID = customers.customerID)
        INNER JOIN repairs ON vehicles.vehicleId = repairs.vehicleID)""")

    print ("The file is running.")
    for entry in entries:
        print ("Repair ID:", entry["repairId"])

    #Getting all repair IDs
    repairIds = query_db("""SELECT repairId FROM repairs""")

    print (repairIds)

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


