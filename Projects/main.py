# this program manages contacts.
import contact
import pickle

# global constants for menu choices.
LOOK_UP=1
ADD=2
CHANGE=3
DELETE=4
QUIT=5

# global constant for the filename.
FILENAME= 'contacts.dat'

# main function
def main():
    ''' The main function '''
    
    # Load the existing contact dictionary and
    # assign it to mycontacts.
    mycontacts=load_contacts()
    
    # initialize a variable for the user's choice.
    choice=0
    
    # process menu selections until user 
    # wants to quit the program
    while choice != QUIT:
        # get the user's menu choice.
        choice = get_menu_choice()
        
        # process the choice.
        if choice==LOOK_UP:
            look_up(mycontacts)
        elif choice==ADD:
            add(mycontacts)
        elif choice==CHANGE:
            change(mycontacts)
        elif choice==DELETE:
            delete(mycontacts)
            
    # save the mycontacts dictionary to a file
    save_contacts(mycontacts)
    