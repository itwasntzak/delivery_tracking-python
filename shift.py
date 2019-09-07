import os

import util_func

shift_path= os.path.join(
    'shift'
)

def start_shift():
    util_func.delivery_number(
        option='reset'
    )
    os.mkdir(shift_path)
    util_func.write_data(
        path=shift_path,
        file='shift_start_time.txt',
        data=util_func.now()
    )


def end_shift():
    util_func.write_data(
        path=shift_path,
        file='shift_end_time.txt',
        data=util_func.now()
    )
    util_func.delivery_number(
        option='reset'
    )
    exit()


def start_split():
    util_func.write_data(
        path=shift_path,
        file='split_start_time.txt',
        data=util_func.now()
    )
    exit()


def end_split():
    util_func.write_data(
        path=shift_path,
        file='split_end_time.txt',
        data=util_func.now()
    )
