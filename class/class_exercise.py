# 1. Create a sample class named Employee with two attributes id and name
# employee :
#     id
#     name
# object initializes id and name dynamically for every Employee object created.

# emp = Employee(1, "coder")

class Employee():
    def __init__(self,id, name):
        self.id = id 
        self.name = name
    
    def display (self):
        print (f"ID : {self.id} , Name : {self.name}")


#creating a emp instance of Employee class 

emp = Employee(1, 'coder')

emp.display()

# 2. Use del property to first delete id attribute and then the entire object

# deleting the property of object 
del emp.id

try: 
    print (emp.id)
except NameError:
    print ("emp.id is not defined")

del emp
try: 
    emp.display()
except NameError:
    print ('emp is not defined ')

# handling exception

x = input ("Enter number1: ")
y = input ("Enter number 2: ")
try: 
    z = int(x) / int(y)
except Exception as e:
    print ('exception occurred', e)
    z = None
print ("Division is :", z)
    