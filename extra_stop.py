import datetime
import os

import id_number
import input_data
import consolidate_data
import utility_function


# //TODO: update to be able to work for delivery or shift extra stops
def extra_stop_quantity():
    extra_stop_quantity_path = os.path.join(
        'delivery', 'extra_stop_quantity.txt')

    if os.path.exists(extra_stop_quantity_path):
        utility_function.write_data(extra_stop_quantity_path,
                                     int(utility_function.read_data(
                                        extra_stop_quantity_path)) + 1)
    else:
        utility_function.write_data(extra_stop_quantity_path, str(1))


def extra_stop_numbers(extra_stop_object):
    if os.path.exists(os.path.join('delivery', 'extra_stop_numbers.txt')):
        utility_function.append_data(
            file='extra_stop_numbers.txt',
            data=',' + str(extra_stop_object.get_id_number()),
            path='delivery')
    else:
        utility_function.write_data(
            path='delivery', file='extra_stop_numbers.txt',
            data=extra_stop_object.get_id_number())


def extra_stop(delivery_object):
    # indicator to program when extra stop has been started
    utility_function.write_data(os.path.join('delivery', 'extra_stop'), None)
    while True:
        wait_for_user = input_data.get_input(
            prompt='\nMaking extra stop...\n1 to continue\n', kind=int)
        if wait_for_user == 1:
            extra_stop_object = Extra_Stop()
            # assign a extra stop id number
            extra_stop_object.id_number = utility_function.write_data(
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
            extra_stop_numbers(extra_stop_object)
            # consolidate extra stop data into one file
            consolidate_data.consolidate_extra_stop()
            # display the amount of time since the delivery was started
            utility_function.time_taken(
                start_time=delivery_object.get_start_time(),
                end_time=extra_stop_object.get_end_time(),
                var_word='Extra stop')
            # remove file telling program that on extra stop
            os.remove(os.path.join('delivery', 'extra_stop'))
            extra_stop_quantity()
            return extra_stop_object
        else:
            print('\nInvalid input...')


class Extra_Stop():
    def get_id_number(self):
        return self.id_number

    def get_extra_stop_location(self):
        return self.location

    def get_extra_stop_reason(self):
        return self.reason

    def get_extra_stop_miles(self):
        return self.miles_traveled

    def get_end_time(self):
        return self.end_time
