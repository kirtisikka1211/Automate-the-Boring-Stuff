import re

def PasswordDetection(x):
    length = re.compile(r'\w{8,}') 
    lower=re.compile(r'[a-z]')
    upper=re.compile(r'[A-Z]')
    num=re.compile(r'[0-9]')
    if length.search is None:
        print("The password is invalid")
    elif lower.search(x) is None:
        print("The password is invalid")
    elif upper.search(x) is None:
        print("The password is invalid")
    elif num.search(x) is None:
        print("The password is invalid")
    else:
        print("The password is strong")
   
x=input("Enter your passwordd:- ")
PasswordDetection(x)
