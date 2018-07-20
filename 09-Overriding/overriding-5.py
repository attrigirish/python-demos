class Bank:
    def __init__(self,acno,name,branch,pan):
        self.__acno=acno
        self.__name=name
        self.__branch=branch
        self.__pan=pan

    def getacno(self):
        return self.__acno

    def getname(self):
        return self.__name

    def getbranch(self):
        return self.__branch

    def getpan(self):
        return self.__pan


class Saving(Bank):
    def __init__(self,acno,name,branch,pan,balance):
        super(Saving,self).__init__(acno,name,branch,pan)
        self.__balance=balance

    def display(self):
        print("Account Number : " + str(self.getacno()))
        print("Name : " + self.getname())
        print("Branch : " + self.getbranch())
        print("Pan : " + self.getpan())
        print("Balance : " + str(self.__balance))

    def deposit(self,amount):
        self.__balance+=amount
        print("Transaction Executed Successfully")
        print("Availale Balance = " + str(self.__balance))

    def withdrawl(self,amount):
        if(self.__balance>=amount):
            self.__balance-=amount
            print("Transaction Executed Successfully")
            print("Availale Balance = " + str(self.__balance))
        else:
            print("Transaction Cancelled")
            print("Insufficient Balance")

    

o=Saving(12345,"Girish","Pitampura","EKELE1234D",50000)
o.display()
o.deposit(20000)
o.withdrawl(80000)



    
