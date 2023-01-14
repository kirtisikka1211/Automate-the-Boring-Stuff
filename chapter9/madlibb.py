from pathlib import Path
import re
file1=open("/Users/kirtisikka/Documents/python/chapter9/mad.txt",'w')
file1.write("Test data \nThe  ADJECTIVE  panda walked to the NOUN and then VERB. A nearby NOUN was unaffected  by these events.")
file1.close()
file1=open("/Users/kirtisikka/Documents/python/chapter9/mad.txt",'r')
b=file1.read()
file1.close()
matching=re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
x= matching.findall(b)

for items in x:
    if items =="ADJECTIVE":
        input1=input("Enter an adjective:")
        replace=b.replace(items,input1,1)
        b=replace
    if items =="NOUN":
        input2=input("Enter a noun:  ")
        replace2=b.replace(items,input2,1)
        b=replace2
    if items =="VERB":
        input3=input("Enter a verb: ")
        replace3=b.replace(items,input3,1)
        b=replace3  
    if items =="ADVERB":
        input4=input("Enter an adverb: ")
        replace4=b.replace(items,input4,1)
        b=replace4
    
               

file2=open("/Users/kirtisikka/Documents/python/chapter9/new.txt",'w')
file2.write(b)
file2.close()   
print(b)  
   

    
    
    
    



    
    