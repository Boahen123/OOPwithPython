# the Contact class holds contact information of individuals

class Contact:
    ''' the Contact class holds contact information of individuals '''
    
    def __init__(self, name, phone, email):
        ''' Initialize the object with the name, phone number 
        and email address of the person '''
        self.__name = name 
        self.__phone = phone
        self.__email = email 
        
    
    def set_name(self, name):
        ''' the set_name method sets the name attribute '''
        self.__name = name
        
    
    def set_phone(self, phone):
        ''' the set_phone method sets the phone attribute '''
        self.__phone = phone
        
   
    def set_email(self, email):
        ''' the set_email method sets the email attribute '''
        self.__email = email 
        
 
    def get_name(self, name):
        ''' the get_name method returns the name attribute '''
        return self.__name 
    
    
    def get_phone(self, phone):
        ''' the get_phone method returns the phone attribute which is the 
        person's phone number'''
        return self.__phone
    
    
    def get_email(self, email):
        ''' the get_email method returns the email attribute '''
        return self.__email
    
    
    def __str__(self):
        ''' the __str__ method returns the object's state
         as a string. '''
        return "Name: " + self.__name + \
            "\nPhone number: " + self.__phone + \
            "\nEmail address: " + self.__email