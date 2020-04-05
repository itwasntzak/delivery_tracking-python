# cnsd: make way to be able take multipule deliveries on one trip
# cnsd: add option to be able to start a second shift for the day (dif store)
from os import chdir, path, mkdir

from shift import shift_menu, Shift
from split import Split
from utility import now


if not path.exists('shifts'):
    mkdir('shifts')
while True:
    shift = Shift(now())
    # check if shift has been completed
    if path.exists(path.join(shift.path, 'shift_info.txt')):
        shift.completed()
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
