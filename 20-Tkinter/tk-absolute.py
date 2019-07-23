from tkinter import *

win=Tk()

lbl1=Label(win,text="One")
lbl2=Label(win,text="Two")
lbl3=Label(win,text="Three")

lbl1.place(in_=win, x=100, y=100)
lbl2.place(in_=win, x=50, y=200)
lbl3.place(in_=win, x=150, y=200)
