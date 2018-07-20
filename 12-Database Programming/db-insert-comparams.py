#Step 1 - Importing MySQLdb module
import MySQLdb


#Step 2 - Establish a Connection
conn = MySQLdb.connect('localhost', user='root', password='')

if conn:
	print("Connection Established")
else:
	print("Connection Failed")


#Step 3 - Select Database

conn.select_db("python")

#Step 4 - Create Cursor object

cursor = conn.cursor()

#Step 5 - Execute Query 

pid=int(input("Enter Id : "))
name=input("Enter Name : ")
price=float(input("Enter Price : "))
stock=int(input("Enter Stock : "))
remark=input("Enter Remark : ")
cursor.execute("insert into product values(%s,%s,%s,%s,%s)",(pid,name,stock,price,remark))

#Step 6 - Close the Connection

conn.close()
