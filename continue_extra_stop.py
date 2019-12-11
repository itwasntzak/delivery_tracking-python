from os import path, remove

import consolidate_data
import delivery
import extra_stop
import id_number
import input_data
import shift
import utility


def continue_extra_stop(object):
    if isinstance(object, type(delivery.Delivery())):
        # set variable path for files to be written
        directory = 'delivery'
    elif isinstance(object, type(shift.Shift())):
        # set variable path for files to be written
        directory = 'shift'
    id_number_path = path.join(directory, 'extra_stop_number.txt')
    location_path = path.join(directory, 'extra_stop_location.txt')
    reason_path = path.join(directory, 'extra_stop_reason.txt')
    miles_path = path.join(directory, 'extra_stop_miles.txt')
    end_time_path = path.join(directory, 'extra_stop_end_time.txt')
    extra_stop_object = extra_stop.Extra_Stop()
    extra_stop_object.directory = directory

    if path.exists(id_number_path):
        extra_stop_object.id_number = int(utility.read_data(
            path.join(id_number_path)))
    else:
        extra_stop_object.id_number = id_number.assign_id_number(
            extra_stop_object) - 1
        # reset id file after accessing
        extra_stop_id_path = path.join('shift', 'extra_stop_id_number.txt')
        utility.write_data(extra_stop_id_path,
                           extra_stop_object.get_id_number())

    if path.exists(location_path):
        extra_stop_object.location = utility.read_data(location_path)
    if path.exists(reason_path):
        extra_stop_object.reason = utility.read_data(reason_path)
    if path.exists(miles_path):
        extra_stop_object.miles_traveled = float(utility.read_data(miles_path))
    if path.exists(end_time_path):
        extra_stop_object.end_time = utility.to_datetime(utility.read_data(
            end_time_path))
    extra_stop_file_path = path.join(
        extra_stop_object.get_directory(),
        str(extra_stop_object.get_id_number()) + '.txt')

    if path.exists(extra_stop_file_path):
        extra_stop_file = utility.read_data(extra_stop_file_path).split(',')
        extra_stop_object.location = extra_stop_file[0]
        extra_stop_object.reason = extra_stop_file[1]
        extra_stop_object.miles_traveled = float(extra_stop_file[2])
        extra_stop_object.end_time = utility.to_datetime(extra_stop_file[3])
    elif path.exists(end_time_path):
        id_number.id_number_file(extra_stop_object)
        # consolidate extra stop data into one file
        consolidate_data.consolidate_extra_stop(extra_stop_object)
    elif path.exists(miles_path):
        # save the time at the end of the extra stop
        extra_stop_object.end_time = utility.write_data(
            path.join(directory, 'extra_stop_end_time.txt'), utility.now())
        id_number.id_number_file(extra_stop_object)
        # consolidate extra stop data into one file
        consolidate_data.consolidate_extra_stop(extra_stop_object)
    elif path.exists(reason_path):
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
    elif path.exists(location_path):
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
    elif path.exists(id_number_path):
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
    else:
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
