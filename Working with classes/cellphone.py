

class CellPhone:
    ''' The CellPhone class holds data about a cell phone. '''
    
    def __init__(self, manufact, model, price):
        ''' the __init__ method initializes the attributes. '''
        self.__manufact=manufact
        self.__model=model
        self.__retail_price=price
        
    
    def set_manufact(self, manufact):
        ''' the set_manufact method accepts an argument for
        the phone's manufacturer. '''
        self.__manufact=manufact
        
    
    def set_model(self, model):
        ''' the set_model method accepts an argument for
        the phone's model number. '''
        self.__model=model 
        
    
    def set_retail_price(self, price):
        ''' the set_retail_price method accepts an argument
         for the phone's retail price. '''
        self.__retail_price=price 
        
    
    def get_manufact(self):
        ''' the get_manufact method returns the
         phone's manufacturer. '''
        return self.__manufact
    
    
    def get_model(self): 
        ''' the get_model method returns the
        phone's model number. '''
        return self.__model
    
    
    def get_retail_price(self):
        ''' the get_retail_price method returns the
        phone's retail price. ''' 
        return self.__retail_price
    
