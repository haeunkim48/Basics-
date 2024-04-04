language = 'Java'

if language == 'Python':
    print ('Language is Python')
    
elif language == 'Java':
    print ('Language is Java')
elif language == 'JavaScript':
    print ('Language is JavaScript')  

else: 
    print('No match')

# and 
# or 
# not # it changes true to false, and false to true 
    
user = 'Admin'
logged_in = True 

if user == 'Admin' and logged_in:
    print ('Admin Page')

else: 
    print ('Bad creds')

# not
if not logged_in:
    print ('Please log in')
else: 
    print ('Welcome')

a = [1, 2, 3]
b = [1, 2, 3]

print (a ==  b) # it prints out true bc they have the same values
print (a is b) # false, bc they are identified as different object in the memory

a = [1, 2, 3]
b = a

print(id(a))
print(id(b))
print (a is b) # this evaluates true, bc they are the same object

# False values: 
    # False 
    # None 
    # Zero of any numberic type 
    # Any empty sequence, for example '', (), []
    # Any empty mapping, for example {}

# input function, they will see this whenever they run
num = input ("Enter a number: ") 
num = int(num)

if num %2  == 0: 
    print ("number is even")

else:
    print ("number is odd")