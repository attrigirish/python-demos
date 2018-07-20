#Classes and Objects

#Class Definition
class Student:
    id=0
    name=''
    std=''
    section=''
    email=''
    phone=''


#Creating Class Object
s=Student()

#Initializing object 
s.id=1
s.name='Ankit Kumar'
s.std='12th'
s.section='A'
s.email='ankit@mail.com'
s.phone='9898984731'

#Displaying object details
print("ID : " + str(s.id))
print("Name : " + s.name)
print("Standard : " + s.std)
print("Section : " + s.section)
print("Email : " + s.email)
print("Phone : " + s.phone)




