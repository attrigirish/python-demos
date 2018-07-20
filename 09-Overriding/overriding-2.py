class A:
    def Print(self):
        print("A Function")

class B(A):
    def Print(self):
        super(B,self).Print()
        print("B Funtion")
    
class C(B):
    def Print(self):
        super(C,self).Print()
        print("C Funtion")

obj=C()
obj.Print()

