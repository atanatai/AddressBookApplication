'''
Information for a single Entry in the Address Book
fName, lName, street, city, state, zipC, email, tel

@author: Atn
'''
class Entry():
    """
    Entry class docstring. Holds info for a single contact.
    """
    def __init__(self, fName, lName, street, city, state, zipC, email, tel, idNum):
        self.fName = str(fName).strip()
        self.lName = str(lName).strip()
        self.street = str(street).strip()
        self.city = str(city).strip()
        self.state = str(state).strip()
        self.zipC = str(zipC).strip()
        self.email = str(email).strip()
        self.tel = str(tel).strip()
        self.idNum = str(idNum).strip()
        self.fields = [self.fName, self.lName, self.street, self.city, self.state, self.zipC, self.email, self.tel, self.idNum]
    def getLastName(self):
        """
        Returns the last name of the Address Entry
        """
        #print(getLastName.__doc__)
        return self.lName
    
    def getFirstName(self):
        return self.fName
    
    def getID(self):
        return self.idNum
    
    def getFields(self):
        return self.fields
    
    def __repr__(self):
        return(self.lName+", "+self.fName+",\n      "+self.street+",\n      "+self.city+",\n      "+self.state+", "+self.zipC+",\n      "+self.email+",\n      "+self.tel+",\n ["+self.idNum+"]")
        #return("["+self.idNum+"] : "+self.fName+" "+self.lName+",\n      "+self.street+",\n      "+self.city+",\n      "+self.state+", "+self.zipC+",\n      "+self.email+",\n      "+self.tel)
    
    def toString(self):
        return(",".join(self.fields))
        
    def toFileString(self):
        return(self.fName+","+self.lName+","+self.street+","+self.city+","+self.state+","+self.zipC+","+self.email+","+self.tel+","+str(self.idNum))
    
