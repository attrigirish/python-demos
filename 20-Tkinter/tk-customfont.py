from tkinter import *

win=Tk()

#Setting Custom Font
win.option_add('*Label.Font', ('verdana', 14, 'bold'))
win.option_add("*Label.Foreground", "blue")
win.option_add("*Label.Background", "red")

win.option_add("*Button.Font", ('calibri', 14, 'bold'))


#Setting Window State/Size
win.state('zoomed')

lbl1=Label(win,text="One")
lbl2=Label(win,text="Two", background="Green")
btn1=Button(win,text="Three")

lbl1.place(in_=win, x=100, y=100)
lbl2.place(in_=win, x=50, y=200)
btn1.place(in_=win, x=150, y=200)
