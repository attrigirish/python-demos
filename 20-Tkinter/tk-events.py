from tkinter import *
from tkinter import messagebox


win=Tk()

win.option_add('*font', ('verdana', 14, 'bold'))
win.state('zoomed')


def Save():
    messagebox.showinfo("Title","Record Saved Successfully")

def Cancel():
    messagebox.showinfo("Title","Record Cancelled")


btn1=Button(win, text="Save", command=Save)
btn2=Button(win, text="Cancel", command=Cancel)


btn1.place(in_=win, x=600,y=300)
btn2.place(in_=win, x=600,y=400)
