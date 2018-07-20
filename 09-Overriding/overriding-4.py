class A:
    def __init__(self):
        print("Parent Constructor")


class B(A):
    def __init__(self):
        super(B,self).__init__()            
        print("Child Constructor")


obj=B()
