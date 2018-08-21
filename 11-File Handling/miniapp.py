#Mini App

while True:
    print("1. Save File")
    print("2. Read File")
    print("3. Copy File")
    print("4. Merge File")
    print("5. Truncate File")
    print("0. Exit File")

    choice=int(input("Enter Your Choice : "))

    if(choice==1):
        filename=input("Enter File Name : ")
        file=open(filename,"w")
        data=input("Enter Data Here\nPress Enter to Save File\n")
        file.write(data)
        file.close()
    elif(choice==2):
        filename=input("Enter File Name : ")
        file=open(filename,"r")
        data=file.read()
        print("File Data\n",data)
        file.close()
    elif(choice==3):
        filename=input("Enter Source File Name : ")
        file=open(filename,"r")
        data=file.read()
        file.close()
        filename=input("Enter Target File Name : ")
        file=open(filename,"w")
        file.write(data)
        file.close()
    elif(choice==4):
        filename=input("Enter Source File Name : ")
        file=open(filename,"r")
        data=file.read()
        file.close()
        filename=input("Enter Target File Name : ")
        file=open(filename,"a")
        file.write(data)
        file.close()
    elif(choice==5):
        filename=input("Enter File Name : ")
        file=open(filename,"w")
        file.close()        
    else:
        break
