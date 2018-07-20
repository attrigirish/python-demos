#Students' Data Keeping Software

import pickle
import os

class Student:
    id=0
    name=""
    course=""
    fees=0.0



def Save():
    s=Student()
    s.id=int(input("Enter Student Id : "))
    s.name=input("Enter Student Name : ")
    s.course=input("Enter Student Course : ")
    s.fees=float(input("Enter Student Fees : "))

    f=open("student.dat","ab")
    pickle.dump(s,f)
    f.close()


def Display():
    f=open("student.dat","rb")
    print("Id\t\tName\t\tCourse\t\tFees")
    while True:
        try:
            s=pickle.load(f)
            print(str(s.id)+"\t\t"+s.name+"\t\t"+s.course+"\t\t"+str(s.fees))
        except:
            break
    f.close()


def Search():
    f=open("student.dat","rb")
    id=int(input("Enter Id to Search : "))
    while True:
        try:
            s=pickle.load(f)
            if(id==s.id):
                print("Matching Record Found")
                print("Id : " + str(s.id))
                print("Name : " + s.name)
                print("Course : " + s.course)
                print("Fees : " + str(s.fees))
        except:
            break
    f.close()

def Delete():
    f=open("student.dat","rb")
    temp=open("temp.dat","wb")
    id=int(input("Enter Id to Search : "))
    while True:
        try:
            s=pickle.load(f)
            if(id!=s.id):
                pickle.dump(s,temp)
        except:
            break
    f.close()
    temp.close()
    os.remove("student.dat")
    os.rename("temp.dat","student.dat")


def Update():
    f=open("student.dat","rb")
    temp=open("temp.dat","wb")
    id=int(input("Enter Id to Search : "))
    while True:
        try:
            s=pickle.load(f)
            if(id==s.id):
                s.name=input("Enter Student Name : ")
                s.course=input("Enter Student Course : ")
                s.fees=float(input("Enter Student Fees : "))
            pickle.dump(s,temp)
        except:
            break
    f.close()
    temp.close()
    os.remove("student.dat")
    os.rename("temp.dat","student.dat")







while True:
    print("1. Add New Record")
    print("2. Display Records")
    print("3. Search Record")
    print("4. Delete Record")
    print("5. Update Record")
    print("0. Exit")

    choice=int(input("Enter Your Choice : "))

    if(choice==1):
        Save()
    elif(choice==2):
        Display()
    elif(choice==3):
        Search()
    elif(choice==4):
        Delete()
    elif(choice==5):
        Update()
    else:
        break
    


    



