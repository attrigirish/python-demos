import pickle

while(True):
    print("-"*50)
    print("1. Add Student")
    print("2. Search Student")
    print("3. Display Students")
    print("4. Delete Student")
    print("5. Update Student")
    print("-"*50)

    choice=int(input("Enter Choice : "))

    if(choice==1):
        f=open("file.txt","ab")
        person={}
        person['id']=int(input("Enter ID : "))
        person['name']=input("Enter Name : ")
        person['course']=input("Enter Course : ")
        person['fees']=int(input("Enter Fees : "))
        pickle.dump(person,f)
        f.close()
    elif(choice==2):
        id=int(input("Enter ID to Search : "))
        f=open("file.txt","rb")
        while(True):
            try:
                person=pickle.load(f)
                if(person['id']==id):
                    print("Name : ", person['name'])
                    print("Course : ", person['course'])
                    print("Fees : ", person['fees'])
            except:
                break        
        f.close()
    elif(choice==3):
        f=open("file.txt","rb")
        while(True):
            try:
                person=pickle.load(f)
                print("Id : ", person['id'])
                print("Name : ", person['name'])
                print("Course : ", person['course'])
                print("Fees : ", person['fees'])
            except:
                break        
        f.close()
    elif(choice==4):
        id=int(input("Enter ID to Search : "))
        f=open("file.txt","rb")
        data=[]
        while(True):
            try:
                person=pickle.load(f)
                if(person['id']!=id):
                    data.append(person)
            except:
                break        
        f.close()
        f=open("file.txt","wb")
        for person in data:
            pickle.dump(person,f)
        f.close()
    elif(choice==5):
        id=int(input("Enter ID to Search : "))
        f=open("file.txt","rb")
        data=[]
        while(True):
            try:
                person=pickle.load(f)
                if(person['id']==id):
                    person['name']=input("Enter Name : ")
                    person['course']=input("Enter Course : ")
                    person['fees']=int(input("Enter Fees : "))
                data.append(person)
            except:
                break        
        f.close()
        f=open("file.txt","wb")
        for person in data:
            pickle.dump(person,f)
        f.close()
    else:
        print("Enter Invalid Choice")

