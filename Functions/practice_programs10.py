# program to underestand the variable length arguments

def add(*numbers):
    print(sum(numbers))
add(1,2,3,4,5)

# program to undersand keyword agrument

def display_info(name,age):
    print(f"Name : {name},Age : {age}")
display_info(age=25,name="kumar")
