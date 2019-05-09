#Orrin and Sean
from app import EZ_Funct

def publish(formInfo):

   #Creates customer from validated form info
   createCustomer(formInfo['customerName'], 
                  formInfo['customerEmail'],
                  formInfo.get('customerPhoneNum'))

   #Creates vehicle form validated from info
   createVehicle(formInfo.get('make'),
                 formInfo.get('model'),
                 formInfo.get('year'),
                 formInfo.get('vin'))

   #Creates repair from validated form info
   createRepair(formInfo['repairType'],
                formInfo['repairDescription'],
                accepted = False,
                completed = False)

