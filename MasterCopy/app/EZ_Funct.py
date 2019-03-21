#EZ_Funct

#Sean Kudrna --> Getters and Setters for Database
import database
from flask import current_app, g


#GETTERS
#---------------------------------------------------------------


#Get Customer Info
#-----------------
def getCustomerName(email):
                        #This may have to be changed to .query_db
    refPoint = customers.query.filter_by(customerEmail = email)
    #refPoint = customer email

    return (refPoint.customerName)
    #Return the name associated with customer email

def getCustomerEmail(name):
                        #This may have to be changed to .query_db
    refPoint = customers.query.filter_by(customerName = name)
    #refPoint = customer name

    return (refPoint.customerEmail)
    #Retrun the email associated with the customer name

def getCustomerPhone(email):
                        #This may have to be changed to .query_db
    refPoint = customers.query.filter_by(customerEmail = email)
    #refPoint = customer email

    return (refPoint.customerPhoneNum)
    #Retrun the phone number associated with the customer name




#Get Car Info
#-------------
def getMake(email):
                        #This may have to be changed to .query_db
    refPoint = customers.query.filter_by(customerEmail = email)
    #refPoint = customer email

    transferID = refPoint.customerID
   #transferID = customer ID number

                        #This may have to be changed to .query_db
    vehicle_refPoint = vehicles.query.filter_by(transferID)
    #vehicle_refPoint = customer ID number attached to vehicles table

    return(vehicle_refPoint.make)
    #Return the make associated with customerID number

def getModle(email):
                        #This may have to be changed to .query_db
    refPoint = customers.query.filter_by(customerEmail = email)
    #refPoint = customer email

    transferID = refPoint.customerID
    #transferID = customer ID number

                        #This may have to be changed to .query_db
    vehicle_refPoint = vehicles.query.filter_by(transferID)
    #vehicle_refPoint = customer ID number attached to vehicles table

    return(vehicle_refPoint.model)
    #Return the model associated with customerID number

def getYear(email):
                        #This may have to be changed to .query_db
    refPoint = customers.query.filter_by(customerEmail = email)
    #refPoint = customer email

    transferID = refPoint.customerID
    #transferID = customer ID number

                        #This may have to be changed to .query_db
    vehicle_refPoint = vehicles.query.filter_by(transferID)
    #vehicle_refPoint = customer ID number attached to vehicles table

    return(vehicle_refPoint.year)
    #Return the year associated with customerID number




#Get Repair Info
#--------------
def getRepairType(email):
                        #This may have to be changed to .query_db
    refPoint = customers.query.filter_by(customerEmail = email)
    #refPoint = customer email

    transferID = refPoint.customerID
    #transferID = customer ID number

                        #This may have to be changed to .query_db
    vehicle_refPoint = vehicles.query.filter_by(transferID)
    #vehicle_refPoint = customer ID number attached to vehicles table

    transferID_Layer2 = vehicle_refPoint.vehicleID
    #transferID_Layer2 = vehicleID number

    repair_refPoint = repairs.query.filter_by(transferID_Layer2)
    #repair_refPoint = vehicle ID number attached to repairs table

    return(repair_refPoint.repairType)
    #Return the repair type associated with vehicle ID number

def getRepairDescription(email):
                        #This may have to be changed to .query_db
    refPoint = customers.query.filter_by(customerEmail = email)
    #refPoint = customer email

    transferID = refPoint.customerID
    #transferID = customer ID number

                        #This may have to be changed to .query_db
    vehicle_refPoint = vehicles.query.filter_by(transferID)
    #vehicle_refPoint = customer ID number attached to vehicles table

    transferID_Layer2 = vehicle_refPoint.vehicleID
    #transferID_Layer2 = vehicleID number

    repair_refPoint = repairs.query.filter_by(transferID_Layer2)
    #repair_refPoint = vehicle ID number attached to repairs table

    return(repair_refPoint.repairDescription)   
    #Return the repair description associated with vehicle ID number

def getStatus(email):
                        #This may have to be changed to .query_db
    refPoint = customers.query.filter_by(customerEmail = email)
    #refPoint = customer email

    transferID = refPoint.customerID
    #transferID = customer ID number

                        #This may have to be changed to .query_db
    vehicle_refPoint = vehicles.query.filter_by(transferID)
    #vehicle_refPoint = customer ID number attached to vehicles table

    transferID_Layer2 = vehicle_refPoint.vehicleID
    #transferID_Layer2 = vehicleID number

    repair_refPoint = repairs.query.filter_by(transferID_Layer2)
    #repair_refPoint = vehicle ID number attached to repairs table

    return(repair_refPoint.accepted)   
    #Return the status associated with vehicle ID number



#SETTERS
#-----------------------------------------------------------------------
#I'm pretty sure this is how you wrap sql code into python? we may have to do this for the methods above if they dont work... shouldn't be too difficult to update if needed.
#(I did these a different way just in case the ones above dont work --> gives us options)



#Set Customer Info
#-----------------
def setcustomerName(name):
    query_db("UPDATE customers SET customerName = ?", name)
    return("customerName has been updated to " + name)

def setcustomerEmail(email):
    query_db("UPDATE customers SET customerEmail = ?", name)
    return("customerEmail has been updated to " + email)

def setcustomerPhoneNum(phoneNum):
    query_db("UPDATE customers SET customerPhoneNum = ?", phoneNum)
    return("customerPhoneNum has been updated to " + phoneNum)


#Set Vehicle Info
#----------------
def setmake(make):
    query_db("UPDATE vehicles SET make = ?", make)
    return("make has been updated to " + make)

def setmodel(model):
    query_db("UPDATE vehicles SET model = ?", model)
    return("model has been updated to " + model)

def setyear(year):
    query_db("UPDATE vehicles SET year = ?", year)
    return("year has been updated to " + year)


#Set Repair Info
#---------------
def setrepairType(repairType):
    query_db("UPDATE repairs SET repairType = ?", repairType)
    return("repair type has been updated to " + repairType)

def setrepairDescription(repairDescription):
    query_db("UPDATE repairs SET repairDescription = ?", repairDescription)
    return("repair description has been updated to " + repairDescription)

def setaccepted(accepted):
    query_db("UPDATE repairs SET accepted = ?", accepted)
    return("status has been updated to " + accepted)















    


    
