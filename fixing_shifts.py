# this script needs to navigate into the correct shift directory
# then it needs to navigate into each delivery directory and load the order files
# after that it needs to check the data to check if it matchs the new 
# way of doing things, and if not to open it in a text editor

from objects import Delivery, Shift
import os
from utility.file import Read, write
from utility.utility import now, To_Datetime
from synchronize import send_completed_shift


list = Read(Shift(now().date()).file_list()['completed_ids']).comma()
id_list = [To_Datetime(date).from_date().date() for date in list]

shifts_list = [Shift(date).load_completed() for date in id_list]
for shift in shifts_list:
    print(str(shift.id))
    send_completed_shift(shift)
