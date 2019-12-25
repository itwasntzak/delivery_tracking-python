from os import path, mkdir
import shutil

import consolidate_data
import id_number
from input_data import input_data
import utility


def start_shift():
    mkdir('shift')
    utility.write_data(
        path.join('shift', 'shift_start_time.txt'), utility.now())
    exit()


def end_shift():
    shift_object = Shift()
    # input total miles traveled for shift
    utility.write_data(
        path.join('shift', 'total_miles_traveled.txt'),
        utility.miles_traveled('Total miles traveled for this shift:    #.#'))
    # input fuel economy
    utility.write_data(path.join('shift', 'fuel_economy.txt'), input_data(
        prompt1='\nEnter fuel economy:    ##.#\n', input_type1=float,
        prompt2='\nIs this correct? [y/n]\n', input_type2=str,
        option_yes='y', option_no='n'))
    # input mileage paid
    utility.write_data(path.join('shift', 'mileage_paid.txt'), input_data(
        prompt1='\nAmount of mileage paid:    $#.##\n', input_type1=float,
        prompt2='\nIs this correct? [y/n]\n', input_type2=str,
        option_yes='y', option_no='n'))
    # input total hours
    utility.write_data(path.join('shift', 'total_hours.txt'), input_data(
        prompt1='\nEnter total hours worked:    $#.##\n', input_type1=float,
        prompt2='\nIs this correct? [y/n]\n', input_type2=str,
        option_yes='y', option_no='n'))
    # input extra claimed
    utility.write_data(
        path.join('shift', 'extra_tips_claimed.txt'),
        input_data(prompt1='\nExtra tips claimed for shift:    $#.##\n$',
                   input_type1=float,
                   prompt2='\nIs this correct? [y/n]\n', input_type2=str,
                   option_yes='y', option_no='n', symbol='$'))
    # save time for end of shift
    utility.write_data(
        path.join('shift', 'shift_end_time.txt'), utility.now())
    consolidate_data.consolidate_shift()
    shutil.move('shift', id_number.assign_id_number(shift_object))
    exit()


def start_split():
    utility.write_data(
        path.join('shift', 'split_start_time.txt'), utility.now())
    exit()


def end_split():
    utility.write_data(
        path.join('shift', 'split_miles_traveled.txt'),
        utility.miles_traveled('Split miles traveled:    #.#'))
    utility.write_data(
        path.join('shift', 'split_end_time.txt'), utility.now())
    consolidate_data.consolidate_split()
    exit()


class Shift:
    def get_id_number(self):
        return self.id_number

    def get_split(self):
        if self.split:
            return self.split
        else:
            return None

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    def get_delivery_quantity(self):
        return self.delivery_quantity

    def get_extra_stop_quantity(self):
        return self.extra_stop_quantity

    def get_fuel_economy(self):
        return self.fuel_economy

    def get_mileage(self):
        return self.mileage_paid

    def get_total_miles(self):
        return self.total_miles_traveled

    def get_total_hours(self):
        return self.total_hours
