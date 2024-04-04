nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print ("Found it")
        break # when they found the value, they stop there
    print (num)

for num in nums:
    if num == 3:
        print ("Found it")
        continue # when they find the value, they still continue the loop
    print (num) 

for num in nums:
    for letter in 'abc':
        print (num, letter)

for i in range(1, 11):
    print(i)



x = 0 

while x < 10:
    # if x == 3:
    #     break
    print(x)
    x += 1

# infinite loop but it can be stopped w Ctrl + C
while True: 
    print (x)
    x += 1

# let's say you want to add all the values in the list 
    
a = [1,2,3,4]
total = 0

for i in a: 
    total = total + i 
print (total)

for item in range(len(a)):
    print ("Month : ", item +1 and "Expense :", a[item])




key_location= 'chair'
locations = ['garage', 'living room']

for i in locations:
    if i == key_location:
        print ("key is found in", i)
        break
    else: 
        print ("key is not found in", i)


for i in range (1,6):
    if i%2 == 0:
        continue 

    print (i*i)