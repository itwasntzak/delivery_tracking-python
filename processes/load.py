
# shift
def load_shift(shift, current=False):
    from objects import Shift
    if not isinstance(shift, Shift):
        raise TypeError

    from objects import Delivery, Extra_Stop, Split
    from os import path
    from utility.file import Read
    from utility.utility import To_Datetime

    file_list = shift.file_list()

    if current is False:
        # shift info
        shift_data = Read(file_list['info']).comma()
        # distance
        shift.miles_traveled = float(shift_data[0])
        # fuel economy
        shift.fuel_economy = float(shift_data[1])
        # vehicle compensation
        shift.vehicle_compensation = float(shift_data[2])
        # device compensation
        shift.device_compensation = float(shift_data[3])
        # extra tips claimed
        shift.extra_tips_claimed = float(shift_data[4])
        # total hours
        shift.total_hours = float(shift_data[5])
        # start time
        shift.start_time = To_Datetime(shift_data[6]).from_datetime()
        # end time
        shift.end_time = To_Datetime(shift_data[7]).from_datetime()

    else:
        # start time
        if path.exists(file_list['start_time']):
            shift.start_time = Read(file_list['start_time']).datetimes()
        # end time
        if path.exists(file_list['end_time']):
            shift.end_time = Read(file_list['end_time']).datetimes()
        # miles traveled
        if path.exists(file_list['miles_traveled']):
            shift.miles_traveled = Read(file_list['miles_traveled']).floats()
        # fuel economy
        if path.exists(file_list['fuel_economy']):
            shift.fuel_economy = Read(file_list['fuel_economy']).floats()
        # vehical compensation
        if path.exists(file_list['vehicle_compensation']):
            shift.vehicle_compensation =\
                Read(file_list['vehicle_compensation']).floats()
        # device compensation
        if path.exists(file_list['device_compensation']):
            shift.device_compensation =\
                Read(file_list['device_compensation']).floats()
        # total hours
        if path.exists(file_list['total_hours']):
            shift.total_hours = Read(file_list['total_hours']).floats()
        # extra tips claimed
        if path.exists(file_list['extra_tips_claimed']):
            shift.extra_tips_claimed =\
                Read(file_list['extra_tips_claimed']).floats()

    return shift


def load_carry_out_tips(shift):
    from objects import Tip
    from utility.file import Read

    file_data = Read(shift.file_list()['tips']).newline()
    for tip in file_data:
        tip_data = tip.split(',')
        shift.carry_out_tips.append(Tip(tip_data[0], tip_data[1], tip_data[2]))

    return shift


def load_shift_deliveries(shift):
    from objects import Delivery
    from os import path
    from utility.file import Read

    deliveries_ids_file = Delivery(shift).file_list()['completed_ids']
    if path.exists(deliveries_ids_file):
        # ids
        shift.delivery_ids = Read(deliveries_ids_file).integers()
        # deliveries
        shift.deliveries =\
            [load_delivery(Delivery(shift, id)) for id in shift.delivery_ids]
    
    return shift


# delivery
def load_delivery(delivery, current=False):
    from objects import Delivery
    if not isinstance(delivery, Delivery):
        # todo: need to write error message
        raise TypeError

    from objects import Extra_Stop, Order
    from os import path
    from utility.file import Read
    from utility.utility import To_Datetime

    # get list of files and directory
    file_list = delivery.file_list()

    if current is False:
        # delivery info
        delivery_data = Read(file_list['info']).comma()
        # miles traveled
        delivery.miles_traveled = float(delivery_data[0])
        # average speed
        delivery.average_speed = int(delivery_data[1])
        # start time
        delivery.start_time = To_Datetime(delivery_data[2]).from_datetime()
        # end time
        delivery.end_time = To_Datetime(delivery_data[3]).from_datetime()

    else:
        # start time
        if path.exists(file_list['start_time']):
            delivery.start_time = Read(file_list['start_time']).datetimes()
        # miles traveled
        if path.exists(file_list['miles_traveled']):
            delivery.miles_traveled = Read(file_list['miles_traveled']).floats()
        # average speed
        if path.exists(file_list['average_speed']):
            delivery.average_speed = Read(file_list['average_speed']).integer()
        # end time
        if path.exists(file_list['end_time']):
            delivery.end_time = Read(file_list['end_time']).datetimes()

    return delivery


def load_delivery_orders(delivery):
    from objects import Order
    order_ids_file = Order(delivery).file_list()['completed_ids']
    if path.exists(order_ids_file):
        # ids
        delivery.order_ids = Read(order_ids_file).integers()
        # orders
        delivery.orders =\
            [Order(delivery, id).load() for id in delivery.order_ids]
    
    return delivery


# order
def load_order(order, current=False):
    from objects import Order
    if not isinstance(order, Order):
        # todo: need to fix error message for taking delivery
        from resources.error_messages import\
            load__order__wrong_parameter as error_message
        raise TypeError(error_message)

    from objects import Tip
    from os import path
    from utility.file import Read
    from utility.utility import To_Datetime

    file_list = order.file_list()

    if current is False:
        # order data
        order_data = Read(order.file_list()['info']).comma()
        # tip
        order.tip = Tip(order_data[0], order_data[1], order_data[2])
        # distance
        order.miles_traveled = float(order_data[3])
        # end time
        order.end_time = To_Datetime(order_data[4]).from_datetime()

    else:
        # tip
        if path.exists(file_list['tip']):
            order.tip = load_tip(file_list['tip'])
        # distance
        if path.exists(file_list['miles_traveled']):
            order.miles_traveled = Read(file_list['miles_traveled']).floats()
        # end time
        if path.exists(file_list['end_time']):
            order.end_time = Read(file_list['end_time']).datetimes()

    return order


# tip
def load_tip(file_path):
    if not isinstance(file_path, str):
        raise TypeError

    from objects import Tip
    from utility.file import Read

    data = Read(file_path).floats()
    return Tip(data[0], data[1], data[2])


# split
def load_split(split, current=False):
    from objects import Split
    if not isinstance(split, Split):
        raise TypeError

    from os import path
    from utility.file import Read
    from utility.utility import To_Datetime

    file_list = split.file_list()

    if current is False:
        # split info
        split_info = Read(file_list['info']).comma()
        # distance
        split.miles_traveled = float(split_info[0])
        # start time
        split.start_time = To_Datetime(split_info[1]).from_datetime()
        # end time
        split.end_time = To_Datetime(split_info[2]).from_datetime()

    else:
        # distance
        if path.exists(file_list['miles_traveled']):
            split.miles_traveled = Read(file_list['miles_traveled']).floats()
        # start time
        if path.exists(file_list['start_time']):
            split.start_time = Read(file_list['start_time']).datetimes()
        # end time
        if path.exists(file_list['end_time']):
            split.end_time = Read(file_list['end_time']).datetimes()

    return split


# extra stop
def load_extra_stop(extra_stop, current=False):
    from objects import Extra_Stop
    if not isinstance(extra_stop, Extra_Stop):
        raise TypeError

    from objects import Delivery, Shift
    from os import path
    from utility.file import Read
    from utility.utility import To_Datetime

    # get files and directory
    file_list = extra_stop.file_list()

    if current is False:
        # extra stop info
        extra_stop_data = Read(file_list['info']).newline()
        # location
        extra_stop.location = extra_stop_data[0]
        # reason
        extra_stop.reason = extra_stop_data[1]
        # distance
        extra_stop.miles_traveled = float(extra_stop_data[2])

        if isinstance(extra_stop.parent, Delivery):
            # end time
            extra_stop.end_time = To_Datetime(extra_stop_data[3]).from_datetime()
        elif isinstance(extra_stop.parent, Shift):
            # start time
            extra_stop.start_time = To_Datetime(extra_stop_data[3]).from_datetime()
            # end time
            extra_stop.end_time = To_Datetime(extra_stop_data[4]).from_datetime()

    else:
        # location
        if path.exists(file_list['location']):
            extra_stop.location = Read(file_list['location']).data
        # reason
        if path.exists(file_list['reason']):
            extra_stop.reason = Read(file_list['reason']).data
        # distance
        if path.exists(file_list['miles_traveled']):
            extra_stop.miles_traveled = Read(file_list['miles_traveled']).floats()
        # end time
        if path.exists(file_list['end_time']):
            extra_stop.end_time = Read(file_list['end_time']).datetimes()

        if isinstance(extra_stop.parent, Shift):
            # start time
            if path.exists(file_list['start_time']):
                extra_stop.start_time = Read(file_list['start_time']).datetimes()

    return extra_stop


def load_parent_extra_stops(parent):
    from objects import Delivery, Shift
    if not isinstance(parent, (Delivery, Shift)):
        raise TypeError

    from objects import Extra_Stop
    from os import path
    from utility.file import Read

    extra_stop_ids_file = Extra_Stop(parent).file_list()['completed_ids']
    if path.exists(extra_stop_ids_file):
        # ids
        parent.extra_stop_ids = Read(extra_stop_ids_file).integers()
        # extra stops
        parent.extra_stops = [load_extra_stop(Extra_Stop(parent, id))
                              for id in parent.extra_stop_ids]
    
    return parent
