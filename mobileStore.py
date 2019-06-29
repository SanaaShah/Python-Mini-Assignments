
item = {'Samsung Galaxy S10': 5, 'Samsung Galaxy S10+': 5, 'Samsung Galaxy Note 9': 5, 'Samsung Galaxy A9': 5, 'Samsung Galaxy J7': 5, 'Samsung Galaxy S9': 5, 'Samsung Galaxy S9+': 5, 'Samsung Galaxy Note 8': 5, 'Samsung Galaxy A30': 5, 'Samsung Galaxy S8': 5}
itemsList = ['Samsung Galaxy S10', 'Samsung Galaxy S10+', 'Samsung Galaxy Note 9', 'Samsung Galaxy A9', 'Samsung Galaxy J7', 'Samsung Galaxy S9', 'Samsung Galaxy S9+', 'Samsung Galaxy Note 8', 'Samsung Galaxy A30', 'Samsung Galaxy S8']

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('~~~~~~~~~~~~~  WELCOME TO INVENTORY MANAGEMENT PROGRAM ~~~~~~~~~~~~~~~~~~~')
print('~~~~~~~~~~~~~~~~~~~  OF SAMSUNG GALAXY MOBILE STORE  ~~~~~~~~~~~~~~~~~~~~~')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def printItems():

    for value, key in item.items():
        if key >= 1:
            print(value, "    Quantity:   ", key)

def sellItem():
    print('Phones in stock: ')
    printItems()
    buy = input('Enter the item you want to sell: ')
    quantity = int(input('Enter the quantity of the item that you want to sell: '))
    reqKey = 0
    count = 0
    for value, key in item.items():
        if value.lower() == buy.lower():
            reqKey = key
            break
        count = count + 1

    if reqKey < 1:
        print('Sorry that item is not avalaible.')
    else:

        newKey = reqKey - quantity

    buy = list(item)[count]
    item[buy] = newKey
    print('You have sold ', buy, ' QTY. ', quantity)

def updateStock():

    print('You can buy the following items for your store: ')
    for items in itemsList:
        print(items)
    val = input('Enter the item you want to buy: ')
    q = int(input('Enter the quantity: '))

    for i in itemsList:
        k = 0
        n = 0
        for n in range(10):
            if i.lower() == val.lower():
                count = 0
                for value, key in item.items():
                    if str(value).lower() == val.lower():
                        val = list(item)[count]
                        k = item.get(val)
                        item[val] = k + q
                        return
                    count = count + 1



    index = 0
    for j in itemsList:
        if val.lower() == j.lower():
            break
        else:
            index = index + 1
    new_value = itemsList[index]
    item[new_value] = q

n = 0

while(n == 0):

    inp = int(input("\n Press  1  to view available items.\n Press  2  to sell any item.\n Press  3  if you want to update stock.\n Press  0  to exit.\n"))
    if inp == 1:
        printItems()
    elif inp == 0:
        n = 1
    elif inp == 2:
        sellItem()
    elif inp == 3:
        updateStock()
    else:
        print('Please enter a valid number.')
