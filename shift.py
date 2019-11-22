from os import path, mkdir
import shutil

import consolidate_data
import id_number
import utility


def start_shift():
    mkdir('shift')
    utility.write_data(
        path.join('shift', 'shift_start_time.txt'), utility.now())
    exit()


# // TODO: add inputs for all the end of shift data
def end_shift():
    shift_object = Shift()
    # input total miles traveled for shift
#    utility_function.write_data(path.join())
    # input fuel economy

    # input mileage paid

    # input total hours

    # input extra claimed

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

# //TODO: write class for shift
class Shift:
    def get_id_number(self):
        return self.id_number

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time
