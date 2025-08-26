# # Input:
# # str = hello 
# # x = llo
# # Output:
# # hello 
# # 2 
# # Hello 
# # HELLO

# def trim(str):
#     str = str.strip()
#     return str


# def exists(str, x):
#     count = 0
#     if x in str:
#         return str.index(x)


# def titleIt(str):
#     return str.capitalize()


# def casesSwap(str):
#     return str.upper()

# Function to check if string
# starts and ends with 'gfg'
# def gfg(S):
#     b = S.lower()
#     if (b.startswith('gfg') and b.endswith('gfg')):
#         print("Yes")
#     else:
#         print("No")


# Given a string s. The task is to convert string characters to lowercase.
# class Solution:
#     def toLower (self , s : str)-> str :
#         return s.lower()

# Given a string s, reverse the string without reversing its individual words. Words are separated by dots(.).
# class Solution:
#     def reverseWords(self, s):
#         forward = s
#         lst = list(forward.split('.'))
#         lst1 = lst[: :-1]
#         backward = ".".join(lst1)
#         return backward

# Function to Welcome the person
# def welcomeAboard(name):
    # print(f"Welcome {name}")  # Your code here


# Input: 
# bound_by = [[]], tag_name = tag
# Output:
# [[tag]]
# Function to join given bound_by and tag
# def join_middle(bound_by, tag_name):
  # complete the statement below to return the string as required
#   return bound_by[0 :   2 ] + tag_name + bound_by[ 2: ]

# # Function to join given strings
# def combo_string(a, b):
#     longer , short = None , None
#     if len(a) > len(b):
#         longer = a
#         short = b
#     else:
#         longer = b
#         short = a

#     return short + longer + short

# class Solution:
#     def isPalindrome(self, s):
#         if s == s[: : -1]:
#             return True 
#         else: 
#             return False
        
# Remove Duplicate 
# class Solution:
#     def removeDuplicates(self, s):
#         seen = set()
#         result = ""

#         for ch in s:
#             if ch not in seen:
#                 result += ch
#                 seen.add(ch)
#         return result

# Check Anagram 
# class Solution:
#     def areAnagrams(self, s1, s2):
#         if s1 in s2:
#             return "Anagram"
#         else:
#             return "Not Anagram"


