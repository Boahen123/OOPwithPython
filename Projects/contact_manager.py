# A program for managing contact information
import contact
import pickle

# global constants for menu choices.
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
SHOW = 5
QUIT = 6

# global constant for the filename.
FILENAME= 'contacts.dat'

# main function
def main():
    ''' The main function '''
    
    # Load the existing contact dictionary and
    # assign it to mycontacts.
    mycontacts = load_contacts()
    
    # initialize a variable for the user's choice.
    choice = 0
    
    # process menu selections until user 
    # wants to quit the program
    while choice != QUIT:
        # get the user's menu choice.
        choice = get_menu_choice()
        
        # process the choice.
        if choice == LOOK_UP:
            look_up(mycontacts)
        elif choice == ADD:
            add(mycontacts)
        elif choice == CHANGE:
            change(mycontacts)
        elif choice == DELETE:
            delete(mycontacts)
        elif choice == SHOW:
            show(mycontacts)
      
        
            
    # save the mycontacts dictionary to a file
    save_contacts(mycontacts)
    
def load_contacts():
    ''' Load the existing contact dictionary, create one if not already existing '''
    try:
        # attempting to open contacts.dat file
        with open(FILENAME,'rb') as input_file:
            #unpickle the dictionary
            contact_dct = pickle.load(input_file)
    except:
        # Failed to open file, create new file
        contact_dct = dict()
    
    return contact_dct
    
def look_up(mycontacts):
    ''' The look_up function looks up an item or keyword in the
    specified dictionary. '''
    
    # Get a name to look up
    name = input('Enter a name to look up: ')
    
    # Search for it in the dictionary
    print(mycontacts.get(name, 'That name is not found.'))
    
def add(mycontacts):
    ''' The add function adds a new entry into the
    specified dictionary '''
    
    # Get the contact's information
    name = input('Name: ')
    phone = input('Phone number: ')
    email = input('Email address: ')
    
    # Create a Contact object named entry
    entry = contact.Contact(name, phone, email)
    
    # If the name does not exist in the dictionary 
    # add it as a key with the entry object as the 
    # associtate value
    
    if name not in mycontacts:
        mycontacts[name] = entry
        print('The entry has been added successfully.')
    else:
        print('The name provided already exists.')
        
def get_menu_choice():
    ''' The get_menu_choice function displays the menu
     and gets a validated choice from the user. '''
     
    print()
    print('This is the Menu')
    print('----------------')
    print('1. Look up an existing contact')
    print('2. Add a new contact')
    print('3. Change an existing contact')
    print('4. Delete a contact')
    print('5. Display contact names')
    print('6. Exit the program')
    print()
    
    # Get the user's choice
    choice = int(input('Enter your choice (1-5): \n'))
    
    # Validate the user's choice
    while choice < LOOK_UP  or choice > QUIT:
        choice = int(input('Enter your choice from 1 to 5: '))
        
    # return the user's choice
    return choice

def change(mycontacts):
    ''' The change function changes an existing
    entry in the specified dictionary '''
    
    # Get name to make changes to
    name = input("Enter the name you want to modify: ")
    
    # Validate the name to confirm its existence in
    # the dictionary
    if name in mycontacts:
        # Be informed about the specific modifications the user
        # wants to make
        
        print("Choose which field to modify")
        print('1. Phone number')
        print('2. Email address')
        
        response = int(input('Enter your choice (1-2): \n'))
        
        # Validate the response
        while response < 1  or response > 2:
            response = int(input('Enter your choice from 1 to 2: '))
            
        if response == 1:
            # Get an updated phone number
            phone = input("Enter the new/updated phone number: ")
            choice = input("Do you wish to modify the email address too?(y for yes,anything else means no) ")
            if choice.lower() == 'y':
                # Get an updated email address
                email = input('Enter the new/updated email address: ')
                 
        elif response == 2:
            # Get an updated email address
            email = input('Enter the new email address: ')
            choice = input("Do you wish to modify the phone number as well? (y for yes,anything else means no) ")
            if choice.lower() == 'y':
                # Get an updated phone number
                phone = input('Enter the new phone number: ')
                
        # Create a new Contact object named entry
        entry = contact.Contact(name, phone, email)
        mycontacts[name] = entry # update the dictionary with this info
        print('Modifications applied successfully')
    else:
        print('Sorry, specified name was not found.')
            
def delete(mycontacts):
    ''' The delete function deletes an entry from the
    specified dictionary. '''
    
    # Get a name to be deleted
    name = input('Enter a name to be deleted: ')
    
    # If the name is found, then deletion is possible
    if name in mycontacts:
        del mycontacts[name]
        print('Entry/Contact deleted successfully.')
        
    else:
        print('Sorry, name was not found.')
        
def show(mycontacts):
    ''' Display the contact list '''
    if mycontacts:
        for item in mycontacts:
            print(item)
    else:
        print("Contact list is empty.")


def save_contacts(mycontacts):
    ''' The save_contacts funtion pickles the specified
    object and saves it to the contacts file '''
    
    # Open the file to append contacts
    with open(FILENAME, 'ab') as output_file:
        # pickle the dictionary and save it
        pickle.dump(mycontacts, output_file)

if __name__=='__main__':
    main()