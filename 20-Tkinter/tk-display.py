from tkinter import *
from tkinter import messagebox
import MySQLdb

con=MySQLdb.connect('localhost',user='root',password='')
con.select_db('pyapp')
cur=con.cursor()
stmt="SELECT * FROM STUDENT"
cur.execute(stmt)
students=cur.fetchall()
con.close()


win=Tk()

win.option_add('*font', ('verdana', 14, 'bold'))

row=1
for student in students:
    Label(win,text=student[0], width=20).grid(row=row,column=1)
    Label(win,text=student[1].strip(), width=20).grid(row=row,column=2)
    Label(win,text=student[2].strip(), width=20).grid(row=row,column=3)
    Label(win,text=student[3], width=20).grid(row=row,column=4)
    row=row+1
