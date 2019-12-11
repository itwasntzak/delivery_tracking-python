from os import path, remove

import consolidate_data
import id_number
import input_data
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
    else:
        while True:
            completed_order_check = input_data.get_input(
                'Have you completed any orders yet?\n[y/n]\n', str)
            if completed_order_check == 'y':
                # input the order number as a form of id
                order_object.id_number = id_number.assign_id_number(
                    order_object)
# //TODO: figure out how to do this differently, currently very confusing
                order_file_path = path.join('delivery',
                                            str(order_object.get_id_number())
                                            + '.txt')
                remove(path.join('delivery', 'order_number.txt'))
                order_file = utility.read_data(order_file_path).split(',')
                order_object.tip = float(order_file[0])
                order_object.tip_type = int(order_file[1])
                order_object.miles_traveled = float(order_file[2])
                order_object.end_time = utility.to_datetime(order_file[3])
                break
            elif completed_order_check == 'n':
                order_file_path = ''
                break
            else:
                print('\nInvalid input...')
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
        # consolidate order files into one file
        consolidate_data.consolidate_order()
    elif path.exists(miles_path):
        # save/assign current time for end of order
        order_object.end_time = utility.write_data(
            end_time_path, utility.now())
        # consolidate order files into one file
        consolidate_data.consolidate_order()
    elif path.exists(tip_type_path):
        # input the miles since prev destination
        order_object.miles_traveled = utility.write_data(
            miles_path, utility.miles_traveled('Order miles traveled:    #.#'))
        # save/assign current time for end of order
        order_object.end_time = utility.write_data(
            end_time_path, utility.now())
        # consolidate order files into one file
        consolidate_data.consolidate_order()
    elif path.exists(tip_path):
        # input the tip type. if no tip, automaticly inputs
        order_object.tip_type = order.input_tip_type(order_object)
        # input the miles since prev destination
        order_object.miles_traveled = utility.write_data(
            miles_path, utility.miles_traveled('Order miles traveled:    #.#'))
        # save/assign current time for end of order
        order_object.end_time = utility.write_data(
            end_time_path, utility.now())
        # consolidate order files into one file
        consolidate_data.consolidate_order()
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
        # consolidate order files into one file
        consolidate_data.consolidate_order()
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
        # consolidate order files into one file
        consolidate_data.consolidate_order()

    # remove file telling program order has ended
    remove(path.join('delivery', 'order'))
    # return order class object to the function that called this one
    return order_object
