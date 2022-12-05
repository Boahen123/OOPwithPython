def look_up(mycontacts):
    ''' The look_up function looks up an item or keyword in the
    specified dictionary. '''
    
    # Get a name to look up
    name = input('Enter a name to look up: ')
    
    # Search for it in the dictionary
    print(mycontacts.get(name, 'That name is not found.'))
    
    