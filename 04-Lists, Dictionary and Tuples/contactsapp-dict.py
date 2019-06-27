contacts=[]
while(True):
	print("1. Add Contact")
	print("2. Display Contacts")
	print("0. Exit")

	choice=int(input("Enter Choice : "))

	if(choice==1):
		contact={}
		contact['name']=input("Enter Name : ")
		contact['email']=input("Enter Email : ")
		contact['phone']=int(input("Enter Phone : "))
		contacts.append(contact)
	elif(choice==2):
		for contact in contacts:
			print("Name : ", contact['name'])
			print("Email : ", contact['email'])
			print("Phone : ", contact['phone'])
	elif(choice==3):
		name=input("Enter Name : ")
		isfound=False
		for contact in contacts:
			if(contact['name']==name):
				print("Email : ", contact['email'])
				print("Phone : ", contact['phone'])
				isfound=True

		if(isfound==False):
			print("Contact Not Found")

	elif(choice==4):
		name=input("Enter Name : ")
		isfound=False
		for contact in contacts:
			if(contact['name']==name):
				contacts.remove(contact)
				isfound=True

		if(isfound==False):
			print("Contact Not Found")

	elif(choice==7):
		contacts.sort(key=lambda item:item['phone'])
		for contact in contacts:
			print("Name : ", contact['name'])
			print("Email : ", contact['email'])
			print("Phone : ", contact['phone'])

	elif(choice==0):
		exit(0)
