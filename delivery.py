import order
import main


def endOrder():
    while True:
        print('driving to address...\n1 to continue after returning to vehicle\n2 for extra stop')
        try:
            waitForUser = int(input())

            if waitForUser == 1:
                return (order.order())

        except ValueError:
            print('invalid input')

        else:
            print('invalid input')


def numbOfOrders():
    while True:
        print('number of orders?')
        try:
            numbOfOrders = int(input())
            if numbOfOrders == 1:
                return([numbOfOrders, endOrder()])

            elif numbOfOrders > 1:
                return([numbOfOrders, [endOrder() for value in range(numbOfOrders)]])

        except ValueError:
            print('invalid input')


def delivery():
    orders = numbOfOrders()

    while True:
        print('returning to store...\nupon arival, 1 to continue\n2 for extra stop')
        try:
            waitForUser = int(input())
            if waitForUser == 1:
                return([orders])

        except ValueError:
            print('invalid input')


def createDelivery():
    startTime = main.time()

    with open('dlvNumb.txt', 'r+') as dlvNumb:
        dlvNum = int(dlvNumb.read())
        dlv = delivery()

        with open(main.date() + '.py', 'a+') as today:
            content = today.read()
            today.seek(len(content))
            today.write('\ndlv' + str(dlvNum) + ' = ' + str([startTime, dlv, order.milesTrav('Total '), main.time()]))

        dlvNum = str(dlvNum + 1)
        dlvNumb.seek(0)
        dlvNumb.write(dlvNum)
