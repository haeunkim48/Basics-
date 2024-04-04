# 1. After flipping a coin 10 times you got this result,
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# Using for loop figure out how many times you got heads

count = 0

for heads in result:
    if heads == 'heads':
        count += 1
        print("Heads count: ", count)


# 2. Print square of all numbers between 1 to 10 except even numbers
for i in range(1, 11):
    if i%2 == 0: 
        continue 
    print(i*i)

# 3. Your monthly expense list (from Jan to May) looks like this,

    # Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred. If expense is not found then it should print that as well.

expense_list = [2340, 2500, 2100, 3100, 2980]
month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May']

a = input ("This is my expense: ")
a = int()

for i in range(len(expense_list)):
    if a == expense_list[i]:
        month = i 
        break 


# 4. Lets say you are running a 5 km race. Write a program that,
#    1. Upon completing each 1 km asks you "are you tired?"
#    2. If you reply "yes" then it should break and print "you didn't finish the race"
#    3. If you reply "no" then it should continue and ask "are you tired" on every km
#    4. If you finish all 5 km then it should print congratulations message
    
for i in range (5):
    print (f'You ran {i+1} miles')
    
    tired = input ('Are you tired?')
    if tired == 'yes':
        break 

if i == 4: 
    print ('You just finished 5km!')
else: 
    print ('You did not finish the 5km race! You still ran {i+1} km')

# 5. Write a program that prints following shape

# *
# **
# ***
# ****
# *****

    
for i in range(1,6):
    s = ''
    for j in range (i):
        s += '*'
        
    print (s)



