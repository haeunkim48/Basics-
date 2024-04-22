# 1. create inheritance using animal Dog relation.
# for example, 
#     Animal and Dog both has same habitat so create a method for habitat 

class Animal: 
    def __init__(self, habitat): 
        self.habitat = habitat
    def print_habitat(self):
        print (self.habitat)
    def sound(self):
        print ('Some Animal Sound')

class Dog(Animal):
    def __init__(self):
        super().__init__("Kennel")

    def sound(self):
        print ('woof woof!')

x = Dog()
x.print_habitat
x.sound()

# Design a class hierarchy with inheritance between Animal and Bird, where both have a common method for sound(). Utilize super() constructor for calling the parent constructor.
# Your task is to implement the Animal class with a constructor that takes a species parameter and a method describe_species() that prints the species of the animal. Then, implement the Bird class that inherits from Animal and adds an additional attribute wingspan and a method describe_bird() to describe the bird.

class Animal: 
    def species(self, species):
        self.species = species
    def describe_species(self):
        print (f'This animal belongs to this species:', {self.species})

    def sound (self, sound):
        self.describe_sound = sound

class Bird(Animal):
    def __init__ (self, species, parrot):
        super.__init__("species")
        self.parrot = parrot

    def describe_bird(self):
        print(f"This bird belongs to the species: {self.species} and has a wingspan of {self.parrot}.")

    def sound(self):
        print("Tweet tweet!")
