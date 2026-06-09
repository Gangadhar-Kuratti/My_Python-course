# program to count the even numbers 

def even(num):
    count=0
    for i in str(num):
        if int(i)%2==0:
            count+=1
    print(count)
even(12345)

#program to check pallindrome or not

def pallindrome(string):
    reverse=""
    
    for i in range(len(string)-1,-1,-1):
        reverse+=string[i]
        
    if string==reverse:
        print("Pallindrome")
    else:
        print("Not a pallindrome")
pallindrome("madam")


    