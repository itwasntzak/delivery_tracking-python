# this script needs to navigate into the correct shift directory
# then it needs to navigate into each delivery directory and load the order files
# after that it needs to check the data to check if it matchs the new 
# way of doing things, and if not to open it in a text editor

from objects import Delivery, Shift
import os
from utility.file import Read, write
from utility.utility import To_Datetime

shift_id = '2020-10-24'
shift = Shift(To_Datetime(shift_id).from_date().date())

os.chdir(os.path.join('data', 'shifts', shift_id))

# delivery_directories = os.listdir()
# delivery_ids = Read('delivery_ids.txt').integer_list()
# for delivery_id in delivery_ids:
#     os.chdir(f'{delivery_id}')

#     order_ids = Read('order_ids.txt').integer_list()
#     for order_id in order_ids:
#         order_file = f'{order_id}.txt'
#         os.system(f'code {order_file}')

#     os.chdir('..')

# untracked_delivery_ids = [11, 12, 13]
# for id in untracked_delivery_ids:
#     os.mkdir(f'{id}')
#     os.chdir(f'{id}')
#     delivery_distance = input('input delivery miles traveled\n')
#     ave_speed = input('input average speed\n')
#     order_ids = input('input order ids\n')
#     order_distance = input('input order miles traveled\n')
#     tip = input('input tip data\n')
#     write(f'{delivery_distance},{ave_speed},,', 'delivery_info.txt')
#     write(f'{order_ids}', 'order_ids.txt')
#     for order_id in order_ids.split(','):
#         write(f'{tip},{order_distance},', f'{order_id}.txt')
#     os.chdir('..')

# delivery_ids_string = ''
# for id in range(untracked_delivery_ids[-1] + 1):
#     delivery_ids_string += f'{id},'

# if delivery_ids_string[-1] == ',':
#     delivery_ids_string = delivery_ids_string[:-1]

# with open('delivery_ids.txt', 'w') as file:
#     file.write(delivery_ids_string)

os.rename('start_time.txt', 'shift_info.txt')
os.system(f'code shift_info.txt')

# os.system(f'explorer {os.path.join("data", "shifts", shift_id)}')
