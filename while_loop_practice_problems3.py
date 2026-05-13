# program to print the sum of even numbers entered by the user
summation=0
count=1
while count<=5:
    num=int(input("Enter number: "))
    if num%2==0:
        summation+=num
    count+=1
print("The sum of even numbers you entered is",summation)  


# program to print the count of +ve,-veand null values entered by the user

count=1
pos_count=0
neg_count=0
zero_count=0
while count<=10:
    num=int(input("Enter number: "))
    if num>0:
        print("POSITIVE")
        pos_count+=1
    elif num==0:
        print("ZERO")
        zero_count+=1
    else:
        print("NEGATIVE")
        neg_count+=1
    count+=1        
print(f"you entered{pos_count}positive numbers")    
print(f"you entered{neg_count}negative numbers")    
print(f"you entered{zero_count}null values")    


# program to take input until user enters 0 and print the sum of numbers entered

summation=0
count=0
while True:
    num=int(input("Enter number:"))
    if num==0:
        break
    else:
        summation+=num
    count+=1 
print(summation)    
    
