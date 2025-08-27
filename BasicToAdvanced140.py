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
# lower = int(input("Enter the lower limit of the interval: "))
# upper = int(input("Enter the upper limit of the interval: "))
# for num in range(lower, upper + 1): # Iterate through the numbers i
#     order = len(str(num)) # Find the number of digits in 'num'
#     temp_num = num
#     sum = 0
#     while temp_num > 0:
#         digit = temp_num % 10
#         sum += digit ** order
#         temp_num //= 10
#  # Check if 'num' is an Armstrong number
#     if num == sum:
#         print(num)

# Q21 Write a Python Program to Find the Sum of Natural Numbers

# num = int(input("Enter the number you want to sum :-  "))

# sum=0

# while num!=0:
#     digit = num % 10
#     sum += digit
#     num//=10

# print(sum)

# Q22 Write a Python Program to Find LCM
# def compute_lcm(x, y):
#     if x > y: # choose the greater number
#         greater = x
#     else:
#         greater = y
#     while(True):
#         if((greater % x == 0) and (greater % y == 0)):
#             lcm = greater
#             break
#             greater += 1
#     return lcm
# num1 = int(input('Enter the number: '))
# num2 = int(input('Enter the number: '))
# print("The L.C.M. is", compute_lcm(num1, num2))

# Q23 Write a Python Program to Find HCF
# def compute_hcf(x, y):
#     if x > y:
#         smaller = y
#     else:   
#         smaller = x
#     for i in range(1, smaller+1):
#         if((x % i == 0) and (y % i == 0)):
#             hcf = i
#     return hcf
# num1 = int(input('Enter the number: '))
# num2 = int(input('Enter the number: '))
# print("The H.C.F. is", compute_hcf(num1, num2))

# Q24 Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal
# num = int(input("Enter the number you want to convert:-  "))

# print(bin(num))
# print(oct(num))
# print(hex(num))

# Q25 Write a Python Program To Find ASCII value of a character
# char = str(input("Enter the character: "))
# print("The ASCII value of '" + char + "' is", ord(char))

# Q26 Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations

# def add(x,y):
#     return x+y

# def sub(x,y):
#     return x-y
    
# def mul(x,y):
#     return x*y

# def div(x,y):
#     return x/y

# num1 = int(input("Enter the first number:- "))
# num2 = int(input("Enter the second number:- "))

# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")

# while True:
#     choice = input("Enter choice(1/2/3/4): ")

#     if choice in ('1','2','3','4'):

#         if choice == "1":
#             print("The result after addition " , add(num1,num2))
        
#         elif choice == "2":
#             print("The result after subtraction " , sub(num1,num2))
        
#         elif choice == "3":
#             print("The result after multiplication " , mul(num1,num2))
        
#         elif choice == "4":
#             print("The result after division " , div(num1,num2))
        
#         else:
#             print("Invalid choice")
        

#         next_calculation = input("Let's do next calculation? (yes/no):")
#         if next_calculation.lower() == "no":
#             break
#         else:   
#             print("Invalid Input")

# Q27 Write a Python Program to Display Fibonacci Sequence Using Recursion
# def recur_fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return(recur_fibo(n-1) + recur_fibo(n-2))
# nterms = int(input("Enter the number of terms (greater than 0): "))
# # check if the number of terms is valid
# if nterms <= 0:
#  print("Plese enter a positive integer")
# else:
#  print("Fibonacci sequence:")
#  for i in range(nterms):
#     print(recur_fibo(i))

# Q28 Write a Python Program to Find Factorial of Number Using Recursion

# def fact(x):
#     if x == 0:
#         return 1
#     else:
#         return x*fact(x-1)

# num = int(input("Enter the number for factorial :- "))

# print(f"The fact of {num} is {fact(num)}")

# Q29 Write a Python Program to calculate your Body Mass Index.
# def bodymassindex(height, weight):
#  return round((weight / height**2),2)


# h = float(input("Enter your height in meters: "))
# w = float(input("Enter your weight in kg: "))

# print("Welcome to the BMI calculator.")

# bmi = bodymassindex(h, w)
# print("Your BMI is: ", bmi)


# if bmi <= 18.5:
#     print("You are underweight.")
# elif 18.5 < bmi <= 24.9:
#     print("Your weight is normal.")
# elif 25 < bmi <= 29.29:
#     print("You are overweight.")
# else:
#     print("You are obese.")

# Q30 Write a Python Program to calculate the natural logarithm of any number.
# import math

# num = float(input("Enter the number :-"))

# if num <=0:
#     print("Please enter positive number.")
# else:
#     result = math.log(num)
#     print("The value of number into logarithm is " , result)

# Q31 Write a Python Program for cube sum of first n natural numbers?
# n= int(input("Enter the number you want sum of their cube :- "))
# total = sum([i**3 for i in range(1,n+1)])
# print(total)

# Q32 Write a Python Program to find sum of array

# arr = [1,2,3,4,5]

# total = 0 
# for i in arr:
#     total +=i
# print(total)

# Q33 Write a Python Program to find largest element in an array.
# arr = [1,2,3,4,55 ,34, 456,467,4,24324465,5474,321,3]
# print(max(arr))

# maxelement = 0 

# for i in arr :
#     if i > maxelement:
#         maxelement = i
    
# print(maxelement)

# Q34 Write a Python Program for array rotation
# def rotate_array(arr, d):
#     n = len(arr)

#  # Check if 'd' is valid, it should be within the range of array len
#     if d < 0 or d >= n:
#         return "Invalid rotation value"

#  # Create a new array to store the rotated elements.
#     rotated_arr = [0] * n

#  # Perform the rotation.
#     for i in range(n):
#         rotated_arr[i] = arr[(i + d) % n]

#     return rotated_arr
# # Input array
# arr = [1, 2, 3, 4, 5]
# # Number of positions to rotate
# d = 2
# # Call the rotate_array function
# result = rotate_array(arr, d)
# # Print the rotated array
# print("Original Array:", arr)
# print("Rotated Array:", result)

# Q35 Write a Python Program to Split the array and add the first part to the end?

# def split_and_add(arr, k):
#     if k <= 0 or k >= len(arr):
#         return arr
#  # Split the array into two parts
#     first_part = arr[:k]
#     second_part = arr[k:]
#  # Add the first part to the end of the second part
#     result = second_part + first_part
#     return result
# # Test the function
# arr = [1, 2, 3, 4, 5]
# k = 3
# result = split_and_add(arr, k)
# print("Original Array:", arr)
# print("Array after splitting and adding:", result)

# Q36 Write a Python Program to check if given array is Monotonic
# def is_monotonic(arr):
#     increasing = decreasing = True
#     for i in range(1, len(arr)):
#         if arr[i] > arr[i - 1]:
#             decreasing = False
#         elif arr[i] < arr[i - 1]:
#             increasing = False
#     return increasing or decreasing
# # Test the function
# arr1 = [1, 2, 2, 3] # Monotonic (non-decreasing)
# arr2 = [3, 2, 1] # Monotonic (non-increasing)
# arr3 = [1, 3, 2, 4] # Not monotonic
# print("arr1 is monotonic:", is_monotonic(arr1))
# print("arr2 is monotonic:", is_monotonic(arr2))
# print("arr3 is monotonic:", is_monotonic(arr3))

# Q37 Add two Matrices
# def add_matrices(mat1, mat2):
#  # Check if the matrices have the same dimensions
#  if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
#     return "Matrices must have the same dimensions for addition"

#  # Initialize an empty result matrix with the same dimensions
#  result = []
#  for i in range(len(mat1)):
#     row = []
#     for j in range(len(mat1[0])):
#         row.append(mat1[i][j] + mat2[i][j])
#         result.append(row)

#  return result
# # Input matrices
# matrix1 = [
#  [1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]
# ]
# matrix2 = [
#  [9, 8, 7],
#  [6, 5, 4],
#  [3, 2, 1]
# ]
# # Call the add_matrices function
# result_matrix = add_matrices(matrix1, matrix2)
# # Display the result
# if isinstance(result_matrix, str):
#  print(result_matrix)
# else:
#  print("Sum of matrices:")
#  for row in result_matrix:
#     print(row)

# Q38 Write a Python Program to Multiply Two Matrices.
# def multiply_matrices(mat1, mat2):
#     # Determine the dimensions of the input matrices
#     rows1 = len(mat1)
#     cols1 = len(mat1[0])
#     rows2 = len(mat2)
#     cols2 = len(mat2[0])
#  # Check if multiplication is possible
#     if cols1 != rows2:
#         return "Matrix multiplication is not possible. Number of column"
#  # Initialize the result matrix with zeros
#     result = [[0 for _ in range(cols2)] for _ in range(rows1)]
#  # Perform matrix multiplication
#     for i in range(rows1):
#         for j in range(cols2):
#             for k in range(cols1):
#                 result[i][j] += mat1[i][k] * mat2[k][j]
#     return result
# # Example matrices
# matrix1 = [[1, 2, 3],
#             [4, 5, 6]]
# matrix2 = [[7, 8],
#             [9, 10],
#             [11, 12]]
# # Multiply the matrices
# result_matrix = multiply_matrices(matrix1, matrix2)
# # Display the result
# if isinstance(result_matrix, str):
#  print(result_matrix)
# else:
#  print("Result of matrix multiplication:")
#  for row in result_matrix:
#     print(row)

# Q39 Write a Python Program to Transpose a Matrix.

# def transpose_matrix(matrix):
#     rows, cols = len(matrix), len(matrix[0])
#  # Create an empty matrix to store the transposed data
#     result = [[0 for _ in range(rows)] for _ in range(cols)]
#     for i in range(rows):
#         for j in range(cols):
#             result[j][i] = matrix[i][j]
#     return result
# # Input matrix
# matrix = [
#  [1, 2, 3],
#  [4, 5, 6]
# ]
# # Transpose the matrix
# transposed_matrix = transpose_matrix(matrix)
# # Print the transposed matrix
# for row in transposed_matrix:
#  print(row)

# Q40 Write a Python Program to Sort Words in Alphabetic Order
# my_str = input("Enter a string: ")
# # breakdown the string into a list of words
# words = [word.capitalize() for word in my_str.split()]
# # sort the list
# words.sort()
# # display the sorted words
# print("The sorted words are:")
# for word in words:
#  print(word)

# Q41 Write a Python Program to Remove Punctuation From a String
# punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# my_str = input("Enter a string :- ")
# str_without_punc = " "

# for i in punctuations:
#     if i not in punctuations:
#         str_without_punc += i
# print(str_without_punc)

# Q42 Sorting withour in built function
# def bubble_sort(arr):
#     n = len(arr)
#     # Traverse through all elements
#     for i in range(n):
#         # Last i elements are already in place
#         for j in range(0, n-i-1):
#             # Swap if element found is greater than next element
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# # Test
# list1 = [64, 25, 12, 22, 11]
# print("Original List:", list1)
# print("Sorted List:", bubble_sort(list1))

# # List: [64, 25, 12, 22, 11]

# # Pass 1 → [25, 12, 22, 11, 64] (64 bubbled to the end)

# # Pass 2 → [12, 22, 11, 25, 64]

# # Pass 3 → [12, 11, 22, 25, 64]

# # Pass 4 → [11, 12, 22, 25, 64] ✅ Sorted


# Q43 Write a Python program to check if the given number is a Disarium Number.
# def is_disarium(numbers):
#     num_str  = str(numbers)

#     digit_sum = sum(int(i)**(index+1) for index , i in enumerate(numbers))

#     return digit_sum == numbers
# try:
#     num = int(input("Enter a number: "))
#  # Check if it's a Disarium number
#     if is_disarium(num):
#         print(f"{num} is a Disarium number.")
#     else:
#         print(f"{num} is not a Disarium number.")
# except ValueError:
#     print("Invalid input. Please enter a valid number.")

# Q44 Write a Python program to print all disarium numbers between 1 to 100. 

# disarium = []
# for i in range(1,100):
#     num_str = str(i)
#     digit_sum = sum(int(n)**(index+1) for index , n in enumerate(num_str))
#     if digit_sum == i:
#         disarium.append(i)
# print(disarium)

# Q45 Write a Python program to check if the given number is Happy Number.

# def is_happy(num):

#     seen = set()

#     while num != 1 and num not in seen:
#         seen.add(num)
#         num  = sum(int(i)**2 for i in str(num))
    
#     return num ==1

# num = int(input("Enter a number"))
# if is_happy(num):
#     print(f"{num} is a happy number")
# else:
#      print(f"{num} is  not a happy number")

# Q46 Write a Python program to print all happy numbers between 1 and 100
# def is_happy(num):
#     seen = set()
#     while num != 1 and num not in seen:
#         seen.add(num)
#        num  = sum(int(i)**2 for i in str(num))
#     return num ==1

# happy_numbers = []

# for i in range(1,101):
#     if is_happy(i):
#         happy_numbers.append(i)
# print(happy_numbers)
 
# Q47 Write a Python program to determine whether the given number is a Harshad Number.

# def harshad_number(num):
#     original_num = num
#     sum_digit = 0
#     while num > 0:
#         digit = num % 10
#         sum_digit += digit
#         num = num // 10
    
#     if original_num % sum_digit== 0:
#         print(f"{original_num} is a harshad number")
#     else:
#         print(f"{original_num} is not a harshad number")

# harshad_number(18)

# Q48 Write a Python program to print all pronic numbers between 1 and 100.
# def is_pronic(num):
#     # check if num can be written as n*(n+1)
#     for n in range(num+1):
#         if n * (n+1) == num:
#             return True
#     return False

# print("Pronic numbers between 1 and 100 are:")
# for i in range(1, 101):
#     if is_pronic(i):
#         print(i, end=" ")

# Q49 Write a python program to find sum of element of list

# numbers = [1,2,3,4,5,6,7,8,9,10]

# total = sum(num for num in numbers)
# print(total)

# Q50 Write a Python program to Multiply all numbers in the list.
# import math
# numbers = [1,2,3,4,5]

# product = math.prod(num for num in numbers)
# print(product)

# Q51 Write a Python program to find smallest number in a list.

# lst = [12,354,4,545,7,7,435,23545,7567]

# print(min(lst))
# smallest = lst[0]

# for i in lst:
#     if i < smallest:
#         smallest = i
# print(smallest)

# Q52 Write a Python program to find largest number in a list.

# lst = [12,354,4,545,7,7,435,23545,7567]

# print(max(lst))
# largest = lst[0]

# for i in lst:
#     if i > largest:
#         largest = i
# print(largest)

# Q53 Write a Python program to find second largest number in a list.

# number = [12,324,5,456,567,43,325,45,74534]
# number.sort(reverse=True)

# print(number[1])

# def second_largest(nums):
#     if len(nums) < 2:
#         return None  # Not enough elements

#     largest = second = float('-inf')  # start with very small numbers

#     for num in nums:
#         if num > largest:
#             # update both largest and second
#             second = largest
#             largest = num
#         elif num > second and num != largest:
#             # update only second largest
#             second = num

#     return second if second != float('-inf') else None

# # Test
# list1 = [10, 20, 4, 45, 99]
# print("Second largest:", second_largest(list1))

# list2 = [5, 5, 5]   # edge case (all same)
# print("Second largest:", second_largest(list2))


# Q54 Write a Python program to find N largest elements from a list

# number = [12,32,5,346,45,756,734,532,4,2356,457,451]

# number.sort(reverse=True)

# N_Largest = int(input("Enter the number :- "))

# if N_Largest > len(number):
#     print("Element is insuffcient")
# else:
#     print(number[N_Largest])

# Q55 Write a Python program to print even numbers in a list.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even = [num for num in numbers if numbers%2==0]

# Q56 Write a Python program to print odd numbers in a List.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd = [num for num in numbers if num%2 != 0]

# Q57 Write a Python program to Remove empty List from List.
# list_of_lists = [[1, 2, 3], [], [4, 5], [], [6, 7, 8], []]
# filtered = [lst for lst in list_of_lists if lst]

# Q58 Write a Python program to Cloning or Copying a list.
# original_list = [1, 2, 3, 4, 5]
# cloned_list = list(original_list)
# print(cloned_list)

# Q59 Write a Python program to Count occurrences of an element in a list.
# lst = [1,2,3,213,1,1,1,3,4,5,6,6,6,6,3,3,3,2,2,2]
# freq = {}
# for i in lst:
#     freq[i] = freq.get(i,0)+1
# print(freq)

# Q60 Write a Python program to find words which are greater than given length k.
# word_list = ["apple", "banana", "cherry", "date", "elderberry", "dragon"]
# k = 5
# result = []
# for i in word_list:
#     if len(i)>k:
#         result.append(i)

# Q61 Write a Python program for removing 𝑖 character from a string.

# str1 = "HelloGuys"
# i = input(f" ({str1}) Enter the ith value you want to remove from this string :- ")
# str1 = str1.replace(i , " ")
# print(str1)

# Q62 Write a Python program to split and join a string.
# input_str = "Python is a high level programming language"
# word_list = input_str.split()

# separator = " "
# result_after_join = separator.join(word_list)

# print("Original :- " , input_str)
# print("After split :- " , word_list)
# print("After Join :- " , result_after_join)

# Q63 Write a Python program to check if a given string is binary string or not.

# def check_binary(str):
#     for i in str:
#         if i not in "01":
#             return False
#     return True

# print(check_binary("01010101sdg"))

# Q64 Write a Python program to find uncommon words from two Strings.
# def find_uncommon(str1 ,str2):
#     words1 = set(str1.split())
#     words2 = set(str2.split())

#     uncommon_words_set = words1.symmetric_difference(words2)

#     uncommon_words_list = list(uncommon_words_set)

#     return uncommon_words_list

# string1 = "This is first string yoyo"
# string2 = "this is second string honey singh"

# uncommon = find_uncommon(string1 , string2)
# print(uncommon)

# Q65 Write a Python program to find all duplicate characters in string
# string1 = "asfuohidg rdnfgdassdf"
# freq = {}
# duplicate = []

# for i in string1:
#     freq[i] = freq.get(i , 0)+1

# for i ,f in freq.items():
#     if f >= 2:
#         duplicate.append(i)

# print("Duplicate Characters are :- ")
# print(duplicate)

# Q66 Write a Python Program to check if a string contains any special character.
# import re 

# pattern = r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\\/\'"\-=]'
# my_str = "Hello World!"
# if re.search(pattern , my_str):
#     print("Special Character Present")
# else:
#     print("Special Character Not Present")

# Q67 Write a Python program to Extract Unique dictionary values

my_dict = {
 'a': 10,
 'b': 20,
 'c': 10,
 'd': 30,
 'e': 20
}

unique = set()

for i in my_dict.values():
    unique.add(i)

print(unique)