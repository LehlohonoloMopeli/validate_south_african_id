"""
To run the script or check if an ID is valid, run: 
    print(ValidateSouthAfricanID(Id number, gender, Country of origin).is_id_number_valid())  
    
Example:
    print(ValidateSouthAfricanID("2001014800086", "Female", "South Africa").is_id_number_valid()) 
    
    It should return "ID is valid!"

"""


from datetime import date

class SplitIdentityNumber():
    
    def __init__(self, identityNumber):
        self.identityNumber = identityNumber
        
    def date_of_birth(self):
        for i in range(len(self.identityNumber)):
            return [
                int(self.identityNumber[0:2]),
                int(self.identityNumber[2:4]),
                int(self.identityNumber[4:6])
                ]
        
    def gender(self):
        for i in range(len(self.identityNumber)):
            return int(self.identityNumber[6:10])
        
    def citizenship(self):
        for i in range(len(self.identityNumber)):
            return int(self.identityNumber[10:11])
        
    def last_didgit(self):
        for i in range(len(self.identityNumber)):
            return int(self.identityNumber[12:13])
        
    def odd_numbers(self):
        evenNumbersList = []
        for i in range(0, len(self.identityNumber), 2):
            evenNumbersList.append(int(self.identityNumber[i]))
        return evenNumbersList
    
    def even_numbers(self):
        evenNumbersList = []
        for i in range(1, len(self.identityNumber), 2):
            evenNumbersList.append(int(self.identityNumber[i]))
        return evenNumbersList

class ValidateSouthAfricanID():
    
    def __init__(self, identityNumber, gender, countryOfOrigin):
        self.identityNumber = identityNumber
        self.gender = gender
        self.countryOfOrigin = countryOfOrigin
        self.SplitIdentityNumber = SplitIdentityNumber(self.identityNumber)
        
    def validate_string_length(self):
        
         if (
             type(self.identityNumber) == str 
             and 
             len(self.identityNumber) == 13
            ):
             return True
         else:
             return False
         
    def validate_characters_in_string(self):
        
        if self.identityNumber.isdecimal() == True:
            return True
        else:
            return False 
        
    def validate_date_of_birth(self):
        dateObject = self.SplitIdentityNumber.date_of_birth()
        
        try:
            if date(
                dateObject[0],
                dateObject[1],
                dateObject[2]
            ):
                return True
        except:
            return False
        
    def validate_gender(self):
        if (0000<=self.SplitIdentityNumber.gender()<=4999 
            and 
            self.gender == "Female"
            or
            5000<=self.SplitIdentityNumber.gender()<=9999 
            and 
            self.gender == "Male"
        ):
            return True
        else:
            return False
        
    def validate_citizenship(self):
        if (
            self.SplitIdentityNumber.citizenship() == 0
            and
            self.countryOfOrigin == "South Africa"
            or 
            self.SplitIdentityNumber.citizenship() == 1
            and
            self.countryOfOrigin != "South Africa"
        ):
            return True
        else:
            return False
        
    def validate_luhn_algorithm(self):
        listOfDoubledNumbers =[]
        listForLuhn = []
        sum = 0
        
        for i in self.SplitIdentityNumber.even_numbers():
            listOfDoubledNumbers.append(i * 2)
            
        for j in listOfDoubledNumbers:
            if j >= 10:
                j -= 9
                listForLuhn.append(j)
            else:
                listForLuhn.append(j)
            
        for n in listForLuhn:
            sum += n
            
        for k in self.SplitIdentityNumber.odd_numbers():
            sum += k
            
        if sum % 10 == 0:
            return True
        else:
            return False
        
    def is_id_number_valid(self):
        
        if self.validate_string_length() == True:
            if self.validate_characters_in_string() == True:
                if self.validate_date_of_birth() == True:
                    if self.validate_gender() == True:
                        if self.validate_citizenship() == True:
                            if self.validate_luhn_algorithm() == True:
                                
                                return "ID is valid!"
                            
                            else:
                                return "Invalid ID!"
                        else:
                            return "Invalid ID!"
                    else:
                        return "Invalid ID!"
                else:
                    return "Invalid ID!"
            else:
                return "Invalid ID!"
        else:
            return "Invalid ID!"
        
        
        
if __name__ == '__main__':
    print(ValidateSouthAfricanID().is_id_number_valid())
        