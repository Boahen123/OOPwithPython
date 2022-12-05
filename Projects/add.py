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
        print('The name provided already exists')
        
    