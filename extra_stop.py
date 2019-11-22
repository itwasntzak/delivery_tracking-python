from os import path, remove

import consolidate_data
import delivery
import id_number
import input_data
import shift
import utility


def extra_stop_quantity(directory):
    extra_stop_quantity_path =\
        path.join(directory, 'extra_stop_quantity.txt')
    if path.exists(extra_stop_quantity_path):
        utility.write_data(
            extra_stop_quantity_path, int(utility.read_data(
                extra_stop_quantity_path)) + 1)
    else:
        utility.write_data(extra_stop_quantity_path, str(1))


# //TODO: remove quantity files, and instead use len() to check amount in list
def extra_stop(object):
    if isinstance(object, type(delivery.Delivery())):
        # set variable path for files to be written
        directory = 'delivery'
    elif isinstance(object, type(shift.Shift())):
        # set variable path for files to be written
        directory = 'shift'
    # indicator to program when extra stop has been started
    utility.write_data(path.join(directory, 'extra_stop'), None)
    # incrament quintity file by 1
    extra_stop_quantity(directory)
    # create varibale with a extra stop class object
    extra_stop_object = Extra_Stop()
    extra_stop_object.directory = directory
    # assign a extra stop id number
    extra_stop_object.id_number = utility.write_data(
        path.join(directory, 'extra_stop_number.txt'),
        id_number.assign_id_number(extra_stop_object))
    # input extra stop location
    extra_stop_object.location = utility.write_data(
        path.join(directory, 'extra_stop_location.txt'),
        input_data.input_data(
            prompt1='\nExtra stop location:\n', input_type1=str,
            prompt2='\nIs this correct? [y/n]\n', input_type2=str,
            option_yes='y', option_no='n'))
    # input extra stop reason
    extra_stop_object.reason = utility.write_data(
        path.join(directory, 'extra_stop_reason.txt'),
        input_data.input_data(
            prompt1='\nReason for extra stop?\n', input_type1=str,
            prompt2='\nIs this correct? [y/n]\n', input_type2=str,
            option_yes='y', option_no='n'))
    # input extra stop miles traveled
    extra_stop_object.miles_traveled = utility.write_data(
        path.join(directory, 'extra_stop_miles.txt'),
        data=utility.miles_traveled(
            prompt='Extra stop miles traveled:    #.#'))
    # save the time at the end of the extra stop
    extra_stop_object.end_time = utility.write_data(
        path.join(directory, 'extra_stop_end_time.txt'), utility.now())
    id_number.id_number_file(extra_stop_object)
    # consolidate extra stop data into one file
    consolidate_data.consolidate_extra_stop(extra_stop_object)
    # display the amount of time since the delivery was started
    utility.time_taken(
        start_time=object.get_start_time(),
        end_time=extra_stop_object.get_end_time(),
        var_word='Extra stop')
    # remove file telling program that on extra stop
    remove(path.join(directory, 'extra_stop'))
    return extra_stop_object


class Extra_Stop():
    def get_directory(self):
        return self.directory

    def get_id_number(self):
        return self.id_number

    def get_location(self):
        return self.location

    def get_reason(self):
        return self.reason

    def get_miles(self):
        return self.miles_traveled

    def get_end_time(self):
        return self.end_time
