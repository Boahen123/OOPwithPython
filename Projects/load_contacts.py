def load_contacts():
    ''' Load the existing contact dictionary '''
    try:
        # opening contacts.dat file
        with open(FILENAME,'rb') as input_file:
            #unpickle the dictionary
            contact_dct = pickle.load(input_file)
            
    except IOError:
        # Failed to open file, create new file
        contact_dct = {}
        
    else:
        return contact_dct
    