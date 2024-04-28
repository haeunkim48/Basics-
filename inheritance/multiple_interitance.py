# multiple inheritance
class Father ():
    def skills (self):
        print ("I enjoy gardening")

class Mother():
    def skills (self):
        print ("I enjoy cooking")

class Child (Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print ( 'I enjoy sports ')

c = Child()
c.skills()