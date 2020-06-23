'''
todo: thinking should change to storing indavidual data in dir namd after
      class (order or extra stop) it is storing until consolidated, use
      those dirs to tell when in progress. shift and deliveries should stay
      in dirs named after thire ids, because those are also checkable
'''


def start_shift():
    from objects.shift import Shift
    from os import mkdir
    from resources.strings import Shift__start__enter_to_continue__display as\
        shift_started
    from utility.file import write
    from utility.utility import enter_to_continue, now

    shift = Shift(now().date())

    shift.start_time = now()
    mkdir(shift.file_list()['directory'])
    write(shift.start_time, shift.file_list()['start_time'])
    enter_to_continue(shift_started)

    return shift


def end_shift():
    from processes.load import current_shift as load_shift
    shift = load_shift()
    # get list of files
    file_list = shift.file_list()

    # end time
    from os import path
    if not path.exists(file_list['end_time']):
        from utility.file import write
        from utility.utility import now
        shift.end_time = now()
        write(shift.end_time, file_list['end_time'])
    else:
        from utility.file import Read
        shift.end_time = Read(file_list('end_time')).datetimes()

    # miles traveled
    if not path.exists(file_list['miles_traveled']):
        from resources.strings import Shift__miles_traveled__prompt as prompt
        from utility.file import write
        from utility.user_input import User_Input
        shift.miles_traveled = User_Input(prompt).miles_traveled()
        write(shift.miles_traveled, file_list['miles_traveled'])
    else:
        from utility.file import Read
        shift.miles_traveled = Read(file_list['miles_traveled']).floats()

    # fuel economy
    if not path.exists(file_list['fuel_economy']):
        from resources.strings import Shift__fuel_economy__prompt as prompt
        from utility.file import write
        from utility.user_input import decimal
        shift.fuel_economy = decimal(prompt)
        write(shift.fuel_economy, file_list['fuel_economy'])
    else:
        from utility.file import Read
        shift.fuel_economy = Read(file_list['fuel_economy']).floats()

    # vehical compensation
    if not path.exists(file_list['vehical_complensation']):
        from resources.strings import Shift__vehical_compensation__prompt as\
            prompt
        from utility.file import write
        from utility.user_input import money
        shift.vehical_complensation = money(prompt)
        write(shift.vehical_complensation, file_list['vehical_compensation'])
    else:
        from utility.file import Read
        shift.vehical_compensation =\
            Read(file_list['vehical_compensation']).floats()

    # device compensation
    if not path.exists(file_list['device_compensation']):
        from resources.strings import Shift__device_compensation__prompt as\
            promp
        from utility.file import write
        from utility.user_input import money
        shift.device_compensation = money(promp)
        write(shift.device_compensation, file_list['device_compensation'])
    else:
        from utility.file import Read
        shift.device_compensation =\
            Read(file_list['device_compensation']).floats()

    # total hours worked
    if not path.exists(file_list['total_hours']):
        from resources.strings import Shift__total_hours__prompt as prompt
        from utility.file import write
        from utility.user_input import decimal
        shift.total_hours = decimal(prompt)
        write(shift.total_hours, file_list['total_hours'])
    else:
        from utility.file import Read
        shift.total_hours = Read(file_list['total_hours']).floats()

    # extra tips claimed
    if not path.exists(file_list['extra_tips_claimed']):
        from resources.strings import Shift__extra_tips_claimed__prompt as\
            prompt
        from utility.file import write
        from utility.user_input import money
        shift.extra_tips_claimed = money(prompt)
        write(shift.extra_tips_claimed, file_list['extra_tips_claimed'])
    else:
        from utility.file import Read
        shift.extra_tips_claimed =\
            Read(file_list['extra_tips_claimed']).floats()

    # consolidate indavidual files into one
    from processes.consolidate import shift as consolidate_shift
    consolidate_shift(shift)
    # inform user shift was successfully
    from resources.strings import Shift__end___enter_to_continue__display as\
        shift_ended
    from utility.utility import enter_to_continue
    enter_to_continue(shift_ended)

    return shift


def delivery(shift):
    from os import path

    from objects.shift import Shift
    if not isinstance(shift, Shift):
        # todo: need to write error message
        raise TypeError

    # create delivery instance
    from objects.delivery import Delivery
    delivery = Delivery(shift)
    # get list of files and directory for delivery
    file_list = delivery.file_list()
    # create directory to store files
    if not path.exists(file_list['directory']):
        from os import mkdir
        mkdir(file_list['directory'])

    # id
    delivery.assign_id()

    # start time
    if not path.exists(file_list['start_time']):
        from utility.file import write
        from utility.utility import now
        # set and save start time for delivery
        delivery.start_time = now()
        write(delivery.start_time, file_list['start_time'])
    else:
        from utility.file import Read
        # load start time
        delivery.start_time = Read(file_list['start_time']).datetimes()

    # load orders
    from objects.order import Order
    if path.exists(Order(delivery).file_list()['completed_ids']):
        from processes.load import order as load_order
        from utility.file import Read
        delivery.order_ids =\
            Read(Order(delivery).file_list()['completed_ids']).integers()
        for id in delivery.order_ids:
            order = Order(delivery, id)
            delivery.orders.append(load_order(order))

    # load extra stops
    from objects.extra_stop import Extra_Stop
    if path.exists(Extra_Stop(delivery).file_list()['completed_ids']):
        from processes.load import delivery_extra_stop as load_extra_stop
        from utility.file import Read
        delivery.extra_stop_ids =\
            Read(Extra_Stop(delivery).file_list()['completed_ids']).integers()
        for id in delivery.extra_stop_ids:
            extra_stop = Extra_Stop(delivery, id)
            delivery.extra_stops.append(load_extra_stop(extra_stop))

    # orders
    # todo: need to change this to not include quantity but instead add order from a menu
    while delivery.order_quantity > len(delivery.orders):
        # todo: add driving to address after it is fixed

        # input and save order
        delivery.add_order(order(delivery))

    # todo: add driving to store after

    # miles traveled
    if not path.exists(file_list['miles_traveled']):
        from resources.strings import Delivery__miles_traveled_prompt as\
            prompt
        from utility.file import write
        from utility.user_input import User_Input
        # input and save miles traveled
        delivery.miles_traveled =\
            User_Input(prompt).miles_traveled()
        write(delivery.miles_traveled, file_list['miles_traveled'])
    else:
        from utility.file import Read
        # load miles traveled
        delivery.miles_traveled =\
            Read(file_list['miles_traveled']).floats()

    # average speed
    if not path.exists(file_list['average_speed']):
        from resources.strings import Delivery__average_speed_prompt as\
            prompt
        from utility.file import write
        from utility.user_input import User_Input
        # input and save average speed
        delivery.average_speed =\
            User_Input(prompt).average_speed()
        write(delivery.average_speed, file_list['average_speed'])
    else:
        from utility.file import Read
        # load average speed
        delivery.average_speed =\
            Read(file_list['average_speed']).integers()

    # end time
    if not path.exists(file_list['end_time']):
        from utility.file import write
        from utility.utility import now
        # set and save end time
        delivery.end_time = now()
        write(delivery.end_time, file_list['end_time'])
    else:
        from utility.file import Read
        # load end time
        delivery.end_time = Read(file_list['end_time']).datetimes()

    # consolidate all delivery data to one file
    from processes.consolidate import delivery as\
        consolidate_delivery
    consolidate_delivery(delivery)

    # display time taken since starting delivery
    from resources.strings import Delivery__time_taken__display as\
        time_take_display
    from utility.utility import time_taken
    time_taken(delivery.start_time, delivery.end_time, time_take_display)

    # return completed delivery
    return delivery


def order(delivery):
    from objects.delivery import Delivery
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

    if not isinstance(delivery, Delivery):
        # todo: need to write error message
        raise TypeError

    # create order instance
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
        order.tip = tip()
        write(order.tip, order_files['tip'])
    else:
        # load tip
        from processes.load import tip as load_tip
        order.tip = load_tip(order_files['tip'])

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


def tip():
    from objects.tip import Tip
    from resources.strings import\
        Tip__input_card__prompt as card_prompt,\
        Tip__input_cash__prompt as cash_prompt
    from utility.user_input import User_Input

    # input tip
    tip = Tip(card=User_Input(card_prompt).card_tip(),
              cash=User_Input(cash_prompt).cash_tip())

    return tip


def end_split(shift):
    from objects.shift import Shift
    from objects.split import Split
    from processes.consolidate import split as consolidate_split
    from utility.file import Read, write
    from utility.user_input import User_Input
    from utility.utility import now

    if not isinstance(shift, Shift):
        # todo: need to write this error message
        raise TypeError

    # create split instance
    split = Split(shift)
    # get list of files
    file_list = split.file_list()
    # load and set start time
    split.start_time = Read(file_list['start_time']).datetimes()
    # input and save miles traveled for split
    # todo: need to write prompt for miles traveled and put it in resoursces file
    split.miles_traveled = User_Input().miles_traveled()
    write(split.miles_traveled, file_list['miles_traveled'])
    # set and save split end time
    split.end_time = now()
    write(split.end_time, file_list['end_time'])
    # consolidate individual files into one file
    consolidate_split()

    return split


def start_split(shift):
    from objects.shift import Shift
    from objects.split import Split
    from resources.strings import Split__start__enter_to_continue as prompt
    from utility.file import write
    from utility.utility import enter_to_continue, now

    if not isinstance(shift, Shift):
        # todo: need to write this error message
        raise TypeError

    split = Split(shift)
    split.start_time = now()
    write(split.start_time,  split.file_list()['start_time'])

    enter_to_continue(prompt)

    return split


def shift_extra_stop(shift):
    from objects.extra_stop import Extra_Stop
    from objects.shift import Shift
    from os import path
    from processes.consolidate import shift_extra_stop as\
        consolidate_extra_stop
    from resources.strings import Extra_Stop__time_taken__display as\
        time_taken_display
    from utility.utility import time_taken

    if not isinstance(shift, Shift):
        # todo: need to write this error message
        raise TypeError

    extra_stop = Extra_Stop(shift)
    file_list = extra_stop.file_list()

    # start time
    if not path.exists(file_list['start_time']):
        from utility.file import write
        from utility.utility import now
        extra_stop.start_time = now()
        write(extra_stop.start_time, file_list['start_time'])
    else:
        from utility.file import Read
        extra_stop.start_time = Read(file_list['start_time']).datetimes()

    # location
    if not path.exists(file_list['location']):
        from resources.strings import Extra_Stop__location__prompt as prompt
        from utility.file import write
        from utility.user_input import text
        extra_stop.location = text(prompt)
    else:
        from utility.file import Read
        extra_stop.location = Read(file_list['location'])

    # reason
    if not path.exists(file_list['reason']):
        from resources.strings import Extra_Stop__reason__prompt as prompt
        from utility.file import write
        from utility.user_input import text
        extra_stop.reason = text(prompt)
        write(extra_stop.reason, file_list['reason'])
    else:
        from utility.file import Read
        extra_stop.reason = Read(file_list['reason'])

    # miles traveled
    if not path.exists(file_list['miles_traveled']):
        from resources.strings import Extra_Stop__miles_traveled__prompt as\
            prompt
        from utility.file import write
        from utility.user_input import User_Input
        extra_stop.miles_traveled = User_Input(prompt).miles_traveled()
        write(extra_stop.miles_traveled, file_list['miles_traveled'])
    else:
        from utility.file import Read
        extra_stop.miles_traveled = Read(file_list['miles_traveled']).floats()

    # end time
    if not path.exists(file_list['end_time']):
        from utility.file import write
        from utility.utility import now
        extra_stop.end_time = now()
        write(extra_stop.end_time, file_list['end_time'])
    else:
        from utility.file import Read
        extra_stop.end_time = Read(file_list['end_time']).datetimes()

    consolidate_extra_stop(extra_stop)
    time_taken(extra_stop.start_time, extra_stop.end_time, time_taken_display)

    return extra_stop


def delivery_extra_stop(delivery):
    from objects.delivery import Delivery
    from objects.extra_stop import Extra_Stop
    from os import path
    from processes.consolidate import delivery_extra_stop as\
        consolidate_extra_stop
    from resources.strings import Extra_Stop__time_taken__display as\
        time_taken_display
    from utility.utility import time_taken

    if not isinstance(delivery, Delivery):
        # todo: need to write this error message
        raise TypeError

    extra_stop = Extra_Stop(delivery)
    file_list = extra_stop.file_list()

    # location
    if not path.exists(file_list['location']):
        from resources.strings import Extra_Stop__location__prompt as prompt
        from utility.file import write
        from utility.user_input import text
        extra_stop.location = text(prompt)
    else:
        from utility.file import Read
        extra_stop.location = Read(file_list['location'])

    # reason
    if not path.exists(file_list['reason']):
        from resources.strings import Extra_Stop__reason__prompt as prompt
        from utility.file import write
        from utility.user_input import text
        extra_stop.reason = text(prompt)
        write(extra_stop.reason, file_list['reason'])
    else:
        from utility.file import Read
        extra_stop.reason = Read(file_list['reason'])

    # miles traveled
    if not path.exists(file_list['miles_traveled']):
        from resources.strings import Extra_Stop__miles_traveled__prompt as\
            prompt
        from utility.file import write
        from utility.user_input import User_Input
        extra_stop.miles_traveled = User_Input(prompt).miles_traveled()
        write(extra_stop.miles_traveled, file_list['miles_traveled'])
    else:
        from utility.file import Read
        extra_stop.miles_traveled = Read(file_list['miles_traveled']).floats()

    # end time
    if not path.exists(file_list['end_time']):
        from utility.file import write
        from utility.utility import now
        extra_stop.end_time = now()
        write(extra_stop.end_time, file_list['end_time'])
    else:
        from utility.file import Read
        extra_stop.end_time = Read(file_list['end_time']).datetimes()

    consolidate_extra_stop(extra_stop)
    time_taken(delivery.start_time, extra_stop.end_time, time_taken_display)

    return extra_stop
