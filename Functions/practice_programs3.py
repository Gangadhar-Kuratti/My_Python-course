# program to return the largest of two numbers

def largest(num1,num2):
    if num1>num2:
        return (f"{num1} is greater")
    else:   
        return (f"{num2} is greater") 
print(largest(2,3))

# program to return whether a number is evan or odd

def ev_odd(num):
    if num%2==0:
        return (f"{num} is even number")
    else:
        return (f"{num} is odd number")
print(ev_odd(8))

# program to reverse the string

def strings(string):
     return string[::-1]
print(strings("nikhil"))

