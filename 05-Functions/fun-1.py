#Function to calculate Simple Interest


#Function Definition or Function Body
def Interest(p,r,t):	#Formal Arguments
	res=p*r*t/100
	return res;


#Function Calling
p=float(input("Enter Principal : "))
r=float(input("Enter Rate of Interest : "))
t=float(input("Enter Time : "))
res=Interest(p,r,t)	#Actual Arguments
print("Interest : " + str(res))
