# program to count the digits

def digits(num):
    count=0
    for i in str(num):
            count+=1
    print(count)
digits(12345)

# program to find the largest of three numbers

def large(num1,num2,num3):
    if num1>num2 and num1>num3:
        print(f"{num1} is larger")
    elif num2>num1 and num2>num3:
        print(f"{num2} is larger")
    else:
        print(f"{num3} is larger")
large(2,3,4)

# program to count the uppercases

def upper(char):
        count=0
        for i in char:
            if i.isupper():
               count+=1
        print(count)
upper("ASfter")
        
        

