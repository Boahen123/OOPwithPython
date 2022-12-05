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