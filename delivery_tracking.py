# cnsd: make way to be able take multipule deliveries on one trip
# cnsd: add option to be able to start a second shift for the day (dif store)
from os import chdir, path, mkdir

from shift import shift_menu, Shift
from split import Split
from resources.system_names import\
    user_data_directory as user_data, shifts_directory as shifts
from utility import now


shift = Shift(now())
shifts_path = path.join(user_data, shifts)

if not path.exists(user_data):
    mkdir(user_data)
if not path.exists(shifts_path):
    mkdir(shifts_path)

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
