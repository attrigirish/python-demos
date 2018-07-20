#Reading data from a file

file=open("myfile.txt","r")

cursor=file.tell()
print("Cursor Position Before Read : " + str(cursor))
data=file.read(2)

cursor=file.tell()
print("Cursor Position After Read : " + str(cursor))

file.close()
