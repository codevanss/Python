import math

def perfsqr(lst):
    lst1 = []
    for i in lst:
        if i >= 0 and math.isqrt(i) ** 2 == i:  
            lst1.append(i)
    return lst1

print(perfsqr([2, 3, 4, 5, 9, 16, 20, 1]))