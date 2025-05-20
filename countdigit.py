#write a recursive function to count the number of a digit
def count(n):
    if n == 0:
        return 0
    
    return 1 +count(n//10)
print(count(123))