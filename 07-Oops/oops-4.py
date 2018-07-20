class Bank:
    acno=0
    name=''
    branch=''
    balance=0.0

    def OpenAccount(self,acno,name,branch,balance):
        self.acno=acno
        self.name=name
        self.branch=branch
        self.balance=balance

    def DisplayAccount(self):
        print("Account Number : " + str(self.acno))
        print("Name : " + self.name)
        print("Branch : " + self.branch)
        print("Balance : " + str(self.balance))

    def Deposit(self,amount):
        self.balance=self.balance+amount
        print("Updated Account Balance : " + str(self.balance))


    def Withdrawl(self,amount):
        if(self.balance>amount):
            self.balance=self.balance-amount
            print("Updated Account Balance : " + str(self.balance))
        else:
            print("Insufficieint Balance")

    def UpdateName(self,name):
        self.name=name

    def UpdateBranch(self,branch):
        self.branch=branch



b=Bank()

b.OpenAccount(12345,"Girish Attri","Rohini",5000)
b.DisplayAccount()
b.Deposit(5000)
b.Withdrawl(12000)











    
