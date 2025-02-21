# Write a program to create a new string made of an input string’s first, middle, and last character

# str1 = 'James'
# print("Original String is", str1)

# # Get first character
# res = str1[0]

# # Get string size
# l = len(str1)
# # Get middle index number
# mi = int(l / 2)
# # Get middle character and add it to result
# res = res + str1[mi]

# # Get last character and add it to result
# res = res + str1[l - 1]

# print("New String:", res)

# Create a string made of the middle three characters
# str1 = "JhonDipPeta"

# mid = int(len(str1)/2)

# results = str1[mid-1:mid +2]
# print(results)

# Append new string in the middle of a given string
# s1 = "Ault"
# s2 = "Kelly"

# mi = int(len(s1)/2)

# x = s1[:mi:]

# x = x+s2

# x = x + s1[mi:]

# print(x)

# Create a new string made of the first, middle, and last characters of each input string
# s1 = "America"
# s2 = "Japan"

# mid1 = int(len(s1)/2)
# mid2 = int(len(s2)/2)

# s3 = s1[0]+s2[0]+s1[mid1]+s2[mid2]+s1[-1]+s2[-1]

# print(s3)

# Arrange string characters such that lowercase letters should come first
# str1 = 'PyNaTive'
# str2 = ""
# str3= ""
# for i in str1:
#     if i .islower():
#         str2+=i
#     else:
#         str3+=i

# after_filter = str2+str3
# print(after_filter)

# Count all letters, digits, and special symbols from a given string
# str1 = "P@#yn26at^&i5ve"
# chars = 0
# digits = 0
# special_symbols = 0

# for i in str1:
#     if i .isalpha():
#         chars+=1
#     elif i .isdigit():
#         digits+=1
#     else:
#         special_symbols+=1

# print("Total counts of chars,digits and symbols: ")
# print("Characters :" ,chars)
# print("Digits :", digits)
# print("Symbols :" ,special_symbols)

# Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, 
# then the last char of s2, Next, the second char of s1 and second last char of s2, 
# and so on. Any leftover chars go at the end of the result.
# s1 = "Abc"
# s2 = "Xyz"

# # get string length
# s1_length = len(s1)
# s2_length = len(s2)

# # get length of a bigger string
# length = s1_length if s1_length > s2_length else s2_length
# result = ""

# # reverse s2
# s2 = s2[::-1]

# # iterate string 
# # s1 ascending and s2 descending
# for i in range(length):
#     if i < s1_length:
#         result = result + s1[i]
#     if i < s2_length:
#         result = result + s2[i]

# print(result)

# String characters balance Test
# s1 = "Ynt"
# s2 = "PYnative"
# flag = True
# for i in s1:
#     if i in s2:
#         continue
#     else:
#         flag = False
# print(flag)

#  Find all occurrences of a substring in a given string by ignoring the case
# str1 = "Welcome to USA. usa awesome, isn't it?"

# subtring = "USA"
# temp = str1.upper()
# count= temp.count(subtring)
# print(count)

# Calculate the sum and average of the digits present in a string
# str1 = "PYnative29@#8496"
# sum = 0
# length = 0
# for i in str1:
#     if i .isdigit():
#         sum+=int(i)
#         length+=1

# avg = sum/length

# print("The sum is " , sum)
# print("The average is " ,avg)


# Write a program to count occurrences of all characters within a string
# str1 = "Apple"

# # create a result dictionary
# char_dict = dict()

# for char in str1:
#     count = str1.count(char)
#     # add / update the count of a character
#     char_dict[char] = count
# print('Result:', char_dict)

# Reverse a given string
# str1 = "PYnative"
# temp = str1[::-1]
# print(temp)

# Find the last position of a given substring
# str1 = "Emma is a data scientist who knows Python. Emma works at google Emma."
# print("Original String is:", str1)

# index = str1.rfind("Emma")
# print("Last occurrence of Emma starts at index:", index)

# Split a string on hyphens
# str1 = "Emma-is-a-data-scientist"

# temp = str1.split('-')
# for i in temp:
#     print(i)

# Remove empty strings from a list of strings

# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# temp =[]
# for i in str_list:
#     if i:
#         temp.append(i)
# print(temp)

# Remove special symbols / punctuation from a string
# import string

# str1 = "/*Jon is @developer & musician"
# print("Original string is ", str1)

# new_str = str1.translate(str.maketrans('', '', string.punctuation))

# print("New string is ", new_str)
# -----------------------------------------
# import re

# str1 = "/*Jon is @developer & musician"
# print("Original string is ", str1)

# # replace special symbols with ''
# res = re.sub(r'[^\w\s]', '', str1)
# print("New string is ", res)

# Removal all characters from a string except integers
# str1 = 'I am 25 years and 10 months old'
# str2 = "".join([item for item in str1 if item.isdigit()])
# print(str2)

# Find words with both alphabets and numbers
# str1 = "Emma25 is Data scientist50 and AI Expert"
# print("The original string is : " + str1)

# res = []
# # split string on whitespace
# temp = str1.split()

# # Words with both alphabets and numbers
# # isdigit() for numbers + isalpha() for alphabets
# # use any() to check each character

# for item in temp:
#     if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
#         res.append(item)

# print("Displaying words with alphabets and numbers")
# for i in res:
#     print(i)


# Replace each special symbol with # in the following string
import string

str1 = '/*Jon is @developer & musician!!'
print("The original string is : ", str1)

# Replace punctuations with #
replace_char = '#'

# string.punctuation to get the list of all special symbols
for char in string.punctuation:
    str1 = str1.replace(char, replace_char)

print("The strings after replacement : ", str1)


