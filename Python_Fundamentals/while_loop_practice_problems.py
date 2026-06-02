# program to print numbers using while loop

num=1
while num<=10:
    print(num)
    num=num+1
# program to print reverse numbers using while loop    
num1=10
while num1>=0:
    print(num1)
    num1=num1-1
    
# program to print even numbers between 1-20

num2=1
while num2>=0 and num2<=20:
    if num2%2!=0:
        num2+=1
        continue
    print(num2)
    num2+=1
    
# program to print sum of first 10 numbers    
    
number=1
summation=0

while number<=10:
    summation+=number
    number+=1
print(summation)


# program to print multiplication table of a number

num=int(input("Enter number: "))
i=1
while i<=10:
    print(f"{num}x{i}={num*i}")
    i+=1
