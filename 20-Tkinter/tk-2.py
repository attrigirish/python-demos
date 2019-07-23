import tkinter as tk

root=tk.Tk()

#Zoomed Window
root.state('zoomed')

#Setting Font
root.option_add('*font', ('verdana', 12, 'bold'))
        

file=open('userdata.csv','r')
data=file.read()

records=data.split("\n")
row=1
for record in records:
    values=record.split(",")
    column=1
    for value in values:
        tk.Label(root,text=value,width=20,height=2).grid(row=row,column=column,sticky=tk.W)
        column+=1
    row+=1




