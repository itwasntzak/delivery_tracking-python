from os import path, mkdir, remove

from delivery import Delivery
from extra_stop import Extra_Stop
from input_data import input_data, get_input
from split import Split
from utility import append_data, enter_to_continue, now, read_data,\
    to_datetime, to_money, write_data


# todo: make average shifts per month function
# todo: make average miles per delivery function
# todo: make avereage speed per delviery function
# todo: make average delivery per hour function


def load_all_shifts():
    shift_numbers_list = read_data('shift_ids.txt').split(',')
    shifts_list = []
    for shift_id in shift_numbers_list:
        shifts_list.append(Shift(to_datetime(shift_id + ' 00:00:00.0')).load())
    return shifts_list


def load_current_month():
    current_month = now().month
    shifts_list = load_all_shifts()
    current_month_shifts = []
    for shift in shifts_list:
        if shift.id.month == current_month:
            current_month_shifts.append(shift)
        else:
            pass
    return current_month_shifts


def load_current_week():
    current_week = now().isocalendar()[1]
    shifts_list = load_all_shifts()
    current_week_shifts = []
    for shift in shifts_list:
        if shift.id.isocalendar()[1] == current_week:
            current_week_shifts.append(shift)
        else:
            pass
    return current_week_shifts


def average_deliveries_per_shift(shifts_list):
    deliveries = []
    for shift in shifts_list:
        deliveries.append(len(shift.deliveries))
    return round(sum(deliveries)/len(shifts_list), 3)


def average_orders_per_delivery(shifts_list):
    deliveries = []
    orders = []
    for shift in shifts_list:
        deliveries.append(len(shift.deliveries))
        for delivery in shift.deliveries:
            orders.append(len(delivery.orders))
    return round(sum(orders)/sum(deliveries), 3)


def average_orders_per_shift(shifts_list):
    orders = []
    for shift in shifts_list:
        orders.append(len(shift.all_orders()))
    return round(sum(orders)/len(shifts_list), 3)


def average_tip_per_delivery(shifts_list):
    deliveries = []
    for shift in shifts_list:
        for delivery in shift.deliveries:
            deliveries.append(delivery)
    return round(total_tips(shifts_list)/len(deliveries), 2)


def average_tip_per_order(shifts_list):
    orders = []
    for shift in shifts_list:
        orders.append(len(shift.all_orders()))
    return round(total_tips(shifts_list)/sum(orders), 2)


def average_tip_per_shift(shifts_list):
    average_tips = []
    for shift in shifts_list:
        average_tips.append(shift.average_tip_per_delivery())
    return round(sum(average_tips)/len(shifts_list), 2)


def avereage_total_in_hand_per_shift(shifts_list):
    return round(total_in_hand(shifts_list)/len(shifts_list), 2)


def average_total_tips_per_shift(shifts_list):
    return round(total_tips(shifts_list)/len(shifts_list), 2)


def card_tips(shifts_list):
    tips = []
    for shift in shifts_list:
        tips.append(shift.card_tips())
    return round(sum(tips), 2)


def cash_tips(shifts_list):
    tips = []
    for shift in shifts_list:
        tips.append(shift.cash_tips())
    return round(sum(tips), 2)


def total_in_hand(shifts_list):
    tips = []
    mileage = []
    for shift in shifts_list:
        tips.append(sum(shift.all_tips()))
        mileage.append(shift.mileage_paid)
    money = round(round(sum(tips), 2) + round(sum(mileage), 2), 2)
    return money


def total_tips(shifts_list):
    tips = []
    for shift in shifts_list:
        tips.append(sum(shift.all_tips()))
    return round(sum(tips), 2)


def shift_menu(shift):
    while True:
        # todo: reformat strings with format
        user_choice = get_input(
            prompt='\n'
                   'What would you like to do?\n'
                   'D: Start delivery\n'
                   'E: Start an extra stop\n'
                   'C: Enter carry out tip\n'
                   'S: Start split\n'
                   'X: End shift\n'
                   'I: Information on shift\n'
                   'Q: Quit program\n\n',
            kind=str)
        if user_choice in ('d', 'D'):
            delivery_path = path.join(shift.path, 'delivery')
            delivery = Delivery(shift, delivery_path).start()
            shift.delivery_ids.append(delivery.id)
            shift.deliveries.append(delivery)
        elif user_choice in ('e', 'E'):
            extra_stop = Extra_Stop(shift).start()
            shift.extra_stop_ids.append(extra_stop.id)
            shift.extra_stops.append(extra_stop)
        elif user_choice in ('c', 'C'):
            shift.carry_out_tip()
        elif user_choice in ('s', 'S'):
            Split(shift).start()
        elif user_choice in ('x', 'X'):
            shift.end()
        elif user_choice in ('i', 'I'):
            shift.view_statistics()
        elif user_choice in ('q', 'Q'):
            quit()
        else:
            print('\nInvalid input...')


class Shift:
    # todo: add ability to input over counter tips
    def __init__(self, id=''):
        if id != '':
            self.id = id
            self.path = path.join('shifts', str(id.date()))
        self.delivery_ids = []
        self.deliveries = []
        self.extra_stop_ids = []
        self.extra_stops = []
        self.carry_out_tips = []
        # list of all paths
        try:
            self.carry_out_tips_path =\
                path.join(self.path, 'carry_out_tips.txt')
            self.total_miles_path =\
                path.join(self.path, 'total_miles_traveled.txt')
            self.fuel_economy_path = path.join(self.path, 'fuel_economy.txt')
            self.mileage_paid_path = path.join(self.path, 'mileage_paid.txt')
            self.device_usage_paid_path =\
                path.join(self.path, 'device_usage_paid.txt')
            self.extra_tips_claimed_path =\
                path.join(self.path, 'extra_tips_claimed.txt')
            self.total_hours_path = path.join(self.path, 'total_hours.txt')
            self.start_time_path = path.join(self.path, 'shift_start_time.txt')
            self.end_time_path = path.join(self.path, 'shift_end_time.txt')
            self.delivery_ids_path =\
                path.join(self.path, 'delivery_ids.txt')
            self.extra_stop_ids_path =\
                path.join(self.path, 'extra_stop_ids.txt')
            self.shift_info_path = path.join(self.path, 'shift_info.txt')
            self.split_info_path = path.join(self.path, 'split_info.txt')
            self.shift_ids_path = path.join('shift_ids.txt')
        except AttributeError:
            pass

    # methods for basic shift tracking
    def consolidate(self):
        # todo: reformat strings with format
        data = str(self.miles_traveled) + ','\
            + str(self.fuel_economy) + ','\
            + str(self.mileage_paid) + ','\
            + str(self.device_usage_paid) + ','\
            + str(self.extra_tips_claimed) + ','\
            + str(self.total_hours) + ','\
            + str(self.start_time) + ','\
            + str(self.end_time)
        write_data(self.shift_info_path, data)
        # remove files that are no longer needed
        remove(self.total_miles_path)
        remove(self.fuel_economy_path)
        remove(self.mileage_paid_path)
        remove(self.device_usage_paid_path)
        remove(self.extra_tips_claimed_path)
        remove(self.total_hours_path)
        remove(self.start_time_path)
        remove(self.end_time_path)
        self.update_id_file()

    def end(self):
        while True:
            # todo: reformat strings with format
            user_check = get_input(
                '\nAre you sure you want to complete today\'s shift?\n\n'
                'Y: yes\nN: no\n', str)
            if user_check in ('y', 'Y'):
                # create file so program knows if end shift has been started
                write_data(path.join(self.path, 'end_shift'), None)
                # save time for end of shift
                self.end_time = write_data(self.end_time_path, now())
                # input total miles traveled for shift
                self.miles_traveled = self.input_miles_traveled()
                # input fuel economy
                self.fuel_economy = self.input_fuel_economy()
                # input mileage paid
                self.mileage_paid = self.input_mileage_paid()
                self.device_usage_paid = self.input_device_usage_paid()
                # input total hours worked
                self.total_hours = self.input_total_hours()
                # input extra claimed/reported tips
                self.extra_tips_claimed = self.input_extra_tips_claimed()
                remove(path.join(self.path, 'end_shift'))
                self.consolidate()
                print('\n\nShift has been end!')
                enter_to_continue()
                exit()
            elif user_check in ('n', 'N'):
                break
            else:
                print('\nInvalid input...')

    def load(self):
        # todo: need to fix shift files to include device usage paid
        # cnsd: when evaluating missing data, if missing part of time
        shift_data = read_data(self.shift_info_path).split(',')
        shift_data = list(filter(None, shift_data))
        if len(shift_data) == 7:
            self.miles_traveled = float(shift_data[0])
            self.fuel_economy = float(shift_data[1])
            self.mileage_paid = float(shift_data[2])
            self.device_usage_paid = 0.0
            self.extra_tips_claimed = float(shift_data[3])
            self.total_hours = float(shift_data[4])
            self.start_time = to_datetime(shift_data[5])
            self.end_time = to_datetime(shift_data[6])
        elif len(shift_data) == 8:
            self.miles_traveled = float(shift_data[0])
            self.fuel_economy = float(shift_data[1])
            self.mileage_paid = float(shift_data[2])
            self.device_usage_paid = float(shift_data[3])
            self.extra_tips_claimed = float(shift_data[4])
            self.total_hours = float(shift_data[5])
            self.start_time = to_datetime(shift_data[6])
            self.end_time = to_datetime(shift_data[7])
        if path.exists(self.delivery_ids_path):
            delivery_numbers = read_data(self.delivery_ids_path).split(',')
            self.delivery_ids = [int(item) for item in delivery_numbers]
            for delivery in self.delivery_ids:
                delivery_path = path.join(self.path, str(delivery))
                self.deliveries.append(Delivery(self, delivery_path).load())
        if path.exists(self.extra_stop_ids_path):
            extra_stop_ids = read_data(self.extra_stop_ids_path).split(',')
            self.extra_stop_ids = [int(item) for item in extra_stop_ids]
            for extra_stop_id in self.extra_stop_ids:
                self.extra_stops.append(Extra_Stop(self, extra_stop_id).load())
        if path.exists(self.carry_out_tips_path):
            # reading from the file
            tip_data = []
            with open(self.carry_out_tips_path, 'r') as file:
                tip_list = file.readlines()
                for carry_out_tip in tip_list:
                    tip_data.append(carry_out_tip.split(','))
            # removing \n from any strings it occurs
            for tip in tip_data:
                tip_data_list = []
                for data in tip:
                    tip_data_list.append(data.rstrip('\n'))
                self.carry_out_tips.append(tip_data_list)
        if path.exists(self.split_info_path):
            self.split = Split(self).load()
        return self

    def carry_out_tip(self):
        # todo: reformat strings with format
        while True:
            confirmation = get_input(
                '\nAre you sure you want to add a carry out tip? [y/n]\n\n',
                str)
            if confirmation in ('y', 'Y'):
                tip = self.input_carry_out_tip()
                tip_type = self.input_carry_out_tip_type()
                data = f'{tip},{tip_type}\n'
                if path.exists(self.carry_out_tips_path):
                    self.carry_out_tips.append(
                        append_data(self.carry_out_tips_path, data))
                else:
                    self.carry_out_tips.append(
                        write_data(self.carry_out_tips_path, data))
                break

            elif confirmation in ('n', 'N'):
                break
            else:
                print('\nInvalid input...')

    def start(self):
        mkdir(self.path)
        write_data(self.start_time_path, now())
        print('\nShift has been started!\n')
        enter_to_continue()
        exit()

    def update_id_file(self):
        if path.exists(self.shift_ids_path):
            append_data(self.shift_ids_path, ',' + str(self.id.date()))
        else:
            write_data(self.shift_ids_path, self.id.date())

    # methods for inputting data
    def input_carry_out_tip(self):
        return input_data(
            f"\n{'Enter tip amount:':<10}{'$#.##':>12}\n", float,
            f"\n{'Is this correct?':<10}{'[y/n]':>13}\n", str, 'y', 'n')

    def input_carry_out_tip_type(self):
        card = 1
        cash = 2
        while True:
            user_option = get_input(
                '\nType of tip?\n'
                '1. For card\n'
                '2. For cash\n', int)
            if user_option == 1:
                check_correct = get_input(
                   '\nCard\n'
                   f"{'Is this correct?':<10}{'[y/n]':>13}\n", str)
                if check_correct == 'y':
                    return card
                elif check_correct == 'n':
                    continue
                else:
                    print('\nInvalid input...')
            elif user_option == 2:
                confirmation = get_input(
                    '\nCash\n'
                    f"{'Is this correct?':<10}{'[y/n]':>13}\n", str)
                if confirmation == 'y':
                    return cash
                elif confirmation == 'n':
                    continue
                else:
                    print('\nInvalid input...')

    def input_device_usage_paid(self):
        # todo: reformat strings with format
        return write_data(self.device_usage_paid_path, input_data(
            '\nAmount of device usage paid:    $#.##\n$', float,
            '\nIs this correct? [y/n]\n', str, 'y', 'n', '$'))

    def input_extra_tips_claimed(self):
        # todo: reformat strings with format
        return write_data(self.extra_tips_claimed_path, input_data(
            '\nExtra tips claimed for shift:    $#.##\n$', float,
            '\nIs this correct? [y/n]\n', str, 'y', 'n', '$'))

    def input_fuel_economy(self):
        # todo: reformat strings with format
        return write_data(self.fuel_economy_path, input_data(
            '\nEnter fuel economy:    ##.#\n', float,
            '\nIs this correct? [y/n]\n', str, 'y', 'n'))

    def input_mileage_paid(self):
        # todo: reformat strings with format
        return write_data(self.mileage_paid_path, input_data(
            '\nAmount of mileage paid:    $#.##\n$', float,
            '\nIs this correct? [y/n]\n', str, 'y', 'n', '$'))

    def input_miles_traveled(self):
        # todo: reformat strings with format
        return write_data(self.total_miles_path, input_data(
            '\nTotal miles traveled for this shift:    #.#\n', float,
            ' miles\nIs this correct? [y/n]\n', str, 'y', 'n'))

    def input_total_hours(self):
        # todo: reformat strings with format
        return write_data(self.total_hours_path, input_data(
            '\nEnter total hours worked:    #.##\n', float,
            '\nIs this correct? [y/n]\n', str, 'y', 'n'))

    # methods for continuing tracking if program ends
    def load_current(self):
        if path.exists(self.start_time_path):
            self.start_time = to_datetime(read_data(self.start_time_path))
        else:
            self.start_time = write_data(self.start_time_path, now())
        if path.exists(self.delivery_ids_path):
            delivery_ids = read_data(self.delivery_ids_path).split(',')
            for delivery_id in delivery_ids:
                self.delivery_ids.append(int(delivery_id))
                delivery_path = path.join(self.path, delivery_id)
                self.deliveries.append(Delivery(self, delivery_path).load())
        if path.exists(self.extra_stop_ids_path):
            extra_stop_ids = read_data(self.extra_stop_ids_path).split(',')
            for extra_stop_id in extra_stop_ids:
                self.extra_stop_ids.append(int(extra_stop_id))
                self.extra_stops.append(Extra_Stop(self, extra_stop_id).load())
        if path.exists(self.carry_out_tips_path):
            # reading from the file
            tip_data = []
            with open(self.carry_out_tips_path, 'r') as file:
                tip_list = file.readlines()
                for carry_out_tip in tip_list:
                    tip_data.append(carry_out_tip.split(','))
            # removing \n from any strings it occurs
            for tip in tip_data:
                tip_data_list = []
                for data in tip:
                    tip_data_list.append(data.rstrip('\n'))
                self.carry_out_tips.append(tip_data_list)
        if path.exists(self.split_info_path):
            self.split = Split(self).load()
        self.resume()
        return self

    def load_end(self):
        if path.exists(self.end_time_path):
            self.end_time = to_datetime(read_data(self.end_time_path))
        if path.exists(self.total_miles_path):
            self.miles_traveled = float(read_data(self.total_miles_path))
        if path.exists(self.fuel_economy_path):
            self.fuel_economy = float(read_data(self.fuel_economy_path))
        if path.exists(self.mileage_paid_path):
            self.mileage_paid = float(read_data(self.mileage_paid_path))
        if path.exists(self.device_usage_paid_path):
            self.device_usage_paid =\
                float(read_data(self.device_usage_paid_path()))
        if path.exists(self.total_hours_path):
            self.total_hours = float(read_data(self.total_hours_path))
        if path.exists(self.extra_tips_claimed_path):
            self.extra_tips_claimed =\
                float(read_data(self.extra_tips_claimed_path))
        return self

    def resume(self):
        while True:
            # check if an extra stop has been started
            if path.exists(path.join(self.path, 'extra_stop')):
                extra_stop = Extra_Stop(self).load_current()
                self.extra_stop_ids.append(extra_stop.id)
                self.extra_stops.append(extra_stop)
            # check if delivery directory exist, if so complete it
            elif path.exists(path.join(self.path, 'delivery')):
                delivery_path = path.join(self.path, 'delivery')
                delivery = Delivery(self, delivery_path).load_current()
                self.delivery_ids.append(delivery.id)
                self.deliveries.append(delivery)
            # check if end shift has been started
            elif path.exists(path.join(self.path, 'end_shift')):
                self.load_end()
                self.resume_end()
            else:
                return self

    def resume_end(self):
        while True:
            if not path.exists(self.end_time_path):
                # save time for end of shift
                self.end_time = write_data(self.end_time_path, now())
            elif not path.exists(self.total_miles_path):
                # input total miles traveled for shift
                self.miles_traveled = self.input_miles_traveled()
            elif not path.exists(self.fuel_economy_path):
                # input fuel economy
                self.fuel_economy = self.input_fuel_economy()
            elif not path.exists(self.mileage_paid_path):
                # input mileage paid
                self.mileage_paid = self.input_mileage_paid()
            elif not path.exists(self.device_usage_paid_path):
                self.device_usage_paid = self.input_device_usage_paid()
            elif not path.exists(self.total_hours_path):
                # input total hours worked
                self.total_hours = self.input_total_hours()
            elif not path.exists(self.extra_tips_claimed_path):
                # input extra claimed/reported tips
                self.extra_tips_claimed = self.input_extra_tips_claimed()
            else:
                break
        remove(path.join(self.path, 'end_shift'))
        self.consolidate()
        print('Shift has been end!\n')
        enter_to_continue()
        exit()

    # methods for when current day's shift has already been completed
    def completed(self):
        while True:
            # todo: reformat strings with format
            user_choice = get_input(
                '\nYou have already completed a shift for today.\n'
                'Please select an option:\n'
                'R: Resume today\'s shift\n'
                'O: Overwrite shift\n'
                'Q: Quit program\n\n', str)
            if user_choice in ('r', 'R'):
                self.resume_shift()
                break
            elif user_choice in ('o', 'O'):
                self.overwrite()
                break
            elif user_choice in ('q', 'Q'):
                quit()
            else:
                print('\nInvalid input...\n')

    def overwrite(self):
        while True:
            # todo: reformat strings with format
            user_check = get_input(
                '\nAre you sure you want to overwrite the completed shift?\n'
                'Y: Yes\n'
                'N: No\n\n', str)
            if user_check in ('y', 'Y'):
                remove(self.path)
                mkdir(self.path)
                write_data(self.start_time_path, now())
                print('\nShift has been overwriten!\n')
                enter_to_continue()
                exit()
            elif user_check in ('n', 'N'):
                break
            else:
                print('\nInvalid input...')

    def resume_shift(self):
        while True:
            # todo: reformat strings with format
            user_check = get_input(
                '\nAre you sure you want to resume the completed shift?\n'
                'Y: Yes\n'
                'N: No\n\n', str)
            if user_check in ('y', 'Y'):
                shift_data = read_data(self.shift_info_path).split(',')
                self.start_time = write_data(
                    self.start_time_path, to_datetime(shift_data[7]))
                remove(self.shift_info_path)
                break
            elif user_check in ('n', 'N'):
                break
            else:
                print('\nInvalid input...')

    # methods for analyzing data
    def all_orders(self):
        total_orders = []
        for delivery in self.deliveries:
            for order in delivery.orders:
                total_orders.append(order)
        return total_orders

    def all_tips(self):
        tips = []
        for delivery in self.deliveries:
            for order in delivery.orders:
                tips.append(order.tip)
        return tips

    def card_tips(self):
        card_tips = []
        for delivery in self.deliveries:
            for order in delivery.orders:
                if order.tip_type == 1:
                    card_tips.append(order.tip)
                elif order.tip_type in (0, 2):
                    pass
        return card_tips

    def cash_tips(self):
        cash_tips = []
        for delivery in self.deliveries:
            for order in delivery.orders:
                if order.tip_type == 2:
                    cash_tips.append(order.tip)
                elif order.tip_type in (0, 1):
                    pass
        return cash_tips

    # methods for getting statistics on shift's data
    def average_miles_per_delivery(self):
        miles = []
        for delivery in self.deliveries:
            miles.append(delivery.miles_traveled)
        return round(sum(miles)/len(self.deliveries), 1)

    def average_speed_per_delivery(self):
        average_speeds = []
        for delivery in self.deliveries:
            average_speeds.append(delivery.average_speed)
        return round(sum(average_speeds)/len(self.deliveries))

    def average_tip_per_delivery(self):
        return sum(self.all_tips())/len(self.deliveries)

    def average_tip_per_order(self):
        return sum(self.all_tips())/len(self.all_orders())

    def view_statistics(self):
        try:
            data = [len(self.deliveries), len(self.all_orders()),
                    to_money(sum(self.all_tips())),
                    to_money(sum(self.card_tips())),
                    to_money(sum(self.cash_tips())),
                    to_money(self.average_tip_per_delivery()),
                    to_money(self.average_tip_per_order())]
            print(f"\n{'Number of deliveries:'}{data[0]:>9}\n"
                  f"{'Number of orders:'}{data[1]:>13}\n"
                  '\n'
                  f"{'Total tips:':<15}{data[2]:>15}\n"
                  f"{'Card tips:':<15}{data[3]:>15}\n"
                  f"{'Cash tips:':<15}{data[4]:>15}\n"
                  'Average tip per:\n'
                  f"{'Delivery:':^15}{data[5]:>15}\n"
                  f"{'Order:':^13}{data[6]:>17}\n")
            enter_to_continue()
        except ZeroDivisionError:
            print('\n\nNothing has yet to be tracked\n\n')
