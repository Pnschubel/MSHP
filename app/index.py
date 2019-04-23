from flask import Blueprint, render_template, session
from app.database import query_db

bp = Blueprint("index", __name__)


@bp.route("/", methods=["GET"])
def index():
    # Presumably, "vehicles" is the top-level identity in the schema, since only one vehicle with a particular
    # ID can exist at any one time. As such, we'll list some "jobs" from the database where the vehicle and make
    # are listed first, followed up by the owner name, and finally all the repairs associated with the vehicle.

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

    # PAYTON AND MATIAS:
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