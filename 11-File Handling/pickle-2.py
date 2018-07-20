#Reading Structured Data from a file

import pickle

class Student:
    id=0
    name=""
    course=""
    fees=0.0

    
f=open("student.dat","rb")

while True:
    try:
        s=pickle.load(f)
        print("Id = " + str(s.id))
        print("Name = " + s.name)
        print("Course = " + s.course)
        print("Fees = " + str(s.fees))
    except:
        break

f.close()


