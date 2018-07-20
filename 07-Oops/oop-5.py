class report:
    __adno=0
    __name=''
    __marks=[0,0,0,0,0]
    __average=0

    def __getavg(self):
        sum=0
        for i in range(5):
            sum=sum+self.__marks[i]
        self.__average=sum/5

    def __init__(self):
        self.__adno=int(input("enter admission number"))
        self.__name=input("enter name of the student")
        for i in range(5):
            self.__marks[i]=int(input("enter marks"))
        self.__getavg()

    def display_info(self):
        print('adno: '+str(self.__adno))
        print('name: '+self.__name)
        print('marks: '+str(self.__marks))
        print('average: '+str(self.__average))

r=report()
r.display_info()
        
