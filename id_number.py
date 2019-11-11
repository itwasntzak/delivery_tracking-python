import os

import delivery
import extra_stop
import input_data
import order
import utility_function


# //TODO: need to work on function to change id number after already assigning


def assign_id_number(object):
    if isinstance(object, type(delivery.Delivery())):
        file_path = os.path.join('shift', 'delivery_quantity.txt')
        if os.path.exists(file_path):
            return utility_function.write_data(
                file=file_path,
                data=int(utility_function.read_data(file=file_path)) + 1)
        else:
            return utility_function.write_data(file=file_path, data=0)

    elif isinstance(object, type(order.Order())):
        return utility_function.write_data(
            path='delivery', file='order_number.txt',
            data=input_data.input_data(
                prompt1='\nEnter order number:    #-####\n', input_type1=int,
                prompt2='\nIs this correct? [y/n]\n', input_type2=str,
                option_yes='y', option_no='n'))

    elif isinstance(object, type(extra_stop.Extra_Stop())):
        file_path = os.path.join('shift', 'extra_stop_number.txt')
        if os.path.exists(file_path):
            return utility_function.write_data(
                file=file_path,
                data=int(utility_function.read_data(file_path)) + 1)
        else:
            return utility_function.write_data(file_path, 0)


# TODO: write a function to write id_number_files
