# program to understand strings

Name="Gangadhar"
print(Name[0])            # accessing 1st element
print(Name[8])            # accessing last element
print(Name[4])            # accessing middle element

# program for string concatenation

Name="Nikhil"
Last_Name="Kuratti"
Full_Name= Name +" "+ Last_Name
print(Full_Name)          # concatenation
print(Full_Name*5)        # string repetition

# program for string methods

Name="Nikhil"
print(Name.upper())
print(Name.lower())
print(Name.replace("Nikhil","Diya"))

# program to count the character

Name="Nikhil"
ch="i"
count=Name.count(ch)
print(count)

# program to reverse string

Name="Nikhil"
ind=Name[-1:-6:-1]
print(ind)

