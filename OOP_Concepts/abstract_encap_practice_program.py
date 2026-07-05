class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited successfully.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient Balance")
        else:
            self.__balance -= amount
            print("Withdrawal successful.")

    def display_balance(self):
        print("Current Balance:", self.__balance)


# Creating an object
acc = BankAccount(1000)

acc.deposit(500)
acc.withdraw(200)
acc.display_balance()