# 1. Create 3 variables to store street, city and country, now create address variable to
# store entire address. Use two ways of creating this variable, one using + operator and the other using f-string.
# Now Print the address in such a way that the street, city and country prints in a separate line

street = "Hill Street"
city = "Boston"
country = "United States" 

address = street + '\n' + city + '\n' + country
print (address)

address2 = f'{street} {city} {country}'
print (address2)

# 2. Create a variable to store the string "Earth revolves around the sun"
#     1. Print "revolves" using slice operator
#     2. Print "sun" using negative index

a = "Earth revolves around the sun"
print (a[6:14])
print (a[-3:])

# 3. Create two variables to store how many fruits and vegetables you eat in a day.
# Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday.
# Use python f string for this

veggies = 4 
fruits = 3 
print (f"I eat {veggies} veggies and {fruits} fruits daily")

# 4. I have a string variable called s='maine 200 banana khaye'. This of course is a
# wrong statement, the correct statement is 'maine 10 samosa khaye'.
# Replace incorrect words in original strong with new ones and print the new string.
# Also try to do this in one line.

s = 'maine 200 banana khaye'
s = s.replace('200', '100')
s = s.replace ('banana', 'samosa')
print ("Using two line replace:", s)

s = 'maine 200 banana khaye'
s = s.replace('200', '100').replace ('banana', 'samosa')
print ("Using two line replace:", s)





