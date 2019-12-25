import os

import consolidate_data
import id_number
import input_data
import utility


# //TODO: add the ability to add a split tip amount/type
def input_tip():
    file_path = os.path.join('delivery', 'tip.txt')
    while True:
        tip_amount = input_data.get_input(
            '\nEnter tip amount:    $#.##\n(if no tip, enter 0)\n$', float)
        if tip_amount == 0.0:
            user_confirm = input_data.get_input(
                '\nNo tip\nIs this correct?    [y/n]\n', str)
            if user_confirm == 'y':
                return utility.write_data(file_path, 0.0)
            elif user_confirm == 'n':
                continue
            else:
                print('Invalid input...')
        else:
            user_confirm = input_data.get_input(
                '\n$' + str(tip_amount) + '\nIs this correct?    [y/n]\n', str)
            if user_confirm == 'y':
                return utility.write_data(file_path, tip_amount)
            elif user_confirm == 'n':
                continue
            else:
                print('Invalid input...')


def input_tip_type(order_object):
    file_path = os.path.join('delivery', 'tip_type.txt')
    if order_object.get_tip() == 0.0:
        return utility.write_data(file_path, 0)
    else:
        while True:
            user_option = input_data.get_input(
                '\nType of tip?\n1 for card | 2 for cash\n', int)
            if user_option == 1:
                check_correct = input_data.get_input(
                   '\nCard\nIs this correct?    [y/n]\n', str)
                if check_correct == 'y':
                    return utility.write_data(file_path, 1)
                elif check_correct == 'n':
                    continue
                else:
                    print('\nInvalid input...')
            elif user_option == 2:
                check_correct = input_data.get_input(
                    '\nCash\nIs this correct?    [y/n]\n', str)
                if check_correct == 'y':
                    return utility.write_data(file_path, 2)
                elif check_correct == 'n':
                    continue
                else:
                    print('\nInvalid input...')
            else:
                print('\nInvalid input...')


def order():
    # create file, program knows order was started
    utility.write_data(os.path.join('delivery', 'order'), None)
    # create variable assigned to an order class
    order_object = Order()
    # input the order number as a form of id
    order_object.id_number = id_number.assign_id_number(order_object)
    # input the tip amount, or if tipped at all
    order_object.tip = input_tip()
    # input the tip type. if no tip, automaticly inputs
    order_object.tip_type = input_tip_type(order_object)
    # input the miles since prev destination
    order_object.miles_traveled = utility.write_data(
        os.path.join('delivery', 'order_miles_traveled.txt'),
        utility.miles_traveled('Order miles traveled:    #.#'))
    # save/assign current time for end of order
    order_object.end_time = utility.write_data(
        os.path.join('delivery', 'order_end_time.txt'), utility.now())
    # update/create order_numbers.txt
    id_number.id_number_file(order_object)
    # consolidate order files into one file
    consolidate_data.consolidate_order(order_object)
    # remove file telling program order has ended
    os.remove(os.path.join('delivery', 'order'))
    # return order class object to the function that called this one
    return order_object


class Order:
    def get_id_number(self):
        return self.id_number

    def get_tip(self):
        return self.tip

    def get_tip_type(self):
        return self.tip_type

    def get_miles(self):
        return self.miles_traveled

    def get_end_time(self):
        return self.end_time
