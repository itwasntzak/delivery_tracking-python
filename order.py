from os import path, remove

import id_number
import input_data
import utility


# //TODO: add the ability to add a split tip amount/type
def input_tip():
    file_path = path.join('delivery', 'tip.txt')
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


def input_tip_type(order):
    file_path = path.join('delivery', 'tip_type.txt')
    if order.tip == 0.0:
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


class Order:
    def consolidate(self):
        # list of all paths
        # pre consolidation paths
        order_id_path = path.join('delivery', 'order_number.txt')
        tip_path = path.join('delivery', 'tip.txt')
        tip_type_path = path.join('delivery', 'tip_type.txt')
        miles_traveled_path = path.join('delivery', 'order_miles_traveled.txt')
        order_end_time_path = path.join('delivery', 'order_end_time.txt')
        # post consolidation paths
        order_number_file_path =\
            path.join('delivery', str(self.id_number) + '.txt')

        # assign data to variables
        tip = str(self.tip)
        tip_type = str(self.tip_type)
        miles_traveled = str(self.miles_traveled)
        order_end_time = str(self.end_time)

        data = tip + ',' + tip_type + ','\
            + miles_traveled + ',' + order_end_time
        utility.write_data(order_number_file_path, data)
        # update/create order_numbers.txt
        id_number.id_number_file(self)
        # remove files that are no longer needed
        remove(order_id_path)
        remove(tip_path)
        remove(tip_type_path)
        remove(miles_traveled_path)
        remove(order_end_time_path)

    def load(self):
        id_number_path = path.join('delivery', 'order_number.txt')
        tip_path = path.join('delivery', 'tip.txt')
        tip_type_path = path.join('delivery', 'tip_type.txt')
        miles_path = path.join('delivery', 'order_miles_traveled.txt')
        end_time_path = path.join('delivery', 'order_end_time.txt')

        if path.exists(id_number_path):
            self.id_number = int(utility.read_data(id_number_path))
        if path.exists(tip_path):
            self.tip = float(utility.read_data(tip_path))
        if path.exists(tip_type_path):
            self.tip_type = int(utility.read_data(tip_type_path))
        if path.exists(miles_path):
            self.miles_traveled = float(utility.read_data(miles_path))
        if path.exists(end_time_path):
            self.end_time = utility.to_datetime(
                utility.read_data(end_time_path))
        return self

    def resume(self):
        id_number_path = path.join('delivery', 'order_number.txt')
        tip_path = path.join('delivery', 'tip.txt')
        tip_type_path = path.join('delivery', 'tip_type.txt')
        miles_path = path.join('delivery', 'order_miles_traveled.txt')
        end_time_path = path.join('delivery', 'order_end_time.txt')
        while True:
            if not path.exists(id_number_path):
                # input the order number as a form of id
                self.id_number = utility.write_data(
                    id_number_path, id_number.assign_id_number(self))
            elif not path.exists(tip_path):
                # input the tip amount, or if tipped at all
                self.tip = input_tip()
            elif not path.exists(tip_type_path):
                # input the tip type. if no tip, automaticly inputs
                self.tip_type = input_tip_type(self)
            elif not path.exists(miles_path):
                # input the miles since prev destination
                self.miles_traveled = utility.write_data(
                    miles_path,
                    utility.miles_traveled('Order miles traveled:    #.#'))
            elif not path.exists(end_time_path):
                # save/assign current time for end of order
                self.end_time =\
                    utility.write_data(end_time_path, utility.now())
            else:
                break
        # consolidate order files into one file
        self.consolidate()
        # remove file telling program order in progress
        remove(path.join('delivery', 'order'))
        # return order class object to the function that called it
        return self

    def start(self):
        miles_path = path.join('delivery', 'order_miles_traveled.txt')
        end_time_path = path.join('delivery', 'order_end_time.txt')
        # create file, program knows order was started
        utility.write_data(path.join('delivery', 'order'), None)
        # input the order number as a form of id
        self.id_number = id_number.assign_id_number(self)
        # input the tip amount, or if tipped at all
        self.tip = input_tip()
        # input the tip type. if no tip, automaticly inputs
        self.tip_type = input_tip_type(self)
        # input the miles since prev destination
        self.miles_traveled = utility.write_data(
            miles_path, utility.miles_traveled('Order miles traveled:    #.#'))
        # save/assign current time for end of order
        self.end_time = utility.write_data(end_time_path, utility.now())
        # consolidate order files into one file
        self.consolidate()
        # remove file telling program order in progress
        remove(path.join('delivery', 'order'))
        # return order class object to the function that called it
        return self
