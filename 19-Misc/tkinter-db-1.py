#Database 'B11'
#Table 'Student'
#Fields roll int, name varchar(20), course varchar(20), fees decimal(10,2), duration varchar(20)



#Window Application
from tkinter import *

#Window
win=Tk()


#Events
def MyTask():
    roll=txt1.get(1.0,END).strip()    
    name=txt2.get(1.0,END).strip()
    course=txt3.get(1.0,END).strip()    
    fees=txt4.get(1.0,END).strip()
    duration=txt5.get(1.0,END).strip()
    
    import MySQLdb
    con=MySQLdb.connect('localhost',user="root",password="")
    cur=con.cursor()
    cur.execute("INSERT INTO STUDENT values(%s,%s,%s,%s,%s)", (roll,name,course,fees,duration))
    con.commit()
    con.close()


#Controls
lblTitle=Label(win, text="Aptech Computer Education")

lbl1=Label(win, text="Roll:")
txt1=Text(win, height=1, width=50)
lbl2=Label(win, text="Name:")
txt2=Text(win, height=1, width=50)
lbl3=Label(win, text="Course:")
txt3=Text(win, height=5, width=50)
lbl4=Label(win, text="fees:")
txt4=Text(win, height=5, width=50)
lbl5=Label(win, text="duration:")
txt5=Text(win, height=5, width=50)


btn=Button(win, text="Submit", command=MyTask)
lblResult=Label(win, text="")

#Packing Objects
lblTitle.pack()
lbl1.pack()
txt1.pack()
lbl2.pack()
txt2.pack()
lbl3.pack()
txt3.pack()
lbl4.pack()
txt4.pack()
lbl5.pack()
txt5.pack()
btn.pack()
lblResult.pack()

    
    
    
