#UnInstallation Code

import os


def RemoveFiles(path):   #Function to remove all directories recursively
    files=os.listdir(path)
    for file in files:
        try:
            os.remove(path+"\\"+file)
        except:
            #file is a directory
            RemoveFiles(path+"\\"+file)
    os.rmdir(path)            
        

try:
    path="c:\\myprog"
    RemoveFiles(path)
except:
    #Directory doesn't exist nothing to delete
    None



