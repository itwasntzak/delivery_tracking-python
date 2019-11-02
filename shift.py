import os
import shutil

import consolidate_data
import utility_function


def start_shift():
    os.mkdir('shift')
    utility_function.write_data(
        path='shift', file='shift_start_time.txt', data=utility_function.now())
    exit()


def end_shift():
    utility_function.write_data(
        path='shift', file='shift_end_time.txt', data=utility_function.now())
    consolidate_data.consolidate_shift()
    shutil.move('shift', str(utility_function.now().date()))
    exit()


def start_split():
    utility_function.write_data(
        path='shift', file='split_start_time.txt', data=utility_function.now())
    exit()


def end_split():
    utility_function.write_data(
        path='shift', file='split_end_time.txt', data=utility_function.now())
    utility_function.write_data(
        path='shift', file='split_miles_traveled.txt',
        data=utility_function.miles_traveled(
            prompt='Split miles traveled:    #.#'))
    consolidate_data.consolidate_split()
    exit()
