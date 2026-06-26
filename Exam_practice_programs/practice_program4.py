#program for student scholarship management

name = input("Name: ") 
marks = float(input("Marks: ")) 
income = float(input("Income: ")) 
attendance = float(input("Attendance: ")) 
category = input("Category: ").lower() 
sports = input("Sports (yes/no): ").lower() 
print("\n--- Result ---")
if marks < 60:
    print("Not eligible: Low marks")
elif attendance < 75:
    print("Not eligible: Low attendance")
elif income > 500000:
    print("Not eligible: High income")
else:
    print(name, "is eligible")
    if marks >= 90:
        print("High scholarship")
    elif marks >= 75:
        print("Standard scholarship") 
    else: 
        print("Basic scholarship") 
        if sports == "yes": 
            print("Sports bonus") 
            if category in ["sc", "st"]: 
                print("Full fee waiver") 
            elif category == "obc": 
                print("Partial concession") 
                print("Thank you") 