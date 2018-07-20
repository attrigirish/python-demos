#class and objects

#Class Definition
class Book:
    author=''
    book=''
    price=0.0
    pages=0


#Creating an object
b=Book()
b.author='J K Rowling'
b.book='Harry Potter'
b.price=1300
b.pages=700

print("Author : " + b.author)
print("Book : " + b.book)
print("Price : " + str(b.price))
print("Pages : " + str(b.pages))


