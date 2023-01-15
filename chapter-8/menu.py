import pyinputplus as pyip
while True:
    prompt="Do you want to make your own sandwich?"
    response = pyip.inputYesNo(prompt)
    if response == 'no':
        print("Thank you ,Have a nice day!!")
        break
    else:
        price={'wheat':15, 'white':10,  'sourdough':20,'chicken':25,'Turkey':25,'Ham':25,'Tofu':25,'cheddar':15, 'Swiss':10,  'mozzarella':15,
               'mayo':5 , 'mustard':10, 'lettuce':10,  'tomato':12}
        custmer_order=[]
        total=0
        print("Ok here you go, Customise your order")
        b="What is ur bread type?\n"
        r=pyip.inputMenu(['wheat', 'white',  'sourdough'],numbered=True,prompt=b)
        custmer_order.append(r)
        
        d="protein type: \n"
        c=pyip.inputMenu(['chicken','Turkey','Ham','Tofu'],numbered=True,prompt=d)
        custmer_order.append(c)
        i=("Do you want cheese?   (Enter y for yes and n for no)\n")
        e=pyip.inputYesNo(yesVal='y', noVal='n',prompt=i)
        if e== 'y':
            f=pyip.inputMenu(['cheddar', 'Swiss',  'mozzarella'],numbered=True)
            print(f)
            custmer_order.append(f)
        
        k=("Do you want additionals? \n Mayo (Enter y for yes and n for no)\n")
        o=pyip.inputYesNo(yesVal='y', noVal='n',prompt=k)
        if o== 'y':
            print(o)
            custmer_order.append('mayo')
      
        Mustard=(" Mustard (Enter y for yes and n for no)\n")
        Mus=pyip.inputYesNo(yesVal='y', noVal='n',prompt=Mustard)
        if Mus== 'y':
            print(Mustard)
            custmer_order.append('mustard')
        else:
            print(" ")
        Lettuce=("Lettuce (Enter y for yes and n for no)\n")
        Let=pyip.inputYesNo(yesVal='y', noVal='n',prompt=Lettuce)
        if Let== 'y':
            print(Lettuce)
            custmer_order.append('lettuce')
        else:
            print(" ")
        Tomato=("Tomato  (Enter y for yes and n for no)\n")
        Tom=pyip.inputYesNo(yesVal='y', noVal='n',prompt=Tomato)
        if Tom== 'y':
            print(Tom)
            custmer_order.append( 'tomato')
        else:
            print(" ")
        
        p="How many sandwiches do you want?"
        l=pyip.inputInt(min=1,prompt=p)
        
        print("Your order \n")
        for items in custmer_order:
            total+=price[items]
        print("Your total bill is :- ",total)
        
        break

