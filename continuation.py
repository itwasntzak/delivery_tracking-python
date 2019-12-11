# //TODO: still needs to be written
# //TODO: still needs to be refactored


import datetime
from os import path, remove
import shutil

import consolidate_data
from continue_extra_stop import continue_extra_stop
from continue_order import continue_order
import delivery
import extra_stop
import id_number
import input_data
import order
import shift
import utility


# //TODO: if number of orders has not been entered, deliv start time still exist need to add logic for this
def continuation():
    if path.exists(path.join('shift', 'extra_stop')):
        continue_extra_stop(shift.Shift())
    elif path.exists(path.join('delivery')):
        delivery_object = delivery.Delivery()
        delivery_object.start_time = utility.to_datetime(utility.read_data(
            path.join('delivery', 'delivery_start_time.txt')))
        delivery_object.order_quantity = int(utility.read_data(
            path.join('delivery', 'order_quantity.txt')))
        if path.exists(path.join('delivery', 'extra_stop')):
            continue_extra_stop(delivery_object)
        elif path.exists(path.join('delivery', 'order')):
            continue_order()
        elif path.exists(path.join('delivery', 'driving')):
            prompt = '\nDriving to address...'
            while True:
                wait_for_user = input_data.get_input(
                    prompt=prompt + '\n1 after returning | 2 for extra stop\n',
                    kind=int)
                if wait_for_user == 1:
                    # remove driving file so code can knows driving has ended
                    remove(path.join('delivery', 'driving'))
                    break
                elif wait_for_user == 2:
                    # remove driving file so code can knows driving has ended
                    remove(path.join('delivery', 'driving'))
                    # extra stop option
                    extra_stop.extra_stop(delivery_object)
                    continue
                else:
                    print('\nInvalid input...')
        else:
            order_quantity = delivery_object.get_order_quantity()
            if path.exists(path.join('delivery', 'order_numbers.txt')):
                completed_orders = utility.read_data(
                    path.join('delivery', 'order_numbers.txt')).split(',')
            else:
                completed_orders = 0
                for value in range(order_quantity):
                    # wait for user input after completing order or take extra stop
                    delivery.driving(delivery_object, '\nDriving to address...')
                    # enter data for orders
                    order_object = order.order()
                    # update/create order_numbers.txt
                    id_number.id_number_file(order_object.get_id_number())
                    # display amount of time to complete the order
                    utility.time_taken(
                        start_time=delivery_object.get_start_time(),
                        end_time=order_object.get_end_time(), var_word='Order')
                    completed_orders = utility.read_data(
                        path.join('delivery', 'order_numbers.txt')).split(',')
            if order_quantity > len(completed_orders):
                for value in range(order_quantity - len(completed_orders)):
                    # wait for user input after completing order or take extra stop
                    delivery.driving(delivery_object, '\nDriving to address...')
                    # enter data for orders
                    order_object = order.order()
                    # update/create order_numbers.txt
                    id_number.id_number_file(order_object.get_id_number())
                    # display amount of time to complete the order
                    utility.time_taken(
                        start_time=delivery_object.get_start_time(),
                        end_time=order_object.get_end_time(), var_word='Order')
            elif order_quantity == len(completed_orders):
                pass
            # driving back to work
            delivery.driving(delivery_object, 'Driving back to store...')
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
            consolidate_data.consolidate_delivery()
            shutil.move('delivery', path.join(
                'shift', str(delivery_object.get_id_number())))
            return delivery_object
