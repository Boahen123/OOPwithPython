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
        
        print("Choose which fields to modify")
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
                email = input('Enter the new email address: ')
                 
        elif response == 2:
            # Get an updated email address
            email = input('Enter the new email address: ')
            choice = input("Do you wish to modify the phone number as well? (y for yes,anything else means no) ")
            if choice.lower() == 'y':
                # Get an updated phone number
                phone = input('Enter the new phone number: ')
            
            
        
        