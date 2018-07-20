#Sum Program

import sys

parameters=sys.argv

#Skip the First Parameters as it defines program name only

len=parameters.__len__()

if(len<4):
    print("Invalid Number of Arguments")
    print("Correct Syntax is : prg val1 val2")
else:
    command=parameters[1]
    first=float(parameters[2])
    second=float(parameters[3])
    if(command=="sum"):
        result=first+second
    elif(command=="sub"):
        result=first-second
    elif(command=="mul"):
        result=first*second
    elif(command=="div"):
        result=first/second
    else:
        print("Invalid Command Parameter")
        exit()
    print(result)
