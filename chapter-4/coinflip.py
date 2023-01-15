import random
numberOfStreaks = 0
testlist=[]
a=[]
b=[]
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
        if random.randint(0,1)==0:
            testlist.append('H')
        else:
            testlist.append('T')
leg=len(testlist)
for i in range(leg-1):
    if testlist[i]== testlist[i+1]:
        num+=1
    else:
        a.append(num)
        b.append(testlist[i])
        num=1
a.append(num)
b.append(testlist[i+1])
numberOfStreaks= a.count(6)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))