from os import path, remove

import input_data
from utility import append_data, now, read_data, time_taken,\
    to_datetime, write_data


# function to check if order id number file exists
def check_id_number(delivery):
    if path.exists(delivery.id_path):
        return int(read_data(delivery.id_path))
    else:
        return write_data(delivery.id_path, delivery.input_id_number())


class Order:
    def __init__(self, delivery, id=''):
        self.parent = delivery
        self.path = delivery.path
        if id == '':
            self.id_path = path.join(self.path, 'order_id.txt')
            if not path.exists(self.id_path):
                self.id = self.input_id_number()
            else:
                self.id = int(read_data(self.id_path))
        else:
            self.id = id
        # list of all paths
        self.tip_path = path.join(self.path, 'tip.txt')
        self.tip_type_path = path.join(self.path, 'tip_type.txt')
        self.miles_path = path.join(self.path, 'order_miles_traveled.txt')
        self.end_time_path = path.join(self.path, 'order_end_time.txt')
        self.order_file_path = path.join(self.path, str(self.id) + '.txt')

    # methods for order tracking
    def consolidate(self):
        # todo: reformat strings with format
        data = str(self.tip) + ','\
            + str(self.tip_type) + ','\
            + str(self.miles_traveled) + ','\
            + str(self.end_time)
        write_data(self.order_file_path, data)
        # remove files that are no longer needed
        remove(self.id_path)
        remove(self.tip_path)
        remove(self.tip_type_path)
        remove(self.miles_path)
        remove(self.end_time_path)
        # update/create order_numbers.txt
        self.update_id_file()
        # remove file telling program, order is in progress
        remove(path.join(self.path, 'order'))

    def load(self):
        # todo: need to take into account missing data
        order_data = read_data(self.order_file_path).split(',')
        self.tip = float(order_data[0])
        self.tip_type = int(order_data[1])
        self.miles_traveled = float(order_data[2])
        self.end_time = to_datetime(order_data[3])
        return self

    def start(self):
        # create file, program knows order was started
        write_data(path.join(self.path, 'order'), None)
        # input the tip amount, or if tipped at all
        self.tip = self.input_tip()
        # input the tip type. if no tip, automaticly inputs
        self.tip_type = self.input_tip_type()
        # input the miles since prev destination
        self.miles_traveled = self.input_miles_traveled()
        # save/assign current time for end of order
        self.end_time = write_data(self.end_time_path, now())
        # consolidate order files into one file
        self.consolidate()
        # display amount of time to complete the order
        time_taken(self.parent.start_time, self.end_time,
                   'Order completed in:\t')
        # return order class object to the function that called it
        return self

    def update_id_file(self):
        if path.exists(self.parent.order_ids_path):
            append_data(self.parent.order_ids_path, ',' + str(self.id))
        else:
            write_data(self.parent.order_ids_path, self.id)

    # methods for inputting data
    def input_miles_traveled(self):
        return write_data(self.miles_path, input_data.input_data(
            f"\n{'Order miles traveled:':<10}{'#.#':>8}\n", float,
            ' miles\n'
            f"{'Is this correct?':<10}{'[y/n]':>13}\n", str, 'y', 'n'))

    def input_id_number(self):
        # todo: reformat strings with format
        return write_data(self.id_path, input_data.input_data(
            f"\n{'Enter order number:':<10}{'#-####':>11}\n", int,
            f"\n{'Is this correct?':<10}{'[y/n]':>14}\n", str, 'y', 'n'))

    def input_tip(self):
        # todo: add the ability to add a split tip amount/type
        while True:
            tip_amount = input_data.get_input(
                f"\n{'Enter tip amount:':<10}{'$#.##':>12}\n"
                '(if no tip, enter 0)\n$',
                float)
            if tip_amount == 0.0:
                user_confirm = input_data.get_input(
                    '\nNo tip'
                    f"\n{'Is this correct?':<10}{'[y/n]':>13}\n", str)
                if user_confirm == 'y':
                    return write_data(self.tip_path, 0.0)
                elif user_confirm == 'n':
                    continue
                else:
                    print('Invalid input...')
            else:
                user_confirm = input_data.get_input(
                    f"\n{'$'}{tip_amount}\n"
                    f"{'Is this correct?':<10}{'[y/n]':>13}\n", str)
                if user_confirm == 'y':
                    return write_data(self.tip_path, tip_amount)
                elif user_confirm == 'n':
                    continue
                else:
                    print('Invalid input...')

    def input_tip_type(self):
        no_tip = 0
        card = 1
        cash = 2
        if self.tip == 0.0:
            return write_data(self.tip_type_path, no_tip)
        else:
            while True:
                user_option = input_data.get_input(
                    '\nType of tip?\n'
                    '1. For card\n'
                    '2. For cash\n', int)
                if user_option == 1:
                    check_correct = input_data.get_input(
                       '\nCard\n'
                       f"{'Is this correct?':<10}{'[y/n]':>13}\n", str)
                    if check_correct == 'y':
                        return write_data(self.tip_type_path, card)
                    elif check_correct == 'n':
                        continue
                    else:
                        print('\nInvalid input...')
                elif user_option == 2:
                    check_correct = input_data.get_input(
                        '\nCash\n'
                        f"{'Is this correct?':<10}{'[y/n]':>13}\n", str)
                    if check_correct == 'y':
                        return write_data(self.tip_type_path, cash)
                    elif check_correct == 'n':
                        continue
                    else:
                        print('\nInvalid input...')
                else:
                    print('\nInvalid input...')

    # methods for continuing tracking if program ends
    def load_current(self):
        if path.exists(self.tip_path):
            self.tip = float(read_data(self.tip_path))
        if path.exists(self.tip_type_path):
            self.tip_type = int(read_data(self.tip_type_path))
        if path.exists(self.miles_path):
            self.miles_traveled = float(read_data(self.miles_path))
        if path.exists(self.end_time_path):
            self.end_time = to_datetime(read_data(self.end_time_path))
        self.resume()
        return self

    def resume(self):
        while True:
            if not path.exists(self.tip_path):
                # input the tip amount, or if tipped at all
                self.tip = self.input_tip()
            elif not path.exists(self.tip_type_path):
                # input the tip type. if no tip, automaticly inputs
                self.tip_type = self.input_tip_type()
            elif not path.exists(self.miles_path):
                # input the miles since prev destination
                self.miles_traveled = self.input_miles_traveled()
            elif not path.exists(self.end_time_path):
                # save/assign current time for end of order
                self.end_time = write_data(self.end_time_path, now())
            else:
                break
        # consolidate order files into one file
        self.consolidate()
        # display amount of time to complete the order
        time_taken(self.parent.start_time, self.end_time,
                   'Order completed in:\t')
        return self
