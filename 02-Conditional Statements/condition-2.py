#Write a program to calculate Net salary of an employee on the basis of following criterian:
#     Basic Salary            HRA         DA
#     <1500                   10%         90%
#     Else                    500         98%

a=int(input("basic salary = "))
if(a<1500):
      hra=10*a/100
      da=90*a/100
else:
      hra=500
      da=98*a/100
gross = a+hra+da
print("gross=" + str(gross))      
      
       
