#Resetting Cursor Position in the file

file=open("myfile.txt","r")
file.read(10)
file.seek(-5,1)
cursor=file.tell()
print("Cursor Position Before Read : " + str(cursor))
file.close()
