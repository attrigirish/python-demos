from functools import reduce


lst=[1,2,3,4,5]

#Calculating Sum of all elements using reduce()
result=reduce(lambda a,b:a+b, lst)
print(result)
