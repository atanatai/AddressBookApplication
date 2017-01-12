# main .py file for a text based version of address book
from AddressBook import *
import re



class AddressBookApplication():
    addBook = AddressBook()
    
   
    inputNum = 0
    while inputNum != 9:
        print("Press 1 to List Contacts Names")
        print("Press 2 to Load Contacts from file")
        print("Press 3 to Add a Contact")
        print("Press 4 to Delete a Contact")
        print("Press 5 to Search for a Contact")
        print("Press 6 to Save Contacts to file")
        print("Press 7 to List Long Details")
        print("Press 9 to Exit")
        try:
            inputNum = int(input())
        except ValueError:
            print("Not a valid entry\n")
            continue
        
        if inputNum == 1:
            addBook.listEntries()
            
        elif inputNum ==2:
            print("There were "+str(addBook.loadEntries('AddressEntries.txt'))+" successfully added to the current Address Book.")
        elif inputNum ==3:
            entryID = addBook.addEntry()
            print("Contact was added successfully.")
        elif inputNum ==4:
            addBook.listEntries()
            try:
                removeIndex = int(input("Enter the # of the contact you would like to delete (Any other key to exit): "))
                print (removeIndex)
            except:
                print("You cancelled the delete request.\n")
                continue
            try:
                if(addBook.removeEntryID(removeIndex) == True):
                    print("Delete was successful.")
                else:
                    raise ValueError
                #assert(removeIndex not in addBook.getEntryIDs) #Ensures that the user gives a valid index
            except:
                print("That was not a valid index to delete.\n")
                continue
            #addBook.removeEntries(removeIndex)
        elif inputNum == 5:
            #continue
            searchName = input("Enter the Last Name you would like to search for: ")
            results = addBook.findEntry(searchName)
            if len(results) <=0:
                print("There were no contacts found")
            elif len(results) >0:
                print(results)
        elif inputNum ==6:
            addBook.saveEntries('AddressEntries.txt')
        elif inputNum == 7:
            addBook.listEntriesFull()
        elif inputNum ==9:
            print("Thank you for trying! Goodbye!")
            break
        else:
            continue
        print("")