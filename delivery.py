import re
import order
import main


def endOrder():
    while True:
        print('driving to address...\n1 to continue after returning to vehicle\n2 for extra stop')
        try:
            waitForUser = int(input())

            if waitForUser == 1:
                return (order.order())
#                endTime = ord[1][2]
#                eTime = [int(endTime[0:2]), int(endTime[3:5]), int(endTime[6:8]), int(endTime[9:15])]

#                hour = eTime[0] - sTime[0]
#                min = eTime[1] - sTime[1]
#                sec = eTime[2] - sTime[2]
#                mSec = eTime[3] - sTime[3]

#                if mSec >= 500000:
#                    sec + 1
#                    print('it took you ' + str(hour) + 'hours' + str(min) + 'minutes' + str(sec) + 'seconds' + ' to complete the order')

#                if mSec < 500000:
#                    print('it took you ' + str(hour) + 'hours' + str(min) + 'minutes' + str(sec) + 'seconds' + ' to complete the order')
#                    return(ord)

        except ValueError:
            print('invalid input')

        else:
            print('invalid input')


def numbOfOrders():
#    sTime = sTime
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
#    sTime = sTime
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
#    sTime = [int(startTime[0:1]), int(startTime[3:4]), int(startTime[6:7]), int(startTime[9:14])]

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
