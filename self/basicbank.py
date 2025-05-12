class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("❌ Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"✅ Withdrew ₹{amount}. Remaining balance: ₹{self.balance}")
        else:
            print("❌ Insufficient funds.")

    def display_balance(self):
        print(f"💰 {self.owner}'s Account Balance: ₹{self.balance}")


if __name__ == "__main__":
    name = input("Enter your name: ")
    account = BankAccount(name)

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == "3":
            account.display_balance()
        elif choice == "4":
            print("👋 Thank you for using the Bank Account System!")
            break
        else:
            print("❌ Invalid option.")
