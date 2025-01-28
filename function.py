# #wrte a program to receive three integers from keyboard and get their sum and product calculated through a user defined function cal_sum_prod()
# def cal_sum_prod(a,b,c):
#     # print("sum is" , a+b+c)
#     # print("product is " , a*b*c)
#     # print("Sum is " , a+b+c , "Product is", a*b*c)
#     return a+b+c , a*b*c
# # d = cal_sum_prod(1,2,3)
# # print(d)
# print(cal_sum_prod(2,3,4))

#here-come-the-dots-followed-by-dashes
# s1 = "here-come-the-dots-followed-by-dashes"
# def convert(x):
#     s = [x for x in s1.split('-')]
#     print(s)
#     b = s.sort()
#     d = '-'.join(s)
#     print(d)

# a = convert(s1)

# def squarecubcecalc():
#     a = [(x,x**2,x**3) for x in range(1,21)]
#     print(a)
    
# squarecubcecalc()

# Sakhi was a singer because her mother was a singer , and Sakhi's mother was a singer because her father was a singer
# a= "Sakhi was a singer because her mother was a singer, and Sakhi's mother was a singer because her father was a singer"

# def removeduplicate(x):
#     s = {x for x in a.split(" ") }
#     print(sorted(list((s))))
#     # print(s)

# b = removeduplicate(a)

#write a function to count alpha and digit
# a = "james bond 007"
# def count_alpha_num(a):
#     d={"alphabet": 0 , "digit" : 0}
#     for i in a:
#         if i.isalpha():
#             d["alphabet"]+=1
#         elif i.isdigit():
#             d["digit"]+=1
#         else:
#             pass
#     return d
            
# b = count_alpha_num(a)
# print(b)

#write a function to find the largest number in the list
# num=[1,2,3,4,5,6,8,9]
# def largest(num):
#     largest=0
#     for i in num:
#         if i>largest:
#             largest=i
#     return largest
# b=largest(num)
# print(b)

#write a function to calculate the sum of digit of a number 
# num = 1234
# def cal(num):
#     total = 0
#     while num>0:
#         digit = num%10
#         total += digit
#         num = num//10
#     return total
# print(cal(num))
