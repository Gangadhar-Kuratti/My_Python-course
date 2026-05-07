# program to check the number is even or odd

number=int(input("Enter number: "))

if number%2==0:
    print("Entered number is even")
else:
    print("Entered number is odd")

# program to check whether entered number is positive ,negative or zero

num=int(input("Enter number: "))

if num>0:
    print("Entered number is positive")
elif num<0:
    print("Entered number is negative")    
else:
    print("Entered number is zero")  


# program to find the largest of three numbers

num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
num3=int(input("Enter number 3: "))

if num1>num2 and num1>num3:
    largest=num1
elif num2>num1 and num2>num3:
    largest=num2
else:
    largest=num3        

print(f"The largest of three numbers entered is {largest}")

# program to print the grades based on marks

marks=int(input("Enter your marks: "))
if marks < 0 and marks > 100:
    print("Invalid marks")
elif marks>=90:
    print("Grade : A")
elif marks>=75:
    print("Grade : B")
elif marks>=50:
    print("Grade : C")
else:
    print("Grade : F")            

# program to check the password entered by user

username=input("Enter username: ")
password=int(input("Enter password: "))

if username=="nikhil" and password==12345:
    print("Login successfully")
else:
    print("Invalid credentials")    

