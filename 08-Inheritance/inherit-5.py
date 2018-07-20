#Constructors and Destructors in Inheritance

class Employee:
    __empid=0
    __name=''
    def __init__(self,empid,name):
        self.__empid=empid
        self.__name=name
        
    def Print(self): #Prints Employees basic Details
        print("Employee Id : " + str(self.__empid))
        print("Employee Name : " + self.__name)


class Department(Employee):
    __dept=''
    def __init__(self,empid,name,dept):
        super(Department,self).__init__(empid,name)
        self.__dept=dept

    def Print(self):    #Overriding
        super(Department,self).Print()
        print("Employee Department : " + self.__dept)


o=Department(123,"Ankit","Sales")
o.Print()


