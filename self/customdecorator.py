

def add_sprinkles(func):
    def wrapper(*args , **kwargs):
        print("*You add Sprinkles 🎊*")
        func(*args , **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args , **kwargs):
        print("*You add fudge 🍫*")
        func(*args , **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here's your {flavor} ice cream 🍨")

get_ice_cream("Chocolate")