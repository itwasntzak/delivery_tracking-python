import datetime
import os

import input_data
import process_data
import utility_function


delivery_path = os.path.join(
    'delivery'
)
on_extra_stop_path = os.path.join(
    'delivery', 'extra_stop'
)
extra_stop_number_path = os.path.join(
    'extra_stop_number.txt'
)


def extra_stop_number(option):
    if option == 'number':
        with open(extra_stop_number_path, 'r') as file:
            return file.read()
    elif option == 'update':
        with open(extra_stop_number_path, 'r+') as file:
            extra_stop_number = int(file.read())
            file.seek(0)
            file.write(str(extra_stop_number + 1))


def extra_stop():
    # creating file so code knows while on extra stop, to be able to continue
    with open(on_extra_stop_path, 'w'):
        pass

    while True:
        wait_for_user = input_data.get_input(
            prompt='\nMaking extra stop...'
                   '\n1 to continue\n',
            kind=int
        )
        if wait_for_user == 1:
            # assign a extra stop number
            utility_function.write_data(
                path=delivery_path,
                file='extra_stop_number.txt',
                data=extra_stop_number('number')
            )
        # input extra stop location
            utility_function.write_data(
                path=delivery_path,
                file='extra_stop_location.txt',
                data=input_data.input_data(
                    prompt1='\nExtra stop location:\n',
                    input_type1=str,
                    prompt2='\nIs this correct? [y/n]\n',
                    input_type2=str,
                    option_yes='y',
                    option_no='n'
                )
            )
        # input extra stop reason
            utility_function.write_data(
                path=delivery_path,
                file='extra_stop_reason.txt',
                data=input_data.input_data(
                    prompt1='\nReason for extra stop?\n',
                    input_type1=str,
                    prompt2='\nIs this correct? [y/n]\n',
                    input_type2=str,
                    option_yes='y',
                    option_no='n'
                )
            )
        # input extra stop miles traveled
            utility_function.miles_traveled(
                prompt='Extra miles traveled:    #.#', var_path='extra_stop_'
            )

        # save the time at the end of the extra stop
            extra_stop_end_time = utility_function.write_data(
                path=delivery_path,
                file='extra_stop_end_time.txt',
                data=utility_function.now()
            )
        # consolidate extra stop data into one file
            process_data.consolidate_extra_stop()
        # display the amount of time since the delivery was started
            beginning_delivery_time = utility_function.read_data(
                path=delivery_path,
                file='delivery_start_time.txt'
            )

            utility_function.time_took(
                start_time=datetime.datetime.strptime(
                    beginning_delivery_time, '%Y-%m-%d %H:%M:%S.%f'
                ),
                end_time=extra_stop_end_time,
                var_word='Extra stop'
            )
            extra_stop_number('update')
            os.remove(on_extra_stop_path)
            break
        else:
            print('\nInvalid input...')


#//TODO: add a function for writting and update a number of extra stops file

#//TODO: make a function that will write extra stop numbers to a file in the delivery
