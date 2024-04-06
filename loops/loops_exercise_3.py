# # 1. Look at the example, infer the rules, and take a picture of the stars.
# # The first row is given N (1 ≤ N ≤ 100).
# # From the first line to the 2×N-1th line, the stars are printed in order.

for i in range (1, 101):
    s = " "
    for j in range (2*i+1):
        s = s + "*"
    print(s)

# #2. You have to say hello to N test cases to solve this problem.

# # across N lines

# # "Hello World, Judge i!"

# # Make a program to print out, where i is the number of the line.
# # (1 ≤ N ≤ 200) is given. 
# # print Hello World, Judge i! per line.

for i in range (1, 101):
    print ("Hello World, Judge", i, "!")

# 3. Write a program that, given the natural number N, outputs one line from N to one.
# given The first row is given a natural number N less than or equal to 100,000.
# Print from the first line to the Nth line in order.


# def print_number(n):
#     for i in range (n, 0, -1):
#         print(i)
# print_number(3)

#4. Write a program that outputs the number of positive integers out of the given N integers.

def count_integer(n):
    count = 0 
    for num in n: 
        if num > 0: 
            count += 1 
        
    return count
N = int(input ("The number of integers: "))
n = list 