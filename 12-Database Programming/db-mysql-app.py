import MySQLdb


def GetConnection():
    con=MySQLdb.connect('localhost',user='root',password='')
    con.select_db('aptech')
    cur=con.cursor()
    return con,cur




def Insert():
    id=int(input("Enter ID : "))
    name=input("Enter Student Name : ")
    course=input("Enter Course Name : ")
    fees=float(input("Enter Fees : "))
    
    con,cur=GetConnection()
    query="INSERT INTO STUDENT VALUES(%s,%s,%s,%s)"
    parameters=(id,name,course,fees)
    result=cur.execute(query,parameters)
    con.commit()
    con.close()


def Search():
    id=int(input("Enter Id to Search Record : "))
    
    con,cur=GetConnection()
    query="SELECT * FROM STUDENT WHERE ID=%s"
    parameters=(id,)
    result=cur.execute(query,parameters)

    record=cur.fetchone()
    print(record)

    con.close()

    
def Delete():
    id=int(input("Enter Id to Search Record : "))
    
    con,cur=GetConnection()
    query="DELETE FROM STUDENT WHERE ID=%s"
    parameters=(id,)
    result=cur.execute(query,parameters)

    con.commit()
    con.close()


def UpdateName():
    id=int(input("Enter Id to Search Record : "))
    name=input("Enter Updated Name : ")
    
    con,cur=GetConnection()
    query="UPDATE STUDENT SET name=%s WHERE ID=%s"
    parameters=(name,id)
    result=cur.execute(query,parameters)

    con.commit()
    con.close()


UpdateName()
