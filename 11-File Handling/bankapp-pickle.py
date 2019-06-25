#Banking Application


class Bank:
    acno=0
    name=''
    branch=''
    balance=0.0

    def CreateAccount(self):
        self.acno=int(input("Enter Account Number : "))
        self.name=input("Enter Name : ")
        self.branch=input("Enter Branch : ")
        self.balance=int(input("Enter Balance "))

    def DisplayAccount(self):
        print("Account Number : ", self.acno)
        print("Name : ", self.name)
        print("Branch : ", self.branch)
        print("Balance : ", self.balance)

    def Deposit(self):
        amount=int(input("Enter Amount : "))
        self.balance=self.balance+amount


    def Withdraw(self):
        amount=int(input("Enter Amount : "))
        if(self.balance>=amount):
            self.balance=self.balance-amount



#File Handling Using Pickle

import os
import pickle

def CreateAccount():
    f=open("bank.txt","ab")
    cust=Bank()
    cust.CreateAccount()
    pickle.dump(cust,f)
    f.close()

def DisplayAccount():
    acno=int(input("Enter Account Number : "))
    
    f=open("bank.txt","rb")
    isfound=False

    while(True):
        try:
            cust=pickle.load(f)
            if(cust.acno==acno):
                isfound=True
                cust.DisplayAccount()
        except:
            break

    if(isfound==False):
        print("Record Not Found")
    f.close()



def Deposit():          #File Updation
    acno=int(input("Enter Account Number : "))
    
    f=open("bank.txt","rb")
    t=open("temp.txt","wb")
    isfound=False

    while(True):
        try:
            cust=pickle.load(f)
            if(cust.acno==acno):
                cust.Deposit()
                isfound=True
            pickle.dump(cust,t)
        except:
            break

    if(isfound==False):
        print("Record Not Found")
    f.close()
    t.close()
    os.remove("bank.txt")
    os.rename("temp.txt","bank.txt")
    

def Withdraw():          #File Updation
    acno=int(input("Enter Account Number : "))
    
    f=open("bank.txt","rb")
    t=open("temp.txt","wb")
    isfound=False

    while(True):
        try:
            cust=pickle.load(f)
            if(cust.acno==acno):
                cust.Withdraw()
                isfound=True
            pickle.dump(cust,t)
        except:
            break


    if(isfound==False):
        print("Record Not Found")
    f.close()
    t.close()
    os.remove("bank.txt")
    os.rename("temp.txt","bank.txt")


def CloseAccount():          #File Deletion
    acno=int(input("Enter Account Number : "))
    
    f=open("bank.txt","rb")
    t=open("temp.txt","wb")
    isfound=False

    while(True):
        try:
            cust=pickle.load(f)
            if(cust.acno!=acno):
                pickle.dump(cust,t)
                isfound=True
        except:
            break


    if(isfound==False):
        print("Record Not Found")
    f.close()
    t.close()
    os.remove("bank.txt")
    os.rename("temp.txt","bank.txt")



while(True):
    print("1. Open Account")
    print("2. Display Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Close Account")
    print("0. Exit")

    choice=int(input("Enter Choice : "))

    if(choice==1):
        CreateAccount()
    elif(choice==2):
        DisplayAccount()
    elif(choice==3):
        Deposit()
    elif(choice==4):
        Withdraw()
    elif(choice==5):
        CloseAccount()
    elif(choice==0):
        exit(0)
        9
    


    








