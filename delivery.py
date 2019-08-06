import os

import utilFunc
import order


def onDelivery(option, startTime):
    while True:
        print('\n' + option + '\n1 after returning | 2 for extra stop')
        try:
            waitForUser = int(input())
            if waitForUser == 1:
                break

            elif waitForUser == 2:
                extraStop(startTime)
                continue

        except ValueError:
            print('\ninvalid input')
        else:
            print('\ninvalid input')


def extraStop(startTime):
    while True:
        print('\nmaking extra stop...\n1 to continue')
        try:
            waitForUser = int(input())
            if waitForUser == 1:

                while True:
                    print('\nname of extra stop:')

                    try:
                        extraStopName = input()

                        if extraStopName.isdigit() == False:
                            areYouSure = utilFunc.areYouSure(extraStopName + '.')

                            if areYouSure == True:
                                while True:
                                    print('\nwhat was the reason for the extra stop?')

                                    try:
                                        extraStopReason = str(input())

                                        if extraStopReason.isdigit() == False:
                                            areYouSure2 = utilFunc.areYouSure(extraStopReason + '.')

                                            if areYouSure2 == True:
                                                utilFunc.writeData("deliveryTracking", "delivery", extraStopName + "MilesTrav.txt", milesTrav('extra'))
                                                extraEndTime = utilFunc.writeData("deliveryTracking", "delivery", extraStopName + "EndTime.txt", utilFunc.now(), 'back')

                                                utilFunc.timeTook(startTime, extraEndTime, "extra stop")

                                                utilFunc.writeData("deliveryTracking", "delivery", extraStopName + "Reason.txt", "'" + extraStopReason + "'")
                                                return

                                            else:
                                                continue

                                        else:
                                            print('\ninvalid input...')
                                            continue

                                    except ValueError:
                                        print('\ninvalid input')

                        else:
                            print('\ninvalid input')
                            continue

                    except ValueError:
                        print('\ninvalid input')


        except ValueError:
            print('\ninvalid input')
        else:
            print('\ninvalid input')


def milesTrav(varPath, varWord=''):
    while True:
        print('\n' + varWord + 'miles traveled:')
        try:
            milesTravInput = float(input())
            utilFunc.writeData("deliveryTracking", "delivery", str(varPath) + 'MilesTrav.txt', milesTravInput)
            break

        except ValueError:
            print('\ninvalid input...')


def numbOfOrders():
    while True:
        print('\nnumber of orders:')
        try:
            numbOfOrders = int(input())

            if numbOfOrders >= 1:
                utilFunc.writeData("deliveryTracking", "delivery", "numbOfOrders.txt", numbOfOrders)

                return numbOfOrders

        except ValueError:
            print('\ninvalid input')


def delivery():
    os.mkdir(os.path.join("delivery"))
    startTime = utilFunc.writeData("deliveryTracking", "delivery", "deliveryStartTime.txt", utilFunc.now(), 'back')
    numberOfOrder = int(numbOfOrders())

    if numberOfOrder == 1:
        onDelivery('driving to address...', startTime)

        orderNumb = order.orderNumb()

        order.tip(orderNumb)

        milesTrav(orderNumb)

        orderEndTime = utilFunc.writeData("deliveryTracking", "delivery", str(orderNumb) + "EndTime.txt", utilFunc.now(), 'back')

        utilFunc.timeTook(startTime, orderEndTime, 'order')


    elif numberOfOrder >= 1:
        for value in range(numberOfOrder):
            onDelivery('driving to address...', startTime)

            orderNumb = order.orderNumb()

            order.tip(orderNumb)

            milesTrav(orderNumb)

            orderEndTime = utilFunc.writeData("deliveryTracking", "delivery", str(orderNumb) + "EndTime.txt", utilFunc.now(), 'back')

            utilFunc.timeTook(startTime, orderEndTime, 'order')

    onDelivery('driving back to store...', startTime)

    milesTrav('total', 'total ')

    delivEndTime = utilFunc.writeData("deliveryTracking", "delivery", "deliveryEndTime.txt", utilFunc.now(), 'back')

    utilFunc.timeTook(startTime, delivEndTime, 'delivery')

    utilFunc.writeData("deliveryTracking", "shift", "numbOfDeliveries.txt", int(utilFunc.deliveryNumb('number'))+ 1)
>>>>>>> master
