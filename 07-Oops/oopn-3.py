#constructor and destructors in python


class Book:
    __author=''
    __book=''
    __price=0.0
    __pages=0


    #Constructor Definition
    def __init__(self,author,book,price,pages):
        self.__author=author
        self.__book=book
        self.__price=price
        self.__pages=pages

    #Destructor Definition
    def __del__(self):
        #todo
        pass

    def Get(self):
        print("Author : " + self.__author)
        print("Book : " + self.__book)
        print("Price : " + str(self.__price))
        print("Pages : " + str(self.__pages))


#Creating an object
b=Book("Unknown","Unknown",1200,100)
b.Get()


