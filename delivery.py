import datetime
from os import mkdir, path, remove
import shutil

import extra_stop
import id_number
import input_data
import order
import consolidate_data
import utility


def driving(delivery_object, prompt, destination):
    while True:
        # create file so code knows while driving, and can continue from there
        utility.write_data(path.join('delivery', 'driving-' + destination), None)
        wait_for_user = input_data.get_input(
            prompt=prompt + '\n1 after returning | 2 for extra stop\n',
            kind=int)
        if wait_for_user == 1:
            # remove driving file so code can knows driving has ended
            remove(path.join('delivery', 'driving-' + destination))
            break
        elif wait_for_user == 2:
            # remove driving file so code can knows driving has ended
            remove(path.join('delivery', 'driving-' + destination))
            # extra stop option
            extra_stop.extra_stop(delivery_object)
            continue
        else:
            print('\nInvalid input...')


def input_order_quantity():
    return utility.write_data(
        path.join('delivery', 'order_quantity.txt'),
        input_data.input_data(
            prompt1='\nNumber of orders?\n', input_type1=int,
            prompt2='\nIs this correct? [y/n]\n', input_type2=str,
            option_yes='y', option_no='n'))


# //TODO: remove quantity files, and instead use len() to check amount in list
def delivery():
    # make folder to store data
    mkdir('delivery')
    # set veriable to a delivery class object
    delivery_object = Delivery()
    # save the start time of the delivery and add it to the delivery object
    delivery_object.start_time = utility.write_data(
        path.join('delivery', 'delivery_start_time.txt'), utility.now())
    # save the number of order for the delivery and it to the delivedy object
    delivery_object.order_quantity = input_order_quantity()

    for value in range(delivery_object.get_order_quantity()):
        # wait for user input after completing order or take extra stop
        driving(delivery_object, '\nDriving to address...', 'address')
        # enter data for orders
        order_object = order.order()
        # display amount of time to complete the order
        utility.time_taken(
            start_time=delivery_object.get_start_time(),
            end_time=order_object.get_end_time(), var_word='Order')
    # driving back to work
    driving(delivery_object, 'Driving back to store...', 'store')
    # input/save total number of miles traveled and set it to delivery object
    delivery_object.miles_traveled = utility.write_data(
        path.join('delivery', 'delivery_miles_traveled.txt'),
        utility.miles_traveled('Delivery miles traveled:    #.#'))
    # save end of delivery time and set it to the delivery object
    delivery_object.end_time = utility.write_data(
        path.join('delivery', 'delivery_end_time.txt'), utility.now())
    # display the total time taken on delivery
    utility.time_taken(
        start_time=delivery_object.get_start_time(),
        end_time=delivery_object.get_end_time(),
        var_word='Delivery')
    delivery_object.id_number = id_number.assign_id_number(delivery_object)
    consolidate_data.consolidate_delivery(delivery_object)
    shutil.move('delivery', path.join(
        'shift', str(delivery_object.get_id_number())))
    return delivery_object


class Delivery:
    def get_id_number(self):
        return self.id_number

    def get_start_time(self):
        return self.start_time

    def get_order_quantity(self):
        return self.order_quantity

    def get_miles_traveled(self):
        return self.miles_traveled

    def get_end_time(self):
        return self.end_time
