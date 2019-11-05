# //TODO: still needs to be written
# //TODO: still needs to be refactored


import os
import shutil
import datetime

import consolidate_data
import delivery
import utility_function
import order


# //TODO: need to finish writing continue_delivery
def continue_delivery():
    if os.path.exists(os.path.join('delivery')):
        if os.path.exists(os.path.join('delivery', 'extra_stop')):
            continue_extra_stop()
        elif os.path.exists(os.path.join('delivery', 'order')):
            continue_order()
        else:
            pass
    else:
        pass


def continue_order():
    order_number_path = os.path.join(
        'delivery', 'order_number.txt')
    tip_path = os.path.join(
        'delivery', 'tip.txt')
    tip_type_path = os.path.join(
        'delivery', 'tip_type.txt')
    order_miles_traveled_path = os.path.join(
        'delivery', 'order_miles_traveled.txt')
    order_end_time_path = os.path.join(
        'delivery', 'order_end_time.txt')

    if os.path.exists(order_end_time_path):
        order_object = order.Order()
        order_object.order_number = int(utility_function.read_data(
            file=order_number_path))
        tip_data = utility_function.read_data(tip_path)
        if tip_data == 'n/a':
            order_object.tip = tip_data
        else:
            order_object.tip = float(tip_data)
        order_object.tip_type = utility_function.read_data(
            tip_type_path)
        order_object.miles_traveled = utility_function.read_data(
            order_miles_traveled_path)
    # save current time for end of order
        order_object.end_time = utility_function.read_data(
            order_end_time_path)
        consolidate_data.consolidate_order()

    elif os.path.exists(order_miles_traveled_path):
        order_object = order.Order()
        order_object.order_number = int(utility_function.read_data(
            file=order_number_path))
        tip_data = utility_function.read_data(tip_path)
        if tip_data == 'n/a':
            order_object.tip = tip_data
        else:
            order_object.tip = float(tip_data)
        order_object.tip_type = utility_function.read_data(
            tip_type_path)
        order_object.miles_traveled = utility_function.read_data(
            order_miles_traveled_path)
    # save current time for end of order
        order_object.end_time = utility_function.write_data(
            path='delivery', file='order_end_time.txt',
            data=utility_function.now())
        consolidate_data.consolidate_order()

    elif os.path.exists(tip_type_path):
        order_object = order.Order()
        order_object.order_number = int(utility_function.read_data(
            file=order_number_path))
        tip_data = utility_function.read_data(tip_path)
        if tip_data == 'n/a':
            order_object.tip = tip_data
        else:
            order_object.tip = float(tip_data)
        order_object.tip_type = utility_function.read_data(
            tip_type_path)
        order_object.miles_traveled = utility_function.write_data(
            path='delivery', file='order_miles_traveled.txt',
            data=utility_function.miles_traveled(
                prompt='Order miles traveled:    #.#'))
    # save current time for end of order
        order_object.end_time = utility_function.write_data(
            path='delivery', file='order_end_time.txt',
            data=utility_function.now())
        consolidate_data.consolidate_order()

    elif os.path.exists(tip_path):
        order_object = order.Order()
        order_object.order_number = int(utility_function.read_data(
            file=order_number_path))
        tip_data = utility_function.read_data(tip_path)
        if tip_data == 'n/a':
            order_object.tip = tip_data
        else:
            order_object.tip = float(tip_data)
        if order_object.get_tip() == 'n/a':
            order.tip_type = utility_function.write_data(
                path='delivery', file='tip_type.txt', data='n/a')
        else:
            order_object.tip_type = order.input_tip_type()
        order_object.miles_traveled = utility_function.write_data(
            path='delivery', file='order_miles_traveled.txt',
            data=utility_function.miles_traveled(
                prompt='Order miles traveled:    #.#'))
    # save current time for end of order
        order_object.end_time = utility_function.write_data(
            path='delivery', file='order_end_time.txt',
            data=utility_function.now())
        consolidate_data.consolidate_order()

    elif os.path.exists(order_number_path):
        order_object = order.Order()
        order_object.order_number = int(utility_function.read_data(
            file=order_number_path))
        order_object.tip = order.input_tip()
        if order_object.get_tip() == 'n/a':
            order.tip_type = utility_function.write_data(
                path='delivery', file='tip_type.txt', data='n/a')
        else:
            order_object.tip_type = order.input_tip_type()
        order_object.miles_traveled = utility_function.write_data(
            path='delivery', file='order_miles_traveled.txt',
            data=utility_function.miles_traveled(
                prompt='Order miles traveled:    #.#'))
    # save current time for end of order
        order_object.end_time = utility_function.write_data(
            path='delivery', file='order_end_time.txt',
            data=utility_function.now())
        consolidate_data.consolidate_order()


# //TODO: need to finish writing continue_extra_stop
def continue_extra_stop():
    number_path = os.path.join(
        'delivery', 'extra_stop_number.txt')
    location_path = os.path.join(
        'delivery', 'extra_stop_location.txt')
    reason_path = os.path.join(
        'delivery', 'extra_stop_reason.txt')
    miles_path = os.path.join(
        'delivery', 'extra_stop_miles_traveled.txt')
    end_time_path = os.path.join(
        'delivery', 'extra_stop_end_time.txt')
    extra_stop_numbers_path = os.path.join(
        'delivery', 'extra_stop_numbers.txt')

    if os.path.exists(extra_stop_numbers_path):
        extra_stop_numbers_object = utility_function.read_data(
            extra_stop_numbers_path)
        if ',' in extra_stop_numbers_object:
            extra_stop_numbers_object.split(',')
        else:
            extra_stop_numbers_object
        os.remove(os.path.join('delivery', 'extra_stop'))
    elif os.path.exists(end_time_path):
        consolidate_data.consolidate_extra_stop()
    elif os.path.exists(miles_path):
        pass
    elif os.path.exists(reason_path):
        pass
    elif os.path.exists(location_path):
        pass
    elif os.path.exists(number_path):
        pass
