import datetime
import os

import input_data
import consolidate_data
import utility_function


def extra_stop_number(option):
    if option == 'number':
        with open('extra_stop_number.txt', 'r') as file:
            return file.read()
    elif option == 'update':
        with open('extra_stop_number.txt', 'r+') as file:
            extra_stop_number = int(file.read())
            file.seek(0)
            file.write(str(extra_stop_number + 1))


def delivery_number_of_extra_stops():
    number_of_extra_stops_file = os.path.join(
        'delivery', 'number_of_extra_stops.txt')
    if os.path.exists(number_of_extra_stops_file):
        with open(number_of_extra_stops_file, 'r+') as file:
            data = int(file.read())
            file.seek(0)
            file.write(str(data + 1))
    else:
        utility_function.write_data(
            path='', file=number_of_extra_stops_file,
            data=str(1))


# //TODO: i thought this was something else and probably broke it
def shift_extra_stop():
    number_of_extra_stops_file = os.path.join(
        'shift', 'number_of_extra_stops.txt')
    if os.path.exists(number_of_extra_stops_file):
        with open(number_of_extra_stops_file, 'r+') as file:
            data = int(file.read())
            file.seek(0)
            file.write(str(data + 1))
    else:
        with open(number_of_extra_stops_file, 'w') as file:
            file.write(str(1))


def extra_stop_numbers():
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
    # creating file so code knows while on extra stop, to be able to continue
    utility_function.write_data(
        path='delivery', file='extra_stop', data=None
    )
    while True:
        wait_for_user = input_data.get_input(
            prompt='\nMaking extra stop...\n1 to continue\n', kind=int
        )
        if wait_for_user == 1:
            # assign a extra stop number
            utility_function.write_data(
                path='delivery', file='extra_stop_number.txt',
                data=extra_stop_number('number')
            )
            # input extra stop location
            utility_function.write_data(
                path='delivery', file='extra_stop_location.txt',
                data=input_data.input_data(
                    prompt1='\nExtra stop location:\n', input_type1=str,
                    prompt2='\nIs this correct? [y/n]\n', input_type2=str,
                    option_yes='y', option_no='n'
                )
            )
            # input extra stop reason
            utility_function.write_data(
                path='delivery', file='extra_stop_reason.txt',
                data=input_data.input_data(
                    prompt1='\nReason for extra stop?\n', input_type1=str,
                    prompt2='\nIs this correct? [y/n]\n', input_type2=str,
                    option_yes='y', option_no='n'
                )
            )
            # input extra stop miles traveled
            utility_function.write_data(
                path='delivery', file='extra_stop_miles_traveled.txt',
                data=utility_function.miles_traveled(
                    prompt='Extra stop miles traveled:    #.#'))

            # save the time at the end of the extra stop
            extra_stop_end_time = utility_function.write_data(
                path='delivery', file='extra_stop_end_time.txt',
                data=utility_function.now()
            )
            extra_stop_numbers()
            # consolidate extra stop data into one file
            consolidate_data.consolidate_extra_stop()
            # display the amount of time since the delivery was started
            beginning_delivery_time = utility_function.read_data(
                file='delivery_start_time.txt', path='delivery'
            )

            utility_function.time_taken(
                start_time=datetime.datetime.strptime(
                    beginning_delivery_time, '%Y-%m-%d %H:%M:%S.%f'
                ),
                end_time=extra_stop_end_time,
                var_word='Extra stop'
            )
            os.remove(os.path.join('delivery', 'extra_stop'))
            extra_stop_number('update')
            break
        else:
            print('\nInvalid input...')
