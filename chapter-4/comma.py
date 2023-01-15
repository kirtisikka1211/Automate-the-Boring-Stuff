spam= ['apples', 'bananas', 'tofu', 'cats']
def list_string(list):
    newlist=''
    last=list[-1]
    for i in range(len(list)-1):
        newlist=newlist+list[i]+' , '
    print(newlist+ 'and '+last)        
    
list_string(spam)