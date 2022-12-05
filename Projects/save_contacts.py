def save_contacts(mycontacts):
    ''' The save_contacts funtion pickles the specified
    object and saves it to the contacts file '''
    
    # Open the file to append contacts
    with open(FILENAME, 'ab') as output_file:
        # pickle the dictionary and save it
        pickle.dump(mycontacts, output_file)

