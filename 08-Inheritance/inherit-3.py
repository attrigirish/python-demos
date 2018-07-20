#Inheriting Protected and Public members

class Base:
    __a=0
    _b=0
    c=0

    def __init__(self):
        self.__a=5
        self._b=10
        self.c=15
    
    def PrintBase(self):
        print("A = " + str(self.__a))
        print("B = " + str(self._b))
        print("C = " + str(self.c))


class Derive(Base):    
    def PrintDerive(self):
        #print("A = " + str(self.__a))
        print("B = " + str(self._b))
        print("C = " + str(self.c))

#Testing Derive Object
obj=Derive()
obj.PrintBase()
obj.PrintDerive()






