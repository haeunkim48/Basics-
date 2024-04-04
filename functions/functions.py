def hello_func():
    print ('Hello Function.')

hello_func() # keeping the code dry which means, you don't have to repeat yourself 

# ---------------------------------
def hi_fun():
    return "hi"

print (hi_fun().upper())

print (len('Test'))

#---------------------------------
def hello_func(greeting):
    return '{} Function.'.format (greeting)
print (hello_func('Hi'))

#---------------------------------
def hello_func(greeting, name = 'You'):
    return '{}, {}'.format(greeting, name)
print (hello_func('Hi', name = 'Grace'))

# -----------------------
def student_info(*args, **kwargs): #*args: return the shape of tuple, **kwargs: dictionary
    print (args)
    print (kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(*courses, **info)

#----------------------------

# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    # year 2017
    # month 2
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print (is_leap(2017))

#--------------------
def calculate_total(exp): # exp: function argument
    total = 0 # reset the variable
    for item in exp:
        total += item 
    return total # return value

tom_exp = [1,2,3]
joe_exp = [4,5,6]

toms_total_exp = calculate_total(tom_exp)
joes_total_exp = calculate_total(joe_exp)

# sum of two numbers
total = 0 # global function, it can be accessed anywhere
def sum (a,b=0):
     #b=0 this is default argument, if there is no b assigned, it becomes 0
    print ("a:", a)
    total = a + b    # local variable: total is only visible inside of the function body
    return total 

n= sum(b = 5,a = 6) # two types of arguments: 1) positional arguments, 2) named arguments and this is named agruments bc they are positioned 

print ("Total: ", n)
