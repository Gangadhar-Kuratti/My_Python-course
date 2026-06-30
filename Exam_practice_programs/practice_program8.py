#Write text to a file
 
f=open("myfile.txt","a") 
str=input("enter text:") 
f.write(str) 

#Read text from file

f=open("myfile.txt","r") 
str=f.read() 
print("Reading text from the file is: ",str) 
f.close() 