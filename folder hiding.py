import os
import shutil

realf=input('Enter the dir of folder to protect')
newf=input('Enter folder name to create')
pasw=input('Enter the password')

todir='C:/Users/crezy j/Desktop'
todir=os.path.join(todir,newf) 
os.mkdir(todir)
for i in pasw:
    for j in range(1,11):
        path=os.path.join(todir,str(j))
        try:
            os.mkdir(path)
        except:
            print('complete')
        for k in range(1,11):
            path2=os.path.join(path,str(k))
            try:
                os.mkdir(path2)
            except:
                print('incomplete')

    todir=todir+'/'+i

try:
    shutil.move(realf,todir)
except:
    print()
                
                
 
