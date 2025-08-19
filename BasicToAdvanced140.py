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
# a = 10 
# b = 15

# a = a ^ b
# b = a ^ b
# a = a ^ b

# print(f"The value of a is {a} and b is {b}")

# Q11 Write a Python Program to Check if a Number is Positive, Negative or Zero.
# num = float(input("Enter a num to check whether its a positive,negative or zero:- "))
# if num==0:
#     print("The number you enter is 0")
# elif num>0:
#     print("The number you enter is positive")
# else:
#     print("The number you enter is negative")

# Q12 Write a Python Program to Check if a Number is Odd or Even.
# num = float(input("Enter a num to check whether its a even or a odd:- "))

# if num%2==0:
#     print("The number you enter is even")
# else:
#     print("The number you enter is odd")

# Q13Write a Python Program to Check Leap Year.
# year = int(input("Enter a to check whether its a leap year or not:- "))

# if (year%400==0) and (year%100==0):
#     print(f"{year} is a leap year")

# elif (year%4==0) and (year%100 != 0):
#     print(f"{year} is a leap year")

# else: 
#     print("Not a leap year")

# Q14 Write a Python Program to Check Prime Number
# num = int(input("Enter a number: "))
# # define a flag variable
# flag = False
# if num == 1:
#  print(f"{num}, is not a prime number")
# elif num > 1:
#  # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             flag = True # if factor is found, set flag to True
#             # break out of loop
#             break
# # check if flag is True
# if flag:
#     print(f"{num}, is not a prime number")
# else:
#     print(f"{num}, is a prime number")

# Q15 Write a Python Program to Print all Prime Numbers in an Interval of 1-10.
# lower = 1
# upper = 10
# print("Prime numbers between", lower, "and", upper, "are:")
# for num in range(lower, upper + 1):
#  # all prime numbers are greater than 1
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#             else:
#                 print(num)

# Q16 Write a Python Program to Find the Factorial of a Number
# def fact(num):
#     if num == 1:
#         return 1
#     return num*fact(num-1)

# print(fact(5))

# Q17 Write a Python Program to Display the multiplication Table.
# num = int(input("Enter a number you want a multiplication table:- "))

# for i in range(1,11):
#     print(num*i)

# Q18 Write a Python Program to Print the Fibonacci sequence
# n1 = 0
# n2 = 1
# count = 0
# nterms = int(input("Enter how many number of series you want:- "))

# if nterms <= 0:
#     print("Please enter a positive integer")
# elif nterms ==1:
#     print("Fibonacci Series upto " , nterms ," :-")
#     print(n1)    
# else:
#     while count<nterms:
#         print(n1)
#         nth = n1 + n2
#         # update values
#         n1 = n2
#         n2 = nth
#         count +=1

# Q19 Write a Python Program to Check Armstrong Number?
# num = int(input("Enter a number: "))
# # Calculate the number of digits in num
# num_str = str(num)
# num_digits = len(num_str)
# # Initialize variables
# sum_of_powers = 0
# temp_num = num
# # Calculate the sum of digits raised to the power of num_digits
# while temp_num > 0:
#     digit = temp_num % 10
#     sum_of_powers += digit ** num_digits
#     temp_num //= 10
# # Check if it's an Armstrong number
# if sum_of_powers == num:
#  print(f"{num} is an Armstrong number.")
# else:
#  print(f"{num} is not an Armstrong number.")

# Q20 Write a Python Program to Find Armstrong Number in an Interval.
# Input the interval from the user
lower = int(input("Enter the lower limit of the interval: "))
upper = int(input("Enter the upper limit of the interval: "))
for num in range(lower, upper + 1): # Iterate through the numbers i
    order = len(str(num)) # Find the number of digits in 'num'
    temp_num = num
    sum = 0
    while temp_num > 0:
        digit = temp_num % 10
        sum += digit ** order
        temp_num //= 10
 # Check if 'num' is an Armstrong number
    if num == sum:
        print(num)

