#Writing Multiple Lines in a file

f=open("file1.txt","w")
list=[]
for i in range(10):
    list.append(input("Enter a Number : "))

f.writelines(list)
f.close()
