class BankAccount:

    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")

        self.balance += amount

        self.transactions.append(
            f"Deposited ₹{amount:.2f}"
        )

        print("Amount deposited successfully!")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0.")

        if amount > self.balance:
            raise ValueError("Insufficient balance.")

        self.balance -= amount

        self.transactions.append(
            f"Withdrawn ₹{amount:.2f}"
        )

        print("Amount withdrawn successfully!")

    def show_balance(self):
        print(f"\nCurrent Balance: ₹{self.balance:.2f}")

    def show_transactions(self):
        if not self.transactions:
            print("No transactions yet.")
            return

        print("\n===== TRANSACTION HISTORY =====")

        for number, transaction in enumerate(self.transactions, start=1):
            print(f"{number}. {transaction}")


def get_amount():
    try:
        amount = float(input("Enter amount: "))
        return amount

    except ValueError:
        raise ValueError("Please enter a valid number.")


print("===== BANKING SYSTEM =====")

account_number = input("Enter account number: ")
name = input("Enter account holder name: ")

account = BankAccount(account_number, name)


while True:

    print("\n===== MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    try:

        if choice == "1":

            amount = get_amount()
            account.deposit(amount)

        elif choice == "2":

            amount = get_amount()
            account.withdraw(amount)

        elif choice == "3":

            account.show_balance()

        elif choice == "4":

            account.show_transactions()

        elif choice == "5":

            print("Thank you for using the Banking System!")
            break

        else:

            print("Invalid choice.")

    except ValueError as error:

        print("Error:", error)