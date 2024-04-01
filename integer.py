# Arithmetic Operators: 
# Addition:       3+2
# Subtraction:    3-2 
# Multiplication: 3*2
# Division:       3/2
# Floor Division: 3//2
# Exponent:       3**2
# Modulus:        3%2

# They are the same 
num = 1
num = num + 1
print (num)

num = 1
num += 1

# absolute value abs 
print (abs(-3))

# round the values round
print (round(3.75, 1)) # want to round to the first digit after the decimal

# Comparisons: 
# Equal:             3==2 
# Not equal:         3!=2
# Greater than:      3>2
# Less than:         3<2
# Greater or equal:  3>=2
# Less or equal:     3<=2

num_1 = 3
num_2 = 1

print (num_1 == num_2)


num_3 = '100'
num_4 = '22'

print (num_3 + num_4) # the result comes out as 10022 bc it just concatenates those together 

num_3 = int(num_3) # this int () is called casting 
num_4 = int(num_4)

print (num_3 + num_4)