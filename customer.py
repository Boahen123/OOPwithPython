# Customer class
class Customer:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone
    
class Car:
    def __init__(self, make, model, year):
        ''' assigning data attributes '''
        self.__make = make
        self.__model = model
        self.__year = year
        
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year
    
# constant for the sales tax rate
TAX_RATE=0.05

# ServiceQuote class
class ServiceQuote:
    def __init__(self, pcharge, lcharge): #pcharge = Part Charges and lcharge = Labor charges
        self.__parts_charges=pcharge
        self.__labor_charges=lcharge
        
    def set_parts_charges(self, pcharge):
        self.__parts_charges=pcharge
        
    def set_labor_charges(self, lcharge):
        self.__labor_charges=lcharge
        
    def get_parts_charges(self):
        return self.__parts_charges
    
    def get_labor_charges(self):
        return self.__labor_charges
    
    def get_sales_tax(self):
        ''' Get sales tax that is cost of parts, with tax inclusive '''
        return self.__parts_charges*TAX_RATE
    
    def get_total_charges(self):
        ''' Get the total charge incurred '''
        return __parts_charges + __labor_charges + \
            (__parts_charges * TAX_RATE)