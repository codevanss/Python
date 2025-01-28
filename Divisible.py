# write a program to find how many number between 1 to 100 are divisible by both 3 and 5
count = 0
for i in range(1,100):
    if ((i%3 == 0) or (i%5 == 0)):
        print("The number is " ,i)
        count += 1
        # print("Total numbers are divisible by 3 and 5 is : " , count)
    else:
        pass
print("Total numbers are divisible by 3 and 5 is : " , count)
    