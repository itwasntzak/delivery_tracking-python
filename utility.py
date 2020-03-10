import datetime
from os import path, remove

import delivery
import input_data
import shift


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


def time_taken(start_time, end_time, prompt):
    time_diff = end_time - start_time
    print('\n' + prompt + str(time_diff) + '\n')


def driving(object, prompt, destination):
    from extra_stop import Extra_Stop
    while True:
        if path.exists(path.join(object.path, 'driving-' + destination)):
            pass
        else:
            # create file so program knows while in driving process
            write_data(path.join(object.path, 'driving-' + destination), None)
        wait_for_user = input_data.get_input(
            prompt + '\nC: To complete'
                     '\nE: For extra stop'
                     '\nT: To see current time'
                     '\nQ: To quit program\n\n', str)
        if wait_for_user in ('c', 'C'):
            # remove driving file so code can knows driving has ended
            remove(path.join(object.path, 'driving-' + destination))
            break
        # extra stop option
        elif wait_for_user in ('e', 'E'):
            # remove driving file so code can knows driving has ended
            remove(path.join(object.path, 'driving-' + destination))
    # todo: still need to work how to update shift extra stop id & parent lists
            if isinstance(object, type(shift.Shift(now()))):
                extra_stop = Extra_Stop(object, object.extra_stop_id).start()
                object.extra_stop_numbers.append(extra_stop.id)
                object.extra_stops.append(extra_stop)
                return object
    # todo: still need to work how to update shift extra stop id & parent lists
            elif isinstance(object, type(delivery.Delivery(
                    shift.Shift(now()), ''))):
                extra_stop =\
                    Extra_Stop(object, object.parent.extra_stop_id).start()
                object.parent.extra_stop_numbers.append(extra_stop.id)
                object.parent.extra_stops.append(extra_stop)
                return object
        elif wait_for_user in ('t', 'T'):
            time_taken(object.start_time, now(), 'Current time is:\t')
        elif wait_for_user in ('q', 'Q'):
            quit()
        else:
            print('\nInvalid input...\n')
