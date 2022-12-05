class Vegetable:
    def __init__(self, vegtype):
        self.__vegtype = vegtype
    def message(self):
        print("I'm a vegetable.")
        
class Potato(Vegetable):
    def __init__(self):
        Vegetable.__init__(self, 'potato')
    def message(self):
        print("I'm a potato.")
        
v = Vegetable('veggie')
p = Potato()
v.message()
p.message()