#Tkinter

from tkinter import *

root=Tk()

lblFirst = Label(root, text="First")
lblSecond = Label(root, text="Second")
lblThird = Label(root, text="Third")
lblFourth = Label(root, text="Fourth")

#lblFirst.pack()
#lblSecond.pack()
#lblThird.pack()
#lblFourth.pack()

#lblFirst.grid(row=0,column=0)
#lblSecond.grid(row=0,column=1)
#lblThird.grid(row=1,column=0)
#lblFourth.grid(row=1,column=1)

lblFirst.place(in_=root, x=100,y=100)
lblSecond.place(in_=root, x=100,y=150)
lblThird.place(in_=root, x=100,y=200)
lblFourth .place(in_=root, x=100,y=250)
