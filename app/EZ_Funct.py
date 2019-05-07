#EZ_Funct

#Sean Kudrna --> Getters and Setters for Database

# By the way, most of this file is completely broken. My interpreter is detecting 41 errors
# and 92 warnings.
# ~Justas

from app.database import query_db
from flask import current_app, g
import array

#Create Customer, Vehicle, Repair
#---------------------------------





#GETTERS
#---------------------------------------------------------------

#Get ALL RepairIds
def getRepairIds():
    #array for all the repairIds
    myIds = array.array('i')
    #Returns a list of dictionaries of all repairIds with key repairId
    repairIds = query_db("""SELECT repairId FROM repairs""")
    
    #puts all the repair Ids into the array for Matias
    for myId in repairIds:
        myIds.append(myId["repairId"])

    return myIds


#Get Associated Info
def getAssociatedRepairs(vehID):
    #THIS RETURNS AN ARRAY OF DICTIONARIES
    #Which should be fine since you're the only using it within this file.
    repairIds = query_db("SELECT repairId FROM repairs WHERE vehicleId = ?", int(vehID),)
    return repairIds

def getAssociatedVehicle(repID):
    vehicleId =  query_db("SELECT vehicleId  FROM repairs WHERE repairId = ?", (int(repID),), True)
    print("TEST:", vehicleId)#Test
    return vehicleId["vehicleId"]

def getAssociatedVehicles(customerID):
    #THIS RETURNS AN ARRAY OF DICTIONARIES
    #Which should be fine since you're the only using it within this file.
    vehicleIds = query_db("SELECT vehicleId FROM vehicles WHERE customerId = ?", (int(customerID),))
    return vehicleIds

def getAssociatedCustomer(vehID):
    customerId =  query_db("SELECT customerId  FROM vehicles WHERE vehicleId = ?", (int(vehID),), True) 
    return customerId["customerId"]


#Get Customer Info
def getCustomerName(custID):
   
    customerName =  query_db("SELECT customerName FROM customers WHERE customerId = ?", (int(custID),), True) 
    return customerName["customerName"]
    
def getCustomerEmail(custID):

    customerEmail = query_db("SELECT customerEmail FROM customers WHERE customerId = ?", (int(custID),), True)
    return customerEmail["customerEmail"]
    
def getCustomerPhone(custID):

    customerPhone =  query_db("SELECT customerPhoneNum FROM customers WHERE customerId = ?", (int(custID),), True)
    return customerPhone["customerPhoneNum"]

#Get Vehicle Info
def getVehicleMake(vehID):

    v =  query_db("SELECT make FROM vehicles WHERE vehicleId = ?", (int(vehID),), True)
    return v["make"]
   
def getVehicleModel(vehID):
    v =  query_db("SELECT model FROM vehicles WHERE vehicleId = ?", (int(vehID),), True)
    return v["model"]

      
def getVehicleYear(vehID):
    v =  query_db("SELECT year FROM vehicles WHERE vehicleId = ?", (int(vehID),), True)
    return v["year"]

def getVehicleVin(vehID):
    v =  query_db("SELECT vin FROM vehicles WHERE vehicleId = ?", (int(vehID),), True)
    return v["vin"]      


#Get Repair Info
def getRepairType(repID):

    r =  query_db("SELECT repairType FROM repairs WHERE repairId = ?", (int(repID),), True)
    return r["repairType"]   
    
def getRepairDescription(repID):

    r =  query_db("SELECT repairDescription FROM repairs WHERE repairId = ?", (int(repID),), True)
    return r["repairDescription"]  
    
def getRepairAccepted(repID):

    r =  query_db("SELECT accepted FROM repairs WHERE repairId = ?", (int(repID),), True)
    return r["accepted"]  
    


#SETTERS
#-----------------------------------------------------------------------
#I'm pretty sure this is how you wrap sql code into python? we may have to do this for the methods above if they dont work... shouldn't be too difficult to update if needed.
#(I did these a different way just in case the ones above dont work --> gives us options)

#Concantenator with variable because we need to put variable in the string of SQL

#Make sure table is singular (though the tables are plural)
def concantenate(table, row, var):
    mySQL = "UPDATE " + table + "s SET " + row + " = \"" + var
    mySQL = mySQL + "\" WHERE " + table + "Id = ?"

    return mySQL


#Set Customer Info
def setCustomerName(custID, name):
    mySQL = concantenate("customer", "customerName", name)
    query_db(mySQL, (int(custID),))
    return("customerName has been updated to " + name)

def setCustomerEmail(custID, email):
    mySQL = concantenate("customer", "customerEmail", email)
    query_db(mySQL, (int(custID),))
    return("customerEmail has been updated to " + email)

def setCustomerPhoneNum(custID, phoneNum):
    mySQL = concantenate("customer", "customerPhoneNum", phoneNum)
    query_db(mySQL, (int(custID),))
    return("customerPhoneNum has been updated to " + phoneNum)


#Set Vehicle Info
def setVehicleMake(vehID, make):
    mySQL = concantenate("vehicle", "make", make)
    query_db(mySQL, (int(vehID),))
    return("make has been updated to " + make)

def setVehicleModel(vehID, model):
    mySQL = concantenate("vehicle", "model", model)
    query_db(mySQL, (int(vehID),))
    return("model has been updated to " + model)

def setVehicleYear(vehID, year):
    mySQL = concantenate("vehicle", "year", year)
    query_db(mySQL, (int(vehID),))
    return("year has been updated to " + year)


#Set Repair Info
def setRepairType(repID, repairType):
    mySQL = concantenate("repair", "repairType", repairType)
    query_db(mySQL, (int(repID),))
    return("repair type has been updated to " + repairType)

def setRepairDescription(repID, repairDescription):
    mySQL = concantenate("repair", "repairDescription", repairDescription)
    query_db(mySQL, (int(repID),))
    return("repair description has been updated to " + repairDescription)

def setRepairAccepted(repID, accepted):
    mySQL = concantenate("repair", "accepted", accepted)
    query_db(mySQL, (int(repID),))
    return("status has been updated to " + accepted)

def setRepairCompleted(repID, completed):
    mySQL = concantenate("repair", "completed", completed)
    query_db(mySQL, (int(repID),))
    return("status has been updated to " + completed)


#THE CREATORS
#These are how you insert new items into the database. These will...
#   - Take all values of the table as parameters (with defaults)
#   - Precondition: None of the Not Null values are Null 
#   - If all is good, add to table.
#NOTE: Create the customer, then the vehicle, then the repairs.
#Otherwise the IDs won't exist.

def createCustomer(customerName,
                    customerEmail,
                    customerPhoneNum = None):
    #Only thing I'm worried about: if none = null or not.
    query_db("INSERT INTO customers (customerName, customerEmail, customerPhoneNum) VALUES(?,?,?)", (customerName, customerEmail, customerPhoneNum))
    return "Customer has been created."

def createVehicle(make = None, 
                    model = None,
                    year = None,
                    vin = None,
                    customerId = 'default'):
    #If customerId isn't specified, gets the most recent one.
    if (customerId == 'default'):
        getId = query_db("SELECT customerId FROM customers ORDER BY customerId DESC", one = True)
    query_db("INSERT INTO vehicles (make, model, year, vin, customerId) VALUES(?,?,?,?,?)", (make, model, year, vin, getId['customerId']))
    return "Vehicle has been created."

def createRepair(repairType,
                    repairDescription = None,
                    accepted = None,
                    completed = False,
                    vehicleId = 'default'):
    #If vehicleId isn't specified, gets the most recent one
    if (vehicleId == 'default'):
        getId = query_db("SELECT vehicleId FROM vehicles ORDER BY vehicleId DESC", one = True)
    query_db("INSERT INTO repairs (repairType, repairDescription, accepted, completed, vehicleId) VALUES(?,?,?,?,?)", (repairType, repairDescription, accepted, completed, getId['vehicleId']))
    return "Repair has been created."

#BIG RED BUTTON FUNCTIONS --
    #These haven't been troubleshooted, so use with caution.
#-----------------------------------------------------------------------------------------------------------


#Wipe Customers
def BIG_RED_BUTTON_CUSTOMERS():
    confirmation = input("You are about to wipe all customers from user database... are you sure> (y/n)")
    if confirmation.lower() == "y":
        query_db("DELETE FROM customers;")
    else:
        return ("Data whipe canceled")

#Wipe vehicles
def BIG_RED_BUTTON_VEHICLES():
    confirmation = input("You are about to wipe all vehicles from database... are you sure> (y/n)")
    if confirmation.lower() == "y":
        query_db("DELETE FROM vehicles;")
    else:
        return ("Data whipe canceled")

#Wipe repairs
def BIG_RED_BUTTON_REPAIRS():
    confirmation = input("You are about to wipe all repairs from database... are you sure> (y/n)")
    if confirmation.lower() == "y":
        query_db("DELETE FROM repairs;")
    else:
        return ("Data whipe canceled")

#Remove a row
#-----------------------------------------------------------------------------------------------------------


#Remove repair
def RemoveRepair(repID):
    query_db("DELETE FROM repairs WHERE repairId = ?", (int(repID),))
    return "Repair has been deleted"

#Remove vehicle
def RemoveVehicle(vehID):
    query_db("DELETE FROM vehicles WHERE vehicleId = ?", (int(vehID),))
    query_db("DELETE FROM repairs WHERE vehicleId = ?", (int(vehID),))
    return "Vehicle has been deleted"
    #Deletes repairs associated with vehicle

#Remove customer
def RemoveCustomer(cusID):
    #Gets all vehicleIds associated with this customer. 
    vehIds = getAssociatedVehicles(cusID)
    
    for vehId in vehIds:
        RemoveVehicle(vehId["vehicleId"])
 
    query_db("DELETE FROM customers WHERE customerId = ?", (int(cusID),))
    return "Customer has been deleted"


















    


    
