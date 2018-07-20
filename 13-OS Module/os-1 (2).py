#Installation Code

import os

try:
    os.mkdir("c:\\myprog")
except:
    #File already exists, Nothing to do
    None

file=open("c:\\myprog\\log.txt","w")
file.write("Application Installed Successfully")
file.close()

