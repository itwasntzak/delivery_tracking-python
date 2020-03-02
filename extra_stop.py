from os import path, remove

import delivery
import input_data
import shift
from utility import append_data, miles_traveled, now, read_data,\
    to_datetime, time_taken, write_data


def check_id_number(parent):
    id_number_path = path.join(parent.path, 'extra_stop_number.txt')
    if path.exists(id_number_path):
        return int(read_data(id_number_path))
    else:
        if isinstance(parent, type(shift.Shift(00-00-00))):
            return write_data(id_number_path, parent.extra_stop_id)
        if isinstance(parent, type(delivery.Delivery(
                shift.Shift(00-00-00), ''))):
            return write_data(id_number_path, parent.parent.extra_stop_id)


class Extra_Stop:
    def __init__(self, parent, id_number):
        self.parent = parent
        self.path = parent.path
        self.id = id_number
        # list of all paths
        self.id_number_path = path.join(self.path, 'extra_stop_number.txt')
        self.location_path = path.join(self.path, 'extra_stop_location.txt')
        self.reason_path = path.join(self.path, 'extra_stop_reason.txt')
        self.miles_path = path.join(self.path, 'extra_stop_miles.txt')
        self.start_time_path =\
            path.join(self.path, 'extra_stop_start_time.txt')
        self.end_time_path = path.join(self.path, 'extra_stop_end_time.txt')
        self.extra_stop_path = path.join(self.path, str(self.id) + '.txt')
        self.extra_stop_numbers_path =\
            path.join(self.path, 'extra_stop_numbers.txt')
        if isinstance(parent, type(shift.Shift(00-00-00))):
            self.shift_extra_stop_id_path =\
                path.join(self.path, 'extra_stop_id_number.txt')
        elif isinstance(parent, type(delivery.Delivery(
                shift.Shift(00-00-00), ''))):
            self.shift_extra_stop_id_path =\
                path.join(self.parent.parent.path, 'extra_stop_id_number.txt')

    def consolidate(self):
        if isinstance(self.parent, type(shift.Shift(00-00-00))):
            data = str(self.location) + ','\
                + str(self.reason) + ','\
                + str(self.miles_traveled) + ','\
                + str(self.start_time) + ','\
                + str(self.end_time)
        elif isinstance(self.parent, type(delivery.Delivery(
                shift.Shift(00-00-00), ''))):
            data = str(self.location) + ','\
                + str(self.reason) + ','\
                + str(self.miles_traveled) + ','\
                + str(self.end_time)
        write_data(self.extra_stop_path, data)
        # remove files that are no longer needed
        remove(self.id_number_path)
        remove(self.location_path)
        remove(self.reason_path)
        remove(self.miles_path)
        remove(self.end_time_path)
        if path.exists(self.start_time_path):
            remove(self.start_time_path)
        self.update_id_file()
        self.update_id_number()
        # remove file telling program that extra stop in progress
        remove(path.join(self.path, 'extra_stop'))
        return self

    def load(self):
        if path.exists(self.extra_stop_path):
            extra_stop_data = read_data(self.extra_stop_path).split(',')
            if isinstance(self.parent, type(shift.Shift(00-00-00))):
                self.location = extra_stop_data[0]
                self.reason = extra_stop_data[1]
                self.miles_traveled = extra_stop_data[2]
                self.start_time = extra_stop_data[3]
                self.end_time = extra_stop_data[4]
            elif isinstance(self.parent, type(delivery.Delivery(
                    shift.Shift(00-00-00), ''))):
                self.location = extra_stop_data[0]
                self.reason = extra_stop_data[1]
                self.miles_traveled = extra_stop_data[2]
                self.end_time = extra_stop_data[3]

    def load_current(self):
        if isinstance(self.parent, type(shift.Shift(00-00-00))):
            if path.exists(self.start_time_path):
                self.start_time = to_datetime(read_data(self.start_time_path))
        if path.exists(self.location_path):
            # input extra stop location
            self.location = read_data(self.location_path)
        if path.exists(self.reason_path):
            # input extra stop reason
            self.reason = read_data(self.reason_path)
        if path.exists(self.miles_path):
            # input extra stop miles traveled
            self.miles_traveled = float(read_data(self.miles_path))
        if path.exists(self.end_time_path):
            # save the time at the end of the extra stop
            self.end_time = to_datetime(read_data(self.end_time_path))
        self.resume()
        return self

    def resume(self):
        while True:
            if isinstance(self.parent, type(shift.Shift(00-00-00))):
                if not path.exists(self.start_time_path):
                    self.start_time = write_data(self.start_time_path, now())
            if not path.exists(self.location_path):
                # input extra stop location
                self.location = write_data(
                    self.location_path, input_data.input_data(
                        '\nExtra stop location:\n', str,
                        '\nIs this correct? [y/n]\n', str, 'y', 'n'))
            elif not path.exists(self.reason_path):
                # input extra stop reason
                self.reason = write_data(
                    self.reason_path, input_data.input_data(
                        '\nReason for extra stop?\n', str,
                        '\nIs this correct? [y/n]\n', str, 'y', 'n'))
            elif not path.exists(self.miles_path):
                # input extra stop miles traveled
                self.miles_traveled = write_data(
                    self.miles_path, miles_traveled(
                        'Extra stop miles traveled:    #.#'))
            elif not path.exists(self.end_time_path):
                # save the time at the end of the extra stop
                self.end_time = write_data(self.end_time_path, now())
            else:
                break
        # consolidate extra stop data into one file
        self.consolidate()
        # display the amount of time since the delivery was started
        if isinstance(self.parent, type(shift.Shift(00-00-00))):
            time_taken(self.start_time, self.end_time,
                       'Extra stop completed in:\t')
        elif isinstance(self.parent, type(delivery.Delivery(
                shift.Shift(00-00-00), ''))):
            time_taken(self.parent.start_time, self.end_time,
                       'Extra stop completed in:\t')
        return self

    def start(self):
        # indicator to program when extra stop has been started
        write_data(path.join(self.path, 'extra_stop'), None)
        # assign a extra stop id number
        if isinstance(self.parent, type(shift.Shift(00-00-00))):
            # add start time if extra stop is seperate from a delivery
            self.start_time = write_data(self.start_time_path, now())
        write_data(self.id_number_path, self.id)
        # input extra stop location
        self.location = write_data(self.location_path, input_data.input_data(
            '\nExtra stop location:\n', str,
            '\nIs this correct? [y/n]\n', str, 'y', 'n'))
        # input extra stop reason
        self.reason = write_data(self.reason_path, input_data.input_data(
            '\nReason for extra stop?\n', str,
            '\nIs this correct? [y/n]\n', str, 'y', 'n'))
        # input extra stop miles traveled
        self.miles_traveled = write_data(self.miles_path, miles_traveled(
            'Extra stop miles traveled:    #.#'))
        # save the time at the end of the extra stop
        self.end_time = write_data(self.end_time_path, now())
        # consolidate extra stop data into one file
        self.consolidate()
        # display the amount of time since the delivery was started
        if isinstance(self.parent, type(shift.Shift(00-00-00))):
            time_taken(self.start_time, self.end_time,
                       'Extra stop completed in:\t')
        elif isinstance(self.parent, type(delivery.Delivery(
                shift.Shift(00-00-00), ''))):
            time_taken(self.parent.start_time, self.end_time,
                       'Extra stop completed in:\t')
        # return extra stop object to the function that called it
        return self

    def update_id_file(self):
        # todo: figure out how to update parent extra stop lists with this info
        if path.exists(self.extra_stop_numbers_path):
            append_data(self.extra_stop_numbers_path, ',' + str(self.id))
        else:
            write_data(self.extra_stop_numbers_path, self.id)

    def update_id_number(self):
        # todo: needs to update shift's extra stop id without having to reload
        write_data(self.shift_extra_stop_id_path, self.id + 1)
