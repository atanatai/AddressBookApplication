
from Entry import *
import re

class AddressBook():
    idNum = 0
    def __init__(self):
        self.addBook = []
    
    def addEntry(self):
        fName = str(input("Enter contact's First Name: "))
        lName = str(input("Enter contact's Last Name: "))
        street = input("Enter their Street Address: ")
        city = input("Enter their City: ")
        state = input("Enter their State: ")
        zipC = input("Enter their Zip Code: ")
        email = input("Enter their Email: ")
        tel = input("Enter their Telephone Number: ")
        
        
        newEntry = Entry(fName, lName, street, city, state, zipC, email, tel, self.getIDNum())
        data = newEntry.toString().split(",")
        data[-1] = data[-1].strip() #prevents \n from being added at end (where there isnt a ',')
        #newEntry2 = Entry(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8])
        self.addBook.insert(self.findEntryPosition(newEntry),newEntry)
        #self.addBook.append(newEntry)
        #self.listEntries()
        self.idNum += 1
        return newEntry.getID()
    
    def addCreatedEntry(self, newContactFields):
        try:
            newContact = Entry(newContactFields[0], newContactFields[1], newContactFields[2], newContactFields[3], newContactFields[4], newContactFields[5], newContactFields[6], newContactFields[7], self.getIDNum())
            self.idNum += 1
            self.addBook.insert(self.findEntryPosition(newContact), newContact)
        except:
            print("Error occured. Insertion failed.")
        
        
    def findEntryPosition(self, entry):
        #newContactFields = entry.getFields()
        insertIndex = 0
        allContacts = []
        compareName = entry.getLastName().lower()
        #print(len(self.addBook))
        if len(self.addBook) <= 0:
            #print("returning 0")
            return insertIndex #no contacts means insert at beginning, at index 0
        for entries in self.addBook:
            allContacts.append(entries.getFields())
        for i in range(0,(len(self.addBook))):
            addressName = self.addBook[i].getLastName().lower()
            #print("Values are "+compareName+" AND "+addressName)
            #print(compareName<=addressName)
            if compareName < addressName:
                #print("Value is less than "+addressName)
                return insertIndex
            elif compareName > addressName:
                assert(str(compareName) > str(addressName))
                #print("Value is larger than "+addressName)
                insertIndex += 1
                continue
            elif compareName == addressName:
                for j in range(i,(len(self.addBook))):
                    if entry.getFields()[0] < allContacts[j][0] and entry.getFields()[1] == allContacts[i][1]:
                        return insertIndex
                    elif entry.getFields()[0] > allContacts[j][0] and entry.getFields()[1] == allContacts[i][1]:
                        insertIndex += 1
                        continue
                    elif entry.getFields()[0] == allContacts[j][0] and entry.getFields()[1] == allContacts[i][1]:
                        return insertIndex
        return insertIndex
                
            
        allContacts.append(entry.getFields())
        print(allContacts)
        def getKey(item):
            return item[1]
        allContacts.sort(key=getKey)
        print(allContacts)
        
    def loadEntries(self, fileName):
        addedContacts = 0
        try:
            addressFile = open(fileName)
            for line in addressFile:
                #print(line)
                data = line.split(",")
                newEntry = Entry(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],self.getIDNum())
                self.idNum += 1
                self.addBook.insert(self.findEntryPosition(newEntry),newEntry)
                addedContacts += 1
            #self.addBook.append(newEntry)
        except:
            print("Error with file opening.")
        finally:
            addressFile.close
            return addedContacts
        
    def saveEntries(self, addressFileName):
        addressFile = open(addressFileName, 'w')
        for entry in self.addBook:
            addressFile.write(entry.toFileString())
            addressFile.write("\n")
        addressFile.close
        
    def removeEntries(self,index):
        self.addBook.pop(index)
    
    def removeEntryID(self, removalID):
        for i in range(0,(len(self.addBook))):
            #print(int(self.addBook[i].getID()) == int(removalID))
            if(int(self.addBook[i].getID()) == int(removalID)):
                self.removeEntries(i)
                return True
        return False
    
    def getEntry(self,index):
        return self.addBook[int(index)]
    
    def getEntryID(self,searchID):
        for i in range(0,(len(self.addBook))):
            #print(int(self.addBook[i].getID()) == int(removalID))
            if(int(self.addBook[i].getID()) == int(searchID)):
                return self.addBook[i]
        
    def sortContacts(self):
        def getKey(item):
            return item[1]
        self.addBook.sort(key=getKey)
        self.listEntries()
         
    def getIDNum(self):
        if len(self.addBook) <= 0 and len(self.addBook) <= self.idNum: #definitely initial contact
            return(0)
        else:
            currentMaxId = int(max(self.getEntryIDs())) + 1
            if(self.idNum >= currentMaxId):
                return self.idNum
            else:
                self.idNum = currentMaxId
            #makes sure the largest number that has been assigned (in case of item deletion) sets the next ID
            return(self.idNum)
            '''
            if self.idNum >= len(self.addBook): #if contacts were deleted, idNum prevents backtracking to old index
                return(self.idNum)
            else:
                self.idNum = len(self.addBook)
            return(self.idNum)
            '''
    
    def listEntries(self):
        if len(self.addBook) <= 0:
            print("AddressBook is Empty.")
            return
        print("Current Entries in the AddressBook")
        for entry in self.addBook:
            print(str(entry.getID())+" : "+str(entry.getFirstName())+" "+str(entry.getLastName()))
    
    def getEntryIDs(self):
        ids = []
        for entry in self.addBook:
            ids.append(entry.getID())
        return ids
            
            
    def listSpecificEntries(self, entryList):
        if len(entryList) <= 0:
            return
        num = 0
        for entry in entryList:
            print(str(entry.getID())+" : "+str(entry.getFirstName())+" "+str(entry.getLastName()))
            num += 1   
            
    def listEntriesFull(self):  
        if len(self.addBook) <= 0:
            print("AddressBook is Empty.")
            return
        print("Current Entries in the AddressBook")
        num = 0
        for entry in self.addBook:
            print(entry) #calls the __doc__ function of the entry class
            print("")
            num += 1  
            
    def findEntry(self,lastName):
        entriesFound = []
        for i in range(0,(len(self.addBook))):  #iterates through every contact in addressbook
            '''
            if (re.match(r"^"+lastName.lower()+"$", self.addBook[i].lName.lower())):
                print("Entry found by re.")
                entriesFound.append(self.addBook[i])
                #return self.addBook[i].toString()
            '''
            #print("Comparing "+self.addBook[i].lName+" to "+lastName)
            #print(self.addBook[i].lName.lower() == lastName.lower())
            if(self.addBook[i].lName.lower() == lastName.lower()):
                print("Entry found.")
                entriesFound.append(self.addBook[i])
                #return self.addBook[i].toString()
            
        return entriesFound
        
    def getEntries(self):
        return(self.addBook)     