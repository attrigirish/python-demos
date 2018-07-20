#Cash Register

class CashRegister:
    def __init__(self,cash=0):
        self.__cash=cash

    def getcurrentbalance(self):
        return self.__cash

    def acceptamount(self,cash):
        self.__cash=self.__cash+cash


class Dispenser:
    def __init__(self,nitems=None,cost=None):
        if(nitems==None):
            self.__nitems=50
        else:
            self.__nitems=nitems

        if(cost==None):
            self.__cost=50
        else:
            self.__cost=cost


    def getitems(self):
        return self.__nitems

    def getcost(self):
        return self.__cost

    def makesale(self):
        self.__nitems=self.__nitems-1






#Main Program

def sellproduct(product,dispenser,cashregister):
    if(dispenser.getitems()>0):
        print("Price : " + str(dispenser.getcost()))
        amount=int(input(("Enter Amount : ")))
        if(dispenser.getcost()<=amount):
            dispenser.makesale()
            cashregister.acceptamount(dispenser.getcost())
            print("Collect Your "+product+" and Balance Amount = " + str(amount-dispenser.getcost()))
        else:
            print("Insufficient Amount")
    else:
        print("Out of Stock")

        

def showselection():
    print("1. Candy")
    print("2. Chips")
    print("3. Cookies")
    print("4. Gums")

    print("-"*20)
    option=int(input("Enter Your Option : "))
    print("-"*20)
    return option
    


candy=Dispenser(1000,10)
chips=Dispenser(500,20)
cookies=Dispenser(200,50)
gums=Dispenser(1000,5)
cashregister=CashRegister(2000)

while True:
    option=showselection()
    if(option==1):
        sellproduct("Candy",candy,cashregister)        
    elif(option==2):
        sellproduct("Chips",chips,cashregister)
    elif(option==3):
        sellproduct("Cookies",cookies,cashregister)
    elif(option==4):
        sellproduct("Gums",gums,cashregister)
    elif(option==0):
        break
    elif(option==999):
        print("Machine Stats")
        print("Candy : " + str(candy.getitems()))
        print("Chips : " + str(chips.getitems()))
        print("Gums : " + str(gums.getitems()))
        print("Cookies : " + str(cookies.getitems()))
        print("Available Cash : " + str(cashregister.getcurrentbalance
              ()))
    else:
        print("Please Try Again!")

    
        
    
