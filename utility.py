import datetime
from os import path, remove

from input_data import get_input


def now():
    return datetime.datetime.now()


def to_datetime(string):
    return datetime.datetime.strptime(string, '%Y-%m-%d %H:%M:%S.%f')


def to_money(value):
    return '${:.2f}'.format(round(value, 2))


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


# todo: func cacluates len of strings, force everything to same screen length
def time_taken(start_time, end_time, prompt):
    time_diff = end_time - start_time
    print(f"\n{prompt}     {time_diff}\n")


def driving(object, prompt, destination):
    from extra_stop import Extra_Stop
    while True:
        if path.exists(path.join(object.path, 'driving-' + destination)):
            pass
        else:
            # create file so program knows while in driving process
            write_data(path.join(object.path, 'driving-' + destination), None)
        wait_for_user = get_input(
            f'{prompt}\n'
            'C: To complete\n'
            'E: For extra stop\n'
            'T: See current time\n'
            'Q: Quit program\n\n', str)
        if wait_for_user in ('c', 'C'):
            # remove driving file so code can knows driving has ended
            remove(path.join(object.path, 'driving-' + destination))
            break
        # extra stop option
        elif wait_for_user in ('e', 'E'):
            extra_stop = Extra_Stop(object).start()
            object.extra_stop_ids.append(extra_stop.id)
            object.extra_stops.append(extra_stop)
        elif wait_for_user in ('t', 'T'):
            time_taken(object.start_time, now(), 'Current time is:\t')
        elif wait_for_user in ('q', 'Q'):
            quit()
        else:
            print('\nInvalid input...\n')
    return object
