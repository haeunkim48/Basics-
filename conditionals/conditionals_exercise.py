# 1. Using following list of cities per country,
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

# 1) Write a program that asks user to enter a city name and it should tell which country the city belongs to
# 2) Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"

# 1) 
city = input("Enter city name: ")

if city in india:
    print(f"{city} is in india")
elif city in pakistan:
    print(f"{city} is in pakistan")
elif city in bangladesh:
    print(f"{city} is in bangladesh")
else:
    print(f"I won't be able to tell you which country {city} is in! Sorry!")

#2)
city_1 = input ("Enter the city1: ")
city_2 =input ("Enter the city2: ")

if city_1 and city_2 in india:
    print (f"{city_1} and {city_2} are in India.")
elif city_1 and city_2 in pakistan:
    print (f"{city_1} and {city_2} are in Pakistan.")
elif city_1 and city_2 in bangladesh:
    print (f"{city_1} and {city_2} are in Bangladesh")
else: 
    print(f"{city_1} and {city_2} are not in the same country!")

# 2. Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
#     1. Ask user to enter his fasting sugar level
#     2. If it is below 80 to 100 range then print that sugar is low
#     3. If it is above 100 then print that it is high otherwise print that it is normal

sugar = input("Your sugar is low, go eat some juice :")
sugar = float(sugar)

if sugar <80:
    print ("Your sugar is low, go eat some juice :")
elif sugar >100:
    print ("Your sugar is too high, stop eating")
else: 
    print ("Your sugar level is normal.")
