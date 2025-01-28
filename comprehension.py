# #generate a list of squares of all numbers from 1 to 10
# lst=[x*x for x in range(1,11)]
# print(lst)

# #create a list of all numbers divisible by 3 from 1 to 50
# lst1=[x for x in range(1,50) if x%3==0]
# print(lst1)

# #extract vowels from a string "comprehension"
# # str = "comprehension"
# lst3=[x for x in "comprehension" if x in 'aeiou']
# print(lst3)

# #create a list of tuple where each tuple contain a number and its square for number from 1 to 5
# tuple_lst=[(x,x**2)for x in range(1,6)]
# print(tuple_lst)

# #create a dictionary where key are number and their values are cube from 1 to 5
# dictt={x:x*x*x for x in range(1,6)}
# print(dictt)

#create a dictionary from 1 to 10 where key are number and values are even and odd
# dict={i:("even" if i%2==0 else "odd") for i in range(1,11)}
# print(dict)

# dicc={}
# for i in range(1,11):
#     if i%2==0:
#         dicc[i]="even"
#     else:
#         dicc[i]="odd"
# print(dicc)

# #Create a list of all words in a sentence that are longer than 4 characters.
# sentence = "List comprehension is a powerful feature in Python"
# lst=[i for i in sentence.split() if len(i)>4]
# print(lst)

#Reverse each word in a given list of words
# word=["hello" , "world" , "pyhton" , "rocks"]
# ls2=[word[::-1] for word in word ]
# print(ls2)

#create a list of common elements between two list
# lst1=[1,2,3,4,5]
# lst2=[3,4,5,6,7]

# lst3=[x for x in lst1 and lst2 if x==x]
# print(lst3)

# lst4=[x for x in lst1 if x in lst2]
# print(lst4)

#create a dictionary from a list of words where keys are words and length are values
words=["list" , "dic" , "is" , "amazing"]
dic={x:len(x) for x in words}
print(dic)