# program to count the even numbers 

num=1
count=0
while num<=50:
    if num%2==0:
        count+=1
    num+=1
print(count)

# program to print the numbers divisible by 3 and 5

num= 1
while num<=100:
    if num%3==0 and num%5==0:
        print(num)
    num+=1
    
# program to print the factorial of a number    
    
num=5
fact=1
while num>0:
    fact=fact*num
    num-=1
print(fact)    