
# program to print the even numbers from 1-20 using for loop 

for i in range(1,21):
    if i%2==0:
        print(i)
        
# program to print the tables of a number using for loop        
        
num=int(input("Enter number : "))
for i in range(1,11):
    print(f"{num}x{i}={num*i}")


# program to print the sum of numbers between 1-10 using for loop

num=1
summation=0
for i in range(1,11):
    summation+=num
    num+=1
print(summation)


# program to print the product of numbers between 1-5 using for loop

num=1
product=1
for i in range(1,6):
    product*=num
    num+=1
print(product)   

# program to print the character of given string
name="Nikhil"
for i in name:
    print(i)