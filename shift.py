import os

import util_func

folder_path= os.path.join('delivery_tracking', 'shift')

def start_shift():
    util_func.delivery_number(
        option='reset'
    )
    os.mkdir(folder_path)
    util_func.write_data(
        path=folder_path,
        file='shift_start_time.txt',
        data=util_func.now()
    )


def end_shift():
    util_func.write_data(
        path=folder_path,
        file='shift_end_time.txt',
        data=util_func.now()
    )
    util_func.delivery_number(
        option='reset'
    )
    exit()


def start_split():
    util_func.write_data(
        path=folder_path,
        file='split_start_time.txt',
        data=util_func.now()
    )
    exit()


def end_split():
    util_func.write_data(
        path=folder_path,
        file='split_end_time.txt',
        data=util_func.now()
    )
