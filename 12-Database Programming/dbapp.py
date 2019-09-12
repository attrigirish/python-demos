import MySQLdb
con=MySQLdb.connect('localhost','root','')
con.select_db('pydb')
cur=con.cursor()


def PrintRow(a,b,c,d,e):
    print(a + " "*(10-len(a)) , end="")
    print(b + " "*(30-len(b)) , end="")
    print(c + " "*(20-len(c)) , end="")
    print(d + " "*(8-len(d)) , end="")
    print(e + " "*(8-len(e)) , end="")
    print()
    print("-"*90)




def AddRecord():
    #Data Input
    id=int(input("Enter Id : "))
    name=input("Enter Name : ")
    brand=input("Enter Brand : ")
    price=float(input("Enter Price : "))
    stock=int(input("Enter Stock : "))

    stmt="insert into product values(%s,%s,%s,%s,%s)"
    parameters=(id,name,brand,price,stock)

    cur.execute(stmt,parameters)
    con.commit()
           

def DisplayRecord():
    #Data Output
    stmt="select * from product"
    cur.execute(stmt)
    records=cur.fetchall()
    PrintRow("Id","Name","Brand","Price","Stock")    
    for record in records:
        PrintRow(str(record[0]),record[1],record[2],str(record[3]),str(record[4]))

def SearchRecord():
    name=input("Enter Name : ")
    parameters=(name,)
    stmt="select * from product where name=%s"
    cur.execute(stmt,parameters)
    records=cur.fetchall()
    PrintRow("Id","Name","Brand","Price","Stock")    
    for record in records:
        PrintRow(str(record[0]),record[1],record[2],str(record[3]),str(record[4]))
    

def DeleteRecord():
    name=input("Enter Name : ")
    parameters=(name,)
    stmt="delete from product where name=%s"
    cur.execute(stmt,parameters)
    con.commit()


def UpdateRecord():
    name=input("Enter Name : ")
    price=input("Enter New Price : ")
    parameters=(price,name)
    stmt="update product set price=%s where name=%s"
    cur.execute(stmt,parameters)
    con.commit()


while(True):
    print("1. Add New Record")
    print("2. Dispay Records")
    print("3. Search Record")
    print("4. Delete Record")
    print("5. Update Record")
    print("0. Exit")

    choice=int(input("Enter Choice : "))

    if(choice==1):
        AddRecord()
    elif(choice==2):
        DisplayRecord()
    elif(choice==3):
        SearchRecord()
    elif(choice==4):
        DeleteRecord()
    elif(choice==5):
        UpdateRecord()
    elif(choice==0):
        con.close()
        break
    else:
        print("Please Try Again!")
        
    
