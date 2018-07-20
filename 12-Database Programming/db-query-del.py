import MySQLdb

conn = MySQLdb.connect('localhost', user='root', password='')
id=input('input id to be fetched: ')

if conn:
        conn.select_db("python")
        cursor = conn.cursor()
        cursor.execute("delete from  product where id=%s",(id))        
else:
        print("Connection Failed")


