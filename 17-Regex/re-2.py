import re

password=input("Enter Password : ")

invalid_pat=re.compile("[!@$%^&*()]")
digit_pat=re.compile("[0-9]")
lower_pat=re.compile("[a-z]")
upper_pat=re.compile("[A-Z]")

isvalid=True


if(digit_pat.search(password)==None):
    print("Minimum 1 Digit Required")
    isvalid=False

if(lower_pat.search(password)==None):
    print("Minimum 1 Lower case Alphabet Reuired")
    isvalid=False

if(upper_pat.search(password)==None):
    print("Minimum 1 Upper case Alphabet Required")
    isvalid=False

if(len(password)<6):
    print("Minimum 6 characters required")
    isvalid=False

if(len(password)>12):
    print("Maximum 12 characters required")
    isvalid=False

if(invalid_pat.search(password)!=None):
    print("Special Characters are not allowed")
    isvalid=False

if(isvalid==True):
    print("Password is valid")
else:
    print("Password is invalid")


