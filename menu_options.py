import os
import shutil

import delivery
import delivery_tracking
import input_data
import shift
import utility_function


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
            prompt="\nALERT:\nToday's shift has already been ended\n"
                   "\nWhat would you like to do?"
                   "\n1 to continue shift | 0 for settings\n",
            kind=int
        )
        if user_menu_choice == 1:
            user_menu_choice2 = input_data.get_input(
                prompt='\nWARNING!!!\nThis will delete the already existing:'
                       '\nshift_end_time.txt\nAre you sure? [y/n]\n',
                kind=str
            )
            if user_menu_choice2 == 'y':
                shutil.move(str(utility_function.now().date()), 'shift')
                os.remove(os.path.join('shift', 'shift_end_time.txt'))
# //TODO: need to rewrite to fix this
                number_of_deliveries_path = os.path.join(
                    'shift', 'number_of_deliveries.txt')
                if os.path.exists(number_of_deliveries_path):
                    with open(number_of_deliveries_path, 'r') as file:
                        return utility_function.write_data(
                            path='', file='delivery_number.txt',
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
                   '\n1 to continue shift | 0 for settings\n',
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
                   '\n1 to end split | 0 for settings\n',
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
    shutil.move('delivery', os.path.join(
        'shift', 'delivery' + str(utility_function.get_delivery_number())))
    while True:
        wait_for_user = input('Press enter to continue.\n')
        if wait_for_user == '':
            exit()
        else:
            continue


def overwrite_shift_file():
    if os.path.exists('shift'):
        while True:
            user_choice = input_data.get_input(
                prompt="\nALERT!!!"
                       "\nAre you sure you want to overwrite today's file?"
                       "\n[y/n]\n",
                kind=str
            )
            if user_choice == 'y':
                shutil.rmtree('shift')
                shift.start_shift()
                break
            elif user_choice == 'n':
                break
            else:
                print('\nInvalid input...')
                continue
    else:
        print("\nToday's shift has not been started yet")
