# program to understand the local and global variables

def marriage():
    boy="nikhil"                  # local variable
    girl="nikhita"
    print(girl2)                  # can be printed inside
    print(boy)                    # cannot be printed outside
girl2="x"                         # global variable
marriage()

# program to understand the default parameter

def marriage(boy,girl="nikhita"):  # here girl is default parameter
    print(f"{boy} Married! {girl}")
marriage("nikhil")