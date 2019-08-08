import os

import utilFunc
import order


def onDelivery(option, startTime):
    os.mknod(os.path.join('delivery', 'onDelivery'))
    while True:
        print('\n' + option + '\n1 after returning | 2 for extra stop')
        try:
            waitForUser = int(input())
            if waitForUser == 1:
                os.remove(os.path.join('delivery', 'onDelivery'))
                break

            elif waitForUser == 2:
                extraStop(startTime)
                os.remove(os.path.join('delivery', 'onDelivery'))
                continue

        except ValueError:
            print('\ninvalid input')
        else:
            print('\ninvalid input')


def extraStop(startTime):
    os.mknod(os.path.join('delivery', 'extraStop'))
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
                                                utilFunc.writeData("delivery", extraStopName + "Reason.txt", extraStopReason)
                                                utilFunc.writeData("delivery", extraStopName + "MilesTrav.txt", milesTrav('extra'))
                                                extraEndTime = utilFunc.writeData("delivery", extraStopName + "EndTime.txt", utilFunc.now(), 'back')
                                                utilFunc.timeTook(startTime, extraEndTime, "extra stop")
                                                os.remove(os.path.join('delivery', 'extraStop'))
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
            utilFunc.writeData("delivery", str(varPath) + 'MilesTrav.txt', milesTravInput)
            break

        except ValueError:
            print('\ninvalid input...')


def numbOfOrders():
    while True:
        print('\nnumber of orders:')
        try:
            numbOfOrders = int(input())

            if numbOfOrders >= 1:
                utilFunc.writeData('delivery', 'numbOfOrders.txt', numbOfOrders)

                return numbOfOrders

        except ValueError:
            print('\ninvalid input')


def delivery():
    os.mkdir(os.path.join('delivery'))
    startTime = utilFunc.writeData('delivery', 'deliveryStartTime.txt', utilFunc.now(), 'back')
    numberOfOrder = int(numbOfOrders())

    if numberOfOrder == 1:
        onDelivery('driving to address...', startTime)

        orderNumb = order.orderNumb()

        order.tip(orderNumb)

        milesTrav(orderNumb)

        orderEndTime = utilFunc.writeData('delivery', str(orderNumb) + 'EndTime.txt', utilFunc.now(), 'back')

        utilFunc.timeTook(startTime, orderEndTime, 'order')


    elif numberOfOrder >= 1:
        for value in range(numberOfOrder):
            onDelivery('driving to address...', startTime)

            orderNumb = order.orderNumb()

            order.tip(orderNumb)

            milesTrav(orderNumb)

            orderEndTime = utilFunc.writeData('delivery', str(orderNumb) + 'EndTime.txt', utilFunc.now(), 'back')

            utilFunc.timeTook(startTime, orderEndTime, 'order')

    onDelivery('driving back to store...', startTime)

    milesTrav('total', 'total ')

    delivEndTime = utilFunc.writeData('delivery', 'deliveryEndTime.txt', utilFunc.now(), 'back')

    utilFunc.timeTook(startTime, delivEndTime, 'delivery')

    utilFunc.writeData('shift', 'numbOfDeliveries.txt', int(utilFunc.deliveryNumb('number'))+ 1)