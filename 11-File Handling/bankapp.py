#Banking Application

import os

def CreateAccount():
    f=open("bank.txt","a")
    acno=input("Enter Account Number : ")
    name=input("Enter Name : ")
    branch=input("Enter Branch : ")
    balance=input("Enter Balance : ")
    f.write(acno+","+name+","+branch+","+balance+"\n")
    f.close()

def DisplayAccount():
    acno=input("Enter Account Number : ")
    
    f=open("bank.txt","r")
    data=f.read()
    #Split Records from the Data
    data=data.split("\n")
    isfound=False
    for record in data:
        if(record!=''):
            record=record.split(",")
            if(record[0]==acno):
                isfound=True
                print("Account Number  : ", record[0])
                print("Name : ", record[1])
                print("Branch : ", record[2])
                print("Balance : ", record[3])

    if(isfound==False):
        print("Record Not Found")
    f.close()



def Deposit():          #File Updation
    acno=input("Enter Account Number : ")
    
    f=open("bank.txt","r")
    t=open("temp.txt","w")
    data=f.read()
    #Split Records from the Data
    data=data.split("\n")
    isfound=False
    for record in data:
        if(record!=''):
            record=record.split(",")
            if(record[0]==acno):
                isfound=True
                amount=input("Enter Amount to Deposit : ")
                record[3]=str(int(record[3])+int(amount))
            t.write(record[0]+","+record[1]+","+record[2]+","+record[3]+"\n")
    if(isfound==False):
        print("Record Not Found")
    f.close()
    t.close()
    os.remove("bank.txt")
    os.rename("temp.txt","bank.txt")
    

def Withdraw():          #File Updation
    acno=input("Enter Account Number : ")
    
    f=open("bank.txt","r")
    t=open("temp.txt","w")
    data=f.read()
    #Split Records from the Data
    data=data.split("\n")
    isfound=False
    for record in data:
        if(record!=''):
            record=record.split(",")
            if(record[0]==acno):
                isfound=True
                amount=input("Enter Amount to Deposit : ")
                record[3]=str(int(record[3])-int(amount))
            t.write(record[0]+","+record[1]+","+record[2]+","+record[3]+"\n")
    if(isfound==False):
        print("Record Not Found")
    f.close()
    t.close()
    os.remove("bank.txt")
    os.rename("temp.txt","bank.txt")


def CloseAccount():          #File Deletion
    acno=input("Enter Account Number : ")
    
    f=open("bank.txt","r")
    t=open("temp.txt","w")
    data=f.read()
    #Split Records from the Data
    data=data.split("\n")
    isfound=False
    for record in data:
        if(record!=''):
            record=record.split(",")
            if(record[0]!=acno):
                isfound=True
                t.write(record[0]+","+record[1]+","+record[2]+","+record[3]+"\n")
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
        
    


    








