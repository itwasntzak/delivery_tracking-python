# todo: make way to be able take multipule deliveries on one trip
# todo: add option to be able to start a second shift for the day (dif store)
# todo: write functions for data anyalisis

from input_data import get_input
from os import chdir, path, mkdir
from shift import shift_menu, Shift
from split import Split
from utility import now


chdir('delivery_tracking')
if not path.exists('shifts'):
    mkdir('shifts')
while True:
    shift = Shift(now().date())
    # check if shift has been completed
    if path.exists(path.join(shift.path, 'shift_info.txt')):
        user_choice = get_input(
            'You have already completed a shift for today.\n'
            'Please select an option:\n'
            'R: Resume today\'s shift\n'
            'O: Overwrite shift\n'
            'Q: Quit program\n\n', str)
        if user_choice in ('r', 'R'):
            shift.resume_shift()
        elif user_choice in ('o', 'O'):
            shift.overwrite()
        elif user_choice in ('q', 'Q'):
            quit()
        else:
            print('\nInvalid input...\n')
    # check if shift has started
    if not path.exists(shift.path):
        shift.start()
    else:
        shift.load_current()
    # check if split has been started
    if path.exists(path.join(shift.path, 'split_start_time.txt')):
        shift.split = Split(shift).end()
    else:
        shift_menu(shift)
