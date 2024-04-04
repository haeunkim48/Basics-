student = {'name' : 'John', 'age' : 25, 'course' : ['Math', 'Comsci']}

print (student ['course'])

student['phone'] = '555-555'
student ['name'] = 'Jane' # you can update the key by giving another key
student.update({'name': 'Jane', 'age': '26'}) # update method is when you want to change multiple keys in dictionary 

# when you want to check if there is the keys 
print(student.get('phone', 'Not found')) # not found is when there is no key, it prints out not found

del student ['age'] # when you want to delete the key

age = student.pop('age')
print (age)

print(len(student))
print(student.keys()) # when you want to see all the keys
print(student.values()) # when you want to see all the values
print(student.items()) #keys and values

for key, value in student.items():
    print(key, value)
