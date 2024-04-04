# 1. Suppose you want to write a program that prints numbers from 1 to 10, formatted like this:

# Current value: 1
# Current value: 2
# ...
# Current value: 10
# How can you do that?

for i in range (1,11):
    print ("Current value: ", i)

# 2. Try the above exercise using a while loop. You’ll need to define a counter and an appropriate stopping condition. And you’ll need to manually increment the counter after every loop.
counter = 1
while counter <= 10:
    print ("Counter value: ", counter)
    counter += 1

# 3. Use nested loops to print the following output:

# 111111111
# 222222222
# ...
# 888888888
# 999999999
# First, you will need a string variable where you will add the characters to be printed on the current line.
# If your outer loop uses a variable named i, then your inner loop should use range(0, 9). In the inner loop, all you have to do is add the value of i to the string variable. You have to cast the integer i to a string first with str(i).

# After the inner loop finishes, the outer loop prints the string variable and then sets it to the empty string '', clear for reuse in the next iteration.

line_to_print = 'love'

for i in range(1, 10):
    for j in range (0,9):
        line_to_print += str(i)

for i in range (10):
    for j in range (1, 11):
        print ('*', end = "")