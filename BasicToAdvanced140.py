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

# my_dict = {
#  'a': 10,
#  'b': 20,
#  'c': 10,
#  'd': 30,
#  'e': 20
# }

# unique = set()

# for i in my_dict.values():
#     unique.add(i)

# print(unique)

# Q68 Write a Python program to find the sum of all items in a dictionary

# my_dict = {
#  'a': 10,
#  'b': 20,
#  'c': 10,
#  'd': 30,
#  'e': 20
# }

# total = 0
# for i in my_dict.values():
#     total += i

# print(total)

# Q69 Write a Python program to Merging two Dictionaries.
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}

# dict1.update(dict2)

# print(dict1)

# Q70 Write a Python program to convert key-values list to flat dictionary.
# key_values_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

# flat_dict ={}

# for key,value in key_values_list:
#     flat_dict[key] = value

# print(flat_dict)

#  Q71 Write a Python program to insertion at the beginning in OrderedDict.

# from collections import OrderedDict

# ordered_dict = OrderedDict([('b', 2), ('c', 3), ('d', 4)])

# new_item = ('a',1)

# new_ordered_dict = OrderedDict([new_item])

# new_ordered_dict.update(ordered_dict)

# print(new_ordered_dict)

# Q72 Write a Python program to check order of character in string using OrderedDict().

# from collections import OrderedDict

# def check_order(string, reference):
#  # Create OrderedDicts for both strings
#     string_dict = OrderedDict.fromkeys(string)
#     reference_dict = OrderedDict.fromkeys(reference)

#     return string_dict == reference_dict

# input_string= "hello world"
# reference_string = "Helo wrd"

# if check_order(input_string , reference_string):
#     print("The order are similar")

# else:
#     print("Order are not similar")

# Q73 Write a Python program to sort Python Dictionaries by Key or Value.

# sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}
# sorted_dict_by_keys = dict(sorted(sample_dict.items()))

# print("Sorted by keys:")
# for key, value in sorted_dict_by_keys.items():
#     print(f"{key}: {value}")


# Q74 Write a program that calculates and prints the value according to the given formula:
# Following are the fixed values of C and H:
# C is 50. H is 30.
# Q = ((2*C*D)/H)
# import math
# # Fixed values
# C = 50
# H = 30
# # Function to calculate Q
# def calculate_Q(D):
#     return int(math.sqrt((2 * C * D) / H))
# # Input comma-separated sequence of D values
# input_sequence = input("Enter comma-separated values of D: ")
# D_values = input_sequence.split(',')
# # Calculate and print Q for each D value
# result = [calculate_Q(int(D)) for D in D_values]
# print(','.join(map(str, result)))


# Q75 Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional
# array. The element value in the i-th row and j-th column of the array should be i*j.
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

# X, Y = map(int, input("Enter two digits (X, Y): ").split(','))
# # Initialize a 2D array filled with zeros
# array = [[0 for j in range(Y)] for i in range(X)]
# # Fill the array with values i * j
# for i in range(X):
#     for j in range(Y):
#         array[i][j] = i * j

# for row in array:
#  print(row)

# Q76 Write a program that accepts a comma separated sequence of words as input and
# prints the words in a comma-separated sequence after sorting them alphabetically

# input_sentence = input("Enter the words with comma seperateed value: ")

# words = input_sentence.split(',')

# sorted_words = sorted(words)

# sequence_words = ','.join(sorted_words)
# print(sequence_words)


# Q77 Write a program that accepts a sequence of whitespace separated words as input
# and prints the words after removing all duplicate words and sorting them
# alphanumerically.

# input_sequence = input("Enter a sequence of whitespace-separated words: ")

# words = set(input_sequence.split())

# sorted_words = sorted(words)

# sentence_sequence = ' '. join(sorted_words)
# print(sentence_sequence)

# Q79 Write a program that accepts a sentence and calculate the number of letters and
# digits. Suppose the following input is supplied to the program:

# sentence = input("Enter a sentence that contain Alphabets and Numbers : ")

# letter_count = 0
# digit_count = 0

# for char in sentence:
#     if char.isalpha():
#         letter_count+=1
#     elif char.isdigit():
#         digit_count+=1
    
# print(letter_count)
# print(digit_count)

# Q80 A website requires the users to input username and password to register. Write a
# program to check the validity of password input by users. Following are the criteria
# for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will
# check them according to the above criteria. Passwords that match the criteria are to
# be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1

# import re

# def is_valid_password(password):
#     if 6 <= len(password) <= 12:
#         if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])", password):
#             return True
#     return False

# passwords = input("Enter passwords separated by commas: ").split(',')
# valid_passwords = []
# for psw in passwords:
#     if is_valid_password(psw):
#         valid_passwords.append(psw)

# print(','.join(valid_passwords))

# Q81 Define a class with a generator which can iterate the numbers, which are divisible by
# 7, between a given range 0 and n.

# class DivisibleBySeven:

#     def __init__(self , n):
#         self.n = n
    
#     def generator_divisible_by_seven(self):
#         for num in range(self.n+1):
#             if num%7==0:
#                 yield num
# n = int(input("Enter your desired range: "))
# divisible_by_seven_generator = DivisibleBySeven(n).generate_divisible_by_seven()
# for num in divisible_by_seven_generator:
#     print(num)

# Q82 Write a program to compute the frequency of the words from the input. The output
# should output after sorting the key alphanumerically. Suppose the following input is
# supplied to the program:

# input string = New to Python or choosing between Python 2 and Python 3? Read Python 2 or
# Python 3.

# input_sentence = input("Enter a Sentence: - ")

# words = input_sentence.split()

# word_freq = {}

# for word in words:

#     word = word.strip('.,?')
#     word = word.lower()

#     if word in word_freq:
#         word_freq[word] +=1
#     else:
#         word_freq = 1

# sorted_words = sorted(word_freq.items())

# for word ,frequency in sorted_words:
#     print(f"{word}:{frequency}")

# Q83 Define a class Person and its two child classes: Male and Female. All classes have a
# method "getGender" which can print "Male" for Male class and "Female" for Female
# class

# class Person:
#     def getGender(self):
#         print("This is Person Class Get Gender Function")

# class Male(Person):
#     def getGender(self):
#         return "Male"

# class Female(Person):
#     def getGender(self):
#         return "Female"


# print(Person().getGender())
# print(Male().getGender())
# print(Female().getGender())

# Q84 Please write a program to generate all sentences where subject is in ["I", "You"] and
# verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

# subjects = ["I", "You"]
# verbs = ["Play", "Love"]
# objects = ["Hockey", "Football"]
# sentences = []

# for sbj in subjects:
#     for vrb in verbs:
#         for obj in objects:
#             sentence = f"{sbj} {vrb} {obj}"
#             sentences.append(sentence)

# for sentence in sentences:
#     print(sentence)

# Q85 Please write a program to compress and decompress the string "hello world!hello
# world!hello world!hello world!".

# import zlib 

# string = "hello world!hello world!hello world!hello world!"

# # Compress the string
# compressed_string = zlib.compress(string.encode())
# # Decompress the string
# decompressed_string = zlib.decompress(compressed_string).decode()
# print("Original String:", string)
# print("Compressed String:", compressed_string)
# print("Decompressed String:", decompressed_string)

# Q86 Please write a binary search function which searches an item in a sorted list. The
# function should return the index of element to be searched in the list.
# def search(lst , target):
#     l,r= 0,len(lst)-1
#     while l <= r:
#         mid = (l+r) // 2

#         if lst[mid] == target:
#             return mid
#         elif lst[mid] < target:
#             l = mid+1
#         else: 
#             r = mid-1
#     return -1
# sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# target_element = 4
# result = search(sorted_list, target_element)
# if result != -1:
#  print(f"Element {target_element} found at index {result}")
# else:
#  print(f"Element {target_element} not found in the list")

# Q87 Please write a program using generator to print the numbers which can be divisible
# by 5 and 7 between 0 and n in comma separated form while n is input by console.

# def divisible_by_5_and_7(n):
#     for num in range(n+1):
#         if num%5==0 and num%7==0:
#             yield num

# try:
#     n = int(input("Enter a value for n : "))
#     result = divisible_by_5_and_7(n)
#     print(','.join(map(str,result)))
# except ValueError:
#     print("Please enter a valid integer for n.")

# Q88 Please write a program using generator to print the even numbers between 0 and n in
# comma separated form while n is input by console.

# def even_num(nums):
#     for num in nums:
#         if num%2==0:
#             yield num

# try:
#     n = int(input("Enter a value for n : "))
#     result = even_num(n)
#     print(','.join(map(str,result)))
# except ValueError:
#     print("Please enter a valid integer for n.")


# Q89 Please write a program using list comprehension to print the Fibonacci Sequence in
# comma separated form with a given n input by console.

# def fibonacci(n):
#     sequence = [0, 1] 
#     [sequence.append(sequence[-1] + sequence[-2]) for _ in range(2, n)]
#     return sequence

# try:
#     n = int(input("Enter a value for n : "))
#     result = fibonacci(n)
#     print(','.join(map(str,result)))
# except ValueError:
#     print("Please enter a valid integer for n.")


# Q90 Assuming that we have some email addresses in the
# "username@companyname.com (mailto:username@companyname.com)" format,
# please write program to print the user name of a given email address. Both user
# names and company names are composed of letters only.

# def extract_name(email):
#     name = email.split('@')

#     if len(email)==2:
#         return name[0]
#     else:
#         print("Invalid Format")

# try:
#     n = int(input("Enter a value for n : "))
#     result = extract_name(n)
#     print(','.join(map(str,result)))
# except ValueError:
#     print("Please enter a valid integer for n.")

# Q91 Define a class named Shape and its subclass Square. The Square class has an init
# function which takes a length as argument. Both classes have an area function which
# can print the area of the shape where Shape's area is 0 by default.

# class Shape:
#     def __init__(self):
#         pass 

#     def area(self):
#         return 0

# class Square(Shape):
#     def __init__(self,length):
#         super().__init__()
#         self.l = length
#     def area(self):
#         return (self.l)**2

# Q92 Write a function that stutters a word as if someone is struggling to read it. The first
# two letters are repeated twice with an ellipsis ... and space after each, and then the
# word is pronounced with a question mark ?.
# stutter("incredible") ➞ "in... in... incredible?"
# def stutters(word):
#     if len(word)<2:
#         return "Word must be atleast 2 character long"
#     stutter_word = f"{word[:2]}... {word[:2]}...{word}"
#     return stutter_word

# Q93 Create a function that takes an angle in radians and returns the corresponding angle
# in degrees rounded to one decimal place.
# Examples
# radians_to_degrees(1) ➞ 57.3
# radians_to_degrees(20) ➞ 1145.9
# radians_to_degrees(50) ➞ 2864.8

# import math

# def radians_to_degrees(radians):
#     degrees = radians * (180/ math.pi)
#     return round(degrees,1)

# print(radians_to_degrees(1))
# print(radians_to_degrees(20))
# print(radians_to_degrees(50))

# Q94 In this challenge, establish if a given integer num is a Curzon number. If 1 plus 2
# elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a
# Curzon number.
# Given a non-negative integer num, implement a function that returns True if num is a
# Curzon number, or False otherwise.

# def is_curzon(num):
#     if num<0:
#         return "Enter a positive number"
#     elif ((2**num)+1)%((2*num)+1)==0:
#         return f"{num} is a curzon number"
#     else:
#         return f"{num} is not a curzon number"

# print(is_curzon(6))

# Q95 Given the side length x find the area of a hexagon.
# import math 

# def hexagon(length):
#     area = (3*(math.sqrt(3))* (length**2))/2
#     return round(area,1)

# Q96 Create a function that returns a base-2 (binary) representation of a base-10 (decimal)
# string number. To convert is simple: ((2) means base-2 and (10) means base-10)
# 010101001(2) = 1 + 8 + 32 + 128.

# def binary(decimal):
#     binary_str = ""
#     while decimal > 0:
#         remainder = decimal % 2
#         binary_str = str(remainder) + binary_str
#         decimal = decimal // 2
#     return binary_str if binary_str else "0"

# Q97 Create a function that takes three arguments a, b, c and returns the sum of the
# numbers that are evenly divided by c from the range a, b inclusive.

# def evenlu_divisible(a,b,c):
    # total = 0
    # for num in range(a,b+1):
    #     if num%c==0:
    #         total+=num
    # return total

# Q98 Create a function that returns True if a given inequality expression is correct and
# False otherwise
# correct_signs("3 < 7 < 11") ➞ True
# correct_signs("13 > 44 > 33 <1") ➞ False
# correct_signs("1 < 2 < 6 < 9 > 3") ➞ True

# def correct_sign(expression):
#     try:
#         return eval(expression)
#     except:
#         return False

# Q99 Create a function that replaces all the vowels in a string with a specified character.
# Examples
# replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"

# def replace_vowels(sentence):
#     vowels = "AEIOUaeiou"
#     if vowels in sentence:
#         sentence = sentence.replace(vowels ,"#")
#     return sentence


# Q100 Write a function that calculates the factorial of a number recursively

# def factorial(num):
#     if num == 0:
#         return 1
#     else:
#         return num*(factorial(num-1))


# Q101 Hamming distance is the number of characters that differ between two strings.
# To illustrate:
# String1: "abcbba"
# String2: "abcbda"
# Hamming Distance: 1 - "b" vs. "d" is the only difference.

# def hamming_distance(str1, str2):
#     if len(str1) != len(str2):
#         raise ValueError("Input strings must have the same length")
#     distance = 0

#     for i in range(len(str1)):
#         if str1[i] != str2[i]:
#             distance += 1 # Increment the counter for differences
#     return distance

# Q102 Create a function that takes a list of non-negative integers and strings and return a
# new list without the strings.
# Examples
# filter_list([1, 2, "a", "b"]) ➞ [1, 2]
# def filter_list(obj):
#     filtered_list = []
#     if isinstance(obj ,int):
#         filtered_list.append(obj)
#     elif isinstance(obj ,(list,tuple)):
#         for item in obj:
#             filtered_list.extend(filter_list(item))
#     return filtered_list


# Q103 The "Reverser" takes a string as input and returns that string in reverse order, with
# the opposite case. Examples
# reverse("Hello World") ➞ "DLROw OLLEh"

# def reverser(s):
#     return (s[ : :-1 ].swapcase())

# Q104 You can assign variables from lists like this:
# lst = [1, 2, 3, 4, 5, 6]
# first = lst[0]
# middle = lst[1:-1]
# last = lst[-1]
 
# writeyourcodehere = [1, 2, 3, 4, 5, 6]
# # Unpack the list into variables
# first, *middle, last = writeyourcodehere
# print(first)
# print(middle)
# print(last)


# Q105 Write a function that calculates the factorial of a number recursively.
# Examples
# factorial(5) ➞ 120

# def fact(num):
#     if num == 0:
#         return 1
#     return num * fact(num-1)


# Q106 Write a function that moves all elements of one type to the end of the list.
# move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]

# def move_to_end(lst, element):
#     count = lst.count(element)
#     lst = [x for x in lst if x != element]
#     lst.extend([element] * count)
#     return lst

# Q107 Create a function that takes a string and returns a string in which each character is
# repeated once

# def double_char(s):
#     double_str = ""

#     for char in s:
#         double_str += char*2
#     return double_str

# Q108 Create a function that reverses a boolean value and returns the string "boolean
# expected" if another variable type is given.
# Examples
# reverse(True) ➞ False

# def reverser(value):
#     if isinstance(value , bool):
#         return not value
#     else:
#         return "bool expected"

# Q109 Create a function that returns the thickness (in meters) of a piece of paper after
# folding it n number of times. The paper starts off with a thickness of 0.5mm.
# Examples
# num_layers(1) ➞ "0.001m"
# - Paper folded once is 1mm (equal to 0.001m)
# num_layers(4) ➞ "0.008m"
# - Paper folded 4 times is 8mm (equal to 0.008m)

# def num_layers(n):
#     initial_thickness_mm = 0.5 # Initial thickness in millimeters
#     final_thickness_mm = initial_thickness_mm * (2 ** n)
#     final_thickness_m = final_thickness_mm / 1000 # Convert millimeter
#     return f"{final_thickness_m:.3f}m"


# Q110 Create a function that takes a single string as argument and returns an ordered list
# containing the indices of all capital letters in the string.
# index_of_caps("eDaBiT") ➞ [1, 3, 5]

# def index_of_caps(word):
#     return [i for i, char in enumerate(word) if char.upper()]

# Q111 Using list comprehensions, create a function that finds all even numbers from 1 to
# the given number.

# def even_num(nums):
#     even = [x for x in range(1 ,nums+1) if x%2==0]
#     return even

# print(even_num(56))

# Q112 Create a function that takes a list of strings and integers, and filters out the list so
# that it returns a list of integers only.
# Examples
# filter_list([1, 2, 3, "a", "b", 4]) ➞ [1, 2, 3, 4]

# def filter_list(lst):
    # return [x for x in lst if isinstance(x,int)]

# Q113 Given a list of numbers, create a function which returns the list but with each
# element's index in the list added to itself. This means you add 0 to the number at
# index 0, add 1 to the number at index 1, etc...

# def add_index(lst):
#     return [i+val for i,val in enumerate(lst)]
        
# Q114 Create a function that takes the height and radius of a cone as arguments and returns
# the volume of the cone rounded to the nearest hundredth. See the resources tab for
# the formula.

# import math
# def cone_volume(height, radius):
#     if radius == 0:
#         return 0
#     volume = (1/3) * math.pi * (radius**2) * height
#     return round(volume, 2)

# Q115 This Triangular Number Sequence is generated from a pattern of dots that form a
# triangle. The first 5 numbers of the sequence, or dots, are:
# 1, 3, 6, 10, 15
# This means that the first triangle has just one dot, the second one has three dots, the
# third one has 6 dots and so on.

# def triangle(n):
#     if n < 1:
#         return 0
#     return n * (n + 1) // 2
# print(triangle(5))

# Q116 Create a function that takes a list of numbers between 1 and 10 (excluding one
# number) and returns the missing number.

# def missing_num(lst):
#     total_sum = sum(range(1, 11)) 
#     given_sum = sum(lst)
#     missing = total_sum - given_sum
#     return missing

# Q117 Write a function that takes a list and a number as arguments. Add the number to the
# end of the list, then remove the first element of the list. The function should then
# return the updated list.

# def next_in_line(lst, num):
#     if lst:
#         lst.pop(0) 
#         lst.append(num) 
#         return lst
#     else:
#         return "No list has been selected"

# Q118 Create the function that takes a list of dictionaries and returns the sum of people's budgets.
# Examples
# get_budgets([
# { 'name': 'John', 'age': 21, 'budget': 23000 },
# { 'name': 'Steve', 'age': 32, 'budget': 40000 },
# { 'name': 'Martin', 'age': 16, 'budget': 2700 }
# ]) ➞ 65700

# def get_budgets(lst):
#     total_budget = sum(person['budget'] for person in lst)
#     return total_budget

# Q119 Create a function that takes a string and returns a string with its letters in
# alphabetical order.

# def sorting(txt):
#     return "".join(sorted(txt))

# Q120 Create a function that accepts the principal p, the term in years t, the interest rate r,
# and the number of compounding periods per year n. The function returns the value at
# the end of term rounded to the nearest cent.

# def compound_interest(p, t, r, n):
#  #compound interest formula
#     a = p * (1 + (r / n)) ** (n * t)
#     return round(a,2)

# Q121 Write a function that takes a list of elements and returns only the integers.

# def return_integer(lst):
#     return [x for x in range(lst) if isinstance(x,int)]

# Q122 Create a function that takes three parameters where:
# - x is the start of the range (inclusive).
# - y is the end of the range (inclusive).
# - n is the divisor to be checked against.

# def divisible_by_third(x,y,n):
#     return [i for i in range(x,y+1) if i%n==0]

# Q123 Create a function that takes in two lists and returns True if the second list follows the
# first list by one element, and False otherwise. In other words, determine if the second
# list is the first list shifted to the right by 1.

# def simon_says(list1, list2):
#     return list1[:-1] == list2[1:]

# Q124 A group of friends have decided to start a secret society. The name will be the first
# letter of each of their names, sorted in alphabetical order. Create a function that takes
# in a list of names and returns the name of the secret society.
# Examples
# society_name(["Adam", "Sarah", "Malcolm"]) ➞ "AMS"

# def society_name(names):
#     secret_name = ''.join(sorted([name[0] for name in names]))
#     return secret_name

# Q125 An isogram is a word that has no duplicate letters. Create a function that takes a
# string and returns either True or False depending on whether or not it's an "isogram"

# def isogram(txt):
#     word = txt.lower()
#     unique_letters = set()
#     for letter in txt:
#         if letter not in unique_letters:
#             unique_letters.add(letter)
#     return unique_letters

# Q126 Create a function that takes a string and returns True or False, depending on whether
# the characters are in order or not.

# def checkorder(str):
#     return str == "".join(sorted(str))

# Q127 Create a function that takes a number as an argument and returns True or False
# depending on whether the number is symmetrical or not. A number is symmetrical
# when it is the same as its reverse.

# def symmetrical(num):
#     reverse_num = 0
#     original = num
#     while num != 0:
#         reverse_num = reverse_num*10 + num%10
#         num = num//10
#     return reverse_num == num 
# print(symmetrical(5665))

# Q128 Given a string of numbers separated by a comma and space, return the product of
# the numbers.
# Examples
# multiply_nums("2, 3") ➞ 6

# def multiply_num(nums_str):

#     nums = [int(num) for num in nums_str.split(", ")]
#     result = 1

#     for num in nums:
#         result *= num
#     return result


# Q129 Create a function that squares every digit of a number.
# Examples
# square_digits(9119) ➞ 811181

# def square_digits(n):
#     num_str = str(n)
#     result_str = ""
#     for digit in num_str:
#         squared_digit = int(digit) ** 2
#     result_str += str(squared_digit)


# Q130 Create a function that sorts a list and removes all duplicate items from it.
# def setify(lst):
#     unique_set = set(sorted(lst))

#     return unique_set

# Q131 Create a function that returns the mean of all digits.
# def mean(n):
#     n_str = str(n)
#     digit_sum = sum(int(digit) for digit in n_str)

#     digit_count = len(n_str)
#     digit_mean = digit_sum / digit_count

#     return int(digit_mean)

#Q132 Create a function that takes an integer and returns a list from 1 to the given number,
# where:
# 1. If the number can be divided evenly by 4, amplify it by 10 (i.e. return 10 times the
# number).
# 2. If the number cannot be divided evenly by 4, simply return the number.
# def amplify(num):
#  return [n * 10 if n % 4 == 0 else n for n in range(1, num + 1)]

#Q133 Create a function that takes a list of numbers and return the number that's unique.
def unique(numbers):
    count_dict = {}

    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    for num, count in count_dict.items():
        if count == 1:
            return num