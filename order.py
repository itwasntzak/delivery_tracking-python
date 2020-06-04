from os import path, remove

from input_data import get_input, input_data
from utility import append_data, now, read_data, time_taken,\
    to_datetime, write_data


class Order:
    def __init__(self, delivery, id=''):
        self.parent = delivery
        self.path = delivery.path
        if id == '':
            self.id_path = path.join(self.path, 'order_id.txt')
            if not path.exists(self.id_path):
                self.input_id_number()
            else:
                self.id = int(read_data(self.id_path))
        else:
            self.id = id
        # list of all paths
        self.tip_path = path.join(self.path, 'tip.txt')
        self.tip_type_path = path.join(self.path, 'tip_type.txt')
        self.miles_path = path.join(self.path, 'order_miles_traveled.txt')
        self.end_time_path = path.join(self.path, 'order_end_time.txt')
        self.order_file_path = path.join(self.path, f'{self.id}.txt')

    # todo: impament tip class changes
    # methods for order tracking
    def consolidate(self):
        try:
            data = '{0[0]},{1[0]},{0[1]},{1[1]},{2},{3}'.format(
                self.tip, self.tip_type, self.miles_traveled, self.end_time)
        except TypeError:
            data = '{0},{1},{2},{3}'.format(
                self.tip, self.tip_type, self.miles_traveled, self.end_time)
        write_data(self.order_file_path, data)
        # remove files that are no longer needed
        remove(self.id_path)
        remove(self.tip_path)
        remove(self.tip_type_path)
        remove(self.miles_path)
        remove(self.end_time_path)
        # update/create order_numbers.txt
        self.update_ids_file()
        # remove file telling program, order is in progress
        remove(path.join(self.path, 'order'))

    def load(self):
        order_data = read_data(self.order_file_path).split(',')
        if len(order_data) == 6:
            card = 1
            cash = 2
            try:
                self.tip = [float(order_data[0]), float(order_data[2])]
                self.tip_type = [card, cash]
                self.miles_traveled = float(order_data[4])
                self.end_time = to_datetime(order_data[5])
            except ValueError:
                self.tip = [float(order_data[0]), float(order_data[2])]
                self.tip_type = [card, cash]
                self.miles_traveled = float(order_data[4])
        elif len(order_data) == 4:
            try:
                self.tip = float(order_data[0])
                self.tip_type = int(order_data[1])
                self.miles_traveled = float(order_data[2])
                self.end_time = to_datetime(order_data[3])
            except ValueError:
                self.tip = float(order_data[0])
                self.tip_type = int(order_data[1])
                self.miles_traveled = float(order_data[2])
        return self

    def start(self):
        # create file, program knows order was started
        write_data(path.join(self.path, 'order'), None)
        # input the tip amount, or if tipped at all
        self.tip()
        # input the miles since prev destination
        self.miles_traveled = self.input_miles_traveled()
        # save/assign current time for end of order
        self.end_time = now()
        write_data(self.end_time_path, self.end_time)
        # consolidate order files into one file
        self.consolidate()
        # display amount of time to complete the order
        time_taken(self.parent.start_time, self.end_time,
                   'Order completed in:')
        # return order class object to the function that called it
        return self

    def tip(self):
        while True:
            split_check = get_input(
                '\nWas there a split tip?\n'
                'Y. Yes\n'
                'N. No\n\n', str)
            if split_check in ('y', 'Y'):
                self.input_split_tip()
            elif split_check in ('n', 'N'):
                self.tip = self.input_tip()
                self.tip_type = self.input_tip_type()
            else:
                print('\nInvalid input...')
            return self

    def update_ids_file(self):
        if path.exists(self.parent.order_ids_path):
            append_data(self.parent.order_ids_path, ',' + str(self.id))
        else:
            write_data(self.parent.order_ids_path, self.id)

    # methods for inputting data
    def input_miles_traveled(self):
        self.miles_traveled = input_data(
            '\nOrder miles traveled:\t#.#\n', float,
            'Is this correct?\t[y/n]\n', str,
            ('y', 'Y'), ('n', 'N'), word=' miles')
        write_data(self.miles_path, self.miles_traveled)

    def input_id_number(self):
        self.id = input_data(
            '\nEnter order number:\t#-####\n', int,
            '\nIs this correct?\t[y/n]\n', str,
            ('y', 'Y'), ('n', 'N'))
        write_data(self.id_path, self.id)

    def input_split_tip(self):
        card = 1
        cash = 2
        card_tip = input_data(
            f"\n{'Enter card tip amount:'}   {'$#.##'}\n", float,
            f"\n{'Is this correct?'}         {'[y/n]'}\n", str,
            ('y', 'Y'), ('n', 'N'), '$')
        cash_tip = input_data(
            f"\n{'Enter cash tip amount:'}   {'$#.##'}\n", float,
            f"\n{'Is this correct?'}         {'[y/n]'}\n", str,
            ('y', 'Y'), ('n', 'N'), '$')
        write_data(self.tip_path, f'{card_tip},{cash_tip}')
        write_data(self.tip_type_path, f'{card},{cash}')
        self.tip = [card_tip, cash_tip]
        self.tip_type = [card, cash]
        return self

    def input_tip(self):
        while True:
            tip_amount = get_input(
                f"\n{'Enter tip amount:'}        {'$#.##'}\n"
                '(if no tip, enter 0)\n$', float)
            if tip_amount == 0.0:
                user_confirm = get_input(
                    '\nNo tip'
                    f"\n{'Is this correct?'}         {'[y/n]'}\n", str)
                if user_confirm == 'y':
                    write_data(self.tip_path, 0.0)
                    return 0.0
                elif user_confirm == 'n':
                    continue
                else:
                    print('\nInvalid input...')
            else:
                user_confirm = get_input(
                    f"\n{'$'}{tip_amount}\n"
                    f"{'Is this correct?'}         {'[y/n]'}\n", str)
                if user_confirm == 'y':
                    write_data(self.tip_path, tip_amount)
                    return tip_amount
                elif user_confirm == 'n':
                    continue
                else:
                    print('\nInvalid input...')

    def input_tip_type(self):
        no_tip = 0
        card = 1
        cash = 2
        if self.tip == 0.0:
            write_data(self.tip_type_path, no_tip)
            return no_tip
        else:
            while True:
                user_option = get_input(
                    '\nType of tip?\n'
                    '1. For card\n'
                    '2. For cash\n', int)
                if user_option == 1:
                    check_correct = get_input(
                       '\nCard\n'
                       f"{'Is this correct?'}         {'[y/n]'}\n", str)
                    if check_correct == 'y':
                        write_data(self.tip_type_path, card)
                        return card
                    elif check_correct == 'n':
                        continue
                    else:
                        print('\nInvalid input...')
                elif user_option == 2:
                    check_correct = get_input(
                        '\nCash\n'
                        f"{'Is this correct?'}         {'[y/n]'}\n", str)
                    if check_correct == 'y':
                        write_data(self.tip_type_path, cash)
                        return cash
                    elif check_correct == 'n':
                        continue
                    else:
                        print('\nInvalid input...')
                else:
                    print('\nInvalid input...')

    # methods for continuing tracking if program ends
    def load_current(self):
        if path.exists(self.tip_path):
            tip_data = read_data(self.tip_path).split(',')
            if len(tip_data) == 2:
                self.tip = [float(tip_data[0]), float(tip_data[1])]
            elif len(tip_data) == 1:
                self.tip = float(tip_data[0])
        if path.exists(self.tip_type_path):
            card = 1
            cash = 2
            tip_type_data = read_data(self.tip_type_path).split(',')
            if len(tip_type_data) == 2:
                self.tip_type = [card, cash]
            elif len(tip_type_data) == 1:
                self.tip_type = int(tip_type_data[0])
        if path.exists(self.miles_path):
            self.miles_traveled = float(read_data(self.miles_path))
        if path.exists(self.end_time_path):
            self.end_time = to_datetime(read_data(self.end_time_path))
        self.resume()
        return self

    def resume(self):
        if not path.exists(self.tip_path):
            # input the tip amount, or if tipped at all
            self.tip()
        if not path.exists(self.tip_type_path):
            # input the tip type. if no tip, automaticly inputs
            self.input_tip_type()
        if not path.exists(self.miles_path):
            # input the miles since prev destination
            self.input_miles_traveled()
        if not path.exists(self.end_time_path):
            # save/assign current time for end of order
            self.end_time = now()
            write_data(self.end_time_path, self.end_time)
        self.consolidate()
        # display amount of time to complete the order
        time_taken(self.parent.start_time, self.end_time,
                   'Order completed in:\t')
        return self

# todo: need to write function that allows the user to change data
# todo: need to write function that saves changes to data
