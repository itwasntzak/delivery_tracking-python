import os

import util_func
import order
import input_data


<<<<<<< HEAD
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
=======
def on_delivery(prompt, start_time):
    # creating file so code knows while on delivery, and continue
    with open(os.path.join('delivery', 'on_delivery'), 'w'):
        pass

    while True:
        wait_for_user = input_data.get_input(
            prompt= prompt
                    + '\n1 after returning '
                      '| 2 for extra stop\n',
            kind= int
        )
        if wait_for_user == 1:
            # remove on_delivery file so code can know a delivery has ended
            os.remove(os.path.join(
                'delivery', 'on_delivery'))
>>>>>>> master
            break
        elif wait_for_user == 2:
            # extra stop option
            extra_stop(start_time)
            continue
        else:
            print('\nInvalid input...')


def extra_stop(start_time):
    # creating file so code knows while on extra stop, to be able to continue
    with open(os.path.join('delivery', 'extra_stop'), mode='w'):
        pass

    while True:
<<<<<<< HEAD
        print('\nnumber of orders:')
        try:
            numbOfOrders = int(input())

            if numbOfOrders >= 1:
                utilFunc.writeData("deliveryTracking", "delivery", "numbOfOrders.txt", numbOfOrders)

                return numbOfOrders

        except ValueError:
            print('\ninvalid input')


def delivery():
    os.mkdir(os.path.join("deliveryTracking", "delivery"))
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
=======
        wait_for_user = input_data.get_input(
            prompt='\nMaking extra stop...'
                   '\n1 to continue\n',
            kind=int
        )
        if wait_for_user == 1:
        # input extra stop name and save it
            extra_stop_name = input_data.input_data(
                prompt1='\nName of extra stop:\n',
                input_type1=str,
                prompt2='\nIs this correct? [y/n]\n',
                input_type2=str,
                option_yes='y',
                option_no='n'
            )
            util_func.write_data(
                path='delivery',
                file=extra_stop_name + '_extra_stop.txt',
                data=str(extra_stop_name)
            )
        # input extra stop reason and creating a file with that as contents
            util_func.write_data(
                path='delivery',
                file=extra_stop_name + '_reason.txt',
                data=input_data.input_data(
                    prompt1='\nReason for extra stop?\n',
                    input_type1=str,
                    prompt2='\nIs this correct? [y/n]\n',
                    input_type2=str,
                    option_yes='y',
                    option_no='n'
            ))
        # input and saving miles traveled
            miles_trav(
                var_path=extra_stop_name, prompt='Extra miles traveled:    #.#')
        # save the time at the end of the extra stop
            extra_end_time = util_func.write_data(
                path='delivery',
                file=extra_stop_name + '_end_time.txt',
                data=util_func.now(),
                back=True
            )
        # display the amount of time since the delivery was started
            util_func.time_took(
                start_time=start_time,
                end_time=extra_end_time,
                var_word='extra stop'
            )
            os.remove(os.path.join(
                'delivery', 'extra_stop'))
            break
        else:
            print('\nInvalid input...')


def miles_trav(var_path, prompt):
    miles_trav_input = input_data.input_data(
        prompt1='\n' + prompt + '\n',
        input_type1=float,
        prompt2='\nIs this correct? [y/n]\n',
        input_type2=str,
        option_yes='y',
        option_no='n'
    )
    util_func.write_data(
        path='delivery',
        file=str(var_path) + '_miles_trav.txt',
        data=miles_trav_input
    )


def numb_of_orders():
    return util_func.write_data(
        path='delivery',
        file='numbOfOrders.txt',
        data=input_data.input_data(
            prompt1='\nNumber of orders?\n',
            input_type1=int,
            prompt2='\nIs this correct? [y/n]\n',
            input_type2=str,
            option_yes='y',
            option_no='n'),
        back=True
    )


def delivery():
    os.mkdir(os.path.join('delivery'))
    start_time = util_func.write_data(
        path='delivery',
        file='delivery_start_time.txt',
        data=util_func.now(),
        back=True
    )
    number_of_orders = numb_of_orders()

    if number_of_orders == 1:
        on_delivery(
            prompt='\nDriving to address...', start_time=start_time)
        order_number = order.order_number()
        order.tip(var_path=order_number)
        miles_trav(
            var_path=order_number, prompt='Miles traveled:    #.#')
        order_end_time = util_func.write_data(
            path='delivery',
            file=str(order_number) + '_end_time.txt',
            data=util_func.now(),
            back=True
        )
        util_func.time_took(
            start_time=start_time,
            end_time=order_end_time,
            var_word='order'
        )


    elif number_of_orders >= 1:
        for value in range(number_of_orders):
            on_delivery(
                prompt='\nDriving to address...',
                start_time=start_time
            )
            order_number = order.order_number()
            order.tip(
                var_path=order_number
            )
            miles_trav(
                var_path=order_number, prompt='Miles traveled:    #.#')
            order_end_time = util_func.write_data(
                path='delivery',
                file=str(order_number) + '_end_time.txt',
                data=util_func.now(),
                back=True
            )
            util_func.time_took(
                start_time=start_time,
                end_time=order_end_time,
                var_word='order'
            )
    on_delivery(
        prompt='Driving back to store...', start_time=start_time)
    miles_trav(
        var_path='total', prompt='Total miles traveled:    #.#')
    delivery_end_time = util_func.write_data(
        path='delivery',
        file='delivery_end_time.txt',
        data=util_func.now(),
        back=True
    )
    util_func.time_took(
        start_time=start_time,
        end_time=delivery_end_time,
        var_word='delivery'
    )
    util_func.write_data(
        path='shift',
        file='number_of_deliveries.txt',
        data=int(util_func.delivery_number('number')) + 1
    )
>>>>>>> master
