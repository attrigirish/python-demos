#Classes and Objects

class Student:
    id=0
    name=''
    std=''
    section=''
    email=''
    phone=''

    
    def Input(self):
        self.id=int(input("Enter Student ID : "))
        self.name=input("Enter Student Name : ")
        self.std=input("Enter Student Class : ")
        self.section=input("Enter Student Section : ")
        self.email=input("Enter Student Email : ")
        self.phone=input("Enter Student Phone : ")

    def Output(self):
        print(self.id)
        print(self.name)
        print(self.std)
        print(self.section)
        print(self.email)
        print(self.phone)



        

s=Student()

s.Input()
s.Output()


