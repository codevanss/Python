import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]

    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results


def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row , bet):
    if row[0]==row[1]==row[2]:
        if row[0] == '🍒' or '🍉' or '🍋' or '🔔' or '⭐' :
            return bet * 90
    return 0


def main():
    balance = 100

    print("**************************")
    print("Welcome to my Slot Machine")
    print("Symbols: 🍒 🍉🍋 🔔 ⭐  ")
    print("**************************")

    while balance > 0:
        print(f"Your Balance is ${balance} ----")

        bet = input("Enter your bet amount: ")

        if not bet.isdigit():
            print("Enter valid amount")
            continue
        
        bet = int(bet)

        if bet > balance:
            print("Insufficient Fund")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet
        row = spin_row()
        print("Spinning........\n")
        print_row(row)

        payout = get_payout(row , bet)

        # balance += payout

        if payout > 0:
            print(f"Congratulation You Won! the prize pool of ${payout}")
            # print(f"Your Updated Balance is ${balance}")
        else:
            print("You Lost this round")
        
        balance += payout

        play_again = input("Do want to spin again? (Y/N): ").upper()

        if play_again != 'Y':
            print(f"Your Remaining amount is ${balance}")
            break
        

        print("********************************************")
        print(f"Game Over ! Your final amount is ${balance}")
        print("********************************************")



        


if __name__ == '__main__':
    main()