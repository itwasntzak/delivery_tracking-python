from os import path, mkdir, remove

from delivery import Delivery
from extra_stop import check_id_number, Extra_Stop
from input_data import input_data, get_input
from split import Split
from utility import append_data, enter_to_continue, miles_traveled, now,\
    read_data, to_datetime, write_data


def load_all_shifts():
    shift_numbers_list = read_data('shift_numbers.txt').split(',')
    shift_list = []
    for amount in shift_numbers_list:
        id = to_datetime(shift_numbers_list[len(shift_list)] + ' 00:00:00.0')
        shift_list.append(Shift(id).load())
    return shift_list


def load_current_month_shifts():
    current_month = now().month
    all_shifts = load_all_shifts()
    if path.exists(path.join('shifts', str(now().date()))):
        today = Shift(now()).load_current()
        all_shifts.append(today)
    current_month_shifts = []
    for item in all_shifts:
        if item.id.month == current_month:
            current_month_shifts.append(item)
        else:
            pass
    return current_month_shifts


def load_current_week_shifts():
    current_week = now().isocalendar()[1]
    all_shifts = load_all_shifts()
    if path.exists(path.join('shifts', str(now().date()))):
        today = Shift(now()).load_current()
        all_shifts.append(today)
    current_week_shifts = []
    for item in all_shifts:
        if item.id.isocalendar()[1] == current_week:
            current_week_shifts.append(item)
        else:
            pass
    return current_week_shifts


def current_month_total_tips():
    tips = []
    shifts = load_current_month_shifts()
    for item in shifts:
        tips.append(shifts[len(tips)].total_tips())
    return round(sum(tips), 2)


def current_month_card_tips():
    tips = []
    shifts = load_current_month_shifts()
    for item in shifts:
        tips.append(shifts[len(tips)].card_tips())
    return round(sum(tips), 2)


def current_month_cash_tips():
    tips = []
    shifts = load_current_month_shifts()
    for item in shifts:
        tips.append(shifts[len(tips)].cash_tips())
    return round(sum(tips), 2)


def current_week_total_tips():
    tips = []
    shifts = load_current_week_shifts()
    for item in shifts:
        tips.append(shifts[len(tips)].total_tips())
    return round(sum(tips), 2)


def current_week_card_tips():
    tips = []
    shifts = load_current_week_shifts()
    for item in shifts:
        tips.append(shifts[len(tips)].card_tips())
    return round(sum(tips), 2)


def current_week_cash_tips():
    tips = []
    shifts = load_current_week_shifts()
    for item in shifts:
        tips.append(shifts[len(tips)].cash_tips())
    return round(sum(tips), 2)


def shift_menu(shift):
    while True:
        user_choice = get_input(
            prompt='\nWhat would you like to do?'
                   '\nD: Start delivery'
                   '\nE: Start an extra stop'
                   '\nS: Start split'
                   '\nX: End shift'
                   '\nI: Information on shift'
                   '\nQ: Quit program\n\n',
            kind=str)
        if user_choice in ('d', 'D'):
            delivery_path = path.join(shift.path, 'delivery')
            delivery = Delivery(shift, delivery_path).start()
            shift.delivery_numbers.append(delivery.id)
            shift.deliveries.append(delivery)
        elif user_choice in ('e', 'E'):
    # todo: still need to work how to update shift extra stop id & parent lists
            extra_stop = Extra_Stop(shift, shift.extra_stop_id).start()
            shift.extra_stop_numbers.append(extra_stop.id)
            shift.extra_stops.append(extra_stop)
            shift.extra_stop_id = shift.extra_stop_id + 1
        elif user_choice in ('s', 'S'):
            Split(shift).start()
        elif user_choice in ('x', 'X'):
            shift.end()
        elif user_choice in ('i', 'I'):
            print('Total tips made:   $' + str(shift.total_tips()))
            print('Card tips made:   $' + str(shift.card_tips()))
            print('Cash tips made:   $' + str(shift.cash_tips()))
        elif user_choice in ('q', 'Q'):
            quit()
        else:
            print('\nInvalid input...')


class Shift:
    # todo: add ability to input over counter tips
    # todo: start tracking device usage
    # todo: add total money in hand input for data
    def __init__(self, id):
        self.id = id
        self.path = path.join('shifts', str(id.date()))
        self.delivery_numbers = []
        self.deliveries = []
        self.extra_stop_numbers = []
        self.extra_stops = []
        # list of all paths
        self.total_miles_path =\
            path.join(self.path, 'total_miles_traveled.txt')
        self.fuel_economy_path = path.join(self.path, 'fuel_economy.txt')
        self.mileage_paid_path = path.join(self.path, 'mileage_paid.txt')
        self.extra_tips_claimed_path =\
            path.join(self.path, 'extra_tips_claimed.txt')
        self.total_hours_path = path.join(self.path, 'total_hours.txt')
        self.start_time_path = path.join(self.path, 'shift_start_time.txt')
        self.end_time_path = path.join(self.path, 'shift_end_time.txt')
        self.delivery_numbers_path =\
            path.join(self.path, 'delivery_numbers.txt')
        self.extra_stop_numbers_path =\
            path.join(self.path, 'extra_stop_numbers.txt')
        self.extra_stop_id_path =\
            path.join(self.path, 'extra_stop_id_number.txt')
        self.shift_info_path = path.join(self.path, 'shift_info.txt')
        self.split_info_path = path.join(self.path, 'split_info.txt')
        self.shift_numbers_path = path.join('shift_numbers.txt')

    def card_tips(self):
        card_tips = []
        for items in self.deliveries:
            card_tips.append(
                round(self.deliveries[len(card_tips)].card_tips(), 2))
        return round(sum(card_tips), 2)

    def cash_tips(self):
        cash_tips = []
        for items in self.deliveries:
            cash_tips.append(
                round(self.deliveries[len(cash_tips)].cash_tips(), 2))
        return round(sum(cash_tips), 2)

    def consolidate(self):
        data = str(self.miles_traveled) + ','\
            + str(self.fuel_economy) + ','\
            + str(self.mileage_paid) + ','\
            + str(self.extra_tips_claimed) + ','\
            + str(self.total_hours) + ','\
            + str(self.start_time) + ','\
            + str(self.end_time)
        write_data(self.shift_info_path, data)
        # remove files that are no longer needed
        remove(self.total_miles_path)
        remove(self.fuel_economy_path)
        remove(self.mileage_paid_path)
        remove(self.extra_tips_claimed_path)
        remove(self.total_hours_path)
        remove(self.start_time_path)
        remove(self.end_time_path)
        self.update_id_file()

    def end(self):
        while True:
            user_check = get_input(
                'Are you sure you want to complete today\'s shift?\n'
                'Y: yes\nN: no\n', str)
            if user_check in ('y', 'Y'):
                # create file so program knows if end shift has been started
                write_data(path.join(self.path, 'end_shift'), None)
                # save time for end of shift
                self.end_time = write_data(self.end_time_path, now())
                # input total miles traveled for shift
                self.miles_traveled = write_data(
                    self.total_miles_path,  miles_traveled(
                        'Total miles traveled for this shift:    #.#'))
                # input fuel economy
                self.fuel_economy = write_data(
                    self.fuel_economy_path, input_data(
                        '\nEnter fuel economy:    ##.#\n', float,
                        '\nIs this correct? [y/n]\n', str, 'y', 'n'))
                # input mileage paid
                self.mileage_paid = write_data(
                    self.mileage_paid_path, input_data(
                        '\nAmount of mileage paid:    $#.##\n$', float,
                        '\nIs this correct? [y/n]\n', str, 'y', 'n', '$'))
                # input total hours worked
                self.total_hours = write_data(
                    self.total_hours_path, input_data(
                        '\nEnter total hours worked:    #.##\n', float,
                        '\nIs this correct? [y/n]\n', str, 'y', 'n'))
                # input extra claimed/reported tips
                self.extra_tips_claimed = write_data(
                    self.extra_tips_claimed_path, input_data(
                        '\nExtra tips claimed for shift:    $#.##\n$', float,
                        '\nIs this correct? [y/n]\n', str, 'y', 'n', '$'))
                remove(path.join(self.path, 'end_shift'))
                self.consolidate()
                print('Shift has been end!')
                enter_to_continue()
                exit()
            elif user_check in ('n', 'N'):
                break
            else:
                print('\nInvalid input...')

    def load(self):
        # todo: need to take into account missing data
        # cnsd: when evaluating missing data, if missing part of time. dismiss all time
        shift_data = read_data(self.shift_info_path).split(',')
        self.miles_traveled = float(shift_data[0])
        self.fuel_economy = float(shift_data[1])
        self.mileage_paid = float(shift_data[2])
        self.extra_tips_claimed = float(shift_data[3])
        self.total_hours = float(shift_data[4])
        self.start_time = to_datetime(shift_data[5])
        self.end_time = to_datetime(shift_data[6])
        if path.exists(self.delivery_numbers_path):
            delivery_numbers =\
                read_data(self.delivery_numbers_path).split(',')
            self.delivery_numbers = [int(item) for item in delivery_numbers]
            for value in range(len(self.delivery_numbers)):
                delivery_path = path.join(self.path, str(len(self.deliveries)))
                self.deliveries.append(Delivery(self, delivery_path).load())
        if path.exists(self.extra_stop_numbers_path):
            extra_stop_numbers =\
                read_data(self.extra_stop_numbers_path).split(',')
            self.extra_stop_numbers =\
                [int(item) for item in extra_stop_numbers]
            for value in range(len(self.extra_stop_numbers)):
                extra_stop_id = self.extra_stop_numbers[len(self.extra_stops)]
                self.extra_stops.append(Extra_Stop(self, extra_stop_id).load())
        if path.exists(self.split_info_path):
            self.split = Split(self).load()
        return self

    def load_current(self):
        if path.exists(self.start_time_path):
            self.start_time = to_datetime(read_data(self.start_time_path))
        else:
            self.start_time = write_data(self.start_time_path, now())
        if path.exists(self.delivery_numbers_path):
            delivery_numbers = read_data(self.delivery_numbers_path).split(',')
            self.delivery_numbers = [int(item) for item in delivery_numbers]
            for value in range(len(self.delivery_numbers)):
                delivery_path = path.join(self.path, str(len(self.deliveries)))
                self.deliveries.append(Delivery(self, delivery_path).load())
        if path.exists(self.extra_stop_id_path):
            self.extra_stop_id = int(read_data(self.extra_stop_id_path))
        else:
            self.extra_stop_id = 0
        if path.exists(self.extra_stop_numbers_path):
            extra_stop_numbers =\
                read_data(self.extra_stop_numbers_path).split(',')
            self.extra_stop_numbers =\
                [int(item) for item in extra_stop_numbers]
            for value in range(len(self.extra_stop_numbers)):
                extra_stop_id = self.extra_stop_numbers[len(self.extra_stops)]
                self.extra_stops.append(Extra_Stop(self, extra_stop_id).load())
        if path.exists(self.split_info_path):
            self.split = Split(self).load()
        while True:
            # check if an extra stop has been started
            if path.exists(path.join(self.path, 'extra_stop')):
                extra_stop_id = check_id_number(self)
                extra_stop = Extra_Stop(self, extra_stop_id).load_current()
                self.extra_stop_numbers.append(extra_stop.id)
                self.extra_stops.append(extra_stop)
                self.extra_stop_id = self.extra_stop_id + 1
            # check if delivery directory exist, if so complete it
            elif path.exists(path.join(self.path, 'delivery')):
                delivery_path = path.join(self.path, 'delivery')
                delivery = Delivery(self, delivery_path).load_current()
                self.delivery_numbers.append(delivery.id)
                self.deliveries.append(delivery)
            # check if end shift has been started
            elif path.exists(path.join(self.path, 'end_shift')):
                self.resume_end()
            else:
                return self

    def overwrite(self):
        while True:
            user_check = get_input(
                'Are you sure you want to resume the completed shift?\n'
                'Y: yes\n N: no', str)
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

    def resume_end(self):
        if path.exists(self.end_time_path):
            self.end_time = to_datetime(read_data(self.end_time_path))
        if path.exists(self.total_miles_path):
            self.miles_traveled = float(read_data(self.total_miles_path))
        if path.exists(self.fuel_economy_path):
            self.fuel_economy = float(read_data(self.fuel_economy_path))
        if path.exists(self.mileage_paid_path):
            self.mileage_paid = float(read_data(self.mileage_paid_path))
        if path.exists(self.total_hours_path):
            self.total_hours = float(read_data(self.total_hours_path))
        if path.exists(self.extra_tips_claimed_path):
            self.extra_tips_claimed =\
                float(read_data(self.extra_tips_claimed_path))
        while True:
            if not path.exists(self.end_time_path):
                # save time for end of shift
                self.end_time = write_data(self.end_time_path, now())
            elif not path.exists(self.total_miles_path):
                # input total miles traveled for shift
                self.miles_traveled = write_data(
                    self.total_miles_path, miles_traveled(
                        'Total miles traveled for this shift:    #.#'))
            elif not path.exists(self.fuel_economy_path):
                # input fuel economy
                self.fuel_economy = write_data(
                    self.fuel_economy_path, input_data(
                        '\nEnter fuel economy:    ##.#\n', float,
                        '\nIs this correct? [y/n]\n', str, 'y', 'n'))
            elif not path.exists(self.mileage_paid_path):
                # input mileage paid
                self.mileage_paid = write_data(
                    self.mileage_paid_path, input_data(
                        '\nAmount of mileage paid:    $#.##\n$', float,
                        '\nIs this correct? [y/n]\n', str, 'y', 'n', '$'))
            elif not path.exists(self.total_hours_path):
                # input total hours worked
                self.total_hours = write_data(
                    self.total_hours_path, input_data(
                        '\nEnter total hours worked:    #.##\n', float,
                        '\nIs this correct? [y/n]\n', str, 'y', 'n'))
            elif not path.exists(self.extra_tips_claimed_path):
                # input extra claimed/reported tips
                self.extra_tips_claimed = write_data(
                    self.extra_tips_claimed_path, input_data(
                        '\nExtra tips claimed for shift:    $#.##\n$', float,
                        '\nIs this correct? [y/n]\n', str, 'y', 'n', '$'))
            else:
                break
        remove(path.join(self.path, 'end_shift'))
        self.consolidate()
        print('Shift has been end!\n')
        enter_to_continue()
        exit()

    def resume_shift(self):
        while True:
            user_check = get_input(
                'Are you sure you want to resume the completed shift?\n'
                'Y: yes\n N: no', str)
            if user_check in ('y', 'Y'):
                shift_data = read_data(self.shift_info_path).split(',')
                self.start_time = write_data(
                    self.start_time_path, to_datetime(shift_data[5]))
                remove(self.shift_info_path)
                break
            elif user_check in ('n', 'N'):
                break
            else:
                print('\nInvalid input...')

    def start(self):
        mkdir(self.path)
        write_data(self.start_time_path, now())
        print('\nShift has been started!\n')
        enter_to_continue()
        exit()

    def total_tips(self):
        tips = []
        for items in self.deliveries:
            tips.append(round(self.deliveries[len(tips)].total_tips(), 2))
        return round(sum(tips), 2)

    def update_id_file(self):
        if path.exists(self.shift_numbers_path):
            append_data(self.shift_numbers_path, ',' + str(self.id))
        else:
            write_data(self.shift_numbers_path, self.id)
