# this script needs to navigate into the correct shift directory
# then it needs to navigate into each delivery directory and load the order files
# after that it needs to check the data to check if it matchs the new 
# way of doing things, and if not to open it in a text editor

from objects import Delivery, Shift
import os
from utility.file import Read, write
from utility.utility import To_Datetime

shift_id = '2020-01-07'
shift = Shift(To_Datetime(shift_id).from_date().date())
path = os.path.join('data', 'shifts', shift_id)
# os.mkdir(path)
os.chdir(path)

# delivery_directories = os.listdir()
# delivery_ids = Read('delivery_ids.txt').integer_list()
# for delivery_id in delivery_ids:
#     os.chdir(f'{delivery_id}')

#     order_ids = Read('order_ids.txt').integer_list()
#     for order_id in order_ids:
#         order_file = f'{order_id}.txt'
#         os.system(f'code {order_file}')

#     os.chdir('..')

# untracked_delivery_ids = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
untracked_delivery_ids = range(7)
for id in untracked_delivery_ids:
    # os.mkdir(f'{id}')
    os.chdir(f'{id}')

    # print(f'{id}')
    # order_ids = input('input order ids\n')
    # write('', 'delivery_info.txt')
    # os.system(f'code delivery_info.txt')
    # write(f'{order_ids}', 'order_ids.txt')
    # for order_id in order_ids.split(','):
        # write('', f'{order_id}.txt')
        # os.system(f'code {order_id}.txt')

    # os.rename('order_numbers.txt', 'order_ids.txt')
    os.system('code delivery_info.txt')
    for order_id in Read('order_ids.txt').integer_list():
        os.system(f'code {order_id}.txt')
    os.chdir('..')

delivery_ids_string = ''
for id in range(untracked_delivery_ids[-1] + 1):
# for id in untracked_delivery_ids:
    delivery_ids_string += f'{id},'

if delivery_ids_string[-1] == ',':
    delivery_ids_string = delivery_ids_string[:-1]

write(delivery_ids_string, 'delivery_ids.txt')

# os.rename('start_time.txt', 'shift_info.txt')
# write('', 'shift_info.txt')
os.system(f'code shift_info.txt')

# os.system(f'explorer {os.path.join("data", "shifts", shift_id)}')
