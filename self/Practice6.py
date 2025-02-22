# Create a list by picking an odd-index items from the first list and even index items from the second

# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]
# l3=[]
# l4 = []
# odd = len(l1)
# even = len(l2)

# for i in l1[1: :+2]:
#     l3.append(i)
# print("Element at odd index from list 1 " ,l3)

# for i in l2[0: :+2]:
#     l4.append(i)
# print("Element at even index from list 2" ,l4)

# l5 = l3+l4
# print("After adding" ,l5)

# Remove and add item in a list
# list1 = [54, 44, 27, 79, 91, 41]

# index = int(input("Enter the index value you want to pop: "))
# list1.pop(index)
# print(f"List After deleting {index} index from list : "  ,list1)
# list1.insert(2 ,11)
# print(f"The List after insertion 11 at index 2 : " , list1)

# list1.append(11)
# print("The List after append : " , list1)

# Slice list into 3 equal chunks and reverse each chunk
# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

# chunk_size = int(len(sample_list)/3)
# start = 0
# end = chunk_size

# # run loop 3 times
# for i in range(3):
#     # get indexes
#     indexes = slice(start, end)
    
#     # get chunk
#     list_chunk = sample_list[indexes]
#     print("Chunk ", i, list_chunk)
    
#     # reverse chunk
#     print("After reversing it ", list(reversed(list_chunk)))

#     start = end
#     end += chunk_size

# Count the occurrence of each element from a list

# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
# count = 0
# occur ={}

# for i in sample_list:
#     occur[i] = occur.get(i , count)+1
    
# print(occur)

# Create a Python set such that it shows the element from both lists in a pair
# first_list = [2, 3, 4, 5, 6, 7, 8]
# print("First List ", first_list)

# second_list = [4, 9, 16, 25, 36, 49, 64]
# print("Second List ", second_list)

# result = zip(first_list, second_list)
# result_tuple = tuple(result)
# print(result_tuple)

# Find the intersection (common) of two sets and remove those elements from the first set
# first_set = {23, 42, 65, 57, 78, 83, 29}
# second_set = {57, 83, 29, 67, 73, 43, 48}

# common = first_set & second_set
# for i in common:
#     first_set.remove(i)
# print(first_set)

# Checks if one set is a subset or superset of another set. If found, delete all elements from that set
# first_set = {27, 43, 34}
# second_set = {34, 93, 22, 27, 43, 53, 48}

# print("First set is subset of Second Set: " , first_set.issubset(second_set))
# print("Second set is subset of First Set: " , second_set.issubset(first_set))
# print(" ")
# print("First set is superset of Second Set: " , first_set.issuperset(second_set))
# print("Second set is superset of First Set: " , second_set.issuperset(first_set))
# print("")
# if second_set.issubset(first_set):
#     second_set.clear()
#     print("Second set is subset of First Subset" ,second_set)
# else:
#     print("Second set is not subset of First set")

# if first_set.issubset(second_set):
#     first_set.clear()
#     print("First set is subset of Second Subset" ,first_set)
# else:
#     print("First set is not subset of second set")

# Iterate a given list and check if a given element exists as a key’s value in a dictionary. 
# If not, delete it from the list
# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
# sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

# for i in roll_number:
#     if i not in sample_dict.values():
#         roll_number.remove(i)


# print(roll_number)
# print(sample_dict)

# create new list
# roll_number[:] = [item for item in roll_number if item in sample_dict.values()]
# print("after removing unwanted elements from list:", roll_number)

#  Get all values from the dictionary and add them to a list but don’t add duplicates
# speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53,
#          'july': 54, 'Aug': 44, 'Sept': 54}

# print("Dictionary's values - ", speed.values())

# speed_list = list()

# # iterate dict values
# for val in speed.values():
#     # check if value not present in a list
#     if val not in speed_list:
#         speed_list.append(val)
# print("unique list", speed_list)

# Remove duplicates from a list and create a tuple and find the minimum and maximum number
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
print("Original list", sample_list)

sample_list = list(set(sample_list))
print("unique list", sample_list)

t = tuple(sample_list)
print("tuple ", t)

print("Minimum number is: ", min(t))
print("Maximum number is: ", max(t))