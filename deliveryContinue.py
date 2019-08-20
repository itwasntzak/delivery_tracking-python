#todo still needs to be refactored


import os, shutil, datetime
import util_func, delivery, order


def deliveryContinue():
    if os.path.exists(os.path.join('delivery')) == True:
        if os.path.exists(os.path.join('delivery', 'deliveryStartTime.txt')) == False:
            shutil.rmtree(os.path.join('delivery'))

        else:
            if os.path.exists(os.path.join('delivery', 'onDelivery')) == True and os.path.exists(os.path.join('delivery', 'extraStop')) == True:
                print('name of the extra stop left off on?')
                extraStopName = str(input())

                if os.path.exists(os.path.join('delivery', extraStopName + 'Reason.txt')) == False:
                    while True:
                        print('\nwhat was the reason for the extra stop?')

                        try:
                            extraStopReason = str(input())

                            if extraStopReason.isdigit() == False:
                                areYouSure2 = util_func.areYouSure(extraStopReason + '.')

                                if areYouSure2 == True:
                                    util_func.writeData("delivery", extraStopName + "Reason.txt", extraStopReason)
                                    util_func.writeData("delivery", extraStopName + "MilesTrav.txt", milesTrav('extra'))
                                    extraEndTime = util_func.writeData("delivery", extraStopName + "EndTime.txt", util_func.now(), 'back')
                                    util_func.timeTook(datetime.datetime.strptime(util_func.readData('', 'delivery', 'deliveryStartTime.txt'), '%Y-%m-%d %H:%M:%S.%f'), extraEndTime, "extra stop")
                                    os.remove(os.path.join('delivery', 'extraStop'))

                                else:


                elif os.path.exists(os.path.join('delivery', extraStopName + 'Reason.txt')) == True and os.path.exists(os.path.join('delivery', extraStopName + 'MilesTrav.txt')) == False:
                    util_func.writeData("delivery", extraStopName + "MilesTrav.txt", milesTrav('extra'))
                    extraEndTime = util_func.writeData("delivery", extraStopName + "EndTime.txt", util_func.now(), 'back')
                    util_func.timeTook(datetime.datetime.strptime(util_func.readData('', 'delivery', 'deliveryStartTime.txt'), '%Y-%m-%d %H:%M:%S.%f'), extraEndTime, "extra stop")
                    os.remove(os.path.join('delivery', 'extraStop'))

                else:
                    print('this extra stop does not yet exist,\nwould you like to create it?\n1 for yes | 2 for no')


        elif os.path.exists(os.path.join('delivery',


        elif os.path.exists(os.path.join('delivery', 'numbOfOrders.txt')) == True and os.path.exists(os.path.join('delivery', 'onDelivery')) == False or os.path.exists(os.path.join('delivery', 'onDelivery')) == True:

            with open(os.path.join('delivery', 'numbOfOrders.txt'), 'r') as file:
                numberOfOrder = int(file.read())

            if numberOfOrder == 1:
                onDelivery('driving to address...', datetime.datetime.strptime(util_func.readData('', 'delivery', 'deliveryStartTime.txt'), '%Y-%m-%d %H:%M:%S.%f'))

                orderNumb = order.orderNumb()

                order.tip(orderNumb)

                milesTrav(orderNumb)

                orderEndTime = util_func.writeData('delivery', str(orderNumb) + 'EndTime.txt', util_func.now(), 'back')

                util_func.timeTook(datetime.datetime.strptime(util_func.readData('', 'delivery', 'deliveryStartTime.txt'), '%Y-%m-%d %H:%M:%S.%f'), orderEndTime, 'order')

            elif numberOfOrder >= 1:
                for value in range(numberOfOrder):
                    onDelivery('driving to address...', datetime.datetime.strptime(util_func.readData('', 'delivery', 'deliveryStartTime.txt'), '%Y-%m-%d %H:%M:%S.%f'))

                    orderNumb = order.orderNumb()

                    order.tip(orderNumb)

                    milesTrav(orderNumb)

                    orderEndTime = util_func.writeData('delivery', str(orderNumb) + 'EndTime.txt', util_func.now(), 'back')

                    util_func.timeTook(datetime.datetime.strptime(util_func.readData('', 'delivery', 'deliveryStartTime.txt'), '%Y-%m-%d %H:%M:%S.%f'), orderEndTime, 'order')

            onDelivery('driving back to store...', datetime.datetime.strptime(util_func.readData('', 'delivery', 'deliveryStartTime.txt'), '%Y-%m-%d %H:%M:%S.%f'))

            milesTrav('total', 'total ')

            delivEndTime = util_func.writeData('delivery', 'deliveryEndTime.txt', util_func.now(), 'back')

            util_func.timeTook(datetime.datetime.strptime(util_func.readData('', 'delivery', 'deliveryStartTime.txt'), '%Y-%m-%d %H:%M:%S.%f'), delivEndTime, 'delivery')

            util_func.writeData('shift', 'numbOfDeliveries.txt', int(util_func.deliveryNumb('number')) + 1)



        elif os.path.exists(os.path.join('delivery', 'deliveryStartTime.txt')) == True and os.path.exists(os.path.join('delivery', 'numbOfOrders.txt')) == False:
            numberOfOrder = int(numbOfOrders())

            if numberOfOrder == 1:
                onDelivery('driving to address...', datetime.datetime.strptime(util_func.readData('', 'delivery', 'deliveryStartTime.txt'), '%Y-%m-%d %H:%M:%S.%f'))

                orderNumb = order.orderNumb()

                order.tip(orderNumb)

                milesTrav(orderNumb)

                orderEndTime = util_func.writeData('delivery', str(orderNumb) + 'EndTime.txt', util_func.now(), 'back')

                util_func.timeTook(datetime.datetime.strptime(util_func.readData('', 'delivery', 'deliveryStartTime.txt'), '%Y-%m-%d %H:%M:%S.%f'), orderEndTime, 'order')

            elif numberOfOrder >= 1:
                for value in range(numberOfOrder):
                    onDelivery('driving to address...', datetime.datetime.strptime(util_func.readData('', 'delivery', 'deliveryStartTime.txt'), '%Y-%m-%d %H:%M:%S.%f'))

                    orderNumb = order.orderNumb()

                    order.tip(orderNumb)

                    milesTrav(orderNumb)

                    orderEndTime = util_func.writeData('delivery', str(orderNumb) + 'EndTime.txt', util_func.now(), 'back')

                    util_func.timeTook(datetime.datetime.strptime(util_func.readData('', 'delivery', 'deliveryStartTime.txt'), '%Y-%m-%d %H:%M:%S.%f'), orderEndTime, 'order')

                onDelivery('driving back to store...', datetime.datetime.strptime(util_func.readData('', 'delivery', 'deliveryStartTime.txt'), '%Y-%m-%d %H:%M:%S.%f'))

                milesTrav('total', 'total ')

                delivEndTime = util_func.writeData('delivery', 'deliveryEndTime.txt', util_func.now(), 'back')

                util_func.timeTook(datetime.datetime.strptime(util_func.readData('', 'delivery', 'deliveryStartTime.txt'), '%Y-%m-%d %H:%M:%S.%f'), delivEndTime, 'delivery')

                util_func.writeData('shift', 'numbOfDeliveries.txt', int(util_func.deliveryNumb('number')) + 1)

    else:
        pass