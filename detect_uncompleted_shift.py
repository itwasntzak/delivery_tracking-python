from objects import Shift
import os
from utility.file import Read
from utility.utility import now, To_Datetime



id_list = Read(Shift(now().date()).file_list()['completed_ids']).comma()
uncompleted_id_list = []

os.chdir(os.path.join('data', 'shifts'))
for directory in os.listdir():
    if directory not in id_list:
        uncompleted_id_list.append(directory)

print(f'Total uncompleted shifts: {len(uncompleted_id_list)}')
print('List of uncompleted dates:')
for directory in uncompleted_id_list:
    print(directory)
