# program to understand the concepts of dictionary conditional statements and lists

employees={}
while True:
    print("...Employees details...")
    print("1.add employee: ")
    print("2.search employee: ")
    print("3.display all employees")
    print("4.view highest salary of employee ")
    print("5.exit")
    
    choice=int(input("Enter your choice: "))
    
    if choice==1:
        emp_id=int(input("Enter employee ID: "))
        name=input("Enter employee name: ")
        salary=float(input("Enter employee salary: "))
        employees[emp_id]={"name":name,"salary":salary}
        
        print("Employee added successfully")
        
    elif choice==2:
        emp_id=int(input("Enter employee id to search: "))
        if emp_id in employees:
            print("employee found",employees[emp_id])
        else:
            print("Not found")
            
    elif choice==3:
        if len(employees)==0:
            print("No employees recorded")
        else:
            print("..employees records..")
            for emp_id ,data in employees.items():
                print("emp_id",emp_id,"name",data["name"],"salary",data["salary"])
    elif choice==4:
        print("EXITING PROGRAM....")
        break
    else:
        print("INVALID CHOICE")