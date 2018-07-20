#Writing Structured Data into a file

import pickle

class Student:
    id=0
    name=""
    course=""
    fees=0.0

    
s=Student()
s.id=2
s.name="Ravi Kumar"
s.course='ACWD'
s.fees=75000


f=open("student.dat","ab")
pickle.dump(s,f)
f.close()





