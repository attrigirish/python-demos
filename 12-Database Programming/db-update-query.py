import MySQLdb

conn = MySQLdb.connect('localhost', user='root', password='')
id=input('input id to be fetched: ')
name=input('input name to be updated: ')
price=input('input price to be updated: ')
qty=input('input quantity to be updated: ')


if conn:
        conn.select_db("python")
        cursor = conn.cursor()
        cursor.execute("update product set name=%s,price=%s,stock=%s where id=%s",(name,price,qty,id))
else:
        print("Connection Failed")


