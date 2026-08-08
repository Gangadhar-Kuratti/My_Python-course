# Mini project for Student Management System

print("Student Management System")
students=[]
while True:
    print("1.Add Student")
    print("2.Display all Students")
    print("3.Search Student")
    print("Exit")

    choice=int(input("Enter your choice: "))

    if choice==1:
        name=input("Enter student name: ")
        student_id=int(input("Enter student id: "))
        marks=float(input("Enter marks of student: "))

        student=(student_id ,name , marks)
        students.append(student)

    elif choice==2:
        if len(students)==0:
            print("No students record recorded yet")
        else:
            for i in students:
                print("name: ",i[1])
                print("student_id: ",i[0])
                print("marks: ",i[2])

    elif choice==3:
        if len(students)==0:
            print("No students record recorded yet")
        else:
            rollno=int(input("Enter student_id:"))
            for s in students:
                if s[0]==rollno:
                    print("name: ",s[1])
                    print("marks: ",s[2])
                else:
                    print("invalid reg no")

    elif choice==4:
        print("Exiting...")

