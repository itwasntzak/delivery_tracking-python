import os

import consolidate_data
import utility_function
import id_number
import input_data


# //TODO: instead of asking if tipped, enter 0.0 for no tip.
# //TODO: write to file 0 instead of n/a
def input_tip():
    while True:
        tip_option = input_data.input_data(
            prompt1='\nDid they tip?    [y/n]\n', input_type1=str,
            prompt2='\nIs this correct?    [y/n]\n', input_type2=str,
            option_yes='y', option_no='n')
        if tip_option == 'y':
            flt = float
            return utility_function.write_data(
                path='delivery', file='tip.txt', data=input_data.input_data(
                    prompt1='\nEnter tip amount:    $#.##\n', input_type1=flt,
                    prompt2='\nIs this correct?    [y/n]\n', input_type2=str,
                    option_yes='y', option_no='n', symbol='$'))
            break
        elif tip_option == 'n':
            return utility_function.write_data(
                path='delivery', file='tip.txt', data='n/a')
            break
        else:
            print('\nInvalid input...')


# //TODO: change to write 1 for card, 2 for cash, 0 in the case of none
def input_tip_type():
    while True:
        tip_type_option = input_data.get_input(
           prompt='\nType of tip?\n1 for card | 2 for cash\n', kind=int)
        if tip_type_option == 1:
            print('\nCard')
            check_correct = input_data.get_input(
               prompt='\nIs this correct?    [y/n]\n', kind=str)
            if check_correct == 'y':
                return utility_function.write_data(
                    path='delivery', file='tip_type.txt', data='cr')
            elif check_correct == 'n':
                continue
            else:
                print('\nInvalid input...')

        elif tip_type_option == 2:
            print('\nCash')
            check_correct = input_data.get_input(
               prompt='\nIs this correct?    [y/n]\n', kind=str)
            if check_correct == 'y':
                return utility_function.write_data(
                    path='delivery', file='tip_type.txt', data='cs')
            elif check_correct == 'n':
                continue
            else:
                print('\nInvalid input...')
        else:
            print('\nInvalid input...')


def order():
    utility_function.write_data(file='order', data=None, path='delivery')
    order_object = Order()
    order_object.order_number = id_number.assign_id_number(order_object)
    order_object.tip = input_tip()
# //TODO: have this evaluation take place in its own function
    if order_object.get_tip() == 'n/a':
        order_object.tip_type = utility_function.write_data(
            path='delivery', file='tip_type.txt', data='n/a')
    else:
        order_object.tip_type = input_tip_type()
    order_object.miles_traveled = utility_function.write_data(
        path='delivery', file='order_miles_traveled.txt',
        data=utility_function.miles_traveled(
            prompt='Order miles traveled:    #.#'))
# save current time for end of order
    order_object.end_time = utility_function.write_data(
        path='delivery', file='order_end_time.txt',
        data=utility_function.now())
    consolidate_data.consolidate_order()
    os.remove(os.path.join('delivery', 'order'))
    return order_object


def get_order_data(path, file):
    order_data = utility_function.read_data(file=file, path=path)
    return order_data.split(',')


class Order:
    def get_order_number(self):
        return self.order_number

    def get_tip(self):
        return self.tip

    def get_tip_type(self):
        return self.tip_type

    def get_miles_traveled(self):
        return self.miles_traveled

    def get_end_time(self):
        return self.end_time
