# program to understand the keyword argumentsin function

def friend(boy,girl):
    print(f"{boy} is a friend of {girl}!!")
friend(boy="X",girl="Y")

# program to understand the variable length argument

def summation(*numbers):
    print(sum(numbers))
summation(10,20,30)

# program to understand the kwargs 

def details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} = {value}")
details(name="nikhil",age=18)

# program to understand the lambda function

# 1.
add = lambda a,b: a+b
print(add(3,3))
# 2.
double=lambda a:a*2
print(double(20))

# program to understand the lambda function in dictionary

lists=[
    {"name":"nikhil","age":18},
    {"name":"kumar","age":19},
    {"name":"diya","age":20}
]

lists.sort(key =lambda x : x["age"],reverse=True)
print(lists)

# program to understand the recursive function

def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)
print(factorial(5))

# program to understand the nested functions

def calculate(a,b):
    def add():
        print(a+b)
    def mult():
        print(a*b)
    def sub():
        print(a-b)
    add()
    mult()
    sub()
calculate(10,5)


