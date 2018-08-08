from tkinter import *
import MySQLdb

#Read Data
con=MySQLdb.connect('localhost',user='root',password='')
con.select_db('b11')
cur = con.cursor()
cur.execute("SELECT * FROM student")
records=cur.fetchall()
con.close()

win=Tk()
win.geometry('250x200+100+200')
win.title('Records')

rollLabel = Label(win, text="Roll", width=10)
rollLabel.grid(row=0, column=0)

nameLabel = Label(win, text="Name", width=10)
nameLabel.grid(row=0, column=1)

courseLabel = Label(win, text="Course", width=10)
courseLabel.grid(row=0, column=2)

feesLabel = Label(win, text="Fees", width=10)
feesLabel.grid(row=0, column=3)

durationLabel = Label(win, text="Duration", width=10)
durationLabel.grid(row=0, column=4)


row=1
for record in records:    
    Label(win, text=record[0]).grid(row=row, column=0)
    Label(win, text=record[1]).grid(row=row, column=1)
    Label(win, text=record[2]).grid(row=row, column=2)
    Label(win, text=record[3]).grid(row=row, column=3)
    Label(win, text=record[4]).grid(row=row, column=4)
    row=row+1




