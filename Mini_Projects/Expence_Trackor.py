# Expense Tracker 


expenses = []


def add_expense():
    category = input("Enter expense category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    expense = {
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)
    print("Expense added successfully!")


def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\n===== EXPENSES =====")

    for i, expense in enumerate(expenses, start=1):
        print(f"\nExpense {i}")
        print(f"Category    : {expense['category']}")
        print(f"Amount      : ₹{expense['amount']:.2f}")
        print(f"Description : {expense['description']}")


def total_expense():
    if not expenses:
        print("No expenses found.")
        return

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total Expense: ₹{total:.2f}")


def category_total():
    category = input("Enter category: ")
    total = 0

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            total += expense["amount"]

    print(f"Total spent on {category}: ₹{total:.2f}")


def delete_expense():
    if not expenses:
        print("No expenses found.")
        return

    view_expenses()

    try:
        number = int(input("\nEnter expense number to delete: "))

        if 1 <= number <= len(expenses):
            deleted = expenses.pop(number - 1)
            print(
                f"Deleted {deleted['category']} expense "
                f"of ₹{deleted['amount']:.2f}"
            )
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Show Category Total")
    print("5. Delete Expense")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        category_total()

    elif choice == "5":
        delete_expense()

    elif choice == "6":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")

