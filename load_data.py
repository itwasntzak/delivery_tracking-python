import datetime
import os

import delivery
import extra_stop
import order
import utility


# //TODO: all load_data functions should return classes

def load_order(path, id_number):
    if os.path.exists(path):
        order_data = utility.read_data(path).split(',')
        order_class = order.Order()
        order_class.id_number = int(id_number)
        order_class.tip = float(order_data[0])
        order_class.tip_type = str(order_data[1])
        order_class.miles_traveled = float(order_data[2])
        order_class.end_time = utility.to_datetime(order_data[3])
        return order_class


def load_extras_stop(path, id_number):
    if os.path.exists(path):
        extra_stop_data = utility.read_data(path).split(',')
        extra_stop_class = extra_stop.Extra_stop()
        extra_stop_class.id_number = int(id_number)
        extra_stop_class.location = extra_stop_data[0]
        extra_stop_class.reason = extra_stop_data[1]
        extra_stop_class.miles_traveled = extra_stop_data[2]
        extra_stop_class.end_time = utility.to_datetime(extra_stop_data[3])
        return extra_stop_class


def load_delivery():
    delivery_start_time_path = os.path.join(
        'delivery', 'delivery_start_time.txt')
    number_of_orders_path = os.path.join('delivery', 'number_of_orders.txt')
    number_of_extra_stops_path = os.path.join(
        'delivery', 'number_of_extra_stops.txt')
    order_numbers_path = os.path.join('delivery', 'order_numbers.txt')
    extra_stop_numbers_path = os.path.join(
        'delivery', 'extra_stop_numbers.txt')

    delivery_start_time = utility.to_datetime(
        utility.read_data(delivery_start_time_path))
    if os.path.exists(number_of_orders_path):
        number_of_orders = int(utility.read_data(
            number_of_orders_path))
    else:
        number_of_orders = 0

    if os.path.exists(number_of_extra_stops_path):
        number_of_extra_stops = int(utility.read_data(
            number_of_extra_stops_path))
    else:
        number_of_extra_stops = 0

    if os.path.exists(order_numbers_path):
        if number_of_orders == 1:
            order_numbers = int(utility.read_data(
                order_numbers_path))
        elif number_of_orders > 1:
            order_numbers = utility.read_data(
                order_numbers_path).split(',')
        else:
            pass
    else:
        order_numbers = None

    if os.path.exists(extra_stop_numbers_path):
        if number_of_extra_stops == 1:
            extra_stop_numbers = int(utility.read_data(
                extra_stop_numbers_path))
        elif number_of_extra_stops > 1:
            extra_stop_numbers = utility.read_data(
                extra_stop_numbers_path).split(',')
        else:
            pass
    else:
        extra_stop_numbers = None

    delivery_class = delivery.Delivery()
    delivery_class.start_time = delivery_start_time
    delivery_class.number_of_orders = number_of_orders
    delivery_class.number_of_extra_stops = number_of_extra_stops
    if order_numbers is not None:
        delivery_class.order_numbers = order_numbers
    if extra_stop_numbers is not None:
        delivery_class.extra_stop_numbers = extra_stop_numbers
    return delivery_class


# //TODO: write a split file with a split class
def load_split(path):
    if os.path.exists(path):
        split_data = utility.read_data(path).split(',')
        split_class = split.Split()
        split_class.miles_traveled = float(split_class[0])
        split_class.start_time = utility.to_datetime(split_class[1])
        split_class.end_time = utility.to_datetime(split_class[2])


# //TODO: rewrite shift to return a class
def load_shift():
    shift_path = os.path.join('shift')
    todays_date_path = os.path.join(
        'shift_storage', str(utility.now().today()))

    if os.path.exists(shift_path):
        number_of_deliveries_path = os.path.join(
            'shift', 'number_of_deliveries.txt')
        number_of_extra_stops_path = os.path.join(
            'shift', 'number_of_extra_stops.txt')
        shift_start_time_path = os.path.join('shift', 'shift_start_time.txt')

        shift_start_time = utility.to_datetime(
            utility.read_data(shift_start_time_path))
        if os.path.exists(number_of_deliveries_path):
            number_of_deliveries = int(utility.read_data(
                number_of_deliveries_path))
        if os.path.exists(number_of_extra_stops_path):
            number_of_extra_stops = int(utility.read_data(
                number_of_extra_stops_path))

        if number_of_deliveries and number_of_extra_stops:
            return [number_of_deliveries, number_of_extra_stops,
                    shift_start_time]
        elif number_of_deliveries:
            return [number_of_deliveries, shift_start_time]
        elif number_of_extra_stops:
            return [number_of_extra_stops, shift_start_time]
        else:
            return shift_start_time
    elif os.path.exists(todays_date_path):
        shift_info_path = os.path.join(todays_date_path, 'shift_info.txt')
        return utility.read_data(shift_info_path).split(',')
    else:
        return None
