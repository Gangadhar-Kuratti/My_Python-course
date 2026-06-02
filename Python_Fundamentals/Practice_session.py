# program to understand the concept of list and list operations ,input/output statements.

Name=input("Enter your name: ")
Age=int(input("Enter your age: "))
Empty_list=[]

Marks0=int(input("Enter your marks: "))
Marks1=int(input("Enter your marks: "))
Marks2=int(input("Enter your marks: "))

Empty_list.append(Marks0)
Empty_list.append(Marks1)
Empty_list.append(Marks2)

print(Empty_list)

Total_marks=(Marks0+Marks1+Marks2)
print("The total marks is:",Total_marks)

Avg_marks=(Marks0+Marks1+Marks2)/3
print("The average of marks is:",Avg_marks)

if Avg_marks>=40:
    print("Are marks greater than 40",Avg_marks>=40)
else:
    print("False")

print(Name.upper())
rev=Name[::-1]
print("The reverse of the name entered is:",rev)

# largest of three without using max()
lis=[10,20,30]
largest=lis[0]
for num in lis:
    if num>largest:
        largest=num
print(largest)        