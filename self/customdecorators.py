# from typing import Callable
# from functools import wraps
# from time import perf_counter , sleep

# def get_time(func : Callable) -> Callable:
#     @wraps(func)
#     def wrapper(*args , **kwargs) -> None:
#         """wrapper __doc__"""
#         start_time: float = perf_counter()
#         func(*args ,**kwargs)
#         end_time: float = perf_counter()
#         print(f'"{func.__name__}()" took {end_time - start_time:.3f}s')
    
#     return wrapper

# @get_time
# def calculate(a,b) -> None:
#     """wrapper __doc__"""
#     print(f'Calculating: {a} + {b}')
#     sleep(2)
#     print(f'{a} + {b} = {a+b}') 


# print(calculate(10,20))


def my_decorator(func):
    def wrapper(*args , **kwargs):
        print("hello world")
        res = func(*args , **kwargs)
        if res is not None:
            print(res)
        print("bye bye")
    return wrapper

@my_decorator
def my_function():
    print("We are running")

my_function()

# @my_decorator
# def calculate(x,y):
#     return x+y

# my_function()
# calculate(3,4)

# authenticated = True
# numbers = [x for x in range(101)]

# def is_auth(func):
#     def wrapper(num_list):
#         if not authenticated:
#             print("Access Denied")
#         else:
#             print("works")
#             res = func(num_list)
#             print('result ' , res)
#             print('done')
#     return wrapper

# @is_auth
# def sum(num_list):
#     sum = 0
#     for num in num_list:
#         sum += num
#     return sum

# sum(numbers)

# import time

# def timer(func):
#     def wrapper(p_time):
#         start = time.time()
#         print("Start")
#         func(p_time)
#         total = time.time()- start
#         print("Done" , total)
#     return wrapper

# @timer
# def do_something(pause):
#     time.sleep(pause)
#     print("Hello World")

# do_something(1)
# do_something(5)
# do_something(3)