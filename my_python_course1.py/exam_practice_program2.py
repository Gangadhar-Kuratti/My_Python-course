#program to understand the nested conditional statements

name=input("Enter your name: ")
attendance=int(input("Enter your attendance(%): "))
marks=int(input("Enter your marks: "))
age=int(input("Enter your age: "))
category=input("Enter your category: ").lower()
family_income=int(input("Enter your income: "))

if age>=18:
    print("Not eligible!(big age)")
elif marks<=75:
    print("Not eligible(low marks)")
elif family_income>500000:
    print("Not eligible(too much income)")
elif attendance<=75:
    print("Not eligible(bunking classes): ")
else:
    if marks>=90:
        print("Higher scholarship!!")
    elif marks>=80:
        print("Standard scholarship")
    else:
        print("Basic scholarship")
    if category in ["sc","st"]:
        print("Full fee waiver")
    elif category == "obc":
        print("Partial fee waiver")
 
