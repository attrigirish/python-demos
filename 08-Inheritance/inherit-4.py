#Constructors and Destructors in Inheritance

class Base:
    def __init__(self):
        print("Base Constructor")


class Derive(Base):
    def __init__(self):
        super(Derive, self).__init__()
        print("Derive Constructor")



obj=Derive()
