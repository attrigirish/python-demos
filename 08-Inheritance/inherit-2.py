#Inheritance

class Base:
    def Test(self):
        print("Test from Base")


class Derive(Base):
    def Fun(self):
        print("Fun from Derive")



#Testing Derive Object
obj=Derive()
obj.Test()
obj.Fun()
