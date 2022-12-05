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
    print('5. Exit the program')
    print()
    
    # Get the user's choice
    choice = int(input('Enter your choice (1 -5): \n'))
    
    # Validate the user's choice
    while choice < LOOK_UP  or choice > QUIT:
        choice = int(input('Enter your choice from 1 to 5: '))
        
    # return the user's choice
    return choice

c