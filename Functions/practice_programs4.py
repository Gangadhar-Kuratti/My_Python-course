# program to print the multiplication table usong function

def table(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")
table(5)

# program to find the factorial of a number

def factorial(num):
    if num==1:
        return 1
    return num * factorial(num-1)
print(factorial(5))

# program to count the vowels in a string

def vowel(string):
    count=0
    for ch in string: 
        if ch in "AEIOUaeiou":
            count+=1
    print(count) 
vowel("aoe")
    