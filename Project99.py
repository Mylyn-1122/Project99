import os
import time
import shutil


date = time.ctime()
dateInSeconds = time.time()
print(dateInSeconds)
path = os.getcwd()

#print(path)
#print(os.path.exists(path))

if os.path.exists(path) == True :
    for (root, dirs, files) in os.walk(path):
        file=files
        #print(file)
        for x in file:
            filePath = os.path.join(path, x)
            filetime = os.stat(filePath).st_ctime
            print(filetime)
            
            #30 days in seconds is 2592000
            if filetime+2592000<dateInSeconds:
                
                if os.path.isfile(follow_symlinks=True):
                    os.remove(filePath)
                else:
                    shutil.rmtree(filePath)


            #print(filePath)
else : 
    print("not found")
        

        

