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

cursor.execute("insert into product values(3,'Vivo V9',100,29000,'NA')")

#Step 6 - Close the Connection

conn.close()
