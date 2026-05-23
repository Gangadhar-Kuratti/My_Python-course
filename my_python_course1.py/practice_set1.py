# program to create the rectangle using Tkinter

from tkinter import *
root=Tk()

Canvas_widget=Canvas(root,height='500',width='500')
Canvas_widget.pack()

Canvas_widget.create_rectangle(20,20,200,200,fill="red")
root.mainloop()

# program to create the line using Tkinter

from tkinter import *
root=Tk()

Canvas_widget=Canvas(root,height=500,width='500')
Canvas_widget.pack()
Canvas_widget.create_line(20,10,200,100)
root.mainloop()
