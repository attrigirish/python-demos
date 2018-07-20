#Method Overriding

class A:
    def Output(self):
        print("A Class")

class B(A):
    def Output(self):               #Method Overriding
        super(B,self).Output()      #Calling Base class Method
        #or
        #A.Output(self)
        print("B Class")



b=B()
b.Output()
        
