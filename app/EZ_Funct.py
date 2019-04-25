#EZ_Funct

#Sean Kudrna --> Getters and Setters for Database

# By the way, most of this file is completely broken. My interpreter is detecting 41 errors
# and 92 warnings.
# ~Justas

from app.database import query_db
from flask import current_app, g


#Create Customer, Vehicle, Repair
#---------------------------------





#GETTERS
#---------------------------------------------------------------


#Get Associated Info
def getAssociatedVehicle(repID):

    refPoint = repairs.query.filter_by(repairId = repID)

    return(refPoint.vehicleId)

def getAssociatedCustomer(vehID):
    
    refPoint = vehicles.query.filter_by(vehicleId = vehID)

    return(refPoint.customerId)


#Get Customer Info
def getCustomerName(custID):

    refPoint = customers.query.filter_by(customerId = custID)
   
    return (refPoint.customerName)
    
def getCustomerEmail(custID):

    refPoint = customers.query.filter_by(customerId = custID)
   
    return (refPoint.customerEmail)
    
def getCustomerPhone(custID):

    refPoint = customers.query.filter_by(customerId = custID)

    return (refPoint.customerPhoneNum)
    

#Get Vehicle Info
def getVehicleMake(vehID):

    refPoint = vehicles.query.filter_by(vehicleId = vehID)

    return(refPoint.make)
   
def getVehicleModel(vehID):

    refPoint = vehicles.query.filter_by(vehicleId = vehID)
   
    return(refPoint.model)
    
def getVehicleYear(vehID):

    refPoint = vehicles.query.filter_by(vehicleId = vehID)

    return(refPoint.year)

def getVehicleVin(vehID):

    refPoint = vehicles.query.filter_by(vehicleId = vehID)

    return(refPoint.vin)
   


#Get Repair Info
def getRepairType(repID):

    refPoint = repairs.query.filter_by(repairId = repID)
    
    return(refPoint.repairType)
    
def getRepairDescription(repID):

     refPoint = repairs.query.filter_by(repairId = repID)

     return(refPoint.repairDescription)   
    
def getRepairAccepted(repID):

    refPoint = repairs.query.filter_by(repairId = repID)

    return(refPoint.accepted)   
    


#SETTERS
#-----------------------------------------------------------------------
#I'm pretty sure this is how you wrap sql code into python? we may have to do this for the methods above if they dont work... shouldn't be too difficult to update if needed.
#(I did these a different way just in case the ones above dont work --> gives us options)



#Set Customer Info
def setCustomerName(custID, name):

    query_db("UPDATE customers SET customerName = ? WHERE customerId = ?", (name, custID))
    return("customerName has been updated to " + name)

def setCustomerEmail(custID, email):
    query_db("UPDATE customers SET customerEmail = ? WHERE customerId = ?", (email, custID))
    return("customerEmail has been updated to " + email)

def setCustomerPhoneNum(custID, phoneNum):
    query_db("UPDATE customers SET customerPhoneNum = ? WHERE customerId = ?" , (phoneNum, custID))
    return("customerPhoneNum has been updated to " + phoneNum)


#Set Vehicle Info
def setVehicleMake(vehID, make):
    query_db("UPDATE vehicles SET make = ? WHERE customerId = ?", (make, vehID))
    return("make has been updated to " + make)

def setVehicleModel(vehID, model):
    query_db("UPDATE vehicles SET model = ? WHERE customerId = ?", (model, vehID))
    return("model has been updated to " + model)

def setVehicleYear(vehID, year):
    query_db("UPDATE vehicles SET year = ? WHERE customerId = ?", (year, vehID))
    return("year has been updated to " + year)


#Set Repair Info
def setRepairType(repID, repairType):
    query_db("UPDATE repairs SET repairType = ? WHERE repairId = ?", (repairType, repID))
    return("repair type has been updated to " + repairType)

def setRepairDescription(repID, repairDescription):
    query_db("UPDATE repairs SET repairDescription = ? WHERE repairId = ?", (repairDescription, repID))
    return("repair description has been updated to " + repairDescription)

def setRepairAccepted(repID, accepted):
    query_db("UPDATE repairs SET accepted = ? WHERE repairId = ?", (accepted, repID))
    return("status has been updated to " + accepted)


#BIG RED BUTTON FUNCTIONS
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
        query_db("DELETE FROM reapirs;")
    else:
        return ("Data whipe canceled")

#Remove a row
#-----------------------------------------------------------------------------------------------------------


#Remove repair
def RemoveRepair(repID):
    query_db("DELETE FROM repairs WHERE repairId = ?", repID)

#Remove vehicle
def RemoveVehicle(vehID):
    query_db("DELETE FROM vehicles WHERE vehicleId = ?", vehID)
    query_db("DELETE FROM repairs WHERE vehicleId = ?", vehID)
    #Deletes repairs associated with vehicle

#Remove customer
def RemoveCustomer(cusID):
    #Write while loop until refPoint does not exist if doesnt work. 

    refPoint = vehicle.query.filter_by(customerId = cusID)
    #Sets point of referance to customerId in vehicle table

    transferPoint = repairs.query.filter_by(vehicleId = refPoint.vehicleId)
    #Gets a point of transfer that accesses vehicleId in repairs table using refPoint

    query_db("DELETE FROM repairs WHERE repairId = ?", transferPoint.repairId)
    #Deletes repairs associated with deleted car using repairId gathered from transferPoint
    query_db("DELETE FROM vehicles WHERE customerId = ?", cusID)
    query_db("DELETE FROM customers WHERE customerId = ?", cusID)


















    


    
