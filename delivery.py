import os
import order
import main
import utilFunc


def endOrder(startTime):
    while True:
        print('\ndriving to address...\n1 after returning to vehicle')
        try:
            waitForUser = int(input())

            if waitForUser == 1:
                ord = order.order()
                utilFunc.timeTook(startTime, ord[1][2], 'order')
                return ord

        except ValueError:
            print('\ninvalid input')

        else:
            print('\ninvalid input')


def numbOfOrders(startTime):
    while True:
        print('\nnumber of orders?')
        try:
            numbOfOrders = int(input())

            if numbOfOrders == 1:
                return [numbOfOrders, endOrder(startTime)]

            elif numbOfOrders > 1:
                return [numbOfOrders, [endOrder(startTime) for value in range(numbOfOrders)]]

        except ValueError:
            print('\ninvalid input')


def delivery(startTime):
    orders = numbOfOrders(startTime)
    
    while True:
        print('\nreturning to store...\nupon arival, 1 to continue')
        try:
            waitForUser = int(input())

            if waitForUser == 1:
                return orders

        except ValueError:
            print('\ninvalid input')


def createDelivery():
    startTime = main.now()
    dlv = delivery(startTime)
    totalMilesTrav = utilFunc.milesTrav('total ')
    endTime = main.now()
    
    utilFunc.timeTook(startTime, endTime, 'delivery')

    with open(os.path.join("dlvNumb.txt"), 'r+') as dlvNumb:
        dlvNum = int(dlvNumb.read())
        

        with open(os.path.join("shifts", str(main.now().date()) + '.py'), 'a+') as today:
            content = today.read()
            today.seek(len(content))
            today.write('\ndlv' + str(dlvNum) + ' = ' + str([startTime, dlv, totalMilesTrav, endTime]))

        dlvNum = str(dlvNum + 1)
        dlvNumb.seek(0)
        dlvNumb.write(dlvNum)
