# program to print the character position times the character
name="chandan"
for index, i in enumerate(name):
    print(i*(index+1))
 
 
# program to print the combined list of dictionaries   
name=["nikhil","diya"]
marks=[90,80]
name_marks={}
for index,i in enumerate(name):
    name_marks[i]=marks[index]
print(name_marks)

# program to print the combined list of dictionaries using 'len' function
name=["nikhil","diya"]
marks=[90,80]
name_marks={}
for i in range(len(name)):
    name_marks[name[i]]=marks[0]
print(name_marks)


# program to understand the dictionary compreesion

d={"nikhil","diya","kavya"}
d1={name:len(name) for name in d}
print(d1)