import datetime
import os

import input_data


delivery_path = os.path.join(
    'delivery'
)
delivery_tracking_path = ''
delivery_number_path = os.path.join(
    'delivery_number.txt'
)
begin_order_number_path = os.path.join(
    'begin_order_number.txt'
)


def now():
    return datetime.datetime.now()


def delivery_number(option):
    if option == 'number':
        with open(delivery_number_path, 'r') as delivery_number:
            return delivery_number.read()
    elif option == 'update':
        with open(delivery_number_path, 'r+') as delivery_number:
            previous_delivery_number = int(delivery_number.read())
            delivery_number.seek(0)
            delivery_number.write(str(previous_delivery_number + 1))
    elif option == 'reset':
        with open(delivery_number_path, 'w') as delivery_number:
            delivery_number.write('0')
    elif option == 'change':
        while True:
            print(
                '\nCurrently delivery number is at:    '
                + str(read_data(
                    path=delivery_tracking_path,
                    file='delivery_number.txt'
                ))
            )
            user_choice = input_data.get_input(
                prompt='\nALERT!!!'
                       '\nAre you sure you want to change the delivery number?'
                       '\n[y/n]\n',
                kind=str
            )

            if user_choice == 'y':
                write_data(
                    path=delivery_tracking_path,
                    file='delivery_number.txt',
                    data=input_data.get_input(
                        prompt='\nWhat is the new current delivery number:\n',
                        kind=int
                    )
                )
                break
            elif user_choice == 'n':
                break
            else:
                print('\nInvalid input...')


def begin_order_number(option):
    if option == 'number':
        with open(begin_order_number_path, 'r') as first_half:
            return first_half.read()
    elif option == 'change':
        while True:
            print(
                '\nCurrently first 3 numbers of order numbers are set to:    '
                + read_data(
                    path=delivery_tracking_path,
                    file='begin_order_number.txt'
                )
            )
            user_choice = input_data.get_input(
                prompt='\nALERT!!!'
                       '\nAre you sure you want to change the order number preset?'
                       '\n[y/n]\n',
                kind=str
            )
            if user_choice == 'y':

                new_first_half = input_data.get_input(
                    prompt='\nWhat are the new 3 numbers for order number preset:  ###\n',
                    kind=int
                )
                write_data(
                    path=delivery_tracking_path,
                    file='begin_order_number.txt',
                    data=new_first_half
                )
                break
            elif user_choice == 'n':
                break
            else:
                print('\nInvalid input...')
                continue


def miles_traveled(prompt, var_path=''):
    return write_data(
        path=delivery_path,
        file=var_path + 'miles_traveled.txt',
        data=input_data.input_data(
            prompt1='\n' + prompt + '\n',
            input_type1=float,
            prompt2='\nIs this correct? [y/n]\n',
            input_type2=str,
            option_yes='y',
            option_no='n'
        )
    )


def time_took(start_time, end_time, var_word):
    time_difference = end_time - start_time
    print('\n' + var_word + ' completed in:\t' + str(time_difference) + '\n')


def write_data(path, file, data):
    with open(os.path.join(path, file), 'w') as file_object:
        file_object.write(str(data))
        return data


def append_data(path, file, data):
    with open(os.path.join(path, file), 'a') as file_object:
        return file_object.write(str(data))


def read_data(path, file):
    with open(os.path.join(path, file), 'r') as file_object:
        return file_object.read()






'''def areYouSure(option):
    while True:
        print('\n' + option + ' is this correct?\n1 for yes | 2 for no')
        try:
            areYouSure = int(input())
            if areYouSure == 1:
                return True

            elif areYouSure == 2:
                return False

        except ValueError:
            print('\ninvalid input...')

        else:
            print('\ninvalid input...')'''
