# cnsd: make way to be able take multipule deliveries on one trip
# cnsd: add option to be able to start a second shift for the day (dif store)

# todo: change all variable and attributes called miles_traveled to distance
# todo: change any saved time to just time and remove the date. add To_Datetime().from_time()
# todo: make unit tests for everything
# todo: learn to unit test

# todo: need to finish ending and updating shift for 5-30
# todo: need to finish ending and updating shift for 6-6
# todo: add shift data for 6-14. accidentally deleted it while half asleep
# todo: need to finish ending and updating shift for 6-28. phone died
# todo: need to finish ending and updating shift for 6-30
# todo: need to finish ending and updating shift for 7-11
# todo: need to finish add pretty much everything to shift for 7-21
# todo: need to fix vehical comp for shift on 7-2 through 7-21

from menus import Shift_Tracking_Menu
from objects.shift import Shift
from os import getcwd, path
import re
from resources.system_names import data_directory, shifts_directory
from utility.utility import now

# make directories to store user data
shifts_path = path.join(data_directory, shifts_directory)
if not path.exists(data_directory):
    from os import mkdir
    mkdir(data_directory)
if not path.exists(shifts_path):
    from os import mkdir
    mkdir(shifts_path)

# check for completed shift
if path.exists(Shift(now().date()).file_list()['info']):
    from menus import completed_shift
    shift = completed_shift()
# check if shift has not started
elif not path.exists(Shift(now().date()).file_list()['directory']):
    from processes.input_data import start_shift
    shift = start_shift()
# load shift
else:
    from processes.load import current_shift as load_shift
    shift = load_shift()

# daily shift tracking menu
menu = Shift_Tracking(shift)
while menu.condition:
    menu = Shift_Tracking(menu.shift)
