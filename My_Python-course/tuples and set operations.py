# program to understand operations on set

set_1= {1,2,3,4}
set_2= {3,4,5,6}

print(set_1 | set_2)
print(set_1 & set_2)
print(set_1 - set_2)

# program to understand set properties

lis=[1,2,2,3,4,4,5,6]
print(lis)            # list allows duplicate values
print(set(lis))       # set doesnt allow duplicate values

# program to understand tuple operations

t=(10,20,30,40,20,50,20)
print(type(t))

print(len(t))

print(t.index(30))

print(t.count(20))
