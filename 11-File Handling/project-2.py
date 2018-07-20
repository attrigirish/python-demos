#Bank

import pickle
import os

class Saving:
    acno=0
    name=''
    branch=''
    balance=0.0
    pan=''

    def __init__(self,acno,name,branch,balance,pan):
        self.acno=acno
        self.name=name
        self.branch=branch
        self.balance=balance
        self.pan=pan

    def getacno(self):
        return self.acno

    def getname(self):
        return self.name

    def getbranch(self):
        return self.branch

    def getbalance(self):
        return self.balance

    def getpan(self):
        return self.pan

    def deposit(self,amount):
        self.balance+=amount
        return True

    def withdrawl(self,amount):
        if(self.balance>=amount):
            self.balance-=amount
            return True
        else:
            return False



#File Functions (Database Handling Functions)

def CreateAccount():
    print("Enter Customer Details")
    acno=int(input("Enter Account Number : "))
    name=input("Enter Name : ")
    branch=input("Enter Branch : ")
    pan=input("Enter Pan Number : ")
    balance=float(input("Enter Balance : "))
    
    s=Saving(acno,name,branch,balance,pan)
    file=open("bank.dat","ab")
    pickle.dump(s,file)
    file.close()


def DisplayAccount():
    acno=int(input("Enter Customer Account Number : "))

    file=open("bank.dat","rb")

    while True:
        try:
            s=pickle.load(file)
            if(s.getacno()==acno):
                print("Customer details are")
                print("Name : " + s.getname())
                print("Branch : " + s.getbranch())
                print("Pan : " + s.getpan())
                print("Balance : " + str(s.getbalance()))
        except:
            break
                      
    file.close()


def Deposit():
    acno=int(input("Enter Customer Account Number : "))
    
    file=open("bank.dat","rb")
    temp=open("temp.dat","wb")

    while True:
        try:
            s=pickle.load(file)
            if(s.getacno()==acno):
                amount=float(input("Enter Amount to Deposit : "))
                s.deposit(amount)
            pickle.dump(s,temp)
        except:
            break

    file.close()
    temp.close()

    os.remove("bank.dat")
    os.rename("temp.dat","bank.dat")

def Withdrawl():
    acno=int(input("Enter Customer Account Number : "))
    
    file=open("bank.dat","rb")
    temp=open("temp.dat","wb")

    while True:
        try:
            s=pickle.load(file)
            if(s.getacno()==acno):
                amount=float(input("Enter Amount to Withdrawl : "))
                s.withdrawl(amount)
            pickle.dump(s,temp)
        except:
            break

    file.close()
    temp.close()

    os.remove("bank.dat")
    os.rename("temp.dat","bank.dat")


def CloseAccount():
    acno=int(input("Enter Customer Account Number : "))
    
    file=open("bank.dat","rb")
    temp=open("temp.dat","wb")

    while True:
        try:
            s=pickle.load(file)
            if(s.getacno()!=acno):
                pickle.dump(s,temp)
        except:
            break

    file.close()
    temp.close()

    os.remove("bank.dat")
    os.rename("temp.dat","bank.dat")


#Main Program

while True:
    print("1. Create New Account")
    print("2. Display Account Details")
    print("3. Deposit")
    print("0. Exit")

    choice=int(input("Select an Option : "))
    
    if(choice==1):
        CreateAccount()
    elif(choice==2):
        DisplayAccount()
    elif(choice==3):
        Deposit()
    elif(choice==4):
        Withdrawl()
    elif(choice==5):
        CloseAccount()
    elif(choice==0):
        break
               
    
    
    

