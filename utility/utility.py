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


def user_confirmation(prompt):
    prompt += 'Y: yes\nN: no\n'
    while True:
        user_confirmation = get_input(prompt, str)
        if user_confirmation in ('y', 'Y'):
            return True
        elif user_confirmation in ('n', 'N'):
            return False
        else:
            print('\nInvalid input...')
