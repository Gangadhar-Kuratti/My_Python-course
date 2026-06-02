# program to understand the concept of arithmetic comparison and logical operators

Num=int(input("Enter number: "))
print("Square of a number entered is:",Num**2)
print("Is square of a number is greater than 50", (Num**2)>50)
print("Is square a number even",(Num**2)%2==0)
print("Is square a number is between 10 and 100",(Num**2) > 10 and(Num**2) < 100 )

# program to understand 'and' and comparison operators

Marks=int(input("Enter your marks: "))
Age=int(input("Enter your age: "))
if Marks >= 40 and Age>=18:
    print("Eligible")
else:
    print("Not eligible")    

