import re
def white(string, c):
    if c != '':
    #     strip = re.compile(c)
    #     newstring = strip.sub('', string)
    #     return newstring
    # else:
    #     strip = re.compile('^\s*')
    #     newstring = strip.sub('', string)
    #     strip= re.compile('\s*$')
    #     newstring = strip.sub('', newstring)
    #     return newstring
test=input("enter the text")
ch="Enter thenj"
newstring = white(test, ch)
print(newstring)