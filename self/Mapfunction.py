def square(x):
    return x*x

numbers=[1,2,3,4,5,6,7,8,9]
map(square,numbers) #  using map we can directly send all element to function and store it
list(map(square,numbers)) # converting into list
print(list(map(square,numbers)))