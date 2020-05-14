import MySQLdb
from tkinter import ttk
from tkinter import *
import datetime
import time
import tkinter.messagebox

class school_portal():
    def __init__(self,root):
        self.root= root
        self.root.title('students data')
        #self.photo=PhotoImage(file='master.png')
        #self.label=Label(image=self.photo)
        #self.label.grid(row=0,column=0)
        self.label1=Label(font=('arial',15,'bold'),text='school portal system',fg='dark blue')
        self.label1.grid(row=8,column=0)
        frame=LabelFrame(self.root,text='Add New Record')
        frame.grid(row=0,column=1)
        Label(frame,text='firstname ').grid(row=1,column=1,sticky=W)
        self.firstname=Entry(frame)
        self.firstname.grid(row=1,column=2)

        Label(frame,text='lastname ').grid(row=2,column=1,sticky=W)
        self.lastname=Entry(frame)
        self.lastname.grid(row=2,column=2)

        Label(frame,text='username ').grid(row=3,column=1,sticky=W)
        self.username=Entry(frame)
        self.username.grid(row=3,column=2)

        Label(frame,text='email ').grid(row=4,column=1,sticky=W)
        self.email=Entry(frame)
        self.email.grid(row=4,column=2)

        Label(frame,text='subject ').grid(row=5,column=1,sticky=W)
        self.subject=Entry(frame)
        self.subject.grid(row=5,column=2)

        Label(frame,text='age').grid(row=6,column=1,sticky=W)
        self.age=Entry(frame)
        self.age.grid(row=6,column=2)

        ttk.Button(frame,text='Add Record',command=self.add).grid(row=7,column=2)
        self.message=Label(text='',fg='red')
        self.message.grid(row=8,column=1)
   #----------------table Display box-------------------
        self.tree=ttk.Treeview(height=10,column=['','','','','',''])
        self.tree.grid(row=9,column=0,columnspan=3)
        self.tree.heading('#0',text='id')
        self.tree.column('#0',width=50)
        self.tree.heading('#1',text='firstname')
        self.tree.column('#1',width=80)
        self.tree.heading('#2',text='lastname')
        self.tree.column('#2',width=80)
        self.tree.heading('#3',text='username')
        self.tree.column('#3',width=100)
        self.tree.heading('#4',text='email')
        self.tree.column('#4',width=50)
        self.tree.heading('#5',text='subject')
        self.tree.column('#5',width=50)
        self.tree.heading('#6',text='age')
        self.tree.column('#6',width=50,stretch=False)
        #----------------time -----------------
        def tick():
            d=datetime.datetime.now()
            Today= '{:%B %D %Y}'.format(d)
            mytime=time.strftime('%I %M %S')
            self.lblInfo.config(text=(mytime+'\t'+Today))
            self.lblInfo.after(200,tick)
        self.lblInfo=Label(font=('arial',15,'bold'),fg='dark blue')
        self.lblInfo.grid(row=10,column=0,columnspan=3)
        tick()
#--------Menu bar==--------------
        chooser=Menu()
        itemone=Menu(tearoff=0)
        itemone.add_command(label='Add record',command=self.add)
        itemone.add_command(label='Edit record')
        itemone.add_command(label='Delete record')
        itemone.add_separator()
        itemone.add_command(label='Help')
        itemone.add_command(label='Exit')
    
        chooser.add_cascade(label='File',menu=itemone)
        chooser.add_cascade(label='Add',command=self.add)
        chooser.add_cascade(label='Edit')
        chooser.add_cascade(label='Delete')
        chooser.add_cascade(label='Help')
        chooser.add_cascade(label='exit')
        root.config(menu=chooser)
        self.view_records()
#-------------- Database connection -------------------
    def run_query(self,stmt,para=()):
        con=MySQLdb.connect("localhost","root","")
        con.select_db("StudentList")
        cur=con.cursor()
        query_res=cur.execute(stmt,para)
        con.commit()
        return cur.fetchall()

    def view_records(self):
        records=self.tree.get_children()    
        for element in records:
            self.tree.delete(element)
        stmt="select * from Student"
        db_table=self.run_query(stmt)
        for data in db_table:
            self.tree.insert('',10,text=data[0],values=data[1:])

    def validation(self):
        return len(self.firstname.get()) !=0 and len(self.lastname.get()) !=0 and len(self.username.get()) !=0 and len(self.email.get()) !=0 and len(self.subject.get()) !=0 and len(self.age.get()) !=0

    def add_record(self):
        if self.validation():
            print(self.firstname.get())
            print(self.lastname.get())
            print(self.username.get())
            print(self.email.get())
            print(self.subject.get())
            print(self.age.get())
            
            
            stmt='INSERT INTO STUDENT VALUES(NULL,%s,%s,%s,%s,%s,%s)'
            para=(self.firstname.get(),self.lastname.get(),self.username.get(),
            self.email.get(),self.subject.get(),self.age.get())
            self.run_query(stmt,para)
            self.message['text']='record {} {} is added'.format(self.firstname.get(),self.lastname.get())


            self.firstname.delete(0,END)
            self.lastname.delete(0,END)
            self.username.delete(0,END)
            self.email.delete(0,END)
            self.subject.delete(0,END)
            self.age.delete(0,END)
        else:
            self.message['text']='fields are not completed'
        self.view_records() 
    def add(self):
        ad=tkinter.messagebox.askquestion('add record','want to add a new record ? ')
        if ad=='yes':
            self.add_record()

if __name__ =='__main__':
    root=Tk()
    app=school_portal(root)
    root.geometry('530x465+500+200')
    root.mainloop()    
