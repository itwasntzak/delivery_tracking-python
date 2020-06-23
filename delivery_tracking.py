# cnsd: make way to be able take multipule deliveries on one trip
# cnsd: add option to be able to start a second shift for the day (dif store)
from objects.shift import Shift
from objects.split import Split
from os import path
from resources.system_names import\
    user_data_directory as user_data, shifts_directory as shifts
from utility.utility import now

if not path.exists(user_data):
    from os import mkdir
    mkdir(user_data)

shifts_path = path.join(user_data, shifts)
if not path.exists(shifts_path):
    from os import mkdir
    mkdir(shifts_path)

# check if shift has been completed
if path.exists(Shift(now().date()).file_list()['info']):
    from menus import completed_shift
    shift = completed_shift()

# check if shift has started
elif not path.exists(Shift(now().date()).file_list()['directory']):
    from processes.input_data import start_shift
    shift = start_shift()

else:
    from processes.load import current_shift as load_shift
    shift = load_shift()

# check if split has been started
if path.exists(Split(shift).file_list()['start_time']):
    shift.split = Split(shift).end()

else:
    from menus import daily_tracking as main_menu
    shift, menu_condition = main_menu(shift)
    while menu_condition:
        shift, menu_condition = main_menu(shift)
