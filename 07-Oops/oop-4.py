#Private, Protected and Public Members in Python

#Private : Members can be accessed within the same class only
#Protected : Members can be accessed either in the same class or in derived classes only
#Public : Members can be accessed anywhere in the program using objects


class book:

    __book_no=0
    __book_title=''
    __price=0

    def __total_cost(self,n):
        tot_cost=self.__price*n
        return tot_cost

    def input(self):
        self.__book_no=int(input("enter book number"))
        self.__book_title=input("enter book title")
        self.__price=int(input("enter price of a book"))
        

    def purchase(self):
        n=int(input("enter the number of coppies"))
        tot_cost=self.__total_cost(n)
        print('Book Number : '+str(self.__book_no))
        print('book title: '+self.__book_title)
        print('price: '+str(self.__price))
        print('total cost: '+str(tot_cost))

b=book()
b.input()
b.purchase()

        
