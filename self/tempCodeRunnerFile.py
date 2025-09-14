authenticated = True
numbers = [x for x in range(101)]

def is_auth(func):
    def wrapper(num_list):
        if not authenticated:
            print("Access Denied")
        else:
            print("works")
            res = func(num_list)
            print('result ' , res)
            print('done')
    return wrapper

@is_auth
def sum(num_list):
    sum = 0
    for num in num_list:
        sum += num
    return sum

sum(numbers)
