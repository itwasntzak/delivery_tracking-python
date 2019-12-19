# //TODO: function to change id number files after already assigning

from os import path

import delivery
import extra_stop
import input_data
import order
import shift
import utility


def assign_id_number(object):
    if isinstance(object, type(shift.Shift())):
        return str(utility.now().date())

    elif isinstance(object, type(delivery.Delivery())):
        file_path = path.join('shift', 'delivery_id_number.txt')
        if path.exists(file_path):
            return utility.write_data(
                file_path, int(utility.read_data(file_path)) + 1)
        else:
            return utility.write_data(file_path, 0)

    elif isinstance(object, type(order.Order())):
        return utility.write_data(
            path.join('delivery', 'order_number.txt'),
            input_data.input_data(
                prompt1='\nEnter order number:    #-####\n', input_type1=int,
                prompt2='\nIs this correct? [y/n]\n', input_type2=str,
                option_yes='y', option_no='n'))

    elif isinstance(object, type(extra_stop.Extra_Stop())):
        file_path = path.join('shift', 'extra_stop_id_number.txt')
        if path.exists(file_path):
            return utility.write_data(
                file_path,
                int(utility.read_data(file_path)) + 1)
        else:
            return utility.write_data(file_path, 0)


# //TODO: finish writing for other instances
def id_number_file(object):
    if isinstance(object, type(shift.Shift())):
        pass

    elif isinstance(object, type(order.Order())):
        file_path = path.join('delivery', 'order_numbers.txt')
        if path.exists(file_path):
            utility.append_data(file_path, ',' + str(object.get_id_number()))
        else:
            utility.write_data(file_path, object.get_id_number())

    elif isinstance(object, type(extra_stop.Extra_Stop())):
        file_path = path.join(object.get_directory(), 'extra_stop_numbers.txt')
        if path.exists(file_path):
            utility.append_data(file_path, ',' + str(object.get_id_number()))
        else:
            utility.write_data(file_path, object.get_id_number())
