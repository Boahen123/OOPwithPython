class Triangle:
    ''' Triangle(contains a method for perimeter determination) '''
    def __init__(self, a, b, c): # Initialize the attributes(variables storing data) for the class
        ''' Initialize the attributes of the class '''
        self.side1 = a
        self.side2 = b
        self.side3 = c

    def perimeter(self): # defining a method(function) for the Triangle class
        ''' Method to calculate the perimeter of a triangle '''
        ans = self.side1 + self.side2 + self.side3
        return ans

t1 = Triangle(3, 4, 5) # t1 is an instance of the Triangle class
calculated_perimeter = t1.perimeter()
print("The perimeter is ", calculated_perimeter, ".", sep="")