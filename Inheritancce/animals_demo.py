import animals
# mammal class
mammal = animals.Mammal('regular mammal')
mammal.show_species()
mammal.make_sound()

cat = animals.Cat()
# cat.show_species()
# cat.make_sound()

dog = animals.Dog()
dog.show_species()
dog.make_sound()

def show_mammal_info(creature):
    ''' creature is an object of the class Mammal or any subclass of Mammal '''
    creature.show_species()
    creature.make_sound()
    
show_mammal_info(cat)
