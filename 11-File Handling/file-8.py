#Copying Data of One file to another

try:
    source=input("Enter Source File Name : ")
    file1=open(source,"r")

    dest=input("Enter Destination File Name : ")
    file2=open(dest,"w")

    data=file1.read()
    file2.write(data)

    file1.close()
    file2.close()
except:
    print("Source File doesn't Exist")
