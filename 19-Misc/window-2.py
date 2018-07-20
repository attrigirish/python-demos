#tKinter Library : Developing Windows Applications in Python


from tkinter import *


#Create new Window
window=Tk()


#Event Handlers
def MyTask():
    first=int(txt1.get(1.0,END))
    second=int(txt2.get(1.0,END))
    result=first+second
    lblResult['text']=str(result)
    


#Widgets
lbl1=Label(window,text="First Number : ")
txt1=Text(window,width=40,height=2)
lbl2=Label(window,text="Second Number : ")
txt2=Text(window,width=40,height=2)
btn=Button(window,text="Click Me!",command=MyTask)
lblResult=Label(window)

#Packing Widgets
lbl1.pack()
txt1.pack()
lbl2.pack()
txt2.pack()
btn.pack()
lblResult.pack()


