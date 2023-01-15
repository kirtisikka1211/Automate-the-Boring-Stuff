import re
def white( c):
    le=len(c)
    list=''
    for i in range (le):
        # print(c[i])
        if c[i] != ' ' :
            # list.append(c[i])
            list+=c[i]
    print(list)
    
    
            
    
    # if c != '':
    #     strip = re.compile(c)
    #     newstring = strip.sub('', string)
    #     return newstring
    # else:
    #     strip = re.compile('^\s*')
    #     newstring = strip.sub('', string)
    #     strip= re.compile('\s*$')
    #     newstring = strip.sub('', newstring)
    #     return newstring
# test=input("enter the text")

ch=input("Enter the string")
newstring = white(ch)
print(newstring)