import json

FILE_NAME = "tasks.json"


def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    task_name = input("Enter task: ")

    task = {
        "task": task_name,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully!")


def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\n===== YOUR TASKS =====")

    for number, task in enumerate(tasks, start=1):

        status = "Completed" if task["completed"] else "Pending"

        print(f"{number}. {task['task']} - {status}")


def mark_complete(tasks):
    display_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number to mark complete: "))

        if 1 <= number <= len(tasks):

            tasks[number - 1]["completed"] = True

            save_tasks(tasks)

            print("Task marked as completed!")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    display_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):

            deleted_task = tasks.pop(number - 1)

            save_tasks(tasks)

            print(f"Deleted task: {deleted_task['task']}")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


tasks = load_tasks()


while True:

    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Mark Complete")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        display_tasks(tasks)

    elif choice == "3":
        mark_complete(tasks)

    elif choice == "4":
        delete_task(tasks)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")