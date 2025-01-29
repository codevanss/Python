import random

low = 1
high = 100
is_running = True
guesses = 0
answer = random.randint(low,high)

print("Python number guessing game")
print(f"Select a number between {low} and {high}")

while is_running:
    guess = int(input("Enter a number you guess : "))
    if guess.isdigit():
        guess = int(guess)
        guesses +=1
        if guess < low or guess>high:
            print("You guess the number out of range")
            print(f"Select a number between {low} and {high}")
        elif guess<answer:
            print("Too low! try Again high great number")
        elif guess>answer:
            print("Too high! Try again with smaller number")
        else:
            print(f"Congrats! You guess the right number {guess} in {guesses} attempts")
            is_running = False
    else:
        print("Invalid guess")
        print(f"Select a number between {low} and {high}")

 