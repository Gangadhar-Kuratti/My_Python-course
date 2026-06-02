# program to understand the concept of shapes using tkinter

from tkinter import *
root=Tk()

c=Canvas(root,bg="grey",height="500",width="400")
c.pack()
c.create_oval(50,50,150,150,fill="white")
c.create_line(50,50,150,150,fill="red")
root.mainloop()

