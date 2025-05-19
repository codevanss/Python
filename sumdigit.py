num = 123
def sum(num):
    if num == 0:
        return 0


    return num%10+sum(num//10)
print(sum(num))