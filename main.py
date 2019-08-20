#todo still needs to be refactored

import os
import shutil

import shift
import delivery
import util_func
import input_data


def startMenu():
    while True:
        if os.path.exists(os.path.join('shift', 'shift_start_time.txt')) == False:
            print('\nWhat would you like to do?\n1 to start a new shift | 0 for settings')
            try:
                user_input = int(input())
                if user_input == 1:
                    shift.start_shift()
                    shift_menu()
                    continue
                elif user_input == 0:
                    setting_menu()
                    continue
            except ValueError:
                print('\ninvalid input...')
            else:
                print('\ninvalid input...')

        elif os.path.exists(os.path.join('shift', 'shift_end_time.txt')) == True:
            try:
                user_input = input_data.input_data(
                    prompt1="\nALERT:\nToday's shift has already been ended\n\nWhat would you like to do?\n1 to continue shift | 0 for settings",
                    input_type1=int,
                    prompt2='\nWARNING!!!\nThis will delete the already existing end_shift_file.txt',
                    input_type2=str,
                    option_yes='y',
                    option_no='n')
                if user_input == 1:
                    os.remove(os.path.join('shift', 'shift_end_time.txt'))
                    with open(os.path.join('shift', 'number_of_deliveries.txt'), 'r') as file:
                        util_func.write_data(path='', file='delivery_number.txt', data=file.read())
                    continue
                elif user_input == 0:
                    setting_menu()
                    continue
            except ValueError:
                print('\ninvalid input...')
            else:
                print('\ninvalid input...')

        elif os.path.exists(os.path.join('shift', 'shift_start_time.txt')) == True and os.path.exists(os.path.join('shift', 'split_start_time.txt')) == False or os.path.exists(os.path.join('shift', 'split_end_time.txt')) == True:
            shift_menu()
            print('\nWhat would you like to do?\n1 to continue shift | 0 for settings')
            try:
                user_input = int(input())
                if user_input == 1:
                    shift_menu()
                    continue
                elif user_input == 0:
                    setting_menu()
                    continue
            except ValueError:
                print('\ninvalid input...')
            else:
                print('\ninvalid input...')

        elif os.path.exists(os.path.join('shift', 'shift_start_time.txt')) == True and os.path.exists(os.path.join('shift', 'split_start_time.txt')) == True:
            print('\nwhat would you like to do?\n1 to end split | 0 for settings')
            try:
                user_input = int(input())
                if user_input == 1:
                    shift.end_split()
                    shift_menu()
                    continue
                elif user_input == 0:
                    setting_menu()
                    continue
            except ValueError:
                print('\ninvalid input...')
            else:
                print('\ninvalid input...')


def shift_menu():
    while True:
        print('\nWhat would you like to do?\n1 to start delivery | 2 to end shift | 3 to start split | 0 for start menu')
        try:
            user_input = int(input())
            if user_input == 1:
                delivery.delivery()
                shutil.move(os.path.join('delivery'), os.path.join('shift', 'delivery' + util_func.delivery_number('number')))
                util_func.delivery_number('update')
                continue
            elif user_input == 2:
                shift.end_shift()
                exit()
            elif user_input == 3:
                shift.start_split()
                exit()
            elif user_input == 0:
                break
        except ValueError:
            print('\ninvalid input...')
        else:
            print('\ninvalid input...')


def setting_menu():
    while True:
        print('\nWhat setting to change:\n1 to overwrite shift file | 2 to change deliver number | 3 to change order number preset | 0 to go back')
        try:
            user_input = int(input())
            if user_input == 1:
                util_func.overWriteCheck()
                break
            elif user_input == 2:
                print('\nCurrently delivery number is at:    ' + str(util_func.delivery_number('number')))
                util_func.delivery_number('change')
                continue
            elif user_input == 3:
                print('\nCurrently first 3 numbers of order numbers are set to:    ' + util_func.begin_order_number('number'))
                util_func.begin_order_number('change')
                continue
            elif user_input == 0:
                break
        except ValueError:
            print('\ninvalid input...')
        else:
            print('\ninvalid input...')


if __name__ == "__main__":
    startMenu()
