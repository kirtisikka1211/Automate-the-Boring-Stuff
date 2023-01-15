tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
def printable(n):
    colWidths = [0] * len(n)
    for x in range(len(n)):
        for y in n[x]:
            if  colWidths[x]<len(y):
                colWidths[x]=len(y)
    for y in range(len(n[0])):
        for x in range(len(n)):#rotate 
            print(n[x][y].rjust(colWidths[x]),end=' ')
        print()
        
printable(tableData)
            
    
    
