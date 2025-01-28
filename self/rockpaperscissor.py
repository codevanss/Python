import random

options = ("rock" , "paper" , "scissor")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice(rock ,paper, scissor): ")

    print(f"player: {player}")
    print(f"computer: {computer}")

    if player==computer:
        print({"It's a tie"})
    elif player=="rock" and computer =="scissor":
        print("You win") 
    elif player=="rock" and computer =="paper":
        print("Computer win") 
    elif player=="paper" and computer =="scissor":
        print("Computer win") 
    elif player=="paper" and computer =="rock":
        print("You win")
    elif player=="scissor" and computer =="rock":
        print("Computer win")
    elif player=="scissor" and computer =="paper":
        print("You win")
    else:
        pass

    play_again = input("You wnat to play again? (y/n) : ").lower()
    if not play_again =="y":
        running = False

print("Thanks for playing!")
