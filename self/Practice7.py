# Reverse a list in Python
# list1 = [100, 200, 300, 400, 500]
# list1.reverse()
# print(list1)

# Concatenate two lists index-wiseConcatenate two lists index-wise
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# list3 = [i+j for i,j in zip(list1,list2)]
# print(list3)

# Turn every item of a list into its square
# numbers = [1, 2, 3, 4, 5, 6, 7]
# square = [i**2 for i in numbers]
# print(square)

# Concatenate two lists in the following order
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]

# for i in list1:
#     for j in list2:
#         print((i+j))

# res = [x+y for x in list1 for y in list2]
# print(res)

# Iterate both lists simultaneously
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]

# for x, y in zip(list1, list2[::-1]):
#     print(x, y)

# Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# res =list(filter(None,list1))
# print(res)

# Add new item to list after a specified item
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# # understand indexing
# # list1[0] = 10
# # list1[1] = 20
# # list1[2] = [300, 400, [5000, 6000], 500]
# # list1[2][2] = [5000, 6000]
# # list1[2][2][1] = 6000
# list1[2][2].append(7000)
# print(list1)

# Extend nested list by adding the sublist
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub_list = ["h", "i", "j"]
# # understand indexing
# # list1[2] = ['c', ['d', 'e', ['f', 'g'], 'k'], 'l']
# # list1[2][1] = ['d', 'e', ['f', 'g'], 'k']
# # list1[2][1][2] = ['f', 'g']
# # 2122
# list1[2][1][2].extend(sub_list)
# print(list1)

# Replace list’s item with new value if found
# list1 = [5, 10, 15, 20, 25, 50, 20]

# index = list1.index(20)

# list1[index] = 200
# print(list1)

# Remove all occurrences of a specific item from a list.
list1 = [5, 20, 15, 20, 25, 50, 20]

value = 20

update = [i for i in list1 if i != value]
print(update)
