import tkinter as tk

root=tk.Tk()


tk.Label(root,text="ID").grid(row=1,column=1)
tk.Label(root,text="Name").grid(row=1,column=2)
tk.Label(root,text="Cours").grid(row=1,column=3)
tk.Label(root,text="Fees").grid(row=1,column=4)

tk.Label(root,text="1").grid(row=2,column=1)
tk.Label(root,text="Anil").grid(row=2,column=2)
tk.Label(root,text="Java").grid(row=2,column=3)
tk.Label(root,text="10000").grid(row=2,column=4)

tk.Label(root,text="2").grid(row=3,column=1)
tk.Label(root,text="Ravi").grid(row=3,column=2)
tk.Label(root,text="Python").grid(row=3,column=3)
tk.Label(root,text="10000").grid(row=3,column=4)




