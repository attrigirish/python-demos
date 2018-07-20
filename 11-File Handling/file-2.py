#Reading data from a file

file=open("myfile.txt","r")
data=file.read()
print("File Data : " + data)
file.close()
