#Variable Scope

#Local Variable : Any variable which is declared inside a function
#body is called a local variable. A local variable can be
#accessed inside its function only. 

#Global Variable : Any variable which is declared outside a function
#is called a global variable. Global variables can be accessed
#anywhere in the program.


a=1     #global variable

def fun():
    print(a)
    b=1     #local variable

print(b)    #Error, b is undefined
print(a)
