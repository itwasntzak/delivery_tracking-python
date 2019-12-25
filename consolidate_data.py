# //TODO: change these function to work with the classes
# //TODO: consider moving consol/read data functions into each class

from os import path, remove

import utility


def consolidate_order(order_object):
    order_id_path = path.join('delivery', 'order_number.txt')
    tip_path = path.join('delivery', 'tip.txt')
    tip_type_path = path.join('delivery', 'tip_type.txt')
    miles_traveled_path = path.join('delivery', 'order_miles_traveled.txt')
    order_end_time_path = path.join('delivery', 'order_end_time.txt')

    order_id = str(order_object.get_id_number())
    tip = str(order_object.get_tip())
    tip_type = str(order_object.get_tip_type())
    miles_traveled = str(order_object.get_miles())
    order_end_time = str(order_object.get_end_time())

    file_path = path.join('delivery', order_id + '.txt')
    data = tip + ',' + tip_type + ',' + miles_traveled + ',' + order_end_time
    utility.write_data(file_path, data)

    remove(order_id_path)
    remove(tip_path)
    remove(tip_type_path)
    remove(miles_traveled_path)
    remove(order_end_time_path)


def consolidate_extra_stop(extra_stop_object):
    directory = extra_stop_object.get_directory()
    extra_stop_id_path = path.join(directory, 'extra_stop_number.txt')
    extra_stop_location_path = path.join(directory, 'extra_stop_location.txt')
    extra_stop_reason_path = path.join(directory, 'extra_stop_reason.txt')
    extra_stop_miles_path = path.join(directory, 'extra_stop_miles.txt')
    extra_stop_end_time_path = path.join(directory, 'extra_stop_end_time.txt')

    extra_stop_id = str(extra_stop_object.get_id_number())
    location = str(extra_stop_object.get_location())
    reason = str(extra_stop_object.get_reason())
    extra_stop_miles = str(extra_stop_object.get_miles())
    end_time = str(extra_stop_object.get_end_time())

    utility.write_data(
        path.join(directory, extra_stop_id + '.txt'),
        location + ',' + reason + ',' + extra_stop_miles + ',' + end_time)
    remove(extra_stop_id_path)
    remove(extra_stop_location_path)
    remove(extra_stop_reason_path)
    remove(extra_stop_miles_path)
    remove(extra_stop_end_time_path)


def consolidate_delivery():
    order_quantity_path = path.join('delivery', 'order_quantity.txt')
    extra_stop_quantity_path = path.join('delivery', 'extra_stop_quantity.txt')
    miles_traveled_path = path.join('delivery', 'delivery_miles_traveled.txt')
    delivery_start_time_path = path.join('delivery', 'delivery_start_time.txt')
    delivery_end_time_path = path.join('delivery', 'delivery_end_time.txt')

    if not path.exists(extra_stop_quantity_path):
        utility.write_data(extra_stop_quantity_path, 0)

    order_quantity = utility.read_data(order_quantity_path)
    extra_stop_quantity = utility.read_data(extra_stop_quantity_path)
    miles_traveled = utility.read_data(miles_traveled_path)
    delivery_start_time = utility.read_data(delivery_start_time_path)
    delivery_end_time = utility.read_data(delivery_end_time_path)

    data = order_quantity + ',' + extra_stop_quantity + ','\
        + miles_traveled + ',' + delivery_start_time + ',' + delivery_end_time
    utility.write_data(path.join('delivery', 'delivery_info.txt'), data)

    remove(order_quantity_path)
    remove(extra_stop_quantity_path)
    remove(miles_traveled_path)
    remove(delivery_start_time_path)
    remove(delivery_end_time_path)


def consolidate_split():
    split_miles_path = path.join('shift', 'split_miles_traveled.txt')
    split_start_time_path = path.join('shift', 'split_start_time.txt')
    split_end_time_path = path.join('shift', 'split_end_time.txt')

    split_miles = utility.read_data(split_miles_path)
    split_start_time = utility.read_data(split_start_time_path)
    split_end_time = utility.read_data(split_end_time_path)

    data = split_miles + ',' + split_start_time + ',' + split_end_time
    utility.write_data(path.join('shift', 'split_info.txt'), data)

    remove(split_miles_path)
    remove(split_start_time_path)
    remove(split_end_time_path)


def consolidate_shift():
    delivery_id_number_path = path.join('shift', 'delivery_id_number.txt')
    extra_stop_quantity_path = path.join('shift', 'extra_stop_quantity.txt')
    shift_start_time_path = path.join('shift', 'shift_start_time.txt')
    shift_end_time_path = path.join('shift', 'shift_end_time.txt')
    total_miles_path = path.join('shift', 'total_miles_traveled.txt')
    fuel_economy_path = path.join('shift', 'fuel_economy.txt')
    mileage_paid_path = path.join('shift', 'mileage_paid.txt')
    extra_tips_claimed_path = path.join('shift', 'extra_tips_claimed.txt')
    total_hours_path = path.join('shift', 'total_hours.txt')

    if not path.exists(delivery_id_number_path):
        delivery_quantity = str(utility.write_data(
            delivery_id_number_path, 0))
    else:
        delivery_quantity = str(int(utility.read_data(
            delivery_id_number_path)) + 1)

    if not path.exists(extra_stop_quantity_path):
        extra_stop_quantity = str(utility.write_data(
            extra_stop_quantity_path, 0))
    else:
        extra_stop_quantity = utility.read_data(extra_stop_quantity_path)

    shift_start_time = utility.read_data(shift_start_time_path)
    shift_end_time = utility.read_data(shift_end_time_path)
    total_miles = utility.read_data(total_miles_path)
    fuel_economy = utility.read_data(fuel_economy_path)
    mileage_paid = utility.read_data(mileage_paid_path)
    extra_tips_claimed = utility.read_data(extra_tips_claimed_path)
    total_hours = utility.read_data(total_hours_path)

    shift_info_path = path.join('shift', 'shift_info.txt')
    data = delivery_quantity + ',' + extra_stop_quantity + ','\
        + total_miles + ',' + fuel_economy + ',' + mileage_paid + ','\
        + extra_tips_claimed + ',' + total_hours + ','\
        + shift_start_time + ',' + shift_end_time
    utility.write_data(shift_info_path, data)

    remove(delivery_id_number_path)
    remove(extra_stop_quantity_path)
    remove(shift_start_time_path)
    remove(shift_end_time_path)
    remove(total_miles_path)
    remove(fuel_economy_path)
    remove(mileage_paid_path)
    remove(extra_tips_claimed_path)
    remove(total_hours_path)
    remove(path.join('shift', 'extra_stop_id_number.txt'))
