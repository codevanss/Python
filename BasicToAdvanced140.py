# Q1 Write a Python program to print "Hello Python".
# print("Hello Python")

# Q2 Write a Python program to do arithmetical operations addition and division
# a = int(input("Enter first numbers for addition:-"))
# b = int(input("Enter second numbers for addition:-"))
# print("The Value a is " , a)
# print("The Value b is " , b)
# addition = a+b
# print("The result after addition will be:- " , addition)

# try:
#     divide = a/b
#     print(f"The quotient after division {a}/{b} is:- ",divide)
# except ZeroDivisionError:
#     print("B should be greater than 0")

# Q3 Write a Python program to find the area of a triangle.
#  Formula of area of triangle is 0.5*base*height
# base = float(input("Enter the value of base:- "))
# height = float(input("Enter the value of height:- "))
# area = 0.5*base*height
# print(f"The area of triangle of having {base} and {height} is {area}")

# Q4 Write a Python program to swap two variables.
# a = int(input("Enter first number:-"))
# b = int(input("Enter second number:-"))
# print("The Value a is before swap" , a)
# print("The Value b is before swap" , b)
# a,b=b,a
# print("The Value a is after swap" , a)
# print("The Value b is after swap" , b)
# Swap the values using a temporary variable
# temp = a
# a = b
# b = temp
# Swap the values without using a temporary variable
# a = a ^ b
# b = a ^ b
# a = a ^ b

# a = a - b
# b = a + b
# a = b - a

# Q5 Write a Python program to generate a random number.
# import random
# print(f"Random number: {random.randint(1, 100)}")

# Q6 Write a Python program to convert kilometers to miles
# 1km = 0.621371miles
# km = float(input("Enter the value you want to change from kilometre into  :- "))
# miles = 0.621371
# print(f"Value after changing kilometre into miles : {km*miles}")

# Q7 Write a Python program to convert Celsius to Fahrenheit.
# Formula F = (9/5 × C) + 32
# celsius = float(input("Enter the value of celsius : "))
# farenhite = (9/5 * celsius) + 32 # (1.8 × C) + 32 also
# print(f"The value of {celsius} into Farenhite is :- {farenhite}")

# Q8 Write a Python program to display calendar
# import calendar
# year = int(input("Enter year: "))
# month = int(input("Enter month: "))
# cal = calendar.month(year, month)
# print(cal)

# Q9 Write a Python program to solve quadratic equation.
# import math
# # Input coefficients
# a = float(input("Enter coefficient a: "))
# b = float(input("Enter coefficient b: "))
# c = float(input("Enter coefficient c: "))
# # Calculate the discriminant
# discriminant = b**2 - 4*a*c
# # Check if the discriminant is positive, negative, or zero
# if discriminant > 0:
#  # Two real and distinct roots
#  root1 = (-b + math.sqrt(discriminant)) / (2*a)
#  root2 = (-b - math.sqrt(discriminant)) / (2*a)
#  print(f"Root 1: {root1}")
#  print(f"Root 2: {root2}")
# elif discriminant == 0:
#  # One real root (repeated)
#  root = -b / (2*a)
#  print(f"Root: {root}")
# else:
#  # Complex roots
#  real_part = -b / (2*a)
#  imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
#  print(f"Root 1: {real_part} + {imaginary_part}i")
#  print(f"Root 2: {real_part} - {imaginary_part}i")

# Q10 Write a Python program to swap two variables without temp variable.
a = 10 
b = 15

a = a ^ b
b = a ^ b
a = a ^ b

print(f"The value of a is {a} and b is {b}")