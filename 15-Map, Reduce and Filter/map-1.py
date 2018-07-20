#Map Function Without Lambda Expressions

lst=[1,2,3,4,5]


def Increment(x):
    return x+1


lst=list(map(Increment,lst))

print(lst)
