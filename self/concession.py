menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.00,
        "chips": 3.79,
        "pretzel" : 3.45,
        "soda":4.56,
        "lemonade":7.44}
cart=[]
total = 0
print("Here's is our Menu")
for key,value in menu.items():
    print(f"{key:10} : ${value:.2f}")
print("----------")
while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food , end=" ")
print()
print(f"The total is ${total:.2f}")

