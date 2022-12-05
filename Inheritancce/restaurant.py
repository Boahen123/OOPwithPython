class Restaurant():
    def __init__(self, name, food_type):
        self.restaurant_name = name
        self.cuisine_type = food_type
        
    def describe_restaurant(self):
        ''' Print out the attributes of Restaurant'''
        print(self.restaurant_name)
        print(self.cuisine_type)
        
    def open_restaurant(self):
        ''' message indicating the restaurant is opened '''
        print("The restaurant is open.")
        
Djoint = Restaurant("The Dining Joint", "Continental dishes")
Barcelos = Restaurant("Barcelos", "Pizza")
Papaye = Restaurant("Papaye", "Fried rice")

Djoint.describe_restaurant()
Barcelos.describe_restaurant()
Papaye.describe_restaurant()

class User():
    ''' Stores user information '''
    def __init__(self, first_name, last_name, age):
        ''' define user's first and last names '''
        self.fname = first_name
        self.lname = last_name
        self.age = age
        
    def describe_user(self):
        ''' Print a summary of the user's information '''
        user_name = f'The name of this user is {self.fname} {self.lname}.'
        user_age = f'The user is {self.age} years old.'
        print(user_name)
        print(user_age)
        
    def greet_user(self):
        ''' Greet the user '''
        greet = f'Hello {self.fname} {self.lname}.'
        print(greet)
        
fname = input("What is your first name?\n")
lname = input("What is your last name?\n")
age = int(input("Please enter your age in digits:\n"))

user1 = User(fname, lname, age)

print()
print()
user1.describe_user()
user1.greet_user()