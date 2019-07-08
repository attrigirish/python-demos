from bankmodel import Bank

b=Bank()
while(True):
    print("1. Create Account")
    print("2. Change Name")
    print("3. Change Branch")
    print("4. Deposit Amount")
    print("5. Withdrawl Amount")
    print("6. Check Balance")
    print("7. Check Branch")

    choice=int(input("Enter Choice : "))

    if(choice==1):
        acno=int(input("Enter Account Number : "))
        name=input("Enter Name : ")
        branch=input("Enter Branch : ")
        balance=int(input("Enter Balance : "))
        b.CreateAccount(acno,name,branch,balance)
    elif(choice==2):
        name=input("Enter New Name : ")
        b.SetName(name)
    elif(choice==3):
        branch=input("Enter Branch : ")
        b.SetBranch(branch)
    elif(choice==4):
        amount=int(input("Enter Deposit Amount : "))
        b.Deposit(amount)
    elif(choice==5):
        amount=int(input("Enter Withdrawl Amount : "))
        b.Withdrawl(amount)
    elif(choice==6):
        print("Available Balance : ", b.GetBalance())
    elif(choice==7):
        print("Branch : ", b.GetBranch())


        
        



