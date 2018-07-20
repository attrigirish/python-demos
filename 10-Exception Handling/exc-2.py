#Program with Exception Handling

num=input("Enter a Number : ")

try:
    num=int(num)
    print("Number =  "+str(num))
except ValueError:
    print("An Error has occured")
print("End of Program")
