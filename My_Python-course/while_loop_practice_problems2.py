# program to print the square numbers   

num=1
while num<=10:
    squ_num=(num)**2
    num+=1
    print(squ_num)
    
# programto print the cube numbers

num=1
while num<=10:
    cub_num=num**3
    num+=1
    print(cub_num)
    
# program to print the sum of even numbers from 1-10

num=1
summation=0
while num<=10:
    if num%2==0:
        summation+=num
    num+=1
print(summation)     

# program to count the factors of between 1-100
num=1
count=0
while num<=100:
    if num%5==0:
        count+=1
    num+=1
print(count)    

# program to find the product of numbers from 1-5

num=1
product=1
while num<=5:
    product=product*num
    num=num+1
print(product)
    