import datetime
import os
import shutil

import shift


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
            print('\nALERT!!!\nAre you sure you want to change the delivery number?\n1 for yes | 2 for no')
            try:
                user_input = int(input())
                if user_input == 1:
                    print('\nwhat is the new current delivery number:')
                    try:
                        change_delivery_number = int(input())
                        with open(file=os.path.join(path='deliveryNumb.txt'), mode='w') as delivery_number:
                            delivery_number.write(str(change_delivery_number))
                            break

                    except ValueError:
                        print('\ninvalid input...')

                elif user_input == 2:
                    break

            except ValueError:
                print('\ninvalid input...')

            else:
                print('\ninvalid input...')


def begin_order_number(option):
    if option == 'number':
        with open(file=os.path.join('begin_order_number.txt'), mode='r') as first3:
            return first3.read()

    elif option == 'change':
        while True:
            print('\nALERT!!!\nAre you sure you want to change the order number preset?\n1 for yes | 2 for no')
            try:
                user_input = int(input())
                if user_input == 1:
                    print('\nWhat is the new set of 3 numbers for order number preset:')
                    first_3_numbers = int(input())
                    with open(file=os.path.join(path='begin_order_number.txt'), mode='w') as first3:
                        first3.write(str(first_3_numbers))

                elif user_input == 2:
                    break

            except ValueError:
                print('\ninvalid input...')

            else:
                print('\ninvalid input...')


def overWriteCheck():
    if os.path.exists(path=os.path.join(path='shift')) == True:
        while True:
            print("\nALERT!!!\nAre you sure you want to overwrite today's file?\n1 for yes | 2 for no")
            try:
                user_input = int(input())
                if user_input == 1:
                    shutil.rmtree(path=os.path.join(path='shift'))
                    shift.start_shift()
                    break

                elif user_input == 2:
                    break
            except ValueError:
                print('\ninvalid input...')
            else:
                print('\ninvalid input...')

    else:
        return print("\nALERT!!!\nfile doesn't exist")


def time_took(start_time, end_time, var_word):
    time_dif = end_time - start_time
    minutes = int(time_dif.total_seconds() / 60)
    seconds = str(time_dif.total_seconds() - (minutes * 60))

    if minutes == 0:
        print('\nIt took you    ' + seconds + '   seconds to complete this ' + var_word)

    elif minutes >= 1:
        print('\nIt took you    ' + str(minutes) + ':' + seconds + '    to complete this ' + var_word)

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