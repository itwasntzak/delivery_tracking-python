import datetime
import os

import id_number
import input_data
import consolidate_data
import utility_function


def extra_stops_quantity(var_path):
    extra_stops_quantity_file = os.path.join(
        var_path, 'number_of_extra_stops.txt')
    if os.path.exists(extra_stops_quantity_file):
        with open(extra_stops_quantity_file, 'r+') as file:
            data = int(file.read())
            file.seek(0)
            file.write(str(data + 1))
    else:
        utility_function.write_data(
            path='', file=extra_stops_quantity_file,
            data=str(1))


def extra_stop_numbers(extra_stop_object):
    if os.path.exists(os.path.join('delivery', 'extra_stop_numbers.txt')):
        utility_function.append_data(
            file='extra_stop_numbers.txt',
            data=',' + utility_function.read_data(
                file='extra_stop_number.txt', path='delivery'),
            path='delivery')
    else:
        utility_function.write_data(
            path='delivery', file='extra_stop_numbers.txt',
            data=utility_function.read_data(
                file='extra_stop_number.txt', path='delivery'))


def extra_stop():
    # creating file so program knows while on extra stop, to be able to continue
    utility_function.write_data(
        path='delivery', file='extra_stop', data=None)
    while True:
        wait_for_user = input_data.get_input(
            prompt='\nMaking extra stop...\n1 to continue\n', kind=int)
        if wait_for_user == 1:
            extra_stop_object = Extra_Stop()
            # assign a extra stop number
            extra_stop_object.extra_stop_number = utility_function.write_data(
                path='delivery', file='extra_stop_number.txt',
                data=id_number.assign_id_number(extra_stop_object))
            # input extra stop location
            extra_stop_object.location = utility_function.write_data(
                path='delivery', file='extra_stop_location.txt',
                data=input_data.input_data(
                    prompt1='\nExtra stop location:\n', input_type1=str,
                    prompt2='\nIs this correct? [y/n]\n', input_type2=str,
                    option_yes='y', option_no='n'))
            # input extra stop reason
            extra_stop_object.reason = utility_function.write_data(
                path='delivery', file='extra_stop_reason.txt',
                data=input_data.input_data(
                    prompt1='\nReason for extra stop?\n', input_type1=str,
                    prompt2='\nIs this correct? [y/n]\n', input_type2=str,
                    option_yes='y', option_no='n'))
            # input extra stop miles traveled
            extra_stop_object.miles_traveled = utility_function.write_data(
                path='delivery', file='extra_stop_miles_traveled.txt',
                data=utility_function.miles_traveled(
                    prompt='Extra stop miles traveled:    #.#'))
            # save the time at the end of the extra stop
            extra_stop_object.end_time = utility_function.write_data(
                path='delivery', file='extra_stop_end_time.txt',
                data=utility_function.now())
            extra_stop_numbers()
            # consolidate extra stop data into one file
            consolidate_data.consolidate_extra_stop()
            os.remove(os.path.join('delivery', 'extra_stop'))
            return extra_stop_end_time
        else:
            print('\nInvalid input...')


class Extra_Stop():
    def get_extra_stop_number(self):
        return self.extra_stop_number

    def get_extra_stop_location(self):
        return self.location

    def get_extra_stop_reason(self):
        return self.reason

    def get_extra_stop_miles(self):
        return self.miles_traveled

    def get_extra_stop_end_time(self):
        return self.end_time
