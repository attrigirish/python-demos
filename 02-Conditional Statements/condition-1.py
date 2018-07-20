#Simple if..else program

balance=100000
amount=int(input("Enter Amount to withdraw : "))

if(balance>amount):
    balance=balance-amount
    print("Transaction Completed Successfully")
    print("Available Balance = " + str(balance))
else:
    print("Transaction Declined! Insufficient Balance")
