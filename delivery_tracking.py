# cnsd: make way to be able take multipule deliveries on one trip
# cnsd: add option to be able to start a second shift for the day (dif store)
from os import chdir, path, mkdir

from shift import shift_menu, Shift
from split import Split
from utility import now


if not path.exists('shifts'):
    mkdir('shifts')
shift = Shift(now())
# check if shift has been completed
if path.exists(shift.info_path):
    shift.completed()
# check if shift has started
elif not path.exists(shift.path):
    shift.start()
else:
    shift.load_current()
# check if split has been started
if path.exists(shift.split.start_time_path):
    shift.split = Split(shift).end()
else:
    shift_menu(shift)

# todo: need to improve modularity of all classes
