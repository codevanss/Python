# Given two integer numbers, write a Python code 
# to return their product only if the product is equal to or lower than 1000. 
# Otherwise, return their sum.

def sum(a,b):
    return a+b

def mul(a,b):
    return a*b

num1 = input("Enter A Value: ")
num2 = input("Enter A Value: ")
total = 1000

if num1*num2 <= total:
    print(mul(num1,num2))
else:
    print(sum(num1,num2))


# Print the Sum of a Current Number and a Previous number

previous_num = 0
for i in range(1,11):
    print("Current Number " , i, "Previous Number " , previous_num, " And The Sum is " ,previous_num+i)
    previous_num = i


#  Print characters present at an even index number
str = "PYnative"
print(str[0: :2])

# Remove first n characters from a string

str = "PYnative"
n = int(input("Enter the value for n : "))

x = str[n:]
print(x)

def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))

# Check if the first and last numbers of a list are the same
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

if numbers_x[0] == numbers_x[-1]:
    print("True")
else:
    print("False")

# Display numbers divisible by 5
lst =  [10, 20, 33, 46, 55]

for i in lst:
    if i%5==0:
        print(i)
    else:
        pass

# Find the number of occurrences of a substring in a string
str_x = "Emma is good developer. Emma is a writer"
cnt = str_x.count("Emma")
print(cnt)


# Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

n = int(input("Enter the value for N: "))

for i in range(n):
    for j in range(i):
        print(i , end =" ")
    print(" ")

# Check Palindrome Number

def palindrome(number):
    print("original number", number)
    original_num = number
    
    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    # check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")

palindrome(121)
palindrome(125)

# Merge two lists using the following condition odd from list1 and even from list2

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list3 = []

for i in list1:
    if i%2 != 0:
        list3.append(i)
    else:
        pass
print(list3)

for i in list2:
    if i%2 == 0:
        list3.append(i)
    else:
        pass
print("Final list is: " , list3)

# Get each digit from a number in the reverse order.
def reverse(number):
    print("original number", number)
    original_num = number
    
    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10
    print(reverse_num)
reverse(7536)

number = 7536
print("Given number", number)
while number > 0:
    # get the last digit
    digit = number % 10
    # remove the last digit and repeat the loop
    number = number // 10
    print(digit, end=" ")

# Calculate income tax
income = 5000
tax_payable = 0
print("Given income", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    # no tax on first 10,000
    x = income - 10000
    # 10% tax
    tax_payable = x * 10 / 100
else:
    # first 10,000
    tax_payable = 0

    # next 10,000 10% tax
    tax_payable = 10000 * 10 / 100

    # remaining 20%tax
    tax_payable += (income - 20000) * 20 / 100

print("Total tax to pay is", tax_payable)

# Print multiplication table from 1 to 10
for i in range(1 ,11):
    for j in range(1, 11):
        print(i*j , end =" ")
    print("\t\t")
    

# Print a downward half-pyramid pattern of stars
for i in range(5,0,-1):
    for j in range(0, i):
        print(i , end = " ")
    print(" ")

# Get an int value of base raises to the power of exponent
def exponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to the power of", exp, "is: ", result)

exponent(5, 4)