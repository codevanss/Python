# Convert two lists into a dictionary
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# res_dict = dict(zip(keys,values))
# print(res_dict)

# Merge two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# dict3 = {**dict1 ,**dict2}
# print(dict3)

# Print the value of key ‘history’ from the below dict
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }

# # understand how to located the nested key
# # sampleDict['class'] = {'student': {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}}
# # sampleDict['class']['student'] = {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}
# # sampleDict['class']['student']['marks'] = {'physics': 70, 'history': 80}

# # solution
# print(sampleDict['class']['student']['marks']['history'])

# Initialize dictionary with default values
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}

# res = dict.fromkeys(employees, defaults)
# print(res)

# # Individual data
# print(res["Kelly"])

# Create a dictionary by extracting the keys from a given dictionary

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
# keys = ["name", "salary"]
# newDict = {k: sample_dict[k] for k in keys}
# print(newDict)

# res = dict()

# for k in keys:
    ## add current key with its va;ue from sample_dict
    # res.update({k: sample_dict[k]})
# print(res)

# Delete a list of keys from a dictionary
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# # Keys to remove
# keys = ["name", "salary"]

# for k in keys:
#     sample_dict.pop(k)
# print(sample_dict)

# Check if a value exists in a dictionary
# sample_dict = {'a': 100, 'b': 200, 'c': 300}

# for i in sample_dict.keys():
#     if i == 200:
#         print("200 present in a dict as a key")

# for i in sample_dict.values():
#     if i == 200:
#         print("200 present in a dict as a value")

# Rename key of a dictionary
# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }

# sample_dict['location'] = sample_dict['city']
# sample_dict.pop('city')
# print(sample_dict)

# Get the key of a minimum value from the following dictionary

# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# print(min(sample_dict, key=sample_dict.get))

# Change value of a key in a nested dictionary
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
sample_dict['emp3']['salary'] = 8500
print(sample_dict)