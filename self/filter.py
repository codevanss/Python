def even(num):
    if num%2==0:
        return True

even(24)

lst = [1,2,3,4,5,6,7,8,9]

even_num = list(filter(even,lst))
print(even_num)


#filter using lambda function 
numbers = [1,2,3,4,5,6,7,8,9]
greater_than_five = list(filter(lambda x : x>5 , numbers))
print(greater_than_five)

# filter using multiple condition
numbers = [1,2,3,4,5,6,7,8,9]
even_and_greater_than_five = list(filter(lambda x : x>5 and x%2==0 , numbers))
print(even_and_greater_than_five)

#filter using dictionaries
people=[
    {'name' : 'krish' , 'age': 34},
    {'name' : 'vansh' , 'age': 30},
    {'name' : 'parth' , 'age': 23},
    {'name' : 'jeet' , 'age': 54},
    {'name' : 'aniket' , 'age': 14},
    {'name' : 'mohan' , 'age': 24},
]

def age (person):
    return person['age']>25

print(list(filter(age , people)))