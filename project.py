print("----EXPENCE TRACKOR----")
expences=[]

while True:
    print("=:=: MENU :=:=")
    print("1.ADD EXPENCE: ")
    print("2.VIEW EXPENCE'S")
    print("3.TOTAL AMOUNT OF EXPENDITURE is: ")
    print("4.EXIT")

    choice=int(input("Enter your choice(1-4): "))
    if choice==1:
        date=input("Enter date of expenditure(DD-MM-YYYY): ")
        category=input("Enter type of expenditure (FOOD,CLOTHS,TRAVEL) : ")
        description=input("Enter your experience in expenditure: ")
        total_amount=float(input("Enter amount : "))

        expence={
            "date":date,
            "category":category,
            "description":description,
            "total_amount":total_amount
        }

        expences.append(expence)
        print("\n ✅ Expence added successfully\n")

    elif choice==2:
        if len(expences)==0:
            print("No expence recorded yet")
        else:
            i=1
            for e in expences:
                print(f"{i}. {e['date']} | {e['category']} | {e['description']} | {e['total_amount']}")   
                i+=1
                print("=====================================") 
    
    elif choice==3:
        total=0
        for e in expences:
            total+=e["total_amount"]
        print("Total spending is:",total)

    elif choice==4:
        print("....Thankyou bye!....")
        break

    else:
        print(" PLEASE ENTER VALID CHOICE!!")

