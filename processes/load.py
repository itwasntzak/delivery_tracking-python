
def current_shift():
    from objects.shift import Shift
    from os import path
    from utility.file import Read
    from utility.utility import now

    shift = Shift(now().date())
    file_list = shift.file_list()

    # start time
    if not path.exists(file_list['start_time']):
        from utility.file import write
        shift.start_time = now()
        write(shift.start_time, file_list['start_time'])
    else:
        shift.start_time = Read(file_list['start_time']).datetimes()

    # delivery
    from objects.delivery import Delivery
    if path.exists(Delivery(shift).file_list()['completed_ids']):
        shift.delivery_ids =\
            Read(Delivery(shift).file_list()['completed_ids']).integers()
        shift.deliveries = [delivery(shift, id) for id in shift.delivery_ids]

    # extra stops
    from objects.extra_stop import Extra_Stop
    if path.exists(Extra_Stop(shift, 0).file_list()['completed_ids']):
        from processes.load import shift_extra_stop as load_extra_stop
        shift.extra_stop_ids =\
            Read(Extra_Stop(shift).file_list()['completed_ids']).integers()
        shift.extra_stops =\
            [load_extra_stop(shift, id) for id in shift.extra_stop_ids]

    # carry out tips
    if path.exists(file_list['tips']):
        shift.carry_out_tips = carry_out_tips(shift)

    # split
    from objects.split import Split
    if path.exists(Split(shift).file_list()['info']):
        shift.split = split(shift)

    return shift


def shift(shift_id):
    from objects.shift import Shift
    from os import path
    from utility.file import Read
    from utility.utility import now

    if not isinstance(shift_id, type(now().date())):
        # todo: write error message for this
        raise TypeError

    print(shift_id)
    shift = Shift(shift_id)
    shift_info_file = shift.file_list()['info']

    if not path.exists(shift_info_file):
        # todo: need to figure out how to handle this
        # probably tell user info file doesnt exist and ask if they want to input data for it
        raise FileNotFoundError

    from utility.utility import To_Datetime
    # shift info
    shift_data = Read(shift_info_file).comma()
    shift.miles_traveled = float(shift_data[0])
    shift.fuel_economy = float(shift_data[1])
    shift.vehicle_compensation = float(shift_data[2])
    shift.device_compensation = float(shift_data[3])
    shift.extra_tips_claimed = float(shift_data[4])
    shift.total_hours = float(shift_data[5])
    shift.start_time = To_Datetime(shift_data[6]).from_datetime()
    shift.end_time = To_Datetime(shift_data[7]).from_datetime()

    # delivery
    from objects.delivery import Delivery
    deliveries_ids_file = Delivery(shift).file_list()['completed_ids']
    if path.exists(deliveries_ids_file):
        shift.delivery_ids = Read(deliveries_ids_file).integers()
        shift.deliveries = [delivery(shift, id) for id in shift.delivery_ids]

    # extra stops
    from objects.extra_stop import Extra_Stop
    extra_stop_ids_file = Extra_Stop(shift).file_list()['completed_ids']
    if path.exists(extra_stop_ids_file):
        shift.extra_stop_ids = Read(extra_stop_ids_file).integers()
        shift.extra_stops =\
            [shift_extra_stop(shift, id) for id in shift.extra_stop_ids]

    # carry out tips
    if path.exists(shift.file_list()['tips']):
        shift.carry_out_tips = carry_out_tips(shift)

    # split
    from objects.split import Split
    if path.exists(Split(shift).file_list()['info']):
        shift.split = split(shift)

    return shift


def delivery(shift, id):
    from objects.shift import Shift
    if not isinstance(shift, Shift):
        # todo: need to write error message
        raise TypeError

    from objects.delivery import Delivery
    from os import path

    delivery = Delivery(shift, id)
    delivery_file = delivery.file_list()['info']

    # delivery info
    if path.exists(delivery_file):
        from utility.file import Read
        delivery_data = Read(delivery_file).comma()

        from utility.utility import To_Datetime
        delivery.miles_traveled = float(delivery_data[0])
        delivery.average_speed = int(delivery_data[1])
        delivery.start_time = To_Datetime(delivery_data[2]).from_datetime()
        delivery.end_time = To_Datetime(delivery_data[3]).from_datetime()

    # orders
    from objects.order import Order
    order_ids_file = Order(delivery).file_list()['completed_ids']
    if path.exists(order_ids_file):
        from utility.file import Read
        delivery.order_ids = Read(order_ids_file).integers()
        delivery.orders = [order(delivery, id) for id in delivery.order_ids]

    # extra stops
    from objects.extra_stop import Extra_Stop
    if path.exists(Extra_Stop(delivery).file_list()['completed_ids']):
        from processes.load import delivery_extra_stop as load_extra_stop
        delivery.extra_stop_ids =\
            Read(Extra_Stop(delivery).file_list()['completed_ids']).integers()
        delivery.extra_stops =\
            [load_extra_stop(delivery, id) for id in delivery.extra_stop_ids]

    return delivery


def order(delivery, id):
    from objects.delivery import Delivery
    if not isinstance(delivery, Delivery):
        # todo: need to fix error message for taking delivery
        from resources.error_messages import\
            load__order__wrong_parameter as error_message
        raise TypeError(error_message)

    from objects.order import Order
    order = Order(delivery, id)
    order_file = order.file_list()['info']

    from os import path
    if path.exists(order_file):
        from utility.file import Read
        order_data = Read(order_file).comma()

        from objects.tip import Tip
        from utility.utility import To_Datetime
        order.tip = tip(tip_data=order_data)
        order.miles_traveled = float(order_data[3])
        order.end_time = To_Datetime(order_data[4]).from_datetime()
        return order

    # else:
    #     # todo: present user with the option to change the id
    #     # todo: present user with option to enter data for the order
    #     # todo: present user with option to remove the order id
    #     from resources.error_messages import Order__load__file_not_found
    #     raise FileNotFoundError(Order__load__file_not_found)


def tip(file_path=None, tip_data=None):
    """
    file_path=sting of file path or\n
    tip_data=list/tuple
    """
    from objects.tip import Tip
    from utility.file import Read
    if isinstance(file_path, str):
        # todo: this needs work, doesn't count for file not found
        data = Read(file_path).floats()
        tip = Tip(data[0], data[1], data[2])
    elif file_path:
        raise TypeError

    if isinstance(tip_data, (list, tuple)):
        tip = Tip(tip_data[0], tip_data[1], tip_data[2])
    elif tip_data:
        raise TypeError

    return tip


def carry_out_tips(shift):
    from utility.file import Read

    carry_out_tips = []
    temp_carry_out_tips = Read(shift.file_list()['tips']).newline()
    for tip_data in temp_carry_out_tips:
        carry_out_tips.append(tip(tip_data=tip_data.split(',')))

    return carry_out_tips


def split(shift):
    from objects.split import Split
    from utility.file import Read

    split = Split(shift)

    try:
        split_info = Read(split.file_list()['info']).comma()
    except FileNotFoundError:
        # todo: figure out how to handle this, shouldnt occer but idk
        pass
    else:
        from utility.utility import To_Datetime

        split.miles_traveled = float(split_info[0])
        split.start_time = To_Datetime(split_info[1]).from_datetime()
        split.end_time = To_Datetime(split_info[2]).from_datetime()

        return split


def shift_extra_stop(shift, id):
    from objects.extra_stop import Extra_Stop
    from utility.file import Read

    extra_stop = Extra_Stop(shift, id)
    try:
        extra_stop_data = Read(extra_stop.file_list()['info']).newline()
    except FileNotFoundError:
        # todo: need to figure out how to handle this
        pass
    else:
        from utility.utility import To_Datetime
        extra_stop.location = extra_stop_data[0]
        extra_stop.reason = extra_stop_data[1]
        extra_stop.miles_traveled = float(extra_stop_data[2])
        extra_stop.start_time = To_Datetime(extra_stop_data[3]).from_datetime()
        extra_stop.end_time = To_Datetime(extra_stop_data[4]).from_datetime()

        return extra_stop


def delivery_extra_stop(delivery, id):
    from objects.extra_stop import Extra_Stop
    from utility.file import Read

    extra_stop = Extra_Stop(delivery, id)
    try:
        extra_stop_data = Read(extra_stop.file_list()['info']).newline()
    except FileNotFoundError:
        # todo: need to figure out how to handle this
        pass
    else:
        from utility.utility import To_Datetime
        extra_stop.location = extra_stop_data[0]
        extra_stop.reason = extra_stop_data[1]
        extra_stop.miles_traveled = float(extra_stop_data[2])
        extra_stop.end_time = To_Datetime(extra_stop_data[3]).from_datetime()

        return extra_stop
