#OOPS - Object Oriented Programming

#Defining a class
class Mobile:
    model=''
    name=''
    brand=''
    price=0.0
    ram=0
    storage=0
    def Input(self):
        self.model=input("Enter Model Number : ")        
        self.name=input("Enter Name : ")
        self.brand=input("Enter Brand : ")
        self.price=float(input("Enter Price : "))
        self.ram=int(input("Enter RAM : "))
        self.storage=int(input("Enter Storage : "))

    def Output(self):
        print("Model : " + self.model)
        print("Name : " + self.name)
        print("Brand : " + self.brand)
        print("Price : " + str(self.price))
        print("RAM : " + str(self.ram))
        print("Storage : " + str(self.storage))
        


#Creating a class object
a=Mobile()

a.Input()
a.Output()



