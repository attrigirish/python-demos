#Program with try, except and finally

num=input("Enter a Number : ")
try:
    num=int(num)
    print("Number =  "+str(num))
    list=[2,5]
    print(list[5])
except ValueError:
    print("An Error has occured")
else:
    print("Out of Bounds Error")
finally:
    print("End of Program")
