import os

import util_func


def start_shift():
    util_func.delivery_number(
        option='reset'
    )
    os.mkdir(os.path.join(
        'shift'
    ))
    util_func.write_data(
        path='shift',
        file='shift_start_time.txt',
        data=util_func.now()
    )


def end_shift():
    util_func.write_data(
        path='shift',
        file='shift_end_time.txt',
        data=util_func.now()
    )
    util_func.delivery_number(
        option='reset'
    )
    exit()


def start_split():
    util_func.write_data(
        path='shift',
        file='split_start_time.txt',
        data=util_func.now()
    )
    exit()


def end_split():
    util_func.write_data(
        path='shift',
        file='split_end_time.txt',
        data=util_func.now()
    )