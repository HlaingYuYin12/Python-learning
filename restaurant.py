class RestaurantTable:
    menus ={
        'pizza': 4500,
        'cola': 630,
        'apple juice':2000,
        'hamburger': 3400
    }
    
    def __init__(self):
        self.total = 0
        self.orders=[]
    
    def addOrder(self, order):
        self.orders.append(order)
        self.total += self.menus[order]

    def printBill(self):
        for order in self.orders :
            print(f'{order} : {self.menus[order]}')

        print(f'total price is {self.total}')


def startProgram():
    table = RestaurantTable()

    while True:
        order= input('Order : ')
        table.addOrder(order)

        another = input('Order again y/n : ')
        if another == 'y' :
            continue
        else :
            table.printBill()
            break

startProgram()
