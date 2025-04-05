def mod(a,b):
    if b<=0:
        return -1
    div = a//b
    return a-div*b

print(mod(5,3))