contacts=[]

while(True):
	print("1. Add Contact")
	print("2. Delete Contact")
	print("3. Search Contact")
	print("4. Update Contact")
	print("5. Sort (A-Z)")
	print("6. Sort (Z-A)")
	print("7. Clear List")
	print("8. Count Contacts")
	print("0. Exit")


	choice=int(input("Enter Choice : "))

	if(choice==1):
		contact=input("Enter Contact : ")
		contacts.append(contact)
	elif(choice==2):
		contact=input("Enter Contact : ")
		try:
			contacts.remove(contact)
		except:
			print("Contact Not Found")
	elif(choice==3):
		contact=input("Enter Contact : ")
		try:
			pos=contacts.index(contact)
			print("Contact found at ", (pos+1))
		except:
			print("Contact Not Found")
	elif(choice==4):
		contact=input("Enter Contact : ")
		try:
			pos=contacts.index(contact)
			newcontact=input("Enter Updated Value : ")
			contacts[pos]=newcontact
		except:
			print("Contact Not Found")
	elif(choice==5):
		contacts.sort()
		print("Contacts in Ascending Order")
		for contact in contacts:
			print(contact)		
	elif(choice==6):
		contacts.sort(reverse=True)
		print("Contacts in Descending Order")
		for contact in contacts:
			print(contact)
	elif(choice==7):
		contacts.clear()
		print("All contacts removed")
	elif(choice==8):
		contact=input("Enter Contact : ")
		count=contacts.count(contact)
		print("Found " count, "occurences")
	else:
		exit(0)

