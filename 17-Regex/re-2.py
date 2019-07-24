import re

password=input("Enter Password : ")

pass_pat=re.compile("^[0-9A-Za-z#_]{6,12}$")
digit_pat=re.compile("[0-9]")
lower_pat=re.compile("[a-z]")
upper_pat=re.compile("[A-Z]")


if(pass_pat.search(password)!=None and digit_pat.search(password)!=None and lower_pat.search(password)!=None and upper_pat.search(password)!=None):
    print("Password Valid")
else:
    if(digit_pat.search(password)==None):
       print("Minimum 1 Digit Required")
    if(lower_pat.search(password)==None):
       print("Minimum 1 Lower case Alphabet Reuired")
    if(upper_pat.search(password)==None):
       print("Minimum 1 Upper case Alphabet Required")
    if(len(password)<6):
       print("Minimum 6 characters required")
    if(len(password)>12):
       print("Maximum 12 characters required")
