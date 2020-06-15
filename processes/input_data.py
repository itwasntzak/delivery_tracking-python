'''
todo: thinking should change to storing indavidual data in dir namd after
      class (order or extra stop) it is storing until consolidated, use
      those dirs to tell when in progress. shift and deliveries should stay
      in dirs named after thire ids, because those are also checkable
'''


def end_shift(shift):
    # todo: write this
    pass


def delivery(shift):
    from objects.delivery import Delivery
    from objects.order import Order
    from os import mkdir, path
    from processes.consolidate import delivery as consolidate_delivery
    from resources.strings import\
        Delivery__average_speed_prompt as average_speed_prompt,\
        Delivery__miles_traveled_prompt as miles_traveled_prompt,\
        Delivery__order_quantity__prompt as order_quantity_prompt,\
        Delivery__time_taken__display as time_take_display
    from utility.file import Read, write
    from utility.user_input import integer, User_Input
    from utility.utility import now, time_taken
    from processes.load import order as load_order

    # create delivery
    delivery = Delivery(shift)
    # get list of files and directory for delivery
    delivery_files = delivery.delivery_files()
    # create directory to store files
    if not path.exists(delivery_files['directory']):
        mkdir(delivery_files['directory'])

    # start time
    if not path.exists(delivery_files['start_time']):
        # set and save start time for delivery
        delivery.start_time = now()
        write(delivery.start_time, delivery_files['start_time'])
    else:
        # load start time
        delivery.start_time = Read(delivery_files['start_time']).datetimes()

    # order quantity
    if not path.exists(delivery_files['order_quantity']):
        # input and save order quantity
        delivery.order_quantity = integer(order_quantity_prompt)
        write(delivery.order_quantity, delivery_files['order_quantity'])
    else:
        # load order quantity
        delivery.order_quantity =\
            Read(delivery_files['order_quantity']).integers()

    # load orders
    if path.exists(delivery_files['order_ids']):
        delivery.order_ids = Read(delivery_files['order_ids']).integers()
        for id in delivery.order_ids:
            order = Order(delivery, id)
            delivery.orders.append(load_order(order))

    # todo: need to load extra stop if any exist

    # orders
    while delivery.order_quantity > len(delivery.orders):
        # todo: add driving to address after it is fixed

        # input and save order
        delivery.add_order(order(delivery))

    # todo: add driving to store after

    # miles traveled
    if not path.exists(delivery_files['miles_traveled']):
        # input and save miles traveled
        delivery.miles_traveled =\
            User_Input(miles_traveled_prompt).miles_traveled()
        write(delivery.miles_traveled, delivery_files['miles_traveled'])
    else:
        # load miles traveled
        delivery.miles_traveled =\
            Read(delivery_files['miles_traveled']).floats()

    # average speed
    if not path.exists(delivery_files['average_speed']):
        # input and save average speed
        delivery.average_speed =\
            User_Input(average_speed_prompt).average_speed()
        write(delivery.average_speed, delivery_files['average_speed'])
    else:
        # load average speed
        delivery.average_speed =\
            Read(delivery_files['average_speed']).integers()

    # end time
    if not path.exists(delivery_files['end_time']):
        # set and save end time
        delivery.end_time = now()
        write(delivery.end_time, delivery_files['end_time'])
    else:
        # load end time
        delivery.end_time = Read(delivery_files['end_time']).datetimes()

    # consolidate all delivery data to one file
    consolidate_delivery(delivery)
    # display time taken since starting delivery
    time_taken(delivery.start_time, delivery.end_time, time_take_display)
    # return completed delivery
    return delivery


def order(delivery):
    from objects.order import Order
    from os import mkdir, path
    from processes.consolidate import order as consolidate_order
    from resources.strings import\
        Order__input_id__prompt as id_prompt,\
        Order__input_miles_traveled__prompt as miles_traveled_prompt,\
        Order__time_taken__display as order_ended
    from utility.file import Read, write
    from utility.user_input import User_Input
    from utility.utility import now, time_taken

    # create order
    order = Order(delivery)
    # get list of files for order input
    order_files = order.file_list()
    # make directory to store order files
    if not path.exists(order_files['directory']):
        mkdir(order_files['directory'])

    # id
    if not path.exist(order_files['id']):
        # input and save id
        order.id = User_Input(id_prompt).id()
        write(order.id, order_files['id'])
    else:
        # load order id
        order.id = Read(order_files['id']).integers()

    # tip
    if not path.exists(order_files['tip']):
        # input and save tip
        order.tip = tip(order)
        write(order.tip, order_files['tip'])
    else:
        # load tip
        from objects.tip import Tip
        from processes.load import tip as load_tip
        tip = Tip()
        tip.file_path = order_files['tip']
        order.tip = load_tip(tip)

    # miles traveled
    if not path.exists(order_files['miles_traveled']):
        # input and save miles traveled
        order.miles_traveled =\
            User_Input(miles_traveled_prompt).miles_traveled()
        write(order.miles_traveled, order_files['miles_traveled'])
    else:
        # load miles traveled
        order.miles_traveled = Read(order_files['miles_traveled']).floats()

    # end time
    if not path.exists(order_files['end_time']):
        # set and save end time
        order.end_time = now()
        write(order.end_time, order_files['end_time'])
    else:
        # load end time
        order.end_time = Read(order_files['end_time']).datetimes()

    # consolidate order files into one file
    consolidate_order(order)
    # display time taken since delivery was started
    time_taken(order.parent_start_time(), order.end_time, order_ended)
    # return completed order
    return order


def tip(parent):
    from objects.tip import Tip
    from resources.strings import\
        Tip__input_card__prompt as card_prompt,\
        Tip__input_cash__prompt as cash_prompt
    from utility.file import write
    from utility.user_input import User_Input

    # input tip
    tip = Tip(card=User_Input(card_prompt).card_tip(),
              cash=User_Input(cash_prompt).cash_tip())
    # save tip
    write(tip.csv(), parent.file_list()['tip'])

    return tip
