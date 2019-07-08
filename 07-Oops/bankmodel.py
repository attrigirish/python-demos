class Bank:
    acno=0
    name=''
    branch=''
    balance=0.0

    def CreateAccount(self,acno,name,branch,balance):
        self.acno=acno
        self.name=name
        self.branch=branch
        self.balance=balance

    def SetName(self,name):
        self.name=name

    def SetBranch(self,branch):
        self.branch=branch

    def Deposit(self,amount):
        self.balance+=amount

    def Withdrawl(self,amount):
        self.balance-=amount

    def GetAcNo(self):
        return self.acno

    def GetName(self):
        return self.name

    def GetBranch(self):
        return self.branch

    def GetBalance(self):
        return self.balance




    


    
    
