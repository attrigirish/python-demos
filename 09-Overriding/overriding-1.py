class A:
    def Print(self):
        print("A Function")

class B(A):
    None
    
class C(B):
    def Print(self):
        print("C Funtion")

obj=A()
obj.Print()            

obj=B()
obj.Print()

obj=C()
obj.Print()




