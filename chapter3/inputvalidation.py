def collatz(number):
    
         if number%2==0:
             c=number//2
             print(c)                
             
         else:
             d=3*number +1
             print(d)
             return d
while True:
    try:

        num=int(input("Enter the number: "))
        c= collatz(num)

        if c==1:
            break
    except:
        print("Enter an integer")
   
   
        
        
