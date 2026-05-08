# program to understand the if-elif statements

num1=int(input("Enter number_1: "))

if num1%3==0 and num1%5==0:
    print("FIZZBUZZ")
elif num1%3==0 :
    print("FIZZ")
elif num1%5==0:
    print("BUZZ")
else:
    print("Not Divisible")
 
 # program to understand the flow of conditional statements   
    
side1=int(input("Enter size: "))
side2=int(input("Enter size: "))
side3=int(input("Enter size: "))

if side1>0 and side2>0 and side3 > 0:
    print("valid")
    if side1 == side2 == side3:
        print("Equilateral triangle")
    elif (side1 == side2 !=side3) or (side2 == side3!=side1) or (side3 == side1!=side2):
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("Invalid")  

# program to understand the elif statements
    
Balance=int(input("Enter balance amount: "))
withdrawal_amount=int(input("Enter amount to be withdrawan: "))

if withdrawal_amount<=0:
    print("Invaild")
elif withdrawal_amount>Balance :
    print("Insufiicient balance")
else:
    print("Withdrawal successful")
    
print("Remaining balance:",Balance-withdrawal_amount)


char=input("Enter a character: ")
if len(char)>1:
    print("Only 1 character allowed")
elif char.isalpha():
    print("Entered character is Alphabet")
elif char.isdigit():
    print("Entered character is Digit")
else:
    print("Entered character is Special character")
    
 # program to perform the arithmetic operation using conditional statements  

num1=int(input("Enter number: "))    
num2=int(input("Enter number: "))    

operation=input("Enter operation: ")
if operation=="+":
    print("Sum of number the entered is:",num1+num2)
elif operation=="-":
    print("Difference of the numbers entered is:",num1-num2)
elif operation=="*":
    print("Product of the numbers entered is:",num1*num2)
elif operation=="/":
    if num2==0:
        print("Canoot divide by zero")
    else:
        print("The division of the numbers entered is:",num1/num2)
else:
    print("INVALID OPERATION")
    