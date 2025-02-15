# Write a program to accept two numbers from the user and calculate multiplication

a = int(input("Enter a number :  "))
b = int(input("Enter a number :  ")) 
print(a*b)

#  Display three string “Name”, “Is”, “James” as “Name**Is**James”

print("My" , "Name" , "Is" , "Parth" , sep='**')

# Convert Decimal number to octal using print() output formatting

num = 16
print('%o' % num)

#  Display float number with 2 decimal places using print()

num = 458.541315
print('%.2f' % num)

# Accept a list of 5 float numbers as an input from the user

numbers = []

for i in range(0,5):
    print("Enter the floating point numbers at index" , i ,":")

    items = float(input())
    numbers.append(items)
print("User List is :" , numbers)


# Write all content of a given file into a new file by skipping line number 5

# read test.txt
with open("self/output.txt", "r") as fp:
    # read all lines from a file
    lines = fp.readlines()

# open new file in write mode
with open("new_file.txt", "w") as fp:
    count = 0
    # iterate each lines from a test.txt
    for line in lines:
        # skip 5th lines
        if count == 4:
            count += 1
            continue
        else:
            # write current line
            fp.write(line)
        # in each iteration reduce the count
        count += 1


# Accept any three string from one input() call

str1, str2, str3 = input("Enter three string").split()
print('Name1:', str1)
print('Name2:', str2)
print('Name3:', str3)

# Format variables using a string.format() method.

quantity = 3
totalMoney = 1000
price = 450
statement1 = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars."
print(statement1.format(quantity, totalMoney, price))

# Check file is empty or not

import os

size = os.stat("self/output.txt").st_size
if size == 0:
    print('file is empty')
else:
    print("Not Empty")

# Read line number 4 from the following file

with open("self/output.txt", "r") as fp:
    # read all lines from a file
    lines = fp.readlines()
    # get line number 4
    print(lines[3])