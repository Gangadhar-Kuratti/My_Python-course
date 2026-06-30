#Open a file in write and binary mode 
f1=open("Sample.jpg","rb") 
f2=open("new.jpg","wb") 
bytes=f1.read() 
f2.write(bytes)
f2.close() 
