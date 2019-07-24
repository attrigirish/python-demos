import re
card=input("Enter Card Number : ")
pattern=re.compile('^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}$')

if(pattern.match(card)):
	print("Valid Card")
else:
	print("Invalid Card Number")
