#Programs
#Write a function to find the sum of all elements of an array of 5 elements.

def sum(a):
    res=0
    for i in a:
        res=res+i
    return res

a=[1,2,3,5,6]
s=sum(a)
print('output'+str(s))
