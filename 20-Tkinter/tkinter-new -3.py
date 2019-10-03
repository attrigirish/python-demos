from tkinter import *

root=Tk()

root.option_add("*Font", ("calibri", "16"))

def Add():
    first=float(txtFirst.get())
    second=float(txtSecond.get())
    result=first+second
    lblResult['text']=result



lblFirst=Label(root,text="First")
txtFirst=Entry(root)
lblSecond=Label(root,text="Second")
txtSecond=Entry(root)
btnCommand=Button(root,text="Add",command=Add)
lblResult=Label(root,text="")

lblFirst.pack()
txtFirst.pack()
lblSecond.pack()
txtSecond.pack()
btnCommand.pack()
lblResult.pack()

input("Press Any Key to Exit...")

