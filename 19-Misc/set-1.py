import MySQLdb

con=MySQLdb.connect('localhost',user="root",password="")
con.select_db("travelmate")

cur=con.cursor()

cur.execute("select * from package where cost between 20000 and 50000")

s1=set(cur.fetchall())

print(s1)

cur.execute("select * from package where duration='3 Nights'")

s2=set(cur.fetchall())

print(s2)

s3=s1.intersection(s2)

print(s3)

con.close()
