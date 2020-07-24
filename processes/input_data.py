'''
todo: thinking should change to storing indavidual data in dir namd after
      class (order or extra stop) it is storing until consolidated, use
      those dirs to tell when in progress. shift and deliveries should stay
      in dirs named after thire ids, because those are also checkable
'''


def end_shift(shift):
    # todo: current working spot, top priority, make sure this works as inteded
    # get list of files
    file_list = shift.file_list()

    # end time
    from os import path
    if not path.exists(file_list['end_time']):
        from utility.file import write
        from utility.utility import now
        # set and save
        shift.end_time = now()
        write(shift.end_time, file_list['end_time'])

    else:
        from utility.file import Read
        # load
        shift.end_time = Read(file_list['end_time']).datetimes()

    # miles traveled
    if not path.exists(file_list['miles_traveled']):
        from resources.strings import Shift__miles_traveled__prompt as prompt
        from utility.file import write
        from utility.user_input import User_Input
        # input and save
        shift.miles_traveled = User_Input(prompt).miles_traveled()
        write(shift.miles_traveled, file_list['miles_traveled'])

    else:
        from utility.file import Read
        # load
        shift.miles_traveled = Read(file_list['miles_traveled']).floats()

    # fuel economy
    if not path.exists(file_list['fuel_economy']):
        from resources.strings import Shift__fuel_economy__prompt as prompt
        from utility.file import write
        from utility.user_input import User_Input
        # input and save
        shift.fuel_economy = User_Input(prompt).fuel_economy()
        write(shift.fuel_economy, file_list['fuel_economy'])

    else:
        from utility.file import Read
        # load
        shift.fuel_economy = Read(file_list['fuel_economy']).floats()

    # vehical compensation
    if not path.exists(file_list['vehical_compensation']):
        from resources.strings import Shift__vehical_compensation__prompt as\
            prompt
        from utility.file import write
        from utility.user_input import User_Input
        # input and save
        shift.vehical_complensation = User_Input(prompt).money(' vehical compensation')
        write(shift.vehical_complensation, file_list['vehical_compensation'])

    else:
        from utility.file import Read
        # load
        shift.vehical_compensation =\
            Read(file_list['vehical_compensation']).floats()

    # device compensation
    if not path.exists(file_list['device_compensation']):
        from resources.strings import Shift__device_compensation__prompt as\
            promp
        from utility.file import write
        from utility.user_input import User_Input
        # input and save
        shift.device_compensation = User_Input(promp).money(' device compensation')
        write(shift.device_compensation, file_list['device_compensation'])

    else:
        from utility.file import Read
        # load
        shift.device_compensation =\
            Read(file_list['device_compensation']).floats()

    # total hours
    if not path.exists(file_list['total_hours']):
        from resources.strings import Shift__total_hours__prompt as prompt
        from utility.file import write
        from utility.user_input import User_Input
        # input and save
        shift.total_hours = User_Input(prompt).total_hours()
        write(shift.total_hours, file_list['total_hours'])

    else:
        from utility.file import Read
        # load
        shift.total_hours = Read(file_list['total_hours']).floats()

    # extra tips claimed
    if not path.exists(file_list['extra_tips_claimed']):
        from resources.strings import Shift__extra_tips_claimed__prompt as\
            prompt
        from utility.file import write
        from utility.user_input import User_Input
        # input and save
        shift.extra_tips_claimed = User_Input(prompt).money(' extra claimed for taxes')
        write(shift.extra_tips_claimed, file_list['extra_tips_claimed'])

    else:
        from utility.file import Read
        # load
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


class Input_Delivery:
    def average_speed(self):
        from resources.strings import Delivery__average_speed__prompt as\
            prompt
        from utility.user_input import User_Input
        # input average speed
        return User_Input(prompt).average_speed()

    def distance(self):
        from resources.strings import Delivery__miles_traveled_prompt as\
            prompt
        from utility.user_input import User_Input
        # input distance traveled
        return User_Input(prompt).miles_traveled()
    
    def time(self):
        from utility.utility import now
        return now()


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
    if not path.exists(order_files['id']):
        from utility.user_input import User_Input
        # input and save id
        order.id = User_Input(id_prompt).id()
        write(order.id, order_files['id'])

    else:
        # load order id
        order.id = Read(order_files['id']).integer()

    # tip
    if not path.exists(order_files['tip']):
        # input and save tip
        order.tip = tip()
        write(order.tip.csv(), order_files['tip'])

    else:
        # load tip
        from processes.load import tip as load_tip
        order.tip = load_tip(order_files['tip'])

    # miles traveled
    if not path.exists(order_files['miles_traveled']):
        from utility.user_input import User_Input
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
    time_taken(order.parent.start_time, order.end_time, order_ended)
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
    if not isinstance(shift, Shift):
        # todo: need to write this error message
        raise TypeError

    from objects.split import Split
    from os import path
    from processes.consolidate import split as consolidate_split
    from utility.file import Read


    # todo: this needs to add existens checking for all of these
    # create split instance
    split = Split(shift)
    # get list of files
    file_list = split.file_list()

    # load and set start time
    split.start_time = Read(file_list['start_time']).datetimes()
    # miles traveled
    if not path.exists(file_list['miles_traveled']):
        from utility.file import write
        from utility.user_input import User_Input
        # todo: need to write prompt for miles traveled and put it in resoursces file
        # input and save
        split.miles_traveled = User_Input('enter miles traveled').miles_traveled()
        write(split.miles_traveled, file_list['miles_traveled'])

    else:
        # load
        split.miles_traveled = Read(file_list['miles_traveled']).floats()

    # end time
    if not path.exists(file_list['end_time']):
        from utility.utility import now
        # set and save
        split.end_time = now()
        write(split.end_time, file_list['end_time'])

    else:
        # load
        split.end_time = Read(file_list['end_time']).datetimes()

    # consolidate individual files into one file
    consolidate_split(split)

    return split


def start_split(shift):
    from objects.shift import Shift
    if not isinstance(shift, Shift):
        # todo: need to write this error message
        raise TypeError

    from objects.split import Split
    from os import path
    from resources.strings import Split__start__enter_to_continue as prompt
    from utility.utility import enter_to_continue

    shift.split = Split(shift)

    # directory
    if not path.exists(shift.split.file_list()['directory']):
        from os import mkdir
        # create directory
        mkdir(shift.split.file_list()['directory'])

    # start time
    if not path.exists(shift.split.file_list()['start_time']):
        from utility.file import write
        from utility.utility import now
        # set and save
        shift.split.start_time = now()
        write(shift.split.start_time,  shift.split.file_list()['start_time'])

    enter_to_continue(prompt)

    return shift


def extra_stop(extra_stop):
    from objects.extra_stop import Extra_Stop
    if not isinstance(extra_stop, Extra_Stop):
        raise TypeError

    from os import path

    file_list = extra_stop.file_list()

    # id
    extra_stop.assign_id()

    # location
    if not path.exists(file_list['location']):
        from resources.strings import Extra_Stop__location__prompt as prompt
        from utility.file import write
        from utility.user_input import User_Input
        # input and save
        extra_stop.location = User_Input(prompt).location()
        write(extra_stop.location, file_list['location'])

    else:
        from utility.file import Read
        # load
        extra_stop.location = Read(file_list['location'])

    # reason
    if not path.exists(file_list['reason']):
        from resources.strings import Extra_Stop__reason__prompt as prompt
        from utility.file import write
        from utility.user_input import User_Input
        # input and save
        extra_stop.reason = User_Input(prompt).reason()
        write(extra_stop.reason, file_list['reason'])

    else:
        from utility.file import Read
        # load
        extra_stop.reason = Read(file_list['reason'])

    # miles traveled
    if not path.exists(file_list['miles_traveled']):
        from resources.strings import Extra_Stop__miles_traveled__prompt as\
            prompt
        from utility.file import write
        from utility.user_input import User_Input
        # input and save
        extra_stop.miles_traveled = User_Input(prompt).miles_traveled()
        write(extra_stop.miles_traveled, file_list['miles_traveled'])

    else:
        from utility.file import Read
        # load
        extra_stop.miles_traveled = Read(file_list['miles_traveled']).floats()

    # end time
    if not path.exists(file_list['end_time']):
        from utility.file import write
        from utility.utility import now
        # set and save
        extra_stop.end_time = now()
        write(extra_stop.end_time, file_list['end_time'])

    else:
        from utility.file import Read
        # load
        extra_stop.end_time = Read(file_list['end_time']).datetimes()

    return extra_stop


def shift_extra_stop(shift):
    from objects.shift import Shift
    if not isinstance(shift, Shift):
        # todo: need to write this error message
        raise TypeError

    from objects.extra_stop import Extra_Stop
    from os import path
    from processes.consolidate import shift_extra_stop as\
        consolidate_extra_stop
    from resources.strings import Extra_Stop__time_taken__display as\
        time_taken_display
    from utility.utility import time_taken

    extra_stop_instance = Extra_Stop(shift)
    file_list = extra_stop_instance.file_list()

    # directory
    if not path.exists(file_list['directory']):
        from os import mkdir
        mkdir(file_list['directory'])

    # start time
    if not path.exists(file_list['start_time']):
        from utility.file import write
        from utility.utility import now
        # set and save
        extra_stop_instance.start_time = now()
        write(extra_stop_instance.start_time, file_list['start_time'])

    else:
        from utility.file import Read
        # load
        extra_stop_instance.start_time = Read(file_list['start_time']).datetimes()

    extra_stop_instance = extra_stop(extra_stop_instance)

    # consolidate all files into one
    consolidate_extra_stop(extra_stop_instance)
    # display time since starting delivery
    time_taken(extra_stop_instance.start_time,
               extra_stop_instance.end_time,
               time_taken_display)

    return extra_stop_instance


def delivery_extra_stop(delivery):
    from objects.delivery import Delivery
    if not isinstance(delivery, Delivery):
        # todo: need to write this error message
        raise TypeError

    from objects.extra_stop import Extra_Stop
    from os import path
    from processes.consolidate import delivery_extra_stop as\
        consolidate_extra_stop
    from resources.strings import Extra_Stop__time_taken__display as\
        time_taken_display
    from utility.utility import time_taken

    extra_stop_instance = Extra_Stop(delivery)
    file_list = extra_stop_instance.file_list()

    # directory
    if not path.exists(file_list['directory']):
        from os import mkdir
        mkdir(file_list['directory'])

    extra_stop_instance = extra_stop(extra_stop_instance)

    # consolidate all files into one
    consolidate_extra_stop(extra_stop_instance)
    # display time since starting delivery
    time_taken(delivery.start_time,
               extra_stop_instance.end_time,
               time_taken_display)

    return extra_stop_instance
