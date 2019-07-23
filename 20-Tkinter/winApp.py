from tkinter import *
from tkinter import messagebox
import pickle


class Student:
    id=0
    name=''
    course=''
    fees=0.0

    def Input(self,id,name,course,fees):
        self.id=id
        self.name=name
        self.course=course
        self.fees=fees




class Fullscreen_Window:
    win=None
    frame=None
    lblId=None
    txtId=None
    lblName=None
    txtName=None
    lblCourse=None
    txtCourse=None
    lblFees=None
    txtFees=None
    btnSubmit=None

    def __init__(self):
        self.win = Tk()
        #Set the Window in Full Screen Mode
        self.win.state('zoomed')
        #Font
        self.win.option_add('*font', ('verdana', 14, 'bold'))
        #Add a Frame to the Window
        self.frame = Frame(self.win)
        self.frame.pack(fill=BOTH)
        #Add Menu to the Window
        self.menu()

    def menu(self):
        menubar = Menu(self.win)
        menubar.add_command(label="Add Record",command=self.LoadNewRecordWindow)
        menubar.add_command(label="Delete Record",command=self.LoadDeleteRecordWindow)
        menubar.add_command(label="Update Record",command=self.LoadNewRecordWindow)
        menubar.add_command(label="Display Record",command=self.LoadDisplayRecordWindow) 
        self.win.config(menu=menubar)

    def LoadNewRecordWindow(self):
        childFrame = Frame()
        childFrame.place(in_=self.frame, x=400, y=200)

        self.lblId=Label(childFrame, text="Enter Id : ")
        self.txtId=Text(childFrame, width=20, height=1)
        self.lblName=Label(childFrame, text="Enter Name : ")
        self.txtName=Text(childFrame, width=20, height=1)
        self.lblCourse=Label(childFrame, text="Enter Course : ")
        self.txtCourse=Text(childFrame, width=20, height=1)
        self.lblFees=Label(childFrame, text="Enter Fees : ")
        self.txtFees=Text(childFrame, width=20, height=1)
        self.btnSubmit=Button(childFrame, width=30,height=1,text="Add Record",command=self.SaveRecord)

        self.lblId.grid(row=1,column=1,sticky=W)
        self.txtId.grid(row=1,column=2,sticky=W)
        self.lblName.grid(row=2,column=1,sticky=W)
        self.txtName.grid(row=2,column=2,sticky=W)
        self.lblCourse.grid(row=3,column=1,sticky=W)
        self.txtCourse.grid(row=3,column=2,sticky=W)
        self.lblFees.grid(row=4,column=1,sticky=W)
        self.txtFees.grid(row=4,column=2,sticky=W)
        self.btnSubmit.grid(row=5,column=1,columnspan=2,sticky=W+E)


    def LoadUpdateRecordWindow(self):
        childFrame = Frame(width=600, height=600)
        #f1.pack(fill="both", expand=True, padx=20, pady=20)
        childFrame.place(in_=self.frame, x=400, y=200)

        lblId=Label(childFrame, text="Enter Id : ")
        txtId=Text(childFrame, width=20, height=1)
        lblName=Label(childFrame, text="Enter Name : ")
        txtName=Text(childFrame, width=20, height=1)
        lblCourse=Label(childFrame, text="Enter Course : ")
        txtCourse=Text(childFrame, width=20, height=1)
        lblFees=Label(childFrame, text="Enter Fees : ")
        txtFees=Text(childFrame, width=20, height=1)
        btnSave=Button(childFrame, width=30,height=1,text="Update Record")

        lblId.grid(row=1,column=1,sticky=W)
        txtId.grid(row=1,column=2,sticky=W)
        lblName.grid(row=2,column=1,sticky=W)
        txtName.grid(row=2,column=2,sticky=W)
        lblCourse.grid(row=3,column=1,sticky=W)
        txtCourse.grid(row=3,column=2,sticky=W)
        lblFees.grid(row=4,column=1,sticky=W)
        txtFees.grid(row=4,column=2,sticky=W)
        btnSave.grid(row=5,column=1,columnspan=2,sticky=W+E)


    def LoadDeleteRecordWindow(self):
        childFrame = Frame(width=600, height=600)
        #f1.pack(fill="both", expand=True, padx=20, pady=20)
        childFrame.place(in_=self.frame, x=400, y=200)

        lblId=Label(childFrame, text="Enter Id : ")
        txtId=Text(childFrame, width=20, height=1)
        btnSave=Button(childFrame, width=30,height=1,text="Delete Reocrd")

        lblId.grid(row=1,column=1,sticky=W)
        txtId.grid(row=1,column=2,sticky=W)
        btnSave.grid(row=5,column=1,columnspan=2,sticky=W+E)


    def LoadDisplayRecordWindow(self):
        self.frame.grid_forget()
        childFrame = Frame(width=600,height=600)
        childFrame.place(in_=self.frame, x=400, y=200)

        self.lblId=Label(childFrame, width=10, text="Id")
        self.lblName=Label(childFrame, width=10, text="Name")
        self.lblCourse=Label(childFrame, width=10, text="Course")
        self.lblFees=Label(childFrame, width=10, text="Fees")
        self.lblId.grid(row=1,column=1,sticky=W)
        self.lblName.grid(row=1,column=2,sticky=W)
        self.lblCourse.grid(row=1,column=3,sticky=W)
        self.lblFees.grid(row=1,column=4,sticky=W)

        f=open("student.dat","rb")
        row=2
        while(True):
            try:
                s=pickle.load(f)
                Label(childFrame, width=10,  text=s.id).grid(row=row,column=1,sticky=W,)
                Label(childFrame, width=10,  text=s.name).grid(row=row,column=2,sticky=W)
                Label(childFrame, width=10,  text=s.course).grid(row=row,column=3,sticky=W)
                Label(childFrame, width=10,  text=s.fees).grid(row=row,column=4,sticky=W)
                row=row+1
            except:
                break
        f.close()
        

    def SaveRecord(self):
        f=open("student.dat","ab")
        id=int(self.txtId.get(0.1,END))
        name=self.txtName.get(0.1,END)
        course=self.txtCourse.get(0.1,END)
        fees=float(self.txtFees.get(0.1,END))

        s=Student()
        s.Input(id,name,course,fees)
        try:
            pickle.dump(s,f)
            messagebox.showinfo("Student Management System","Record Saved Successfully")            
        except:
            messagebox.showerror("Student Management System","Something went wrong!")
        f.close()
        

        


if __name__ == '__main__':
    w = Fullscreen_Window()
    w.win.mainloop()
    print(dir(w))
