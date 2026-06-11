# program to understand the global() variable
x = 10

def change():
    global x
    x = 20

change()
print(x)


# program t understand the identity operator 
x = [1,2]
y = x

print(x is y)
print(x is not y)