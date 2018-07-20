#tKinter Library : Developing Windows Applications in Python


from tkinter import *


#Create new Window
window=Tk()



#Event Handlers
def MyTask():
    lbl['text']="Button Clicked"


#Widgets
lbl=Label(window,text="Hello World")
btn=Button(window,text="Click Me!",command=MyTask)

#Packing Widgets
lbl.pack()
btn.pack()


