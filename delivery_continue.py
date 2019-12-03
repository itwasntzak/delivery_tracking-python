# //TODO: still needs to be written
# //TODO: still needs to be refactored


from os import path, remove
import shutil
import datetime

import consolidate_data
import delivery
import id_number
import utility
import order


# //TODO: need to finish writing continue_delivery
def continue_delivery():
    if path.exists(path.join('delivery')):
        if path.exists(path.join('delivery', 'extra_stop')):
            continue_extra_stop()
        elif path.exists(path.join('delivery', 'order')):
            continue_order()
        else:
            pass
    else:
        pass


def continue_order():
    order_object = order.Order()
    if path.exists(path.join('delivery', 'order_number.txt')):
        order_object.id_number = utility.read_data(
            path.join('delivery', 'order_number.txt'))
    else:
        # input the order number as a form of id
        order_object.id_number = id_number.assign_id_number(order_object)

    if path.exists(path.join('delivery', 'tip.txt')):
        order_object.tip = utility.read_data(
            path.join('delivery', 'tip.txt'))

    if path.exists(path.join('delivery', 'tip_type.txt')):
        order_object.tip_type = utility.read_data(
            path.join('delivery', 'tip_type.txt'))

    if path.exists(path.join('delivery', 'order_miles_traveled.txt')):
        order_object.miles_traveled = utility.read_data(
            path.join('delivery', 'order_miles_traveled.txt'))

    if path.exists(path.join('delivery', 'order_end_time.txt')):
        order_object.end_time = utility.read_data(
            path.join('delivery', 'order_end_time.txt'))

    order_file = path.join('delivery',
                           str(order_object.get_id_number()) + '.txt')
    if path.exists(order_file):
        pass
    elif order_object.end_time:
        # consolidate order files into one file
        consolidate_data.consolidate_order()
    elif order_object.miles_traveled:
        # save/assign current time for end of order
        order_object.end_time = utility.write_data(
            path.join('delivery', 'order_end_time.txt'), utility.now())
        # consolidate order files into one file
        consolidate_data.consolidate_order()
    elif order_object.tip_type:
        # input the miles since prev destination
        order_object.miles_traveled = utility.write_data(
            path.join('delivery', 'order_miles_traveled.txt'),
            utility.miles_traveled('Order miles traveled:    #.#'))
        # save/assign current time for end of order
        order_object.end_time = utility.write_data(
            path.join('delivery', 'order_end_time.txt'), utility.now())
        # consolidate order files into one file
        consolidate_data.consolidate_order()
    elif order_object.tip:
        # input the tip type. if no tip, automaticly inputs
        order_object.tip_type = order.input_tip_type(order_object)
        # input the miles since prev destination
        order_object.miles_traveled = utility.write_data(
            path.join('delivery', 'order_miles_traveled.txt'),
            utility.miles_traveled('Order miles traveled:    #.#'))
        # save/assign current time for end of order
        order_object.end_time = utility.write_data(
            path.join('delivery', 'order_end_time.txt'), utility.now())
        # consolidate order files into one file
        consolidate_data.consolidate_order()
    elif order_object.id_number:
        # input the tip amount, or if tipped at all
        order_object.tip = order.input_tip()
        # input the tip type. if no tip, automaticly inputs
        order_object.tip_type = order.input_tip_type(order_object)
        # input the miles since prev destination
        order_object.miles_traveled = utility.write_data(
            path.join('delivery', 'order_miles_traveled.txt'),
            utility.miles_traveled('Order miles traveled:    #.#'))
        # save/assign current time for end of order
        order_object.end_time = utility.write_data(
            path.join('delivery', 'order_end_time.txt'), utility.now())
        # consolidate order files into one file
        consolidate_data.consolidate_order()

    # remove file telling program order has ended
    remove(path.join('delivery', 'order'))
    # return order class object to the function that called this one
    return order_object


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
