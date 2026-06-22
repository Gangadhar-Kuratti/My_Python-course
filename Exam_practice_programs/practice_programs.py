# python program to demonstrate different datatypes

a=4
b="Hi python"
c=2+3j
print(type(a))
print(type(b))
print(type(c))


# python program to perform different arithmetic operations on numbers

num1=9
num2=5
print("Summation of the numbers entered is",num1+num2)
print("Substration of the numbers entered is",num1-num2)
print("Product of the numbers entered is",num1*num2)
print("Division of the numbers entered is",num1/num2)

# program to create concatinate print string and access substring

a="Hello Python!!"
b="Iam Coming.."
c=a+b
print("Firstly Entered String is",a)
print("Secondly Entered String is",b)
print("After Concatination",c)
print("Substring from a given string is",c[2:8])

# script to print the current date 
import time;
itime=time.localtime();
print(time.strftime("%a %b %d %H:%M:%S %Z %Y",itime))

# program to find the factorial of a number

def fact(n):
    if n==1:
        return 1
    else:
        return (n*fact(n-1))
n=5
print(fact(n))

# Program to print the fibonacci series

num=6
n1,n2=0,1
print("Fibonacci series",n1,n2,end=" ")
for i in range(2,num):
     n3=n1+n2
     n1=n2
     n2=n3
     print(n3,end=" ")
print()
     
# program to check whether a number is pallindrome or not

num=int(input("Enter number: "))
temp=num
reverse=0
while temp>0:
    remainder=temp%10
    reverse=(reverse*10)+remainder
    temp=temp//10
    
if num==reverse:
    print("Pallindrome")
else:
    print("Not a pallindrome")
    
