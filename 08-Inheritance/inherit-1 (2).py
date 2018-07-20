#Inheritance

class Bank:
    acno=0
    name=''
    address=''
    aadhar=0

    def InputBank(self,acno,name,address,aadhar):
        self.acno=acno
        self.name=name
        self.address=address
        self.aadhar=aadhar

    def GetAcno(self):
        return self.acno

    def GetName(self):
        return self.name

    def GetAddress(self):
        return self.address

    def GetAadhar(self):
        return self.aadhar


class Saving(Bank):
    balance=0.0

    def CreateAccount(self,acno,name,address,aadhar,balance):
        self.InputBank(acno,name,address,aadhar)
        self.balance=balance

    def GetBalance(self):
        return self.balance

    def Deposit(self,amount):
        None

    def Withdrawl(self,amount):
        None



class Fixed(Bank):
    term=0
    amount=0.0

    def CreateAccount(self,acno,name,address,aadhar,term,amount):
        self.InputBank(acno,name,address,aadhar)
        self.term=term
        self.amount=amount

    def GetTerm(self):
        return self.term

    def GetAmount(self):
        return self.amount




s=Saving()
s.CreateAccount(12345,"Ankit","Rohini",989898989898,50000)
print("Account Number : " + str(s.GetAcno()))
print("Name : " + s.GetName())    
    
    
