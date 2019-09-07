import os
import shutil

import delivery
import delivery_tracking
import input_data
import shift
import util_func

delivery_tracking_path = 'delivery_tracking'
delivery_path = os.path.join(
    'delivery_tracking', 'delivery'
)
shift_path = os.path.join(
            'delivery_tracking', 'shift'
)
shift_delivery_path = os.path.join(
            'delivery_tracking', 'shift', 'delivery' + util_func.delivery_number('number')
)
shift_end_time_path = os.path.join(
    'delivery_tracking', 'shift', 'shift_end_time.txt'
)
number_of_deliveries_path = os.path.join(
    'delivery_tracking', 'shift', 'number_of_deliveries.txt'
)


def new_shift():
    while True:
        user_menu_choice = input_data.get_input(
            prompt='\nWhat would you like to do?'
                   '\n1 to start a new shift '
                   '| 0 for settings\n',
            kind=int
        )
        if user_menu_choice == 1:
            shift.start_shift()
            delivery_tracking.shift_menu()
            break
        elif user_menu_choice == 0:
            delivery_tracking.setting_menu()
            continue
        else:
            print('\nInvalid input...')


def ended_shift():
    while True:
        user_menu_choice = input_data.get_input(
            prompt="\nALERT:"
                    "\nToday's shift has already been ended\n"
                    "\nWhat would you like to do?"
                    "\n1 to continue shift | 0 for settings\n",
            kind=int
        )
        if user_menu_choice == 1:
            user_menu_choice2 = input_data.get_input(
                prompt='\nWARNING!!!'
                       '\nThis will delete the already existing:'
                       '\nshift_end_time.txt'
                       '\nAre you sure? [y/n]\n',
                kind=str
            )
            if user_menu_choice2 == 'y':
                os.remove(shift_end_time_path)
                if os.path.exists(number_of_deliveries_path):
                    with open(number_of_deliveries_path, 'r') as file:
                        return util_func.write_data(
                            path=delivery_tracking_path,
                            file='delivery_number.txt',
                            data=file.read()
                        )
                else:
                    break
            elif user_menu_choice2 == 'n':
                break
            else:
                continue
        elif user_menu_choice == 0:
            delivery_tracking.setting_menu()
        else:
            continue


def continue_shift():
    while True:
        user_menu_choice = input_data.get_input(
            prompt='\nWhat would you like to do?'
                   '\n1 to continue shift '
                   '| 0 for settings\n',
            kind=int
        )

        if user_menu_choice == 1:
            delivery_tracking.shift_menu()
            break
        elif user_menu_choice == 0:
            delivery_tracking.setting_menu()
            break
        else:
            print('\nInvalid input...')
            continue


def end_split():
    while True:
        user_menu_choice = input_data.get_input(
            prompt='\nwhat would you like to do?'
                   '\n1 to end split '
                   '| 0 for settings\n',
            kind=int
        )
        if user_menu_choice == 1:
            shift.end_split()
            delivery_tracking.shift_menu()
            break
        elif user_menu_choice == 0:
            delivery_tracking.setting_menu()
            continue
        else:
            print('\nInvalid input...')


def start_delivery():
    delivery.delivery()
    shutil.move(delivery_path, shift_delivery_path)
    util_func.delivery_number('update')


def overwrite_shift_file():
    if os.path.exists(shift_path):
        while True:
            user_choice = input_data.get_input(
                prompt="\nALERT!!!"
                       "\nAre you sure you want to overwrite today's file?"
                       "\n[y/n]\n",
                kind=str
            )
            if user_choice == 'y':
                shutil.rmtree(shift_path)
                shift.start_shift()
                break
            elif user_choice == 'n':
                break
            else:
                print('\nInvalid input...')
                continue
    else:
        print("\nToday's shift has not been started yet")
