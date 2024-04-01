courses = ['history', 'math', 'korean']
courses_2 = ['art', 'education']
nums = [1, 5, 7, 0]

# print (courses[2])
# print (len(courses))
# print(courses[2:]) slicing to the end 

# if you want to add something at the end 
courses.append('art')
print (courses)

# if you want to add something in the specific location
courses.insert (0, 'art')

# if you want to make the list as an individual and add to the original list 
courses.extend(courses_2) 

# remove 
courses.remove('math')
courses.pop() # it removes the values but also gives you the value that was removed
popped = courses.pop()
print(popped)

# reverse
courses.reverse()

# sorting
courses.sort() # when it comes to string, it ordered alphabetically
nums.sort() # ascending order 
nums.sort(reverse = True) # descending 

# min 
print(min(nums))

# max 
print(max(nums))

# sum 
print (sum(nums))

# finding value
print(courses.index('korean'))

# to check the value if it is in th list 
print ('korean' in courses )

for item in courses: 
    print(item)

for index, course in enumerate(courses, start = 1): #enumerate function index and value
    print (index, course)

# separating
course_str = ', '.join(courses)
print (course_str)

new_list = course_str.split('_')

# Mutable (list) and immutable (tuple)
list_1 = ['history', 'english', 'french']
list_2 = list_1

list_1[0] = 'korean'
print (list_1) # in this case, list 1 and 2 change 
print (list_2)

#Immutable (tuple)
tuple_1 = ('history', 'english', 'french')
tuple_2 = tuple_1 # in this case, it gives you an error 

# set - values that are unordered and no duplicates 
cs_course = {'history', 'english', 'french'}
art_course = {'history', 'design', 'french'}

print(cs_course.intersection (art_course)) 
print(cs_course.difference (art_course)) 
print(cs_course.union (art_course))

# Empty Lists 
empty_list = []
empty_list = list()

# Empty Tuples 
empty_tuple = ()
empty_tuple = tuple()

# Empty sets 
empty_set = {} # this is not right, it is a dict
empty_set = set()

