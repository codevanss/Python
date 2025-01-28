#write a lambda function to find a product a of two numbers
# product = lambda a,b : a*b
# print(product(2,3))

#map function
# lst = [10,20,30]

# lst2 = list(map(lambda x : x**2 , lst))
# print(lst2)

# lst1=[1,2,3,4,5]
# def square(s):
#     return s**2

# # sum = lambda x : x+x
# square_numbers = map(square , lst1)
# print(list(square_numbers))


#add list using lambda and map
# lst3=[1,2,3]
# lst4=[4,5,6]

# lst5 = list(map(lambda x , y : x+y , lst3,lst4))
# print(lst5)

#given a list of a number,add 5 to each number using map
# lst=[1,2,3,]

# lst1= list(map(lambda x :x+5 , lst))
# print(lst1)

#write a program to convert a list of temperature from celcius to ferhenhite
# c*9/5+32
# celcius = [0,10,20,30]
# ferhenite = list(map(lambda x : x*9/5+32 , celcius))

# far = map(int , ferhenite)


# print("Ferhenite list are")
# print(list(far))

#if else in map
# num=[-1 ,-2,-3,4,56]
# result=list(map(lambda x: 0 if x<0 else x , num))
# print(result)

#write a python program to double the even number and square using lambda and map
# lst=[1,2,3,4,5,6]
# result=list(map(lambda x : x*2 if x%2==0 else x**2 , lst))
# print(result)


#filter
# number=[1,2,3,4,5,6]
# lst2=list(map(lambda x : x%2==0 , number))
# lst1=list(filter(lambda x : x%2==0 , number))
# print(lst1)

# def greater(x):
#     return x>3
# num=[1,2,3,4,5,6]
# filtered = list(filter(greater , num))
# print(filtered)