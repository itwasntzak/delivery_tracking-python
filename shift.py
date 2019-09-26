import os
import shutil


import utility_function


def start_shift():
    utility_function.delivery_number(option='reset')
    os.mkdir('shift')
    utility_function.write_data(
        path='shift',
        file='shift_start_time.txt',
        data=utility_function.now()
    )


def end_shift():
    utility_function.write_data(
        path='shift',
        file='shift_end_time.txt',
        data=utility_function.now()
    )
    utility_function.delivery_number(option='reset')
    shutil.move('shift', str(utility_function.now().date()))
    exit()


def start_split():
    utility_function.write_data(
        path='shift',
        file='split_start_time.txt',
        data=utility_function.now()
    )
    exit()


def end_split():
    utility_function.write_data(
        path='shift',
        file='split_end_time.txt',
        data=utility_function.now()
    )
