import re

def hasData(userInput):
    if len(userInput) == 0:
        return 0
    else:
        return 1

def vinNumber(userInput):
    userInput == userInput.strip()
    if len(userInput) == 17:
        return 1
    else:
        return 0
    
def emailChecker(userInput):
    re.match("[^@]+@[^\.]+\.[a-z]{2,3}",userInput)is not None
     
def checkLength(stringLength, userInput):
    if userInput == stringLength:
        return 1
    else:
        return 0
