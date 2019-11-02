import datetime
import os

import input_data


def now():
    return datetime.datetime.now()


def delivery_number():
    file_path = os.path.join('shift', 'number_of_deliveries.txt')
    if os.path.exists(file_path):
        delivery_number = get_delivery_number()
        write_data(path='', file=file_path, data=delivery_number + 1)
    else:
        write_data(path='', file=file_path, data=0)


def get_delivery_number():
    file_path = os.path.join('shift', 'number_of_deliveries.txt')
    if os.path.exists(file_path):
        return int(read_data(file=file_path))
    else:
        return print('No deliveries have been completed yet.')


# //TODO: need to work on this to change number of deliveries
# def change_delivery_number():
#    file_path = os.path.join('shift', 'number_of_deliveries.txt')
#    while True:
#        print(
#            '\nCurrently delivery number is at:    '
#            + str(read_data(
#                path='',
#                file=file_path)))
#        user_choice = input_data.get_input(
#            prompt='\nALERT!!!'
#                   '\nAre you sure you want to change the delivery number?'
#                   '\n[y/n]\n',
#            kind=str)

#        if user_choice == 'y':
#            write_data(
#                path=delivery_tracking_path,
#                file='delivery_number.txt',
#                data=input_data.get_input(
#                   prompt='\nWhat is the new current delivery number:\n',
#                    kind=int))
#            break
#        elif user_choice == 'n':
#            break
#        else:
#            print('\nInvalid input...')


def miles_traveled(prompt, variable_path=''):
    return write_data(
        path=variable_path,
        file='miles_traveled.txt',
        data=input_data.input_data(
            prompt1='\n' + prompt + '\n',
            input_type1=float,
            prompt2='\nIs this correct? [y/n]\n',
            input_type2=str,
            option_yes='y',
            option_no='n'
        )
    )


def time_taken(start_time, end_time, var_word):
    time_difference = end_time - start_time
    print('\n' + var_word + ' completed in:\t' + str(time_difference) + '\n')


def write_data(path, file, data):
    with open(os.path.join(path, file), 'w') as file_object:
        file_object.write(str(data))
        return data


def append_data(file, data, path=''):
    with open(os.path.join(path, file), 'a') as file_object:
        return file_object.write(str(data))


def read_data(file, path=''):
    with open(os.path.join(path, file), 'r') as file_object:
        return file_object.read()
