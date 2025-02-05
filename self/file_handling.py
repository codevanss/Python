#***********W**********
# txt_data = "I love Pizza"

# file_path = "self/output.txt"

# with open(file_path , "w") as file:
#     file.write(txt_data)
#     print(f"Your file '{file_path}' has been created")

# **********X*********
# txt_data = "I love Pizza"

# file_path = "self/output.txt"

# try:
#     with open(file_path , "x") as file:
#         file.write(txt_data)
#         print(f"Your file '{file_path}' has been created")
# except FileExistsError:
#     print("File already exists")

# employees = ["Vansh" , "Squidward", "Spongebob" , "Patrick"]

# file_path = "self/output.txt"

# try:
#     with open(file_path , "w") as file:
#         for employee in employees:
#             file.write(employee + " ")
#         print(f"Your file '{file_path}' has been created")
# except FileExistsError:
#     print("File already exists")


#***********A**********

# txt_data = " I love Pizza "

# file_path = "self/output.txt"

# try:
#     with open(file_path , "a") as file:
#         file.write(txt_data)
#         print(f"Your file '{file_path}' has been appened")
# except FileExistsError:
#     print("File already exists")

#*****JSON************

# import json

# employees = {
#     "name": "Vansh",
#     "age": 20,
#     "job": "tutor"
# }

# file_path = "self/output.json"

# try:
#     with open(file_path , "w") as file:
#         json.dump(employees , file , indent=4)
#         print(f"Your json file '{file_path}' has been created")
# except FileExistsError:
#     print("File already exists")

#********CSV**********
# import csv

# employees =[["Name" , "Age" , "Job"],
#             ["Vansh" , 20 , "Tutor"],
#             ["Parth" , 21 , "Programmer"],
#             ["Aditya" , 20 , "Developer"],
#             ["Jeet" , 21 , "Articleship"],
#             ["Aniket" , 20 , "Unemployed"]]
# file_path = "self/output.csv"

# try:
#     with open(file_path , "w" , newline="") as file:
#         writer = csv.writer(file)
#         for row in employees:
#             writer.writerow(row)
#         print(f"Your csv file '{file_path}' has been created")
# except FileExistsError:
#     print("File already exists")

#*********R*********

#        Text

# # file_path = "self/output.txt"

# try:
#     with open(file_path , "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("File was not found")
# except PermissionError:
#     print("You do not have permission to read this file")
# except Exception:
#     print("Something Gone Wrong !")

#     Json

# import json

# file_path = "self/output.json"

# try:
#     with open(file_path , "r") as file:
#         content = json.load(file)
#         print(content)
# except FileNotFoundError:
#     print("File was not found")
# except PermissionError:
#     print("You do not have permission to read this file")
# except Exception:
#     print("Something Gone Wrong !")

#         CSV

import csv

file_path = "self/output.csv"

try:
    with open(file_path , "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
except FileNotFoundError:
    print("File was not found")
except PermissionError:
    print("You do not have permission to read this file")
except Exception:
    print("Something Gone Wrong !")