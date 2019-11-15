# //TODO: create function to be able to take extra stop sepeate from deliveries
# //TODO: make way to be able take multipule deliveries on one trip
# //TODO: add option to be able to start a second shift for the day (dif store)

import os

import menu_options
import input_data
import shift
import utility_function


shift_start_time_path = os.path.join(
    'shift', 'shift_start_time.txt'
)
shift_end_time_path = os.path.join(
    'shift', 'shift_end_time.txt'
)
split_start_time_path = os.path.join(
    'shift', 'split_start_time.txt'
)
split_end_time_path = os.path.join(
    'shift', 'split_end_time.txt'
)


# //TODO: change to start_up function instead
# //TODO: need to take into consideration split_info.txt
def start_menu():
    os.chdir('delivery_tracking')
    while True:
        # check if shift has started
        if not os.path.exists(shift_start_time_path):
            menu_options.new_shift()
        # check if shift has ended
        elif os.path.exists(shift_end_time_path):
            menu_options.ended_shift()
        # check if a split has or has not been started or ended
        elif os.path.exists(shift_start_time_path)\
                and not os.path.exists(split_start_time_path)\
                or os.path.exists(split_end_time_path):
            shift_menu()
            menu_options.continue_shift()
        # check if split has been started
        elif os.path.exists(shift_start_time_path)\
                and os.path.exists(split_start_time_path)\
                and not os.path.exists(split_end_time_path):
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
            kind=int)

        if user_choice == 1:
            menu_options.overwrite_shift_file()
        elif user_choice == 2:
            utility_function.delivery_number('change')
        elif user_choice == 3:
            utility_function.begin_order_number('change')
        elif user_choice == 0:
            break
        else:
            print('\nInvalid input...')


if __name__ == "__main__":
    start_menu()
