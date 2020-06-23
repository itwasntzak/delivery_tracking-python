import datetime
from os import path, remove


def now():
    return datetime.datetime.now()


def to_datetime(string):
    return datetime.datetime.strptime(string, '%Y-%m-%d %H:%M:%S.%f')


def to_money(value):
    return '${:.2f}'.format(round(value, 2))


# todo: func cacluates len of strings, force everything to same screen length
def time_taken(start_time, end_time, prompt):
    time_diff = end_time - start_time
    print(f"\n{prompt}\t{time_diff}")


def enter_to_continue(prompt):
    while True:
        print(prompt + '\n')
        wait_for_user = input('Press enter to continue.\n')
        if wait_for_user == '':
            break
        else:
            continue


# todo: need to fix to work with new system
# todo: want to change so that there isnt an order quantity file,
#       press '[aA]' to add order, press '[eE]' take extra stop, press '[cC]' to complete delivery
def driving(delivery, prompt, destination):
    from extra_stop import Extra_Stop
    while True:
        if path.exists(path.join(delivery.path, 'driving-' + destination)):
            pass
        else:
            # create file so program knows while in driving process
            write_data(path.join(delivery.path, 'driving-' + destination), None)
        wait_for_user = get_input(
            f'{prompt}\n'
            'C: To complete\n'
            'E: For extra stop\n'
            'T: See current time\n'
            'Q: Quit program\n', str)
        if wait_for_user in ('c', 'C'):
            # remove driving file so code can knows driving has ended
            remove(path.join(delivery.path, 'driving-' + destination))
            break
        # extra stop option
        elif wait_for_user in ('e', 'E'):
            delivery.add_extra_stop(Extra_Stop(delivery).start())
        elif wait_for_user in ('t', 'T'):
            time_taken(delivery.start_time, now(), 'Current time is:\t')
        elif wait_for_user in ('q', 'Q'):
            exit()
        else:
            print('\nInvalid input...\n')
    return delivery
