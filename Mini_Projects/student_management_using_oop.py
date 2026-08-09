# Student Management System with OOP

students = []


def add_student():
    roll_no = input("Enter roll number: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("Student with this roll number already exists.")
            return

    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    marks = float(input("Enter marks: "))

    student = {
        "roll_no": roll_no,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")


def display_students():
    if not students:
        print("No students found.")
        return

    print("\n----- Student Details -----")

    for student in students:
        print(f"Roll No : {student['roll_no']}")
        print(f"Name    : {student['name']}")
        print(f"Age     : {student['age']}")
        print(f"Course  : {student['course']}")
        print(f"Marks   : {student['marks']}")
        print("---------------------------")


def search_student():
    roll_no = input("Enter roll number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found!")
            print(f"Name   : {student['name']}")
            print(f"Age    : {student['age']}")
            print(f"Course : {student['course']}")
            print(f"Marks  : {student['marks']}")
            return

    print("Student not found.")


def update_student():
    roll_no = input("Enter roll number to update: ")

    for student in students:
        if student["roll_no"] == roll_no:
            student["name"] = input("Enter new name: ")
            student["age"] = int(input("Enter new age: "))
            student["course"] = input("Enter new course: ")
            student["marks"] = float(input("Enter new marks: "))

            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student():
    roll_no = input("Enter roll number to delete: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice. Please try again.")

