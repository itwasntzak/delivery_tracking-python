# //TODO: write functions to load data
# //TODO: make way to be able take multipule deliveries on one trip
# //TODO: add option to be able to start a second shift for the day (dif store)
# //TODO: consider tracking ave. speed for each delivery

from datetime import datetime
from os import path, chdir

from continuation import continuation
import extra_stop
import menu_options
import input_data
import shift
import utility


shift_start_time_path = path.join('shift', 'shift_start_time.txt')
shift_end_time_path = path.join('shift', 'shift_end_time.txt')
split_start_time_path = path.join('shift', 'split_start_time.txt')
split_end_time_path = path.join('shift', 'split_end_time.txt')


# //TODO: need to add logic for split_info.txt
def start():
#    chdir('delivery_tracking')
    continuation()
    while True:
        # check if shift has started
        if not path.exists(shift_start_time_path):
            menu_options.new_shift()
        # check if shift has ended
        elif path.exists(shift_end_time_path):
            menu_options.ended_shift()
        # check if a split has or has not been started or ended
        elif path.exists(shift_start_time_path)\
                and not path.exists(split_start_time_path)\
                or path.exists(split_end_time_path):
            shift_menu()
            menu_options.continue_shift()
        # check if split has been started
        elif path.exists(shift_start_time_path)\
                and path.exists(split_start_time_path)\
                and not path.exists(split_end_time_path):
            menu_options.end_split()


def shift_menu():
    shift_object = shift.Shift()
    shift_object.start_time = datetime.strptime(
        utility.read_data(
            path.join('shift', 'shift_start_time.txt')),
        '%Y-%m-%d %H:%M:%S.%f')
    while True:
        user_choice = input_data.get_input(
            prompt='\nWhat would you like to do?'
                   '\n1 to start delivery '
                   '| 2 to end shift '
                   '| 3 to start split '
                   '| 4 to start an extra stop '
                   '| 0 for start menu\n',
            kind=int)
        if user_choice == 1:
            menu_options.start_delivery()
        elif user_choice == 2:
            shift.end_shift()
        elif user_choice == 3:
            shift.start_split()
        elif user_choice == 4:
            extra_stop_start_time_path = path.join(
                'shift', 'extra_stop_start_time.txt')
            utility.write_data(extra_stop_start_time_path, utility.now())
            # //TODO: write a menu option function for extra_stop, enter to cont
            extra_stop.extra_stop(shift_object)
        elif user_choice == 0:
            break
        else:
            print('\nInvalid input...')


# //TODO: none of this will work anymore, all needs to be changed later
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
            utility.delivery_number('change')
        elif user_choice == 3:
            utility.begin_order_number('change')
        elif user_choice == 0:
            break
        else:
            print('\nInvalid input...')


if __name__ == "__main__":
    start()
