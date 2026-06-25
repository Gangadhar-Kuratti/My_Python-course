# program for different shapes using tkinter

from tkinter import *
root=Tk()
c=Canvas(root,width=1200,height=700)
c.create_arc(625,425,725,525,start=0,extent=180)
c.create_oval(50,50,100,100,fill="orange")
c.create_line(200,40,300,30,width=2,fill="black")
c.create_rectangle(450,520,500,580)
c.pack()
root.mainloop()