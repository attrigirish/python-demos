#Sum Program

import sys

parameters=sys.argv

#Skip the First Parameters as it defines program name only

len=parameters.__len__()

if(len<3):
    print("Invalid Number of Arguments")
    print("Correct Syntax is : prg val1 val2")
else:
    first=float(parameters[1])
    second=float(parameters[2])
    result=first+second
    print(result)
