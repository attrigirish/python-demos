#Inheritance

#declaration
#class childclass(baseclass):
#types of inheritance (single, multilevel)
#Parent/Super/Base
#Child/Sub/Derive

class Parent:
    id=0
    name=''
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def Get(self):
        print("Id : " + str(self.id))
        print("Name : " + str(self.name))


class Child(Parent):
    address=''
    def __init__(self,id,name,address):
        super(Child, self).__init__(id,name)
        self.address=address

    def GetChild(self):
        print("Address : " + self.address)


obj=Child(1,'Ankit','Kapil Vihar')
obj.Get()
obj.GetChild()



