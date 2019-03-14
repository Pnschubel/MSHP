#EZ_Funct

#Sean Kudrna --> Getters and Setters for Database
import database
from flask import current_app, g

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

    







    


    
