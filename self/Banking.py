def show_balance(balance):
    print(f"Your Balance is ${balance:2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("This is not a valid amount to deposit")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter the amount you want to withdrawn: "))

    if amount > balance:
        print("Insufficient Balance")
    elif amount < 0:
        print("Withdran Amount must be Greater than 0")
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Program")
        print(" ")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print(" ")
        
        choice = input("Enter Your Choice (1/4): ")
        print(" ")
        print("****************************************")
        print(" ")

        if choice =='1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
            print(" ")
            print("Your Amount is deposited...Press 1 to check available Balance")
            print(" ")
            print("****************************************")
            print(" ")
        elif choice == '3':
            balance -= withdraw(balance)
            print(" ")
            print("Your Amount is withdrawn...Press 1 to check available Balance")
            print(" ")
            print("****************************************")
            print(" ")
        elif choice == '4':
            is_running = False
        else:
            print("This is not a valid choice....")

    print("Thank You ! Have a nice day")

if __name__ == '__main__':
    main()

