import csv
import os

import utility_function


delivery_path = 'delivery'
shift_delivery_path = os.path.join(
    'shift', 'delivery' + utility_function.delivery_number('number')
)
shift_delivery_order_path = os.path.join(
    'shift', 'delivery' + utility_function.delivery_number('number'), 'orders'
)


def consolidate_order():
    order_number = utility_function.read_data(
        path=delivery_path,
        file='order_number.txt'
    )
    tip = utility_function.read_data(
        path=delivery_path,
        file='tip.txt'
    )
    tip_type = utility_function.read_data(
        path=delivery_path,
        file='tip_type.txt'
    )
    miles_traveled = utility_function.read_data(
        path=delivery_path,
        file='miles_traveled.txt'
    )
    order_end_time = utility_function.read_data(
        path=delivery_path,
        file='order_end_time.txt'
    )

    data = tip + ',' + tip_type + ',' + miles_traveled + ',' + order_end_time
    utility_function.write_data(
        path=delivery_path,
        file=order_number + '.txt',
        data=data
    )

    os.remove(os.path.join(delivery_path, 'order_number.txt'))
    os.remove(os.path.join(delivery_path, 'tip.txt'))
    os.remove(os.path.join(delivery_path, 'tip_type.txt'))
    os.remove(os.path.join(delivery_path, 'miles_traveled.txt'))
    os.remove(os.path.join(delivery_path, 'order_end_time.txt'))
    return order_number


def consolidate_extra_stop():
    extra_stop_number = utility_function.read_data(
        path=delivery_path,
        file='extra_stop_number.txt'
    )
    location = utility_function.read_data(
        path=delivery_path,
        file='extra_stop_location.txt'
    )
    reason = utility_function.read_data(
        path=delivery_path,
        file='extra_stop_reason.txt'
    )
    miles_traveled = utility_function.read_data(
        path=delivery_path,
        file='extra_stop_miles_traveled.txt'
    )
    end_time = utility_function.read_data(
        path=delivery_path,
        file='extra_stop_end_time.txt'
    )
    utility_function.write_data(
        path=delivery_path,
        file=extra_stop_number + '.txt',
        data=location + ',' + reason + ',' + miles_traveled + ',' + end_time
    )
    os.remove(os.path.join(delivery_path, 'extra_stop_number.txt'))
    os.remove(os.path.join(delivery_path, 'extra_stop_location.txt'))
    os.remove(os.path.join(delivery_path, 'extra_stop_reason.txt'))
    os.remove(os.path.join(delivery_path, 'extra_stop_miles_traveled.txt'))
    os.remove(os.path.join(delivery_path, 'extra_stop_end_time.txt'))
    return extra_stop_number


def consolidate_delivery():
    number_of_orders = utility_function.read_data(
        path=delivery_path,
        file='number_of_orders.txt'
    )
    number_of_extra_stops_path = os.path.join(
        delivery_path, 'number_of_extra_stops.txt'
    )
    if not os.path.exists(number_of_extra_stops_path):
        utility_function.write_data(
            path='',
            file=number_of_extra_stops_path,
            data=0
        )
    number_of_extra_stops = utility_function.read_data(
        path=delivery_path,
        file='number_of_extra_stops.txt'
    )
    miles_traveled = utility_function.read_data(
        path=delivery_path,
        file='miles_traveled.txt'
    )
    delivery_start_time = utility_function.read_data(
        path=delivery_path,
        file='delivery_start_time.txt'
    )
    delivery_end_time = utility_function.read_data(
        path=delivery_path,
        file='delivery_end_time.txt'
    )
    data = number_of_orders + ',' + number_of_extra_stops + ','\
        + miles_traveled + ',' + delivery_start_time + ',' + delivery_end_time
    utility_function.write_data(
        path=delivery_path,
        file='delivery_info.txt',
        data=data
    )
    os.remove(os.path.join(delivery_path, 'number_of_orders.txt'))
    os.remove(os.path.join(delivery_path, 'number_of_extra_stops.txt'))
    os.remove(os.path.join(delivery_path, 'miles_traveled.txt'))
    os.remove(os.path.join(delivery_path, 'delivery_start_time.txt'))
    os.remove(os.path.join(delivery_path, 'delivery_end_time.txt'))
