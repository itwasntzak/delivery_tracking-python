
# shift
# end
def end_shift(shift):
    from objects import Shift
    if not isinstance(shift, Shift):
        raise TypeError

    from os import path
    from utility.file import write

    # get list of files and directory
    file_list = shift.file_list()

    # end time
    if not path.exists(file_list['end_time']):
        if not shift.end_time:
            # set
            shift.set_end_time()
        # save
        write(shift.end_time, file_list['end_time'])

    # distance
    if not path.exists(file_list['miles_traveled']):
        if not shift.miles_traveled:
            # input
            shift.input_miles_traveled()
        # save
        write(shift.miles_traveled, file_list['miles_traveled'])

    # fuel economy
    if not path.exists(file_list['fuel_economy']):
        if not shift.fuel_economy:
            # input
            shift.input_fuel_economy()
        # save
        write(shift.fuel_economy, file_list['fuel_economy'])

    # vehicle compensation
    if not path.exists(file_list['vehicle_compensation']):
        if not shift.vehicle_compensation:
            # input
            shift.input_vehicle_compensation()
        # save
        write(shift.vehicle_compensation, file_list['vehicle_compensation'])

    # device compensation
    if not path.exists(file_list['device_compensation']):
        if not shift.device_compensation:
            # input
            shift.input_device_compensation()
        # save
        write(shift.device_compensation, file_list['device_compensation'])

    # total hours
    if not path.exists(file_list['total_hours']):
        if not shift.total_hours:
            # input
            shift.input_total_hours()
        # save
        write(shift.total_hours, file_list['total_hours'])

    # extra tips claimed
    if not path.exists(file_list['extra_tips_claimed']):
        if not shift.extra_tips_claimed:
            # input
            shift.input_extra_tips_claimed()
        # save
        write(shift.extra_tips_claimed, file_list['extra_tips_claimed'])

    return shift


# start
def start_shift(shift):
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
        if not shift.start_time:
            # set
            shift.set_start_time()
        # save
        write(shift.start_time, file_list['start_time'])

    return shift


# delivery
# end
def end_delivery(delivery):
    from objects import Delivery
    if not isinstance(delivery, Delivery):
        raise TypeError

    from os import path
    from utility.file import write

    # get list of files and directory
    file_list = delivery.file_list()

    # miles traveled
    if not path.exists(file_list['miles_traveled']):
        if not delivery.miles_traveled:
            # input
            delivery.input_miles_traveled()
        # save
        write(delivery.miles_traveled, file_list['miles_traveled'])

    # average speed
    if not path.exists(file_list['average_speed']):
        if not delivery.average_speed:
            # input
            delivery.input_average_speed()
        # save
        write(delivery.average_speed, file_list['average_speed'])

    # end time
    if not path.exists(file_list['end_time']):
        if not delivery.end_time:
            # set
            delivery.input_end_time()
        # save
        write(delivery.end_time, file_list['end_time'])

    return delivery


# start
def start_delivery(delivery):
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
        if not delivery.start_time:
            # set
            delivery.input_start_time()
        # save
        write(delivery.start_time, file_list['start_time'])

    return delivery


# order
def track_order(order):
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
        if not order.id:
            # input
            order.input_id()
        # save
        write(order.id, file_list['id'])

    # tip
    if not path.exists(file_list['tip']):
        if not order.tip:
            # input
            order.input_tip()
        # save
        write(order.tip.csv(), file_list['tip'])

    # miles traveled
    if not path.exists(file_list['miles_traveled']):
        if not order.miles_traveled:
            # input
            order.input_miles_traveled()
        # save
        write(order.miles_traveled, file_list['miles_traveled'])

    # end time
    if not path.exists(file_list['end_time']):
        if not order.end_time:
            # set
            order.set_end_time()
        # save
        write(order.end_time, file_list['end_time'])

    return order


# split
# enjd
def end_split(split):
    from objects import Split
    if not isinstance(split, Split):
        raise TypeError

    from os import path
    from utility.file import write

    file_list = split.file_list()

    # miles traveled
    if not path.exists(file_list['miles_traveled']):
        if not split.miles_traveled:
            # input
            split.input_miles_traveled()
        # save
        write(split.miles_traveled, file_list['miles_traveled'])

    # end time
    if not path.exists(file_list['end_time']):
        if not split.end_time:
            # set
            split.input_end_time()
        # save
        write(split.end_time, file_list['end_time'])

    return split


# start
def start_split(split):
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

        if not split.start_time:
            # input
            split.input_start_time()
        # save
        write(split.start_time,  file_list['start_time'])

    return split


# estra stop
def track_extra_stop(extra_stop):
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
            if not extra_stop.start_time:
                # set
                extra_stop.set_start_time()
            # save
            write(extra_stop.start_time, file_list['start_time'])

    # location
    if not path.exists(file_list['location']):
        if not extra_stop.location:
            # input
            extra_stop.input_location()
        # save
        write(extra_stop.location, file_list['location'])

    # reason
    if not path.exists(file_list['reason']):
        if not extra_stop.reason:
            # input
            extra_stop.input_reason()
        # save
        write(extra_stop.reason, file_list['reason'])

    # miles traveled
    if not path.exists(file_list['miles_traveled']):
        if not extra_stop.miles_traveled:
            # input
            extra_stop.input_miles_traveled()
        # save
        write(extra_stop.miles_traveled, file_list['miles_traveled'])

    # end time
    if not path.exists(file_list['end_time']):
        if not extra_stop.end_time:
            # set
            extra_stop.set_end_time()
        # save
        write(extra_stop.end_time, file_list['end_time'])

    return extra_stop
