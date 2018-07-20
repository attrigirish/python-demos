#OOPS - Object Oriented Programming

#Defining a class
class Mobile:
    model=''
    name=''
    brand=''
    price=0.0
    ram=0
    storage=0


#Creating a class object
a=Mobile()

#Accessing object properties
a.model='X21'
a.name='Vivo X21'
a.brand='Vivo'
a.price=35000
a.ram=6
a.storage=64

print("Model : " + a.model)
print("Name : " + a.name)
print("Brand : " + a.brand)
print("Price : " + str(a.price))
print("RAM : " + str(a.ram))
print("Storage : " + str(a.storage))







