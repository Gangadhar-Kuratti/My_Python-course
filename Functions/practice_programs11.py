# program to count the odd numbers


def odd(numbers):
    count=0
    for i in numbers:
        if i%2!=0:
            count+=1
    print(count)
odd([2,3,4,5,6,7])
    
    
# program to count the odd numbers using return() function


def odd(numbers):
    count=0
    for i in numbers:
        if i%2!=0:
            count+=1
    return(count)
print(odd([1,3,5]))


    