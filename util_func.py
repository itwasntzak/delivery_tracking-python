import datetime
import os
import shutil

import input_data


def now():
    return datetime.datetime.now()


def delivery_number(option):
    if option == 'number':
        with open(os.path.join('delivery_number.txt'), 'r') as delivery_number:
            return delivery_number.read()
    elif option == 'update':
        with open(os.path.join('delivery_number.txt'), 'r+') as delivery_number:
            previous_delivery_number = int(delivery_number.read())
            delivery_number.seek(0)
            delivery_number.write(str(previous_delivery_number + 1))
    elif option == 'reset':
        with open(os.path.join('delivery_number.txt'), 'w') as delivery_number:
            delivery_number.write('0')
    elif option == 'change':
        while True:
            user_choice = input_data.get_input(
                prompt='\nALERT!!!'
                      '\nAre you sure you want to change the delivery number?'
                       '\n[y/n]\n',
                kind=str
            )

            if user_choice == 'y':
                    new_delivery_number = input_data.get_input(
                        prompt='\nWhat is the new current delivery number:\n',
                        kind=int
                    )
                    write_data(
                        path='',
                        file='delivery_number.txt',
                        data=new_delivery_number
                    )
                    break
            elif user_choice == 'n':
                break
            else:
                print('\nInvalid input...')
                continue


def begin_order_number(option):
    if option == 'number':
        with open(os.path.join('begin_order_number.txt'), 'r') as first_half:
            return first_half.read()
    elif option == 'change':
        while True:
            user_choice = input_data.get_input(
                prompt='\nALERT!!!\nAre you sure you want to change the order number preset?'
                '\n[y/n]\n',
                kind=str
            )
            if user_choice == 'y':

                new_first_half = input_data.get_input(
                    prompt='\nWhat are the new 3 numbers for order number preset:  ###\n',
                    kind=int
                )
                write_data(
                    path='',
                    file='begin_order_number.txt',
                    data=new_first_half
                )
                break
            elif user_choice == 'n':
                break
            else:
                print('\nInvalid input...')
                continue


def time_took(start_time, end_time, var_word):
    time_dif = end_time - start_time
    minutes = int(time_dif.total_seconds() / 60)
    seconds = str(time_dif.total_seconds() - (minutes * 60))
    if minutes < 1:
        print('\nIt took you    '
              + seconds
              + '   seconds to complete this ' + var_word)

    elif minutes >= 1:
        print('\nIt took you    '
              + str(minutes) + ':' + seconds
              + '    to complete this ' + var_word)

    elif minutes >= 60:
        print('\nIt took you more then an hour to complete this order')


def write_data(path, file, data, back=False):
    with open(file=os.path.join(path, file), mode='w') as file_object:
        file_object.write(str(data))

    if back == True:
        return data
    else:
        pass


def read_data(path, file):
    with open(file=os.path.join(path, file), mode='r') as fileObject:
        return fileObject.read()






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