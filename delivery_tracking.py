import os

import menu_options
import input_data
import shift
import util_func


def start_menu():
    while True:
        # check if shift has started, if not start a new one
        if not os.path.exists(os.path.join(
                'delivery_tracking',
                'shift',
                'shift_start_time.txt'
        )):
            menu_options.new_shift()
        # check if shift has ended
        elif os.path.exists(os.path.join(
                'delivery_tracking',
                'shift',
                'shift_end_time.txt'
        )):
            menu_options.ended_shift()
        # check if a split has or has not been started or ended
        elif os.path.exists(os.path.join(
                'delivery_tracking',
                'shift',
                'shift_start_time.txt'))\
            and not os.path.exists(os.path.join(
                'delivery_tracking',
                'shift',
                'split_start_time.txt'))\
            or os.path.exists(os.path.join(
                'delivery_tracking',
                'shift',
                'split_end_time.txt'
        )):
            shift_menu()
            menu_options.continue_shift()
        # check if split has been started
        elif os.path.exists(os.path.join(
                'delivery_tracking',
                'shift',
                'shift_start_time.txt'))\
            and os.path.exists(os.path.join(
                'delivery_tracking',
                'shift',
                'split_start_time.txt'))\
            and not os.path.exists(os.path.join(
                'delivery_trackin',
                'shift',
                'split_end_time.txt'
        )):
            menu_options.end_split()


def shift_menu():
    while True:
        user_choice = input_data.get_input(
            prompt='\nWhat would you like to do?'
                   '\n1 to start delivery '
                   '| 2 to end shift '
                   '| 3 to start split '
                   '| 0 for start menu\n',
            kind=int
        )
        if user_choice == 1:
            menu_options.start_delivery()
        elif user_choice == 2:
            shift.end_shift()
        elif user_choice == 3:
            shift.start_split()
        elif user_choice == 0:
            break
        else:
            print('\nInvalid input...')


def setting_menu():
    while True:
        user_choice = input_data.get_input(
            prompt='\nWhat setting to change:'
                    '\n1 to overwrite shift file '
                    '| 2 to change deliver number '
                    '| 3 to change order number preset '
                    '| 0 to go back\n',
            kind=int
        )

        if user_choice == 1:
            menu_options.overwrite_shift_file()
        elif user_choice == 2:
            util_func.delivery_number('change')
        elif user_choice == 3:
            util_func.begin_order_number('change')
        elif user_choice == 0:
            break
        else:
            print('\nInvalid input...')


if __name__ == "__main__":
    start_menu()
