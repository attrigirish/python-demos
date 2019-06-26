class CashRegister:
    __cashonhand=0

    def __init__(self,cash=500):
        self.__cashonhand=cash

    def acceptAmount(self,amount):
        self.__cashonhand += amount

    def getCurrentBalance(self):
        return self.__cashonhand


class DispenserType:
    __nitems=0
    __cost=0

    def __init__(self,nitems=50,cost=50):
        self.__nitems=nitems
        self.__cost=cost

    def getNoOfItems(self):
        return self.__nitems

    def getCost(self):
        return self.__cost

    def makeSale(self):
        self.__nitems -= 1



pepsi=DispenserType(100,35)
fanta=DispenserType(100,35)
limca=DispenserType(100,40)
lays=DispenserType(200,20)
cr=CashRegister(2000)


def sellProduct(item,cr):
    if(item.getNoOfItems()==0):
        print("Out of Stock")
        return
    
    cost=item.getCost()
    print("Cost of the Item : ", cost)

    amount=int(input("Enter Amount : "))

    if(amount>=cost):
        item.makeSale()
        cr.acceptAmount(cost)
        print("Thank You for Ordering With Us")
        print("Please collect your product and balance : ", (amount-cost))
    else:
        print("You've entered wrong amount")


def showMenu():
    while(True):
        print("1. Pepsi")
        print("2. Fanta")
        print("3. Limca")
        print("4. Lays")

        choice=int(input("Enter Choice : "))

        if(choice==1):
            sellProduct(pepsi,cr)
        elif(choice==2):
            sellProduct(fanta,cr)
        elif(choice==3):
            sellProduct(limca,cr)
        elif(choice==4):
            sellProduct(lays,cr)
        elif(choice==98765):
            print("Available Stock")
            print("Pepsi : ", pepsi.getNoOfItems())
            print("Limca : ", limca.getNoOfItems())
            print("Fanta : ", fanta.getNoOfItems())
            print("Lays : ", lays.getNoOfItems())
            print("Available Cash : ", cr.getCurrentBalance())
        else:
            print("Invalid Input")



#To Run the Program
showMenu()
            
        


        



