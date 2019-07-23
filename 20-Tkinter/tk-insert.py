from tkinter import *
from tkinter import messagebox
import MySQLdb

win=Tk()
win.option_add('*font', ('verdana', 14, 'bold'))


def Insert():
    id=int(txtId.get(1.0,END).strip())
    name=txtName.get(1.0,END).strip()
    course=txtCourse.get(1.0,END).strip()
    fees=float(txtFees.get(1.0,END).strip())

    #Saving Database
    con=MySQLdb.connect('localhost',user='root',password='')
    con.select_db('pyapp')
    cur=con.cursor()
    stmt="INSERT INTO STUDENT VALUES(%s,%s,%s,%s)"
    parameters=(id,name,course,fees)
    cur.execute(stmt,parameters)
    con.commit()
    con.close()


lblId=Label(win,text="Id : ")
lblName=Label(win,text="Name : ")
lblCourse=Label(win,text="Course : ")
lblFees=Label(win,text="Fees : ")

txtId=Text(win, height=1, width=30)
txtName=Text(win, height=1, width=30)
txtCourse=Text(win, height=1, width=30)
txtFees=Text(win, height=1, width=30)

btnAdd=Button(win, text="Insert", command=Insert)

lblId.grid(row=1,column=1,sticky=W)
txtId.grid(row=1,column=2)
lblName.grid(row=2,column=1,sticky=E)
txtName.grid(row=2,column=2)
lblCourse.grid(row=3,column=1,sticky=E)
txtCourse.grid(row=3,column=2)
lblFees.grid(row=4,column=1,sticky=E)
txtFees.grid(row=4,column=2)
btnAdd.grid(row=5,column=1,columnspan=2,sticky=W+E)
