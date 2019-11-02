import datetime
import os

import extra_stop
import input_data
import order
import consolidate_data
import utility_function


def driving(prompt):
    # creating file so code knows while on delivery, and can continue
    utility_function.write_data(path='delivery', file='delivery', data=None)

    while True:
        wait_for_user = input_data.get_input(
            prompt=prompt + '\n1 after returning | 2 for extra stop\n',
            kind=int)
        if wait_for_user == 1:
            # remove on_delivery file so code can know a delivery has ended
            os.remove(os.path.join('delivery', 'delivery'))
            break
        elif wait_for_user == 2:
            # extra stop option
            extra_stop.extra_stop()
            extra_stop.delivery_number_of_extra_stops()
            continue
        else:
            print('\nInvalid input...')


def input_number_of_orders():
    return utility_function.write_data(
        path='delivery',
        file='number_of_orders.txt',
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
    delivery = Delivery()
    # save the start time of the delivery and add it to the delivery object
    delivery.start_time = utility_function.write_data(
        path='delivery', file='delivery_start_time.txt',
        data=utility_function.now())
    # save the number of order for the delivery and it to the delivedy object
    delivery.number_of_orders = input_number_of_orders()

    for value in range(delivery.get_number_of_orders()):
        # wait for user input after completing order or take extra stop
        driving(prompt='\nDriving to address...')
        # enter data for orders
        order_object = order.order()
        # update/create order_numbers.txt
        order_numbers_file(order_object.get_order_number())
        # display amount of time to complete the order
        utility_function.time_taken(
            start_time=delivery.get_start_time(),
            end_time=order_object.get_end_time(), var_word='Order')
    # driving back to work
    driving(prompt='Driving back to store...')
    # input/save total number of miles traveled and set it to delivery object
    delivery.miles_traveled = utility_function.write_data(
        path='delivery', file='delivery_miles_traveled.txt',
        data=utility_function.miles_traveled(
            prompt='Delivery miles traveled:    #.#'))
    # save end of delivery time and set it to the delivery object
    delivery.end_time = utility_function.write_data(
        path='delivery', file='delivery_end_time.txt',
        data=utility_function.now())
    # display the total time taken on delivery
    utility_function.time_taken(
        start_time=delivery.get_start_time(),
        end_time=delivery.get_end_time(), var_word='Delivery')
    utility_function.delivery_number()
    consolidate_data.consolidate_delivery()


class Delivery:
    def get_start_time(self):
        return self.start_time

    def get_number_of_orders(self):
        return self.number_of_orders

    def get_miles_traveled(self):
        return self.miles_traveled

    def get_end_time(self):
        return self.end_time
