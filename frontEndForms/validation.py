class validation:

    
    def hasData(userInput):
        if userInput.length() == 0:
            return 0
        else:
            return 1

    def vinNumber(userInput,year):
        userInput == userInput.strip()
        if year <= 1981: 
            if userInput.length() <= 17 and userInput.length() >= 11:
                return 1 
            else: 
                return 0
        else:
            if userInput.length() <= 17:
                return 1
            else: 
                return 0
    def emailChecker(userInput):
        userInput == userInput.strip
        email = 0
        periodAfterAt = 0 
        spaces = 1
        for letter in userInput:
            count = 0
            if letter =='@':
                email = 1
                break
        for letter in userInput:
            if letter == '.' and email == 1:
                periodAfterAt = 1
                break
        for letter in userInput:
            if letter == ' ':
                spaces = 0
                break
        if email == 1 and periodAfterAt == 1 and spaces == 0: 
            return 1
        else: 
            return 0

    def checkLength(stringLength, userInput):
        if userInput == stringLength:
            return 1
        else:
            return 0




