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


def continuation():
    while True:
        if path.exists(path.join('shift', 'extra_stop')):
            continue_extra_stop(shift.Shift())
            continue
        elif path.exists(path.join('delivery')):
            delivery_start_time_path = path.join(
                'delivery', 'delivery_start_time.txt')
            order_quantity_path = path.join('delivery', 'order_quantity.txt')
            miles_traveled_path = path.join(
                'delivery', 'delivery_miles_traveled.txt')
            delivery_end_time_path = path.join(
                'delivery', 'delivery_end_time.txt')

            delivery_object = delivery.Delivery()
            if path.exists(delivery_start_time_path):
                delivery_object.start_time = utility.to_datetime(utility.read_data(
                    delivery_start_time_path))
            if path.exists(order_quantity_path):
                delivery_object.order_quantity = int(utility.read_data(
                    order_quantity_path))
            else:
                delivery_object.order_quantity = delivery.input_order_quantity()
            if path.exists(miles_traveled_path):
                delivery_object.miles_traveled = utility.read_data(
                    miles_traveled_path)
            if path.exists(delivery_end_time_path):
                delivery_object.end_time = utility.to_datetime(
                    utility.read_data(delivery_end_time_path))

            if path.exists(path.join('delivery', 'extra_stop')):
                continue_extra_stop(delivery_object)
                continue
            elif path.exists(path.join('delivery', 'order')):
                continue_order()
                continue
            elif path.exists(path.join('delivery', 'driving-address')):
                prompt = '\nDriving to address...'
                while True:
                    wait_for_user = input_data.get_input(
                        prompt + '\n1 after returning | 2 for extra stop\n',
                        int)
                    if wait_for_user == 1:
                        # remove driving file so code can knows driving has ended
                        remove(path.join('delivery', 'driving-address'))
                        break
                    elif wait_for_user == 2:
                        # remove driving file so code can knows driving has ended
                        remove(path.join('delivery', 'driving-address'))
                        # extra stop option
                        extra_stop.extra_stop(delivery_object)
                        break
                    else:
                        print('\nInvalid input...')
                continue
            else:
                order_quantity = delivery_object.get_order_quantity()
                order_numbers_file_path = path.join(
                    'delivery', 'order_numbers.txt')
                if path.exists(order_numbers_file_path):
                    completed_orders = len(utility.read_data(
                        order_numbers_file_path).split(','))
                else:
                    completed_orders = 0
                    for value in range(order_quantity):
                        # wait for user input after completing order or take extra stop
                        delivery.driving(
                            delivery_object,
                            '\nDriving to address...',
                            'address')
                        # enter data for orders
                        order_object = order.order()
                        # display amount of time to complete the order
                        utility.time_taken(
                            start_time=delivery_object.get_start_time(),
                            end_time=order_object.get_end_time(),
                            var_word='Order')
                        completed_orders = len(utility.read_data(path.join(
                            'delivery', 'order_numbers.txt')).split(','))
                if order_quantity > completed_orders:
                    for value in range(order_quantity - completed_orders):
                        # wait for user input after completing order or take extra stop
                        delivery.driving(
                            delivery_object,
                            '\nDriving to address...',
                            'address')
                        # enter data for orders
                        order_object = order.order()
                        # update/create order_numbers.txt
                        id_number.id_number_file(order_object.get_id_number())
                        # display amount of time to complete the order
                        utility.time_taken(
                            start_time=delivery_object.get_start_time(),
                            end_time=order_object.get_end_time(),
                            var_word='Order')
                elif order_quantity == completed_orders:
                    pass

                if path.exists(delivery_end_time_path):
                    pass
                elif path.exists(miles_traveled_path):
                    # save end of delivery time and set it to the delivery object
                    delivery_object.end_time = utility.write_data(
                        delivery_end_time_path, utility.now())
                else:
                    # driving back to work
                    delivery.driving(
                        delivery_object, 'Driving back to store...', 'store')
                    # input/save total number of miles traveled and set it to delivery object
                    delivery_object.miles_traveled = utility.write_data(
                        miles_traveled_path, utility.miles_traveled(
                            'Delivery miles traveled:    #.#'))
                    delivery_object.end_time = utility.write_data(
                        delivery_end_time_path, utility.now())

                # display the total time taken on delivery
                utility.time_taken(
                    start_time=delivery_object.get_start_time(),
                    end_time=delivery_object.get_end_time(),
                    var_word='Delivery')
                delivery_object.id_number = id_number.assign_id_number(
                    delivery_object)
                consolidate_data.consolidate_delivery(delivery_object)
                shutil.move('delivery', path.join(
                    'shift', str(delivery_object.get_id_number())))
                return delivery_object
        else:
            break
