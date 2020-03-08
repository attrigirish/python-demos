'''
Define a class BOOK with the following specifications:

- bookno
- booktitle             
- price

- TOTAL_COST()  : A function to calculate the total cost for N number of copies where N is passed to the function as argument.

- INPUT() : function to read BOOK_NO. BOOKTITLE, PRICE

- PURCHASE() : function to ask the user to input the number of copies to be purchased. It invokes TOTAL_COST() and prints the total cost to be paid by the user.
'''

class Book:
	bookno=0
	booktitle=''
	price=0.0

	def TOTAL_COST(self,n):
		cost=self.price*n
		return cost

	def INPUT(self,bookno,booktitle,price):
		self.bookno=bookno
		self.booktitle=booktitle
		self.price=price

	def OUTPUT(self):
		print("Book No : ", self.bookno)
		print("Book Title : ", self.booktitle)
		print("Price : ", self.price)

	def PURCHASE(self,n):
		cost=self.TOTAL_COST()
		print("Book No : ", self.bookno)
		print("Book Title : ", self.booktitle)
		print("Book Price : ", self.price)
		print("No. of Copies : ", n)
		print("Total Cost : ", cost)


books=[]

while(True):
	print("1. Add Book")
	print("2. Search Book")
	print("3. Delete Book")
	print("4. Display Books")
	print("5. Purchase Book")

	print()
	choice=input("Enter Choice : ")
	print()

	if(choice==1):
		no=int(input("Enter Book No (ISBN) : "))
		title=input("Enter Book Title : ")
		price=int(input("Enter Book Price : "))
		book=Book()
		book.INPUT(no,title,price)
		books.append(book)
	elif(choice==2):
		name=input("Enter Book Name to Search : ")
		isfound=False
		for book in books:
			if(book.name==name):
				book.OUTPUT()
				isfound=True
		if(isfound==False):
			print("No Book Found")
	elif(choice==3):
		name=input("Enter Book Name to Search : ")
		isfound=False
		for book in books:
			if(book.name==name):
				books.remove(book)
				isfound=True
		if(isfound==False):
			print("No Book Found")
	elif(choice==4):
		for book in books:
			book.OUTPUT()
	elif(choice==5):
		name=input("Enter Book Name to Search : ")
		isfound=False
		for book in books:
			if(book.name==name):
				n=int(input("How many copies you want : "))
				book.PURCHASE(n)
				isfound=True
		if(isfound==False):
			print("No Book Found")
	elif(choice==0):
		break




