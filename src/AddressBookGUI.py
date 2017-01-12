#Main .py file to launch GUI version of address book
import easygui as gui
from AddressBook import *
from tkinter.tix import ButtonBox

addrBook = AddressBook()



def mainAddressBookWindow():
    greetingMessage = "Hello, and welcome to your AddressBook!\nPlease select your menu choice below!"
    mainTitle = "Address Book Application"
    menuChoices = ["List Contacts", "Load Contacts from file", "Add a Contact", "Delete a Contact", "Search for a Contact",
                "Save Contacts to File", ]

    choice = gui.choicebox(greetingMessage, mainTitle, menuChoices)
    if choice == "List Contacts":
        listContacts()
    elif choice == "Load Contacts from file":
        loadContacts()
    elif choice == "Add a Contact":
        addContact()
    elif choice == "Delete a Contact":
        deleteContact()
    elif choice == "Search for a Contact":
        searchContact()
    elif choice == "Save Contacts to File":
        saveContacts()
        
    #print(choice)
    #return choice

def loadContacts():
    addrBook.loadEntries('AddressEntries.txt')
    listContacts()
    
def saveContacts():
    addrBook.saveEntries('AddressEntries.txt')
    mainAddressBookWindow()

def listContacts():
    greetingMessage = "Please select a contact to change, or select cancel to go back"
    title = "Address Book Application: Contacts"
    if len(addrBook.getEntries()) <=0:
        listChoices = ["There are no contacts in your address book"]
    else:
        listChoices = addrBook.getEntries()
    choice = gui.choicebox(greetingMessage, title, listChoices)
    if choice == None or choice == "There are no contacts in your address book":
        mainAddressBookWindow()
    else:
        print(choice)
        idNum = choice.split("[")
        idNum = idNum[1].split("]")
        idNum = int(idNum[0])
        print(idNum)
        contactPrompt(idNum)

def contactPrompt(idNum):
    greetingMessage = "What would you like to do with the contact?\n"+addrBook.getEntryID(idNum).__repr__()
    title = "Contact Option Pane"
    contactChoices = ["Delete Contact", "Return to Main Menu"]
    buttonSelected = gui.buttonbox(greetingMessage, title , contactChoices, None, None, "Return to Main Menu")
    if buttonSelected == None or buttonSelected == "Return to Main Menu":
        mainAddressBookWindow()
    elif buttonSelected == "Delete Contact":
        addrBook.removeEntryID(idNum)
        listContacts()
        #print(buttonSelected)

 
def addContact():
    message = "Please enter the details for a new contact. Cancel to go back."
    title = "Add a Contact"
    fieldNames = ["First Name", "Last Name", "Street Address", "City", "State", "Zip Code", "Email", "Telephone"]
    fieldValues = []
    fieldValues = gui.multenterbox(message, title, fieldNames)
    addrBook.addCreatedEntry(fieldValues)
    listContacts()
#listContacts()    
#prompt = contactPrompt()
    
def deleteContact():
    greetingMessage = "Please select a contact you would like to Delete"
    title = "Address Book Application: Contacts"
    if len(addrBook.getEntries()) <=0:
        listChoices = ["There are no contacts in your address book to delete"]
    else:
        listChoices = addrBook.getEntries()
    choice = gui.choicebox(greetingMessage, title, listChoices)
    if choice == None or choice == "There are no contacts in your address book":
        mainAddressBookWindow()
    else:
        idNum = choice.split("]")
        idNum = idNum[0].split("[")
        idNum = int(idNum[1])
        addrBook.removeEntryID(idNum)
        listContacts()
        
def searchContact():
    message = "Please type the last name of the contact you would like search for."
    title = "Find a Contact"
    contactName = gui.enterbox(message, title)
    foundEntries = addrBook.findEntry(contactName)
   
    if len(foundEntries) <=0:
        contactsFound = "There were no contacts found"
    else:
        contactsFound = ""
        for contact in foundEntries:
            contactsFound = contactsFound+"\n"+contact.__repr__()+"\n"
    title2 = "Contacts found matching "+contactName
    message = gui.msgbox(contactsFound, title2, ok_button="Go Back")
    #choice = gui.choicebox(greetingMessage, title, listChoices)
    if message == None or message == "Go Back":
        mainAddressBookWindow()
    
            
        
    
userChoice = mainAddressBookWindow()
