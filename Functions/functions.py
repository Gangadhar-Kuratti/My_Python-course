# program to print thetables of entered number using functions

def tables(num):
    for i in range(1,11):
        print(f"{num}x{i}={num*i}")
tables(5)

# program to understand the "return" function 

def nikh(num):
    return int(str(num)*3)
a = 100
b = nikh(2)
c = a + b
print(c)