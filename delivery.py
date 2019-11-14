import datetime
import os
import shutil

import extra_stop
import id_number
import input_data
import order
import consolidate_data
import utility_function


def driving(delivery_object, prompt):
    # creating file so code knows while on delivery, and can continue
    utility_function.write_data(file='driving', data=None, path='delivery')

    while True:
        wait_for_user = input_data.get_input(
            prompt=prompt + '\n1 after returning | 2 for extra stop\n',
            kind=int)
        if wait_for_user == 1:
            # remove on_delivery file so code can know a delivery has ended
            os.remove(os.path.join('delivery', 'driving'))
            break
        elif wait_for_user == 2:
            # extra stop option
            extra_stop.extra_stop(delivery_object)
            continue
        else:
            print('\nInvalid input...')


def input_order_quantity():
    return utility_function.write_data(
        path='delivery', file='order_quantity.txt',
        data=input_data.input_data(
            prompt1='\nNumber of orders?\n', input_type1=int,
            prompt2='\nIs this correct? [y/n]\n', input_type2=str,
            option_yes='y', option_no='n'))


def order_numbers_file(order_number):
    if os.path.exists(os.path.join('delivery', 'order_numbers.txt')):
        utility_function.append_data(
            file='order_numbers.txt',
            data=',' + str(order_number),
            path='delivery')
    else:
        utility_function.write_data(
            path='delivery', file='order_numbers.txt',
            data=order_number)


def delivery():
    # make folder to store data
    os.mkdir('delivery')
    # set veriable to a delivery class object
    delivery_object = Delivery()
    # save the start time of the delivery and add it to the delivery object
    delivery_object.start_time = utility_function.write_data(
        path='delivery', file='delivery_start_time.txt',
        data=utility_function.now())
    # save the number of order for the delivery and it to the delivedy object
    delivery_object.number_of_orders = input_order_quantity()

    for value in range(delivery_object.get_number_of_orders()):
        # wait for user input after completing order or take extra stop
        driving(delivery_object, '\nDriving to address...')
        # enter data for orders
        order_object = order.order()
        # update/create order_numbers.txt
        order_numbers_file(order_object.get_order_number())
        # display amount of time to complete the order
        utility_function.time_taken(
            start_time=delivery_object.get_start_time(),
            end_time=order_object.get_end_time(), var_word='Order')
    # driving back to work
    driving(delivery_object, 'Driving back to store...')
    # input/save total number of miles traveled and set it to delivery object
    delivery_object.miles_traveled = utility_function.write_data(
        path='delivery', file='delivery_miles_traveled.txt',
        data=utility_function.miles_traveled(
            prompt='Delivery miles traveled:    #.#'))
    # save end of delivery time and set it to the delivery object
    delivery_object.end_time = utility_function.write_data(
        path='delivery', file='delivery_end_time.txt',
        data=utility_function.now())
    # display the total time taken on delivery
    utility_function.time_taken(
        start_time=delivery_object.get_start_time(),
        end_time=delivery_object.get_end_time(),
        var_word='Delivery')
    delivery_object.id_number = id_number.assign_id_number(delivery_object)
    consolidate_data.consolidate_delivery()
    shutil.move('delivery', os.path.join(
        'shift', str(delivery_object.get_id_number())))
    return delivery_object


class Delivery:
    def get_id_number(self):
        return self.id_number

    def get_start_time(self):
        return self.start_time

    def get_number_of_orders(self):
        return self.number_of_orders

    def get_miles_traveled(self):
        return self.miles_traveled

    def get_end_time(self):
        return self.end_time
