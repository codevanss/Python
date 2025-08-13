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