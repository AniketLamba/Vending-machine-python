# creating a class for the item in vending machine
class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def updateStock(self, stock):
        self.stock = stock

    def buyFromStock(self):
        if self.stock == 0: # if there is no items available
            # raise not item exception
            pass
        self.stock -= 1 # else stock of item decreases by 1

# create a class for the vending machine itself
class VendingMachine:

    def __init__(self):
        self.amount = 0
        self.items = [] # all items contained in this list right here

    def addItem(self, item):
        self.items.append(item) # method to add item to vending machine

    # method for showing items in the vending machine
    def showItems(self):
        print('\nitems available \n***************')

        for item in self.items: # for each item in this vending machine
            if item.stock == 0: # if the stock of this item is 0
                self.items.remove(item) # remove this item from being displayed
        for item in self.items:
            print(item.name + ": " "Rate-", item.price) # otherwise print this item and show its price

        print('***************\n')

    def addCash(self, money):
        self.amount = self.amount + money # add money

    def buyItem(self, item): # if the amount you put is less than the price
        if self.amount < item.price:
            print('You can\'t buy this item. Insert more coins.') # then obvs you cant buy this item
        else:
            self.amount -= item.price # subtract item price from available cash
            item.buyFromStock() # call this function to decrease the item inventory by 1
            # (what if we buy more than one?)
            print('You got ' +item.name)
            print('Cash remaining: ' + str(self.amount))

    def containsItem(self, wanted):
        ret = False
        for item in self.items:
            if item.name == wanted:
                ret = True
                break
        return ret

    def getItem(self, wanted):
        ret = None
        for item in self.items:
            if item.name == wanted:
                ret = item
                break
        return ret

    def insertAmountForItem(self, item):
        price = item.price
        while self.amount < price:
                self.amount = self.amount + float(input('insert ' + str(price - self.amount) + ': '))

    def checkRefund(self):
        if self.amount > 0:
            print(str(self.amount) + " refunded.")
            self.amount = 0

        print('Thank you, have a nice day!\n')


def vend():

    machine = VendingMachine()
    item1 = Item('choc',  1.5,  2)
    item2 = Item('pop', 1.75,  1)
    item3 = Item('chips',  2.0,  3)
    item4 = Item('gum',  0.50, 1)
    item5 = Item('mints',0.75,  3)
    item6 = Item('milkshake',1.2, 5 )
    machine.addItem(item1)
    machine.addItem(item2)
    machine.addItem(item3)
    machine.addItem(item4)
    machine.addItem(item5)
    machine.addItem(item6)

    print('Welcome to the vending machine!\n***************')

    continueToBuy = True
    while continueToBuy == True:
        machine.showItems()
        selected = input('select item: ')
        if machine.containsItem(selected):
            item = machine.getItem(selected)

            machine.insertAmountForItem(item)
            machine.buyItem(item)

            a = input('buy something else? (y/n): ')
            if a == 'n':
                continueToBuy = False
                machine.checkRefund()
            else:
                continue

        else:
            print('Item not available. Select another item.')
            continue
vend()
