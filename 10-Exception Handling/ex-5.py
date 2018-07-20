#Runtime Errors/Exceptions
count=0
while True:
    try:
        if(count==6):
            print("You have reached maximum number of attempts")
            break
        a=input("Enter a Number : ")
        a=int(a)
        print("A = " + str(a))
        break
    except:
        count=count+1
        print("Something went wrong, Please Try Again!")


        
