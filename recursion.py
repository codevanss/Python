# def recur(n):
#     if n == 0:
#         return 0
#     else:
#         print(n)
#         recur(n-1)
# recur(5)

# def sum(n):
#     if n ==0:
#         return 0
#     else:
#         return n + sum(n-1)
# print(sum(5))

#write a recursive function to calculate the sum of digit of a number
# num = 123
# def sum(num):
#     if num == 0:
#         return 0


#     return num%10+sum(num//10)
# print(sum(num))

#write a recursive function to count the number of a digit
# def count(n):
#     if n == 0:
#         return 0
    
#     return 1 +count(n//10)
# print(count(123))

#write a recursive function to reverse a string
# n = "hello"
# def reverse(n):
#     if len(n) ==0:
#         return ""
#     return n[-1] + reverse(n[:-1])
# print(reverse(n))

#write a recursion function to get a factorial of a given number
# def fact(n):
#     if n == 0:
#         return 1
    
#     return n * fact(n-1)
# print(fact(3))


#write a recursive function to sum the element of an array
# lst = [1,2,0,4,0]
# def sum(n):
#     if len(n) ==0:
#        return 0
#     return n[0] + sum(n[1:]) 
# print(sum(lst))

# def sum_list(lsst , nn):
    # if nn==0:
        # return 0
    # return lsst[nn-1] + sum_list(lsst , nn-1)
# print(sum_list([1,2,3,4,5] , 5))

#write a maximum element in an array using recursion
# lst=[1,2,3,4,56,54]
# def maximum(n):
#     if n==0:
#         return 0
    
#     return max(n)
# print(maximum(lst))

# lst1=[1,23,345,56,21,34]
# n =6
# def maximun(lst1,n):
#     if n==1:
#         return lst1[0]

#     return max(lst1[n-1], maximun(lst1 , n-1))

# print(maximun(lst1 , n))

#check array is sorted using recursion
# lst1=[1,2,32,4,5]
# def sorting(lst1):
#     if len(lst1)<=1:
#         return True

#     return lst1[0]<lst1[1] and sorting(lst1[1:])

# print(sorting(lst1))

#check whether a string is a palindrome or not
# lst= ["M" ,"O" , "M"]
# lst = "moam"
# def palindrome(lst):
#     if len(lst)<=1:
#         print("Palindrome")
#         return True
#     return lst[0]==lst[-1] and palindrome(lst[1:-1])   
# print(palindrome(lst))
# s="hiw"
# def is_palindrome(s):
#     if len(s)<=1:
#         return True
#     if s[0]!=s[-1]:
#         print("not palindrome")
#         return False
#     return s[0]==s[-1] and is_palindrome(s[1:-1])  
# print(is_palindrome(s))


#find product of an array
# lst = [1,2,3,4]
# n = 4
# def product(lst , n):
#     if n==0:
#         return 1
    
#     return lst[n-1]*product(lst,n-1)
# print(product(lst , n))

#find occurence of an element in a list
# d = [1,2,2,3,4,2]
# target = 3
# def occurence(d , target):
#     if len(d)==0:
#         return 0
#     return (1 if d[0]==target else 0) + occurence(d[1:] , target)
    
# print(occurence(d,target))
    