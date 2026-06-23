# program for student management system

print("......Student record management system.......")
students=[]
while True:
    print("1.Add student..")
    print("2.Display all students record..")
    print("3.Search student..")
    print("4.Exit ..")
    
    choice=int(input("Enter your choice: "))
    
    if choice==1:
        Name=input("Enter student name: ")
        rollno=int(input("Enter reg_no of student: "))
        marks=float(input("Enter marks of student: "))
        
        student=(rollno,Name,marks)
        students.append(student)
        
    elif choice==2:
        
        if len(students)==0:
            print("No Student recorded")
        else:
            for s in students:
                print(f"Name: {s[1]}")
                print(f"Roll_no: {s[0]}")
                print(f"Marks: {s[2]}")
                
    elif choice==3:
        
        if len(students)==0:
            print("No Student recorded")
        else:
            rollno=int(input("Enter reg_no of student: "))
            
            for s in students:
                if s[0]==rollno:
                    
                     print(f"Name: {s[1]}")
                     print(f"Marks: {s[2]}")
                else:
                    print("Enter valid reg_no")
    elif choice==4:
        print("Exiting...")
                    
                    



    
        