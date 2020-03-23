from os import path, remove

from utility import to_datetime, write_data


def read_data(file):
    with open(file, 'r') as file_object:
        return file_object.read()


def write_data(file, data):
    with open(file, 'w') as file_object:
        file_object.write(str(data))
        return data


shift_list_path = path.join('shift_numbers.txt')
shift_list = read_data(shift_list_path).split(',')

numbers = 0
ids = 0

for shift in shift_list:
    if path.exists(path.join('shifts', shift)):
        shift_info_path = path.join('shifts', shift, 'shift_info.txt')
        shift_data = read_data(shift_info_path).split(',')
        data_list = [float(shift_data[0]), float(shift_data[1]), float(shift_data[2]), 0.00, float(shift_data[3]), float(shift_data[4]), to_datetime(shift_data[5]), to_datetime(shift_data[6])]
        data = '{0[0]},{0[1]},{0[2]},{0[3]},{0[4]},{0[5]},{0[6]},{0[7]}'.format(data_list)
        write_data(shift_info_path, data)
        numbers += 1

text = f'Number of changed files{numbers:>20}\n'\
       f'Number of unchanged files{ids:>20}'

print(text)
