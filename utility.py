import datetime
from os import path, remove

import extra_stop
import input_data


def now():
    return datetime.datetime.now()


def to_datetime(string):
    return datetime.datetime.strptime(string, '%Y-%m-%d %H:%M:%S.%f')


def enter_to_continue():
    while True:
        wait_for_user = input('Press enter to continue.\n')
        if wait_for_user == '':
            break
        else:
            continue


def write_data(file, data):
    with open(file, 'w') as file_object:
        file_object.write(str(data))
        return data


def append_data(file, data):
    with open(file, 'a') as file_object:
        return file_object.write(str(data))


def read_data(file):
    with open(file, 'r') as file_object:
        return file_object.read()


def miles_traveled(prompt):
    return input_data.input_data(
        '\n' + prompt + '\n', float,
        ' miles\nIs this correct? [y/n]\n', str, 'y', 'n')


def time_taken(start_time, end_time, variable_word):
    time_difference = end_time - start_time
    print('\n' + variable_word + ' completed in:\t' + str(time_difference) + '\n')


def driving(object, prompt, destination):
    if path.exists(path.join('delivery', 'driving-' + destination)):
        pass
    else:
        # create file so code knows while driving, and can continue from there
        write_data(path.join('delivery', 'driving-' + destination), None)
    while True:
        wait_for_user = input_data.get_input(
            prompt + '\nC after completing\n'
                     'E for extra stop\n', str)
        if wait_for_user in ('c', 'C'):
            # remove driving file so code can knows driving has ended
            remove(path.join('delivery', 'driving-' + destination))
            break
        elif wait_for_user in ('e', 'E'):
            # remove driving file so code can knows driving has ended
            remove(path.join('delivery', 'driving-' + destination))
            # extra stop option
            extra_stop.Extra_Stop().extra_stop(object)
            continue
        else:
            print('\nInvalid input...')
