# Min and max in array
# arr = [3, 2, 1, 56, 10000, 167]
# print(min(arr) , max(arr))

# Union 
# a = [1, 2, 3, 2, 1]
# b = [3, 2, 2, 3, 3, 2]
# c = a + b
# print(set(c))

# Intersection 
# arr1 = [1, 2, 3, 4]
# arr2 = [2, 4, 6, 7, 8]
# intersection = []
# for i in arr1:
#     if i  in arr2:
#         intersection.append(i)
# print(intersection)

# Maximum of 2 numbers in a python
# # Consecutive
# max_sum = 0
# lst = [2,3,14,5,6,7]

# for i in range(len(lst)-1):
#     if max_sum < (lst[i]+lst[i+1]):
#         max_sum = (lst[i]+lst[i+1])
# print(max_sum)

# lst = [2, 3, 4, 5, 6, 7]
# # Not consecutive
# # initialize two variables
# first = second = float('-inf')

# for num in lst:
#     if num > first:
#         # update both
#         second = first
#         first = num
#     elif num > second:
#         # update only second
#         second = num

# max_sum = first + second
# print("Two largest numbers are:", first, "and", second)
# print("Their sum is:", max_sum)

# Minimum of two numbers in python
# Consecutive
# lst = [1,2,3,4,5,6,1,1]
# min_sum = lst[0]+lst[1]
# for i in range(len(lst)-1):
#     curr = lst[i] + lst[i+1]
#     if curr < min_sum:
#         min_sum = curr

# print(min_sum)

# Non consecutive
# lst = [1,23,45,675,43,2,3,0]

# first = second = float('+inf')

# for i in lst:
#     if i < first:
#         second = first
#         first = i
#     elif i < second:
#         second = i
    
# mini_sum = first + second
# print(mini_sum)

# Swap Two element 
# a=[10,20,30,40,50]

# first = int(input("Enter the  first position you want to swap :- "))
# second = int(input("Enter the second position you want to swap :- "))

# if (first > len(a)) or (second > len(a)):
#     print("Array is out of order for exchange")
# else:
#     a[first] , a[second] = a[second] , a[first]

# print(a)

# Find length of a list
# a = [1, 2, 3, 4, 5]
# c = 0

# for val in a:
#     c += 1

# print(c)
