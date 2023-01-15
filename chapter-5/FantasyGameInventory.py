stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print('Inventory: ')
    items = 0
    for k, v in inventory.items():
        items+= v
        print(str(v)+ ' ' + k)
    print('Total items are: ' + str(items))


displayInventory(stuff)
def addToInventory(inventory, addedItems):
        for i in range(len(addedItems)):
            if addedItems[i] in inventory:
                inventory[addedItems[i]] = inventory[addedItems[i]] + 1
            else:
                inventory.setdefault(addedItems[i],1)
        return inventory                


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)