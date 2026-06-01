# program to print the combined list of dictionaries   
name=["naveen","kiran"]
marks=[90,80]
name_marks={}
for index,i in enumerate(name):
    name_marks[i]=marks[index]
print(name_marks)