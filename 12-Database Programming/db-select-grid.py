import MySQLdb

conn = MySQLdb.connect('localhost', user='root', password='')

if conn:
        conn.select_db("python")
        cursor = conn.cursor()
        cursor.execute("select * from product")
        data=cursor.fetchall()
        print("Id\tName\t\tPrice\t\tQuantity")
        for r in data:
                id=r[0]
                name=r[1]
                price=r[2]
                quan=r[3]
                remark=r[4]
                print(str(id)+"\t"+name+"\t\t"+str(price)+"\t\t"+str(quan))
else:
        print("Connection Failed")


