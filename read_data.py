import datetime
import os

import delivery
import order
import utility


# //TODO: all read_data functions should return classes

# //TODO: tip needs to be changed to check if n/a, or changed to write 0.00
def read_current_order(order_number):
    order_path = os.path.join('delivery', order_number + '.txt')
    if os.path.exists(order_path):
        order_data = utility.read_data(file=order_path).split(',')
        order_class = order.Order()
        order_class.tip = float(order_data[0])
        order_class.tip_type = str(order_data[1])
        order_class.miles_traveled = float(order_data[2])
        order_class.end_time = datetime.datetime.strptime(
            order_data[3], '%Y-%m-%d %H:%M:%S.%f')
        return order_class


def read_today_order(delivery_number, order_number):
    order_path = os.path.join('shift', delivery_number, order_number + '.txt')
    if os.path.exists(order_path):
        order_data = utility.read_data(file=order_path).split(',')
        order_class = order.Order()
        order_class.tip = float(order_data[0])
        order_class.tip_type = str(order_data[1])
        order_class.miles_traveled = float(order_data[2])
        order_class.end_time = datetime.datetime.strptime(
            order_data[3], '%Y-%m-%d %H:%M:%S.%f')
        return order_class


def read_past_order(past_date, delivery_number, order_number):
    order_path = os.path.join(
        'past_shifts', past_date, delivery_number, order_number + '.txt')
    if os.path.exists(order_path):
        order_data = utility.read_data(file=order_path).split(',')
        order_class = order.Order()
        order_class.tip = float(order_data[0])
        order_class.tip_type = str(order_data[1])
        order_class.miles_traveled = float(order_data[2])
        order_class.end_time = datetime.datetime.strptime(
            order_data[3], '%Y-%m-%d %H:%M:%S.%f')
        return order_class


# //TODO: read extra stops function still needs to be writen
def read_extras_stop():
    on_extra_stop_path = os.path.join('delivery', 'extra_stop')
    if os.path.exists(on_extra_stop_path):
        pass


def read_current_delivery():
    delivery_start_time_path = os.path.join(
        'delivery', 'delivery_start_time.txt')
    number_of_orders_path = os.path.join('delivery', 'number_of_orders.txt')
    number_of_extra_stops_path = os.path.join(
        'delivery', 'number_of_extra_stops.txt')
    order_numbers_path = os.path.join('delivery', 'order_numbers.txt')
    extra_stop_numbers_path = os.path.join(
        'delivery', 'extra_stop_numbers.txt')

    delivery_start_time = datetime.datetime.strptime(
        utility.read_data(delivery_start_time_path),
        '%Y-%m-%d %H:%M:%S.%f')
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

# //TODO: need to write read today delivery
def read_today_delivery(delivery_number):
    delivery_path = os.path.join('shift', delivery_number)
    if os.path.exists(delivery_path):
        pass


# //TODO: need to write read past delivery
def read_past_delivery(past_date, delivery_number):
    pass


# //TODO: need to rewrite read split, chaned it to today and past
def read_split():
    split_start_time_path = os.path.join('shift', 'split_start_time.txt')
    split_info_path = os.path.join('shift', 'split_info.txt')

    if os.path.exists(split_start_time_path):
        return datetime.datetime.strptime(utility.read_data(
            split_start_time_path), '%Y-%m-%d %H:%M:%S.%f')
    elif os.path.exists(split_info_path):
        return utility.read_data(split_info_path).split(',')
    else:
        return None


# //TODO: rewrite shift to return a class
def read_shift():
    shift_path = os.path.join('shift')
    todays_date_path = os.path.join(
        'shift_storage', str(utility.now().today()))

    if os.path.exists(shift_path):
        number_of_deliveries_path = os.path.join(
            'shift', 'number_of_deliveries.txt')
        number_of_extra_stops_path = os.path.join(
            'shift', 'number_of_extra_stops.txt')
        shift_start_time_path = os.path.join('shift', 'shift_start_time.txt')

        shift_start_time = datetime.datetime.strptime(
            utility.read_data(shift_start_time_path),
            '%Y-%m-%d %H:%M:%S.%f')
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


# //TODO: rewrite to return a class of the shift
def read_past_shift(date):
    shift_path = os.path.join('shift_storage', date)
    if os.path.exists(shift_path):
        shift_info_path = os.path.join(shift_path, 'shift_info.txt')
        return utility.read_data(shift_info_path).split(',')
    else:
        return None
