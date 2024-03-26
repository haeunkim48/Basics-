1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.
long = 92
wide = 48.8

total_area = long * wide 
print (total_area)

2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?
num_packets=9
cost_per_packet=1.49
total_cost=num_packets*cost_per_packet
money_paid=20
cash_back=money_paid-total_cost
print("Cash back:",cash_back)

3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
length = 5.5
area = length **2
cost = area *500
print("total cost for bathroom tiles replacement:",cost)

4. Print binary representation of number 17
num = 17 
print ("This is binary representation of number: " + format(num,'b'))
