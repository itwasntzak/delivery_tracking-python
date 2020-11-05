# cnsd: make way to be able take multipule deliveries on one trip
# cnsd: add option to be able to start a second shift for the day (dif store)

# todo: change all variable and attributes called miles_traveled to distance
# todo: change any saved time to just time and remove the date. add To_Datetime().from_time()
# todo: there are many, many strings in the code files. need to be moved to strings file
# todo: make unit tests for everything

# todo: add shift data for 6-14. accidentally deleted it while half asleep

from menus import Shift_Tracking_Menu
from objects import Shift
from os import path, chdir
from resources.system_names import data_directory, shifts_directory
from utility.utility import now

# chagne directory for termux version
chdir('delivery_tracking')

# make directories to store user data
shifts_path = path.join(data_directory, shifts_directory)
if not path.exists(data_directory):
    from os import mkdir
    mkdir(data_directory)
if not path.exists(shifts_path):
    from os import mkdir
    mkdir(shifts_path)

shift = Shift(now().date())
# check for completed shift
if path.exists(shift.file_list()['info']):
    from menus import Completed_Shift
    menu = Completed_Shift(shift)
    shift = menu.shift
# check if shift has not started
elif not path.exists(shift.file_list()['directory']):
    shift.start()
# load shift
else:
    shift.load_current()

# daily shift tracking menu
Shift_Tracking_Menu(shift)
