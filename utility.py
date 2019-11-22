import datetime
import os

import input_data


def now():
    return datetime.datetime.now()


def miles_traveled(prompt, variable_path=''):
    return input_data.input_data(
        prompt1='\n' + prompt + '\n',
        input_type1=float,
        prompt2=' miles\nIs this correct? [y/n]\n',
        input_type2=str,
        option_yes='y',
        option_no='n')


def time_taken(start_time, end_time, var_word):
    time_difference = end_time - start_time
    print('\n' + var_word + ' completed in:\t' + str(time_difference) + '\n')


def write_data(file, data):
    with open(file, 'w') as file_object:
        file_object.write(str(data))
        return data


def append_data(file, data):
    with open(file, 'a') as file_object:
        return file_object.write(str(data))


def read_data(file):
    with open(file, 'r') as file_object:
        return file_object.read()
