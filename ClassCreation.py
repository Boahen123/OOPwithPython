''' You can model almost anything using classes. Let’s start by writing a simple 
class, Dog, that represents a dog—not one dog in particular, but any dog. 
What do we know about most pet dogs? Well, they all have a name and age. 
We also know that most dogs sit and roll over. Those two pieces of information (name and age) and those two behaviors (sit and roll over) will go 
in our Dog class because they’re common to most dogs. This class will tell 
Python how to make an object representing a dog. After our class is written, 
we'll use it to make individual instances, each of which represents one specific dog. '''

# Creating the dog class
# A function that’s part of a class is a method


class Dog():
    """A simple attempt to model a dog.""" 
 
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
 
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
            """Simulate rolling over in response to a command."""
            print(self.name.title() + " rolled over!")