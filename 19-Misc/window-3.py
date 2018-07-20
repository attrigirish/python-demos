#Window Based Programming

from tkinter import *



#Create Window
window=Tk()

#Creading Events
def MyTask():
    #Reading Text Box Values
    a=int(txt1.get(1.0,END))
    b=int(txt2.get(1.0,END))
    c=a+b
    lbl3['text']=str(c)

#Creating Widgets
lbl1=Label(window,text="First Number : ")
lbl2=Label(window,text="Second Number : ")
lbl3=Label(window,text="")
txt1=Text(window,height=1,width=30)
txt2=Text(window,height=1,width=30)
btn=Button(window,height=1,width=30,command=MyTask,text="Add")

#Packing Widgets
lbl1.pack()
txt1.pack()
lbl2.pack()
txt2.pack()
btn.pack()
lbl3.pack()
