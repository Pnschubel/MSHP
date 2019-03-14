#EZ_Funct

#Sean Kudrna --> Getters and Setters for Database
import database
from flask import current_app, g

def getCustomerName(email):
                        #This may have to be changed to .query_db
    refPoint = customers.query.filter_by(customerEmail= email)
    return (refPoint.customerName)

def getCustomerEmail(name):
                        #This may have to be changed to .query_db
    refPoint = customers.query.filter_by(customerName = name)
    return (refPoint.customerEmail)
