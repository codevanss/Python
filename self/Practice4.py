# Write a program to create a function that takes two arguments, name and age, and print their value

# def func(name,age):
#     print(f"The name is {name} and age is {age}")

# func('Vansh' , 20)


# Write a program to create function func1() to accept a variable length of arguments and print their value.

# def func1(*args):
#     for  i in args:
#         print(i)

# func1(2,3,43,54,6)

# Write a program to create function calculation() 
# such that it can accept two variables and calculate addition and subtraction.
# Also, it must return both addition and subtraction in a single return call.

# def calculation(a,b):
#     return a+b , a-b

# calc = calculation(5,3)
# print(calc)


# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary


# def display(name,salary = 9000):
#     print(f"The Employee name is {name} and the salary is {salary}")

# display("Parth" , 400000)
# display("Vansh")

# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it

# def parameter(a,b):
#     A = a
#     B = b
    
#     def add(A,B):
#         return A+B
    
#     addition = add(a,b)
#     print(addition+5)
    
# parameter(5 ,5)


# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10
# def recur(x):
#     if x:
#         return x + recur(x-1)
#     else:
#         return 0

# res = recur(10)
# print(res)

# Below is the function display_student(name, age). 
# Assign a new name show_tudent(name, age) to it and call it using the new name.

# def display_student(name,age):
#     print(name,age)

# show_display = display_student

# show_display("Vansh" , 20)

#  Generate a Python list of all the even numbers between 4 to 30
# print(list(range(4,30,2)))

# Find the largest item from a given list
# x = [4, 6, 8, 24, 12, 2]
# largest = 0

# for i in x:
#     if i > largest:
#         largest = i
    
# print(largest)
# print(max(x))