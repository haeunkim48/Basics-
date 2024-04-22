class Vehicle: 
    def general_usage(self):
        print ('General use: transportation')

class Car(Vehicle):
    def __init__(self) :
        print (" I am car")
        self.wheels = 4
        self.has_roof = True
    
    def specific_usage (self):
        self.general_usage()
        print ('specific use: commute to work')

class Motorcycle(Vehicle):

    def __init__(self) :
        print (" I am motorcycle")
        self.wheels = 4
        self.has_roof = True
    
    def specific_usage (self):
        print ('specific use: road trip')

c = Car()
c.general_usage ()
c.specific_usage()

m = Motorcycle()
m.general_usage()
m.specific_usage()

isinstance()

