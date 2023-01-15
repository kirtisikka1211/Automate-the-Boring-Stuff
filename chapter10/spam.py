import shutil
import os
a= input("Enter prefix of file: ")
folder= input("Enter path where files are located: ")
# print(folder)
type= input("Enter file type: ")
count=[]


for file in os.listdir(folder):
    if file.endswith(type):
        print(file)
         
        
        d=file.replace(type,'')
        count.append(d)
count.sort()  
print(count)
lenc= len(count)
# a is the input of prefix
nums=[]
for item in range(1,lenc+1):
    filename= f"{a}{item:03}"
    last=count[-1]
    if filename in count:
        continue
    else:
        shutil.move(f"{folder}/{last}{type}", f"{folder}/{filename}{type}")
        count.pop()

        
    