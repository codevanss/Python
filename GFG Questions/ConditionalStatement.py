# Mark even and odd 
# def checkEven(num):
#     if num % 2 ==0:
#         return "Even"
#     else:
#         return "Odd"

# print(checkEven(5))

# Check the status
# def checkStatus( a, b, flag):
#     if a<0 and b < 0:
#         flag = True
#         return flag
#     else :
#         return flag

# print(checkStatus(-10,-910,"false"))

# Trouble with angry friends

# def friends_in_trouble(j_angry , s_angry):
#     if (j_angry == "yes") and (s_angry== "yes"):
#         print("You are in trouble")
#     elif (j_angry == "yes") or (s_angry== "yes"):
#         print("You are in trouble because any of them is in trouble")
#     else:
#         print("You are not in trouble")
    
# j_angry = input("John are you angry (yes/no): ").lower()
# s_angry = input("Smith are you angry (yes/no): ").lower()

# friends_in_trouble(j_angry,s_angry)

# Cat and Hat 

# str = "catinahat"
# def cat_hat(s):
#     return s.count('cat') == s.count('hat')
# print(cat_hat(str))

# def cat_hat_count(s):
#     cat_count = s.count("cat")
#     hat_count = s.count("hat")
#     is_equal = cat_count == hat_count

#     print(f"'cat' appears {cat_count} times")
#     print(f"'hat' appears {hat_count} times")
#     return is_equal

# # Example tests
# print("Equal?", cat_hat_count("cathatcat"))   # False
# print("Equal?", cat_hat_count("cathat"))      # True

# multiplication table.

# def multiplicationtable(num):
#     for i  in range(1,11):
#         print(num*i)
# multiplicationtable(5)

# string jumper

# def stringJumper(s):
#     for i in range(0,len(s) , 2):
#         print(s[i], end="")
# stringJumper("Parth")

# Decreasing Number
# def printInDecreasing(x):
    
#     while (x >= 0):
#         print(x)
#         x -= 1
    
# printInDecreasing(5)

# Jumping through While 
# x = 10
# square = [i**2 for i in range(1,x+1)]
# print(square)

# Zero Converter
# def pos(n):
#     while n>=0:
#         print(n)
#         n-=1
        
    
# def neg(n):
#     while n<=0:
#         print(n)
#         n +=1

# num = int(input("Enter a number :- "))

# if num==0:
#     print("Number is already Zero")
# elif num>0:
#     pos(num)
# else:
#     neg(num)
