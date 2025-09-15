# Mark Even and Odd

# is_running = True
# while is_running:
#     i = int(input("Enter a number you want to check is the number is even or odd: "))
#     if i == 0:
#         print("Please choose a number other than zero")
#         Play = input("Do you want to continue Y/N? : ").upper()
#         if Play != 'Y':
#             is_running = False
#     elif i%2== 0:
#         print("Even: ",i)
#         Play = input("Do you want to continue Y/N? : ").upper()
#         if Play != 'Y':
#             is_running = False
#     else: 
#         print("Odd: " , i)
#         Play = input("Do you want to continue Y/N? : ").upper()
#         if Play != 'Y':
#             is_running = False


#Check the Status

# a = int(input("Enter 1st Number: "))
# b = int(input("Enter 2nd Number: "))
# flag = input("Enter True or False: ").capitalize()

# if a > 0 or b > 0 and flag == "False":
#     print("True")
# elif a<0 and b<0 and flag == "True":
#     print("True")
# else:
#     print("False")


#Trouble with Angry Friends

# def friends_in_trouble(angry1 , angry2):
#     j_angry = angry1
#     s_angry = angry2

#     if j_angry == "True" and s_angry == "True":
#         print("So you are in Trouble!!!")
#         return True
#     elif j_angry == "True" :
#         print(f"Only John is angry. You are safe")
#         return False
#     elif s_angry == "True":
#         print(f"Only Smith is angry. You are safe")
#         return False
#     else:
#         print("Check your details carefully")

# John = input("John Are you Angry....Enter True if your Angry: ")
# Smith = input("Smith Are you Angry....Enter True if your Angry: ")   
# friends_in_trouble(John , Smith)


# Check for Equal occurences of 'cat' and 'hat' in a string

def cat_hat(s):
    return s.count("cat") == s.count("hat")

print(cat_hat("catinhat"))
print(cat_hat("berozgar"))
print(cat_hat("catbutnotincap"))

# Conditional Booloean Evaluation
def multiplicationTable(N):
    num = N
    for i in range(1,11):
        print(num*i)

multiplicationTable(5)