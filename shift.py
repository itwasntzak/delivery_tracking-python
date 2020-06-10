from os import path, mkdir, remove

from delivery import Delivery
from extra_stop import Extra_Stop
from input_data import get_input, input_data
from split import Split
from tip import Tip
from utility import append_data, enter_to_continue, now, read_data as read,\
    to_datetime, to_money, user_confirmation, write_data


def load_all_shifts():
    shift_numbers_list = read('shift_ids.txt').split(',')
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
    vehicle = []
    for shift in shifts_list:
        tips.append(sum(shift.all_tips()))
        vehicle.append(shift.vehicle_compensation)
    money = round(round(sum(tips), 2) + round(sum(vehicle), 2), 2)
    return money


def total_tips(shifts_list):
    tips = []
    for shift in shifts_list:
        tips.append(sum(shift.all_tips()))
    return round(sum(tips), 2)


def shift_menu(shift):
    while True:
        delivery = Delivery(shift)
        prompt = '\nWhat would you like to do?\n'

        if path.exists(delivery.path):
            prompt += 'D: Continue delivery\n'
        else:
            prompt += 'D: Start delivery\n'

        prompt += 'E: Start an extra stop\n'\
                  'C: Enter carry out tip\n'\
                  'S: Start split\n'\
                  'X: End shift\n'\
                  'I: Information on shift\n'\
                  'Q: Quit program\n'

        user_choice = get_input(prompt, str)

        if user_choice in ('d', 'D'):
            if path.exists(delivery.path):
                shift.add_delivery(delivery.load_current())
            else:
                shift.add_delivery(delivery.start())
        elif user_choice in ('e', 'E'):
            shift.add_extra_stop(Extra_Stop(shift).start())
        elif user_choice in ('c', 'C'):
            shift.carry_out_tip()
        elif user_choice in ('s', 'S'):
            shift.split.start()
        elif user_choice in ('x', 'X'):
            shift.end()
        elif user_choice in ('i', 'I'):
            shift.view_statistics()
        elif user_choice in ('q', 'Q'):
            break
        else:
            print('\nInvalid input...')

# todo: make average shifts per month function
# todo: make average miles per delivery function
# todo: make avereage speed per delviery function
# todo: make average delivery per hour function


class Shift:
    delivery_ids = []
    deliveries = []
    extra_stop_ids = []
    extra_stops = []
    carry_out_tips = []

    def __init__(self, id=None):
        if id is not None:
            self.id = id.date()
            self.path = path.join('shifts', str(id.date()))
        self.split = Split(self)
        # list of all paths
        self.miles_traveled_path =\
            path.join(self.path, 'total_miles_traveled.txt')
        self.fuel_economy_path =\
            path.join(self.path, 'fuel_economy.txt')
        self.vehicle_compensation_path =\
            path.join(self.path, 'vehicle_compensation.txt')
        self.device_compensation_path =\
            path.join(self.path, 'device_compensation.txt')
        self.extra_tips_claimed_path =\
            path.join(self.path, 'extra_tips_claimed.txt')
        self.total_hours_path = path.join(self.path, 'total_hours.txt')
        self.start_time_path = path.join(self.path, 'shift_start_time.txt')
        self.end_time_path = path.join(self.path, 'shift_end_time.txt')
        self.delivery_ids_path = path.join(self.path, 'delivery_ids.txt')
        self.extra_stop_ids_path = path.join(self.path, 'extra_stop_ids.txt')
        self.info_path = path.join(self.path, 'shift_info.txt')
        self.shift_ids_path = path.join('shift_ids.txt')

    # methods for shift tracking
    # add a delivery to the delivery lists
    def add_delivery(self, delivery):
        self.delivery_ids.append(delivery.id)
        self.deliveries.append(delivery)

    # add a extra stop to the extra stop lists
    def add_extra_stop(self, extra_stop):
        self.extra_stop_ids.append(extra_stop.id)
        self.extra_stops.append(extra_stop)

    # move data from multiple files to one
    def consolidate(self):
        self.save()
        # remove files that are no longer needed
        remove(self.miles_traveled_path)
        remove(self.fuel_economy_path)
        remove(self.vehicle_compensation_path)
        remove(self.device_compensation_path)
        remove(self.extra_tips_claimed_path)
        remove(self.total_hours_path)
        remove(self.start_time_path)
        remove(self.end_time_path)
        # remove indicator for program to know end was completed
        remove(path.join(self.path, 'end_shift'))
        self.update_ids_file()

    # input the data for end of shift
    def end(self):
        prompt = "\nAre you sure you want to complete today's shift?\n"
        while user_confirmation:
            #  create indicator for program to know user wants to end
            write_data(path.join(self.path, 'end_shift'), None)
            # load end time file if it exists, else create it
            if path.exists(self.end_time_path):
                self.end_time = to_datetime(read(self.end_time_path))
            else:
                self.end_time()
            # load miles traveled file if it exists, else create it
            if path.exists(self.miles_traveled_path):
                self.miles_traveled = float(read(self.miles_traveled_path))
            else:
                self.input_miles_traveled()
            # load fule economy file if it exists, else create it
            if path.exists(self.fuel_economy_path):
                self.fuel_economy = float(read(self.fuel_economy_path))
            else:
                self.input_fuel_economy()
            # load vehicle paid file if it exists, else create it
            if path.exists(self.vehicle_compensation_path):
                self.vehicle_compensation =\
                    float(read(self.vehicle_compensation_path))
            else:
                self.input_vehicle_compensation()
            # load device usage page file if it exists, else create it
            if path.exists(self.device_compensation_path):
                self.device_compensation =\
                    float(read(self.device_compensation_path()))
            else:
                self.input_device_compensation()
            # load end time file if it exists, else create it
            if path.exists(self.total_hours_path):
                self.total_hours = float(read(self.total_hours_path))
            else:
                self.input_total_hours()
            # load end time file if it exists, else create it
            if path.exists(self.extra_tips_claimed_path):
                self.extra_tips_claimed =\
                    float(read(self.extra_tips_claimed_path))
            else:
                self.input_extra_tips_claimed()
            self.consolidate()
            enter_to_continue('Shift has been ended!')     

    # load a completed shift
    def load(self):
        shift_data = read(self.info_path).split(',')
        self.miles_traveled = float(shift_data[0])
        self.fuel_economy = float(shift_data[1])
        self.vehicle_compensation = float(shift_data[2])
        self.device_compensation = float(shift_data[3])
        self.extra_tips_claimed = float(shift_data[4])
        self.total_hours = float(shift_data[5])
        self.start_time = to_datetime(shift_data[6])
        self.end_time = to_datetime(shift_data[7])
        self.load_parts()
        return self

    # continuing tracking if program ends
    def load_current(self):
        if path.exists(self.start_time_path):
            self.start_time = to_datetime(read(self.start_time_path))
        else:
            self.start_time()
        self.load_parts()
        # check if an extra stop has been started
        if path.exists(path.join(self.path, 'extra_stop')):
            extra_stop = Extra_Stop(self).load_current()
            self.add_extra_stop(extra_stop)
        # check if end shift has been started
        if path.exists(path.join(self.path, 'end_shift')):
            self.load_end()
        return self

    # loads deliveries, extra stops, carry out tips, split if they exist
    def load_parts(self):
        if path.exists(self.delivery_ids_path):
            delivery_ids = read(self.delivery_ids_path).split(',')
            for delivery_id in delivery_ids:
                self.add_delivery(Delivery(self, int(delivery_id)).load())
        if path.exists(self.extra_stop_ids_path):
            extra_stop_ids = read(self.extra_stop_ids_path).split(',')
            for extra_stop_id in extra_stop_ids:
                self.add_extra_stop(Extra_Stop(self, int(extra_stop_id)).load())
        if path.exists(self.carry_out_tips_path):
            with open(self.carry_out_tips_path, 'r') as file:
                tip_list = file.readlines()
            for carry_out_tip in tip_list:
                carry_out_tip = carry_out_tip.split(',')
                self.carry_out_tips.append(
                    Tip(int(carry_out_tip[0]),
                        int(carry_out_tip[1]),
                        int(carry_out_tip[2]))
                )
        if path.exists(self.split.info_path):
            self.split = Split(self).load()

    # todo: need to write another method that changes data for already completed shift
    # prompt += "S. To change the shift's data\n"

    def modify_current_data(self):
        prompt = 'Please select what data you would like to change:\n'\
               + "T. To change the shift's start time\n"
        if path.exists(self.delivery_ids_path):
            prompt += "D. To change a delivery's data\n"
        if path.exists(self.extra_stop_ids_path):
            prompt += "E. To change a extra stop's data\n"
        if path.exists(self.carry_out_tips_path):
            prompt += "C. To change a carry out tip's data\n"
        prompt += 'Q. To quit modifying data for the current shift\n'\
                + 'QQ. To quit the program completely\n'

        while True:
            user_choice = get_input(prompt, str)
            if user_choice in ('s', 's'):
                # todo: write method that allows user to edit start time
                pass
            elif user_choice in ('d', 'D') and\
                    path.exists(self.delivery_ids_path):
                # todo: write method that allows user to select what delivery they want to edit
                pass
            elif user_choice in ('e', 'E') and\
                    path.exists(self.extra_stop_ids_path):
                # todo: write method that allows the user to select what extra stop to edit
                pass
            elif user_choice in ('c', 'C') and\
                    path.exists(self.carry_out_tips_path):
                # todo: write method that allows the user to select a carry out tip to edit
                pass
            elif user_choice in ('s', 's') and\
                    path.exists(self.split.info_path):
                # todo: write method to allow what data of the split they want to change
                pass
            elif user_choice in ('q', 'Q'):
                break
            elif user_choice in ('qq', 'qQ', 'Qq', 'QQ'):
                quit()
            else:
                print('\nInvalid input...\n')

    def save(self):
        write_data(self.info_path, self.string())

    def start(self):
        mkdir(self.path)
        self.start_time()
        enter_to_continue('Shift has been started!')
        exit()

    def update_ids_file(self):
        if path.exists(self.shift_ids_path):
            append_data(self.shift_ids_path, ',' + str(self.id.date()))
        else:
            write_data(self.shift_ids_path, self.id.date())

    # methods for saving/inputting data
    # method to input a carry out tip
    def carry_out_tip(self):
        while True:
            confirmation = get_input(
                '\nAre you sure you want to add a carry out tip?\n'
                'Y. Yes\n'
                'N. No\n', str)
            if confirmation in ('y', 'Y'):
                tip = Tip().input_split()
                tip.save(self.carry_out_tips_path)
                self.carry_out_tips.append(tip)
            elif confirmation in ('n', 'N'):
                break
            else:
                print('\nInvalid input...')

    # method to assign and save end time
    def end_time(self):
        self.end_time = now()
        write_data(self.end_time_path, self.end_time)

    def input_device_compensation(self):
        self.device_compensation = input_data(
            '\nAmount of device usage paid:\t$#.##\n$', float,
            'Is this correct?\t[y/n]', str,
            ('y', 'Y'), ('n', 'N'), '$')
        write_data(self.device_compensation_path, self.device_compensation)

    def input_extra_tips_claimed(self):
        self.extra_tips_claimed = input_data(
            '\nExtra tips claimed for shift:\t$#.##\n$', float,
            'Is this correct?\t[y/n]', str,
            ('y', 'Y'), ('n', 'N'), '$')
        write_data(self.extra_tips_claimed_path, self.extra_tips_claimed)

    def input_fuel_economy(self):
        self.fuel_economy = input_data(
            '\nEnter fuel economy:\t##.#\n', float,
            'Is this correct?\t[y/n]', str,
            ('y', 'Y'), ('n', 'N'))
        write_data(self.fuel_economy_path, self.fuel_economy)

    def input_miles_traveled(self):
        self.miles_traveled = input_data('\nTotal miles traveled for this shift:\t#.#\n', float,
                                         'Is this correct?\t[y/n]', str,
                                         ('y', 'Y'), ('n', 'N'), word=' miles')
        write_data(self.miles_traveled_path, self.miles_traveled)

    def input_total_hours(self):
        self.total_hours = input_data(
            '\nEnter total hours worked:\t#.##\n', float,
            'Is this correct?\t[y/n]', str,
            ('y', 'Y'), ('n', 'N'))
        write_data(self.total_hours_path, self.total_hours)

    def input_vehicle_compensation(self):
        self.vehicle_compensation = input_data(
            '\nAmount of vehicle paid:\t$#.##\n$', float,
            'Is this correct?\t[y/n]', str,
            ('y', 'Y'), ('n', 'N'), '$')
        write_data(self.vehicle_compensation_path, self.vehicle_compensation)

    def start_time(self):
        self.start_time = now()
        write_data(self.start_time_path, self.start_time)

    # methods for when current day's shift has already been completed
    def completed(self):
        while True:
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
            user_check = get_input(
                '\nAre you sure you want to overwrite the completed shift?\n'
                'Y: Yes\n'
                'N: No\n\n', str)
            if user_check in ('y', 'Y'):
                remove(self.path)
                mkdir(self.path)
                self.start_time = now()
                write_data(self.start_time_path, self.start_time)
                remove_id_from_file()
                print('\nShift has been overwriten!\n')
                enter_to_continue()
                exit()
            elif user_check in ('n', 'N'):
                break
            else:
                print('\nInvalid input...')

    def resume_shift(self):
        while True:
            user_check = get_input(
                '\nAre you sure you want to resume the completed shift?\n'
                'Y: Yes\n'
                'N: No\n\n', str)
            if user_check in ('y', 'Y'):
                shift_data = read(self.info_path).split(',')
                self.start_time = to_datetime(shift_data[7])
                write_data(self.start_time_path, self.start_time)
                remove(self.info_path)
                remove_id_from_file()
                break
            elif user_check in ('n', 'N'):
                break
            else:
                print('\nInvalid input...')

    def remove_id_from_file(self):
        temp_id_list = read(self.shift_ids_path).split(',')
        id_list = []
        for id in id_list:
            if id != str(self.id):
                id_list.append(id)
        comma_number = len(id_list) - 1
        new_ids_list = ""
        for value in range(comma_number):
            new_ids_list += id_list[value] + ','
        new_ids_list += id_list[comma_number + 1]
        if len(id_list) == 0:
            remove(self.shift_ids_path)
        elif len(id_list) > 0:
            write_data(self.shift_ids_path, new_ids_list)

    # utility methods
    def string(self):
        '{0},{1},{2},{3},{4},{5},{6},{7}'.format(
            self.miles_traveled, self.fuel_economy, self.vehicle_compensation,
            self.device_compensation, self.extra_tips_claimed, self.total_hours,
            self.start_time, self.end_time)

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
                try:
                    for tip in order.tip:
                        tips.append(tip)
                except TypeError:
                    tips.append(order.tip)
        for tip in self.carry_out_tips:
            tips.append(tip[0])
        return tips

    def card_tips(self):
        card_tips = []
        for delivery in self.deliveries:
            for order in delivery.orders:
                try:
                    index_counter = 0
                    for tip in order.tip:
                        if order.tip_type[index_counter] == 1:
                            card_tips.append(tip)
                        elif order.tip_type in (0, 2):
                            pass
                        index_counter += 1
                except TypeError:
                    if order.tip_type == 1:
                        card_tips.append(order.tip)
                    elif order.tip_type in (0, 2):
                        pass
        for tip in self.carry_out_tips:
            if tip[1] == 1:
                card_tips.append(tip[0])
            elif tip[1] == 2:
                pass
        return card_tips

    def cash_tips(self):
        cash_tips = []
        for delivery in self.deliveries:
            for order in delivery.orders:
                try:
                    index_counter = 0
                    for tip in order.tip:
                        if order.tip_type[index_counter] == 2:
                            cash_tips.append(tip)
                        elif order.tip_type in (0, 1):
                            pass
                        index_counter += 1
                except TypeError:
                    if order.tip_type == 2:
                        cash_tips.append(order.tip)
                    elif order.tip_type in (0, 1):
                        pass
        for tip in self.carry_out_tips:
            if tip[1] == 2:
                cash_tips.append(tip[0])
            elif tip[1] == 1:
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

# todo: need to write function that allows the user to change data
