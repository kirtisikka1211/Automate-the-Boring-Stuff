spam= ['apples', 'bananas', 'tofu', 'cats']
def list_string(list):
    newlist=''
    last=list[len(list)-1]
    leng=int(len(list)-1)
    new=list[0:leng]
    for stri in new:
        newlist=newlist+stri+' , '
    print(newlist+ 'and '+last)        
    
list_string(spam)