# program to understand the nested function

def arithmetic(a,b):
    def add():
        print(a+b)
    def sub():
        print(a-b)
    def mult():
        print(a*b)
    def div():
        print(a/b)
    add()
    sub()
arithmetic(5,4)
    