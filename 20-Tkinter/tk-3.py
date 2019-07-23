import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
#Zoomed Window
root.state('zoomed')
#Setting Font
root.option_add('*font', ('verdana', 12, 'bold'))
        

#Event
def Save():
    messagebox.showinfo("My App","Record Saved Successfully")

def Cancel():
    messagebox.showerror("My App","Cancelled By User")


btnSave=tk.Button(root,text="Save",command=Save).place(in_=root, x=300, y=200)
btnCancel=tk.Button(root,text="Cancel",command=Cancel).place(in_=root, x=400, y=200)
