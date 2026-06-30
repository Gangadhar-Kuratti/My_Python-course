#Open a file in write and binary mode 
f1=open("Sample.jpg","rb") 
f2=open("new.jpg","wb") 
bytes=f1.read() 
<<<<<<< HEAD
f2.write(bytes)
f2.close() 
=======
f2.write(bytes) 
f2.close() 

>>>>>>> 77eb749f07eb5043396996cb0fac9e9e83578082
