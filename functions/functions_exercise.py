# 1. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
# area = (1/2)*base*height

def calculate_area (base, height):
    area = (1/2)*base*height
    return area

n = calculate_area(4,5)
print ("This is area: ", n)

# 2. Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
# rectangle area=length*width

def calculate_area (length, width):
    rectangle_area = length*width
    return rectangle_area

a = calculate_area(4,5)
print ("This is rectangle area: ", a)

# 3. Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
# *
# **
# ***
# if input is 4 then it should print
# *
# **
# ***
# ****
# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)

def print_pattern(n=5):
    
    for i in range (n):
        s = " "
        for j in range (i +1):
            s = s + "*"
            
        print(s)

