#!/usr/bin/env python3

class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        return self.balance

def main():
    cb = Checkbook()
    while True:
        try:
            action = input("\nWhat would you like to do? (deposit, withdraw, balance, exit): ").lower()
        except KeyboardInterrupt:
            print("\nExiting... Goodbye!")
            break

        if action == 'exit':
            print("Exiting... Goodbye!")
            break

        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount <= 0:
                    print("Amount must be positive.")
                    continue
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue
            cb.deposit(amount)

        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount <= 0:
                    print("Amount must be positive.")
                    continue
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue
            cb.withdraw(amount)

        elif action == 'balance':
            print("Current Balance: ${:.2f}".format(cb.get_balance()))

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
