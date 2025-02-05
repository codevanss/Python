import os

file_path = "C:\\Users\\Akash\\Desktop\\Ishi"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exist")

    if os.path.isfile(file_path):
        print("That's a file")
    if os.path.isdir(file_path):
        print("That's a directory")

else:
    print("the location doesn't exist")