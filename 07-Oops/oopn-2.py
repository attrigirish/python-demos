#class and objects

#Class Definition

#Python Name Mangling
#private : __field
#protected : _field

class Book:
    __author=''
    __book=''
    __price=0.0
    __pages=0

    def Set(self,author,book,price,pages):
        self.__author=author
        self.__book=book
        self.__price=price
        self.__pages=pages

    def Get(self):
        print("Author : " + self.__author)
        print("Book : " + self.__book)
        print("Price : " + str(self.__price))
        print("Pages : " + str(self.__pages))


#Creating an object
b=Book()
b.Set("Unknown","Unknown",1200,100)
b.Get()


