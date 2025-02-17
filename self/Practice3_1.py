#  Print the following pattern
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
# rows = 5
# for i in range(1 , rows+1 ,1):
#     for j in range(1 ,i+1):
#         print(j , end=" ")
#     print(" ")


# Calculate sum of all numbers from 1 to a given number
# num = 10
# sum = 0
# for i in range(1,num+1,1):
#     sum += i
# print(f"the total of {num} number is :" ,sum)


# Print multiplication table of a given number
# num = int(input("Enter a number you want their multiplication table:  "))
# for i in range(1,11):
#     print(num*i)

# Display numbers from a list using a loop
# numbers = [12, 75, 150, 180, 145, 525, 50]

# The number must be divisible by five
# for i in numbers:
#     if i%5==0:
#         print(i)
#     else:
#         pass

# If the number is greater than 150, then skip it and move to the following number
# for i in numbers:
#     if i <150:
#         print(i)

# If the number is greater than 500, then stop the loop
# for i in numbers:
#     if i>500:
#         break
#     else:
#         print(i)

# All condition in one
# for i in numbers:
#     if i%5==0 and i<=150 and i<500:
#         print(i)

# for i in numbers:
#     if i>500:
#         break
#     elif i>150:
#         continue
#     elif i%5==0:
#         print(i)

# Count the total number of digits in a number
# number = 75869
# count = 0
# while number !=0:
#     number = number //10
#     count = count+1
# print(count)

# Print the following pattern
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

# n = 5
# k = 5
# for i in range(0,n+1):
#     for j in range(k-i,0,-1):
#         print(j,end=' ')
#     print()

# Print list in reverse order using a loop
# list1 = [10, 20, 30, 40, 50]
# lst2 = reversed(list1)

# for i in lst2:
#     print(i)

# Display numbers from -10 to -1 using for loop
# for num in range(-10, 0, 1):
#     print(num)

# Display a message “Done” after the successful execution of the for loop
# for i in range(5):
#     print(i)
# else:
#     print("Done!")

# Print all prime numbers within a range
# start = 25
# end = 50
# print("Prime numbers between", start, "and", end, "are:")

# for num in range(start, end + 1):
#     # all prime numbers are greater than 1
#     # if number is less than or equal to 1, it is not prime
#     if num > 1:
#         for i in range(2, num):
#             # check for factors
#             if (num % i) == 0:
#                 # not a prime number so break inner loop and
#                 # look for next number
#                 break
#         else:
#              print(num)

# Display Fibonacci series up to 10 terms
# num1 =0
# num2 =1
# for i in range(10):
#     print("Current Number is ",num1)
#     result = num1+num2
#     num1 = num2
#     num2 = result

# Find the factorial of a given number
# num =5 
# factorial = 1
# if num<0:
#     print("Factorial doesn't exist")
# elif num == 0:
#     print("The factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial *= i
# print(factorial)

# Reverse a integer number
# num = 76542
# digit = 0
# while num != 0:
#     remainder = num%10
#     digit = (digit*10)+remainder
#     num = num//10
# print(digit)

# Print elements from a given list present at odd index positions
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# new_list = my_list[1::2]
# for i in new_list:
#     print(i , end=" ")

# Calculate the cube of all numbers from 1 to a given number
# cube = int(input("Enter a Range for cube value: "))

# for i in range(1 , cube+1):
#     print( i ,i**3)

# Find the sum of the series up to n terms
# 2 + 22 + 222 + 2222 + 22222 = 24690
# n = 5
# # first number of sequence
# start = 2
# sum_seq = 0

# # run loop n times
# for i in range(0, n):
#     print(start, end="+")
#     sum_seq += start
#     # calculate the next term
#     start = start * 10 + 2
# print("\nSum of above series is:", sum_seq)

# Print the following pattern
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")