import MySQLdb

conn = MySQLdb.connect('localhost', user='root', password='')

if conn:
        conn.select_db("python")
        cursor = conn.cursor()
        cursor.execute("select * from product")
        data=cursor.fetchall()
        for r in data:
                print("Id : " + str(r[0]))
                print("Name : " + r[1])
                print("Price : " + str(r[2]))
                print("Quantity : " + str(r[3]))
                print("Remark : " + str(r[4]))
else:
        print("Connection Failed")


