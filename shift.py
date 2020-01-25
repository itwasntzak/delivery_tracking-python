from os import path, mkdir, remove
import shutil
from time import sleep

from delivery import Delivery
from extra_stop import Extra_Stop
import id_number
from input_data import input_data, get_input
from split import Split
import utility


def shift_menu(shift):
    while True:
        user_choice = get_input(
            prompt='\nWhat would you like to do?'
                   '\nD to start delivery'
                   '\nX to end shift'
                   '\nS to start split'
                   '\nE to start an extra stop\n',
            kind=str)
        if user_choice in ('d', 'D'):
            delivery = Delivery().start(shift)
        elif user_choice in ('x', 'X'):
            shift.end_shift()
        elif user_choice in ('s', 'S'):
            split = Split().start()
        elif user_choice in ('e', 'E'):
            extra_stop = Extra_Stop().extra_stop(shift)
            exit()
        else:
            print('\nInvalid input...')


class Shift:
    def consolidate(self):
        # list of all paths
        # pre consolidation paths
        extra_stop_id_number_path =\
            path.join('shift', 'extra_stop_id_number.txt')
        total_miles_path = path.join('shift', 'total_miles_traveled.txt')
        fuel_economy_path = path.join('shift', 'fuel_economy.txt')
        mileage_paid_path = path.join('shift', 'mileage_paid.txt')
        extra_tips_claimed_path = path.join('shift', 'extra_tips_claimed.txt')
        total_hours_path = path.join('shift', 'total_hours.txt')
        shift_start_time_path = path.join('shift', 'shift_start_time.txt')
        shift_end_time_path = path.join('shift', 'shift_end_time.txt')
        # pre & post consolidation paths
        delivery_numbers_path = path.join('shift', 'delivery_numbers.txt')
        extra_stop_numbers_path = path.join('shift', 'extra_stop_numbers.txt')
        # post consolidation paths
        shift_info_path = path.join('shift', 'shift_info.txt')

        # assign data to variables
        delivery_quantity = str(len(self.delivery_numbers))
        extra_stop_quantity = str(len(self.extra_stop_numbers))
        miles_traveled = str(self.miles_traveled)
        fuel_economy = str(self.fuel_economy)
        mileage_paid = str(self.mileage_paid)
        extra_tips_claimed = str(self.extra_tips_claimed)
        total_hours = str(self.total_hours)
        shift_start_time = str(self.start_time)
        shift_end_time = str(self.end_time)

        data = delivery_quantity + ',' + extra_stop_quantity + ','\
            + miles_traveled + ',' + fuel_economy + ',' + mileage_paid + ','\
            + extra_tips_claimed + ',' + total_hours + ','\
            + shift_start_time + ',' + shift_end_time
        utility.write_data(shift_info_path, data)
        # remove files that are no longer needed
        remove(total_miles_path)
        remove(fuel_economy_path)
        remove(mileage_paid_path)
        remove(extra_tips_claimed_path)
        remove(total_hours_path)
        remove(shift_start_time_path)
        remove(shift_end_time_path)
        if path.exists(extra_stop_id_number_path):
            remove(extra_stop_id_number_path)
        shutil.move('shift', id_number.assign_id_number(self))

    def end_shift(self):
        miles_traveled_path = path.join('shift', 'total_miles_traveled.txt')
        fuel_economy_path = path.join('shift', 'fuel_economy.txt')
        mileage_paid_path = path.join('shift', 'mileage_paid.txt')
        total_hours_path = path.join('shift', 'total_hours.txt')
        extra_tips_path = path.join('shift', 'extra_tips_claimed.txt')
        end_time_path = path.join('shift', 'shift_end_time.txt')
        # create file so program knows if end shift has been started
        utility.write_data(path.join('shift', 'end_shift'), None)
        # input total miles traveled for shift
        self.miles_traveled = utility.write_data(
            miles_traveled_path, utility.miles_traveled(
                'Total miles traveled for this shift:    #.#'))
        # input fuel economy
        self.fuel_economy = utility.write_data(
            fuel_economy_path, input_data(
                '\nEnter fuel economy:    ##.#\n', float,
                '\nIs this correct? [y/n]\n', str, 'y', 'n'))
        # input mileage paid
        self.mileage_paid = utility.write_data(
            mileage_paid_path, input_data(
                '\nAmount of mileage paid:    $#.##\n$', float,
                '\nIs this correct? [y/n]\n', str, 'y', 'n', '$'))
        # input total hours worked
        self.total_hours = utility.write_data(
            total_hours_path, input_data(
                '\nEnter total hours worked:    #.##\n', float,
                '\nIs this correct? [y/n]\n', str, 'y', 'n'))
        # input extra claimed/reported tips
        self.extra_tips_claimed = utility.write_data(
            extra_tips_path, input_data(
                '\nExtra tips claimed for shift:    $#.##\n$', float,
                '\nIs this correct? [y/n]\n', str, 'y', 'n', '$'))
        # save time for end of shift
        self.end_time = utility.write_data(end_time_path, utility.now())
        remove(path.join('shift', 'end_shift'))
        self.consolidate()
        print('Shift has been end!')
        utility.enter_to_continue()
        exit()

    def load(self):
        delivery_numbers_path = path.join('shift', 'delivery_numbers.txt')
        extra_stop_numbers_path = path.join('shift', 'extra_stop_numbers.txt')
        miles_traveled_path = path.join('shift', 'total_miles_traveled.txt')
        fuel_economy_path = path.join('shift', 'fuel_economy.txt')
        mileage_paid_path = path.join('shift', 'mileage_paid.txt')
        total_hours_path = path.join('shift', 'total_hours.txt')
        extra_tips_claimed_path = path.join('shift', 'extra_tips_claimed.txt')
        start_time_path = path.join('shift', 'shift_start_time.txt')
        end_time_path = path.join('shift', 'shift_end_time.txt')

        if path.exists(start_time_path):
            self.start_time =\
                utility.to_datetime(utility.read_data(start_time_path))
        else:
            self.start_time =\
                utility.write_data(start_time_path, utility.now())
        if path.exists(delivery_numbers_path):
            self.delivery_numbers =\
                utility.read_data(delivery_numbers_path).split(',')
        else:
            self.delivery_numbers = []
        if path.exists(extra_stop_numbers_path):
            self.extra_stop_numbers =\
                utility.read_data(extra_stop_numbers_path).split(',')
        else:
            self.extra_stop_numbers = []
        if path.exists(miles_traveled_path):
            self.miles_traveled =\
                float(utility.read_data(miles_traveled_path))
        if path.exists(fuel_economy_path):
            self.fuel_economy =\
                float(utility.read_data(fuel_economy_path))
        if path.exists(mileage_paid_path):
            self.mileage_paid =\
                float(utility.read_data(mileage_paid_path))
        if path.exists(total_hours_path):
            self.total_hours =\
                float(utility.read_data(total_hours_path))
        if path.exists(extra_tips_claimed_path):
            self.extra_tips_claimed =\
                float(utility.read_data(extra_tips_claimed_path))
        if path.exists(end_time_path):
            self.end_time =\
                utility.to_datetime(utility.read_data(end_time_path))
        return self

    def resume_end(self):
        # set all possible paths to varibles
        miles_traveled_path = path.join('shift', 'total_miles_traveled.txt')
        fuel_economy_path = path.join('shift', 'fuel_economy.txt')
        mileage_paid_path = path.join('shift', 'mileage_paid.txt')
        total_hours_path = path.join('shift', 'total_hours.txt')
        extra_tips_claimed_path = path.join('shift', 'extra_tips_claimed.txt')
        end_time_path = path.join('shift', 'shift_end_time.txt')

        while True:
            if not path.exists(miles_traveled_path):
                # input total miles traveled for shift
                self.miles_traveled = utility.write_data(
                    path.join('shift', 'total_miles_traveled.txt'),
                    utility.miles_traveled(
                        'Total miles traveled for this shift:    #.#'))
            elif not path.exists(fuel_economy_path):
                # input fuel economy
                self.fuel_economy = utility.write_data(
                    fuel_economy_path, input_data(
                        '\nEnter fuel economy:    ##.#\n', float,
                        '\nIs this correct? [y/n]\n', str, 'y', 'n'))
            elif not path.exists(mileage_paid_path):
                # input mileage paid
                self.mileage_paid = utility.write_data(
                    mileage_paid_path, input_data(
                        '\nAmount of mileage paid:    $#.##\n$', float,
                        '\nIs this correct? [y/n]\n', str, 'y', 'n', '$'))
            elif not path.exists(total_hours_path):
                # input total hours worked
                self.total_hours = utility.write_data(
                    total_hours_path, input_data(
                        '\nEnter total hours worked:    #.##\n', float,
                        '\nIs this correct? [y/n]\n', str, 'y', 'n'))
            elif not path.exists(extra_tips_claimed_path):
                # input extra claimed/reported tips
                self.extra_tips_claimed = utility.write_data(
                    extra_tips_claimed_path, input_data(
                        '\nExtra tips claimed for shift:    $#.##\n$', float,
                        '\nIs this correct? [y/n]\n', str, 'y', 'n', '$'))
            elif not path.exists(end_time_path):
                # save time for end of shift
                self.end_time =\
                    utility.write_data(end_time_path, utility.now())
            else:
                break
        remove(path.join('shift', 'end_shift'))
        self.consolidate()
        print('Shift has been end!\n')
        utility.enter_to_continue()
        exit()

    def start(self):
        start_time_path = path.join('shift', 'shift_start_time.txt')
        mkdir('shift')
        utility.write_data(start_time_path, utility.now())
        print('\nShift has been started!\n')
        utility.enter_to_continue()
        exit()
