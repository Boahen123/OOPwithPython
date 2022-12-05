# Papa Kofi's cell phone

# this program tests the CellPhone class.

import cellphone

def main():
    ''' get the phone data. '''
    
    man=input("Enter the manufacturer: ")
    mod=input("Enter the model number: ")
    retail=float(input("Enter the retail price: "))
    
    # create an instance of the CellPhone class.
    papa_phone=cellphone.CellPhone(man,mod,retail)
    
    # display the data that was entered.
    print()
    print("Here is the data you entered: ")
    print("Manufacturer:", papa_phone.get_manufact())
    print("Model Number:", papa_phone.get_model())
    print("Retail Price: Ghana Cedis", format(papa_phone.get_retail_price(), ",.2f"), sep=" ")
          
# call the main function
if __name__ == '__main__':
    main()

