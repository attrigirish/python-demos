from tkinter import *
from tkinter import messagebox

win=Tk()
win.option_add('*font', ('verdana', 14, 'bold'))
win.state('zoomed')

def Add():
    a=int(txt1.get(1.0, END))
    b=int(txt2.get(1.0, END))
    c=a+b
    messagebox.showinfo("Result", c)


lbl1=Label(win,text="First Number : ")
lbl2=Label(win,text="Second Number : ")
txt1=Text(win, height=1, width=30)
txt2=Text(win, height=1, width=30)
btnAdd=Button(win, text="Add", command=Add)

lbl1.place(in_=win, x=400, y=200)
txt1.place(in_=win, x=600, y=200)

lbl2.place(in_=win, x=400, y=300)
txt2.place(in_=win, x=600, y=300)

btnAdd.place(in_=win, x=500, y=400)


