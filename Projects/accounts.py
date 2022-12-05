class SavingsAccount:
    ''' A class that simulates a savings account'''
    def __init__(self, acc_number, rate, balance):
        self.__acc_number = acc_number
        self.__rate = rate
        self.__balance = balance
        
    # set the mutators
    def set_accnumber(self, acc_number):
        ''' Set the account number '''
        self.__acc_number = acc_number
        
    def set_rate(self, rate):
        ''' Set the interest rate '''
        self.__rate = rate
        
    def set_balance(self, balance):
        ''' Set the savings account balance '''
        self.__balance = balance
        
    # set the accessors
    def get_accnumber(self):
        ''' retrieve the account balance '''
        return self.__acc_number
    
    def get_rate(self):
        ''' retrieve the interest rate '''
        return self.__rate
    
    def get_balance(self):
        ''' retrieve the savings account balance '''
        
class CD(SavingsAccount):
    ''' this class represents the certificate of deposite, with
    account maturity date '''
    def __init__(self, acc_number, rate, balance, maturity_date):
        SavingsAccount.__init__(self, acc_number, rate, balance)
        
        self.__maturity_date = maturity_date
        
    def set_date(self, maturity_date):
        ''' set the maturity date '''
        self.__maturity_date = maturity_date
        
    def get_date(self):
        ''' get the maturity date '''
        return self.__maturity_date
        
    
    
    