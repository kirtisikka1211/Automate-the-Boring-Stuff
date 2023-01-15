
def collatz(number):
    if number%2==0:
        c=number//2
        print(c)
        return c
    else:
        d=3*number +1
        print(d)
        return d
    
        
num=int(input("enter your number:  "))
x=collatz(num)
# print(collatz(x))