foods = []
prices = []
total = 0

while True:
    food = input("Enter the food item you want to buy (q to quit): ").lower()
    if food =="q":
        break
    else:
        price = float(input(f"Enter the price of a {food} : $"))
        foods.append(food)
        prices.append(price)
print("----- Your Cart -----")

for food in foods:
    print(food)

for price in prices:
    total += price
print()
print(f"Your Total Price is : ${total}")
