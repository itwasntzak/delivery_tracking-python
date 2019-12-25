from os import path, remove

import consolidate_data
import id_number
import order
import utility


def continue_order():
    id_number_path = path.join('delivery', 'order_number.txt')
    tip_path = path.join('delivery', 'tip.txt')
    tip_type_path = path.join('delivery', 'tip_type.txt')
    miles_path = path.join('delivery', 'order_miles_traveled.txt')
    end_time_path = path.join('delivery', 'order_end_time.txt')

    order_object = order.Order()
    if path.exists(id_number_path):
        order_object.id_number = int(utility.read_data(id_number_path))
    if path.exists(tip_path):
        order_object.tip = float(utility.read_data(tip_path))
    if path.exists(tip_type_path):
        order_object.tip_type = int(utility.read_data(tip_type_path))
    if path.exists(miles_path):
        order_object.miles_traveled = float(utility.read_data(miles_path))
    if path.exists(end_time_path):
        order_object.end_time = utility.to_datetime(
            utility.read_data(end_time_path))

    if path.exists(end_time_path):
        # update/create order_numbers.txt
        id_number.id_number_file(order_object)
    elif path.exists(miles_path):
        # save/assign current time for end of order
        order_object.end_time = utility.write_data(
            end_time_path, utility.now())
        # update/create order_numbers.txt
        id_number.id_number_file(order_object)
    elif path.exists(tip_type_path):
        # input the miles since prev destination
        order_object.miles_traveled = utility.write_data(
            miles_path, utility.miles_traveled('Order miles traveled:    #.#'))
        # save/assign current time for end of order
        order_object.end_time = utility.write_data(
            end_time_path, utility.now())
        # update/create order_numbers.txt
        id_number.id_number_file(order_object)
    elif path.exists(tip_path):
        # input the tip type. if no tip, automaticly inputs
        order_object.tip_type = order.input_tip_type(order_object)
        # input the miles since prev destination
        order_object.miles_traveled = utility.write_data(
            miles_path, utility.miles_traveled('Order miles traveled:    #.#'))
        # save/assign current time for end of order
        order_object.end_time = utility.write_data(
            end_time_path, utility.now())
        # update/create order_numbers.txt
        id_number.id_number_file(order_object)
    elif path.exists(id_number_path):
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
            end_time_path, utility.now())
        # update/create order_numbers.txt
        id_number.id_number_file(order_object)
    else:
        # input the order number as a form of id
        order_object.id_number = id_number.assign_id_number(order_object)
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
        # update/create order_numbers.txt
        id_number.id_number_file(order_object)

    # consolidate order files into one file
    consolidate_data.consolidate_order(order_object)
    # remove file telling program order has ended
    remove(path.join('delivery', 'order'))
    # return order class object to the function that called this one
    return order_object
