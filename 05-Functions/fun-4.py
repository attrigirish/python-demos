#Variable Length Arguments Functions

def Sum(*lst):
        s=0
        for val in lst:
                s=s+val
        return s

print(Sum(11))
print(Sum(11,22))
print(Sum(11,22,33,44,55))
