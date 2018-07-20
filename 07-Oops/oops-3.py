#OOPS - Object Oriented Programming

#Defining a class
class Mobile:
    model=''
    name=''
    brand=''
    price=0.0
    ram=0
    storage=0
    def Input(self,model,name,brand,price,ram,storage):
        self.model=model
        self.name=name
        self.brand=brand
        self.price=price
        self.ram=ram
        self.storage=storage

    def Output(self):
        print("Model : " + self.model)
        print("Name : " + self.name)
        print("Brand : " + self.brand)
        print("Price : " + str(self.price))
        print("RAM : " + str(self.ram))
        print("Storage : " + str(self.storage))
        


#Creating a class object
a=Mobile()

a.Input('X21','Vivo X21','Vivo',35000,6,64)
a.Output()




