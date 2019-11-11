import os

import utility_function


def consolidate_order():
    order_number_path = os.path.join('delivery', 'order_number.txt')
    tip_path = os.path.join('delivery', 'tip.txt')
    tip_type_path = os.path.join('delivery', 'tip_type.txt')
    miles_traveled_path = os.path.join('delivery', 'order_miles_traveled.txt')
    order_end_time_path = os.path.join('delivery', 'order_end_time.txt')

    order_number = utility_function.read_data(file=order_number_path)
    tip = utility_function.read_data(file=tip_path)
    tip_type = utility_function.read_data(file=tip_type_path)
    miles_traveled = utility_function.read_data(file=miles_traveled_path)
    order_end_time = utility_function.read_data(file=order_end_time_path)

    data = tip + ',' + tip_type + ',' + miles_traveled + ',' + order_end_time
    utility_function.write_data(
        path='delivery', file=order_number + '.txt', data=data)

    os.remove(order_number_path)
    os.remove(tip_path)
    os.remove(tip_type_path)
    os.remove(miles_traveled_path)
    os.remove(order_end_time_path)


def consolidate_extra_stop():
    extra_stop_number_path = os.path.join('delivery', 'extra_stop_number.txt')
    extra_stop_location_path = os.path.join(
        'delivery', 'extra_stop_location.txt')
    extra_stop_reason_path = os.path.join('delivery', 'extra_stop_reason.txt')
    extra_stop_miles_traveled_path = os.path.join(
        'delivery', 'extra_stop_miles_traveled.txt')
    extra_stop_end_time_path = os.path.join(
        'delivery', 'extra_stop_end_time.txt')

    extra_stop_number = utility_function.read_data(extra_stop_number_path)
    location = utility_function.read_data(extra_stop_location_path)
    reason = utility_function.read_data(extra_stop_reason_path)
    extra_stop_miles_traveled = utility_function.read_data(
        extra_stop_miles_traveled_path)
    end_time = utility_function.read_data(extra_stop_end_time_path)

    utility_function.write_data(
        path='delivery', file=extra_stop_number + '.txt',
        data=location + ','
             + reason + ','
             + extra_stop_miles_traveled + ','
             + end_time)
    os.remove(extra_stop_number_path)
    os.remove(extra_stop_location_path)
    os.remove(extra_stop_reason_path)
    os.remove(extra_stop_miles_traveled_path)
    os.remove(extra_stop_end_time_path)
    return extra_stop_number


def consolidate_delivery():
    number_of_orders_path = os.path.join('delivery', 'order_quantity.txt')
    number_of_extra_stops_path = os.path.join(
        'delivery', 'extra_stop_quantity.txt')
    miles_traveled_path = os.path.join(
        'delivery', 'delivery_miles_traveled.txt')
    delivery_start_time_path = os.path.join(
        'delivery', 'delivery_start_time.txt')
    delivery_end_time_path = os.path.join('delivery', 'delivery_end_time.txt')

    if not os.path.exists(number_of_extra_stops_path):
        utility_function.write_data(
            path='', file=number_of_extra_stops_path, data=0)

    number_of_orders = utility_function.read_data(number_of_orders_path)
    number_of_extra_stops = utility_function.read_data(
        number_of_extra_stops_path)
    miles_traveled = utility_function.read_data(miles_traveled_path)
    delivery_start_time = utility_function.read_data(delivery_start_time_path)
    delivery_end_time = utility_function.read_data(delivery_end_time_path)

    data = number_of_orders + ',' + number_of_extra_stops + ','\
        + miles_traveled + ',' + delivery_start_time + ',' + delivery_end_time
    utility_function.write_data(
        path='delivery', file='delivery_info.txt', data=data)

    os.remove(number_of_orders_path)
    os.remove(number_of_extra_stops_path)
    os.remove(miles_traveled_path)
    os.remove(delivery_start_time_path)
    os.remove(delivery_end_time_path)


def consolidate_split():
    split_miles_traveled_path = os.path.join(
        'shift', 'split_miles_traveled.txt')
    split_start_time_path = os.path.join('shift', 'split_start_time.txt')
    split_end_time_path = os.path.join('shift', 'split_end_time.txt')

    split_miles_traveled = utility_function.read_data(
        split_miles_traveled_path)
    split_start_time = utility_function.read_data(split_start_time_path)
    split_end_time = utility_function.read_data(split_end_time_path)

    data = split_miles_traveled + ',' + split_start_time + ',' + split_end_time
    utility_function.write_data(path='shift', file='split_info.txt', data=data)

    os.remove(split_miles_traveled_path)
    os.remove(split_start_time_path)
    os.remove(split_end_time_path)


def consolidate_shift():
    number_of_deliveries_path = os.path.join(
        'shift', 'number_of_deliveries.txt')
    number_of_extra_stops_path = os.path.join(
        'shift', 'number_of_extra_stops.txt')
    shift_start_time_path = os.path.join('shift', 'shift_start_time.txt')
    shift_end_time_path = os.path.join('shift', 'shift_end_time.txt')

    if not os.path.exists(number_of_deliveries_path):
        utility_function.write_data(
            path='', file=number_of_deliveries_path, data=0)
    if not os.path.exists(number_of_extra_stops_path):
        utility_function.write_data(
            path='', file=number_of_extra_stops_path, data=0)

    number_of_deliveries = utility_function.read_data(
        number_of_deliveries_path)
    number_of_extra_stops = utility_function.read_data(
        number_of_extra_stops_path)
    shift_start_time = utility_function.read_data(shift_start_time_path)
    shift_end_time = utility_function.read_data(shift_end_time_path)

    data = number_of_deliveries + ',' + number_of_extra_stops + ','\
        + shift_start_time + ',' + shift_end_time
    utility_function.write_data(
        path='shift', file='shift_info.txt', data=data)

    os.remove(number_of_deliveries_path)
    os.remove(number_of_extra_stops_path)
    os.remove(shift_start_time_path)
    os.remove(shift_end_time_path)
