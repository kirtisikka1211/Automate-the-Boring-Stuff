import re

def PasswordDetection(x):
    length = re.compile(r'\w{8,}')
    upper=re.compile(r'[A-Z]')
    lower=re.compile(r'[a-z]')
    num=re.compile(r'[0-9]')
    if length.search(x) == None:
        print("The password is invalid")
    elif lower.search(x) == None:
        print("The password is invalid")
    elif upper.search(x) == None:
        print("The password is invalid")
    elif num.search(x) == None:
        print("The password is invalid")
    else:
        print("The password is strong")
   
x=input("Enter your passwordd:- ")
PasswordDetection(x)
