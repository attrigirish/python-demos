class A:
    def __init__(self,a,b):
        self.__a=a
        self.__b=b

    def Print(self):
        print("A = " + str(self.__a))
        print("B = " + str(self.__b))

class B(A):
    def __init__(self,a,b):
        super(B,self).__init__(a,b)

    def Print(self):
        super(B,self).Print()


obj=B(5,10)
obj.Print()





