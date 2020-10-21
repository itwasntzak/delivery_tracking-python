
# shift
# end
def end_shift(shift, test=False):
    from objects import Shift
    if not isinstance(shift, Shift):
        raise TypeError

    from os import path
    from utility.file import write

    # get list of files and directory
    file_list = shift.file_list()

    # end time
    if not path.exists(file_list['end_time']):
        if test is False:
            # set
            shift.set_end_time()
        # save
        write(shift.end_time, file_list['end_time'])

    # distance
    if not path.exists(file_list['miles_traveled']):
        if test is False:
            # input
            shift.input_miles_traveled()
        # save
        write(shift.miles_traveled, file_list['miles_traveled'])

    # fuel economy
    if not path.exists(file_list['fuel_economy']):
        if test is False:
            # input
            shift.input_fuel_economy()
        # save
        write(shift.fuel_economy, file_list['fuel_economy'])

    # vehicle compensation
    if not path.exists(file_list['vehicle_compensation']):
        if test is False:
            # input
            shift.input_vehicle_compensation()
        # save
        write(shift.vehicle_compensation, file_list['vehicle_compensation'])

    # device compensation
    if not path.exists(file_list['device_compensation']):
        if test is False:
            # input
            shift.input_device_compensation()
        # save
        write(shift.device_compensation, file_list['device_compensation'])

    # total hours
    if not path.exists(file_list['total_hours']):
        if test is False:
            # input
            shift.input_total_hours()
        # save
        write(shift.total_hours, file_list['total_hours'])

    # extra tips claimed
    if not path.exists(file_list['extra_tips_claimed']):
        if test is False:
            # input
            shift.input_extra_tips_claimed()
        # save
        write(shift.extra_tips_claimed, file_list['extra_tips_claimed'])

    return shift


# start
def start_shift(shift, test=False):
    from objects import Shift
    if not isinstance(shift, Shift):
        raise TypeError

    from os import path

    # get list of files and directory
    file_list = shift.file_list()

    # directory
    if not path.exists(file_list['directory']):
        from os import mkdir
        mkdir(file_list['directory'])

    # start time
    if not path.exists(file_list['start_time']):
        from utility.file import write
        if test is False:
            # set
            shift.set_start_time()
        # save
        write(shift.start_time, file_list['start_time'])

    return shift


# delivery
# end
def end_delivery(delivery, test=False):
    from objects import Delivery
    if not isinstance(delivery, Delivery):
        raise TypeError

    from os import path
    from utility.file import write

    # get list of files and directory
    file_list = delivery.file_list()

    # miles traveled
    if not path.exists(file_list['miles_traveled']):
        if test is False:
            # input
            delivery.input_miles_traveled()
        # save
        write(delivery.miles_traveled, file_list['miles_traveled'])

    # average speed
    if not path.exists(file_list['average_speed']):
        if test is False:
            # input
            delivery.input_average_speed()
        # save
        write(delivery.average_speed, file_list['average_speed'])

    # end time
    if not path.exists(file_list['end_time']):
        if test is False:
            # set
            delivery.set_end_time()
        # save
        write(delivery.end_time, file_list['end_time'])
    # inform delivery of its completion
    delivery.in_progress = False

    return delivery


# start
def start_delivery(delivery, test=False):
    from objects import Delivery
    if not isinstance(delivery, Delivery):
        raise TypeError

    from os import path

    # get list of files and directory
    file_list = delivery.file_list()

    # create directory to store files
    if not path.exists(file_list['directory']):
        from os import mkdir
        mkdir(file_list['directory'])

    # start time
    if not path.exists(file_list['start_time']):
        from utility.file import write
        if test is False:
            # set
            delivery.set_start_time()
        # save
        write(delivery.start_time, file_list['start_time'])

    return delivery


# order
def track_order(order, test=False):
    from objects import Order
    if not isinstance(order, Order):
        raise TypeError

    from os import path
    from utility.file import write

    # get list of files for order input
    file_list = order.file_list()
    # make directory to store order files
    if not path.exists(file_list['directory']):
        from os import mkdir
        mkdir(file_list['directory'])
    # id
    if not path.exists(file_list['id']):
        if test is False:
            # input
            order.input_id()
        # save
        write(order.id, file_list['id'])
    # tip
    if not path.exists(file_list['tip']):
        if test is False:
            # input
            order.input_tip()
        # save
        write(order.tip.csv(), file_list['tip'])
    # miles traveled
    if not path.exists(file_list['miles_traveled']):
        if test is False:
            # input
            order.input_miles_traveled()
        # save
        write(order.miles_traveled, file_list['miles_traveled'])
    # end time
    if not path.exists(file_list['end_time']):
        if test is False:
            # set
            order.set_end_time()
        # save
        write(order.end_time, file_list['end_time'])
    # inform order of its completion
    order.in_progress = False

    return order


# split
# enjd
def end_split(split, test=False):
    from objects import Split
    if not isinstance(split, Split):
        raise TypeError

    from os import path
    from utility.file import write

    file_list = split.file_list()

    # miles traveled
    if not path.exists(file_list['distance']):
        if test is False:
            # input
            split.input_miles_traveled()
        # save
        write(split.miles_traveled, file_list['distance'])

    # end time
    if not path.exists(file_list['end_time']):
        if test is False:
            # set
            split.set_end_time()
        # save
        write(split.end_time, file_list['end_time'])

    return split


# start
def start_split(split, test=False):
    from objects import Split
    if not isinstance(split, Split):
        raise TypeError

    from os import path

    file_list = split.file_list()

    # directory
    if not path.exists(file_list['directory']):
        from os import mkdir
        # create directory
        mkdir(file_list['directory'])

    # start time
    if not path.exists(file_list['start_time']):
        from utility.file import write

        if test is False:
            # input
            split.set_start_time()
        # save
        write(split.start_time,  file_list['start_time'])

    return split


# estra stop
def track_extra_stop(extra_stop, test=False):
    from objects import Extra_Stop
    if not isinstance(extra_stop, Extra_Stop):
        raise TypeError

    from objects import Shift
    from os import path
    from utility.file import write

    file_list = extra_stop.file_list()

    # directory
    if not path.exists(file_list['directory']):
        from os import mkdir
        mkdir(file_list['directory'])
    
    # id
    if not extra_stop.id:
        # assign
        extra_stop.assign_id()

    # start time
    if isinstance(extra_stop.parent, Shift):
        if not path.exists(file_list['start_time']):
            if test is False:
                # set
                extra_stop.set_start_time()
            # save
            write(extra_stop.start_time, file_list['start_time'])

    # location
    if not path.exists(file_list['location']):
        if test is False:
            # input
            extra_stop.input_location()
        # save
        write(extra_stop.location, file_list['location'])

    # reason
    if not path.exists(file_list['reason']):
        if test is False:
            # input
            extra_stop.input_reason()
        # save
        write(extra_stop.reason, file_list['reason'])

    # miles traveled
    if not path.exists(file_list['miles_traveled']):
        if test is False:
            # input
            extra_stop.input_miles_traveled()
        # save
        write(extra_stop.miles_traveled, file_list['miles_traveled'])

    # end time
    if not path.exists(file_list['end_time']):
        if test is False:
            # set
            extra_stop.set_end_time()
        # save
        write(extra_stop.end_time, file_list['end_time'])
    # inform extra stop of its completion
    extra_stop.in_progress = True

    return extra_stop
