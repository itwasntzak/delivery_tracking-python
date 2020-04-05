from os import path, remove

from input_data import input_data
from utility import append_data, now, read_data, to_datetime,\
    time_taken, write_data


def parent_type(parent, intended):
    from delivery import Delivery
    from shift import Shift
    if intended == 'delivery':
        if isinstance(parent, type(Delivery())):
            return Delivery()
    elif intended == 'shift':
        if isinstance(parent, type(Shift())):
            return Shift()


class Extra_Stop:
    def __init__(self, parent, id=''):
        self.parent = parent
        self.path = parent.path
        if id == '':
            if isinstance(parent, type(parent_type(parent, 'shift'))):
                self.extra_stop_id_path =\
                    path.join(self.path, 'extra_stop_id_number.txt')
            elif isinstance(parent, type(parent_type(parent, 'delivery'))):
                self.extra_stop_id_path =\
                    path.join(parent.parent.path, 'extra_stop_id_number.txt')
            if not path.exists(self.extra_stop_id_path):
                self.id = 0
            else:
                self.id = int(read_data(self.extra_stop_id_path))
        else:
            self.id = id
        # list of all paths
        self.location_path = path.join(self.path, 'extra_stop_location.txt')
        self.reason_path = path.join(self.path, 'extra_stop_reason.txt')
        self.miles_path = path.join(self.path, 'extra_stop_miles.txt')
        self.start_time_path = path.join(self.path, 'extra_stop_start_time.txt')
        self.end_time_path = path.join(self.path, 'extra_stop_end_time.txt')
        self.extra_stop_path = path.join(self.path, str(self.id) + '.txt')
        self.extra_stop_ids_path = path.join(self.path, 'extra_stop_ids.txt')

    # methods for extra stop tracking
    def consolidate(self):
        if isinstance(self.parent, type(parent_type(self.parent, 'shift'))):
            data = '{0},{1},{2},{3},{4}'.format(
                self.location, self.reason, self.miles_traveled,
                self.start_time, self.end_time)
        elif isinstance(self.parent, type(
                parent_type(self.parent, 'delivery'))):
            data = '{0},{1},{2},{3}'.format(
                self.location, self.reason, self.miles_traveled, self.end_time)
        write_data(self.extra_stop_path, data)
        # remove files that are no longer needed
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

    def load(self):
        if path.exists(self.extra_stop_path):
            extra_stop_data = read_data(self.extra_stop_path).split(',')
            if isinstance(self.parent, type(
                    parent_type(self.parent, 'shift'))):
                self.location = extra_stop_data[0]
                self.reason = extra_stop_data[1]
                self.miles_traveled = extra_stop_data[2]
                self.start_time = extra_stop_data[3]
                self.end_time = extra_stop_data[4]
            elif isinstance(self.parent, type(
                    parent_type(self.parent, 'delivery'))):
                self.location = extra_stop_data[0]
                self.reason = extra_stop_data[1]
                self.miles_traveled = extra_stop_data[2]
                self.end_time = extra_stop_data[3]
            return self

    def start(self):
        # indicator to program when extra stop has been started
        write_data(path.join(self.path, 'extra_stop'), None)
        # assign a extra stop id number
        if isinstance(self.parent, type(parent_type(self.parent, 'shift'))):
            # add start time if extra stop is seperate from a delivery
            self.start_time = write_data(self.start_time_path, now())
        # input extra stop location
        self.location = self.input_location()
        # input extra stop reason
        self.reason = self.input_reason()
        # input extra stop miles traveled
        self.miles_traveled = self.input_miles_traveled()
        # save the time at the end of the extra stop
        self.end_time = write_data(self.end_time_path, now())
        # consolidate extra stop data into one file
        self.consolidate()
        # display the amount of time since the delivery was started
        if isinstance(self.parent, type(parent_type(self.parent, 'shift'))):
            time_taken(self.start_time, self.end_time,
                       'Extra stop completed in:\t')
        elif isinstance(self.parent, type(parent_type(self.parent, 'delivery'))):
            time_taken(self.parent.start_time, self.end_time,
                       'Extra stop completed in:\t')
        # return parent object with updateded lists
        return self

    def update_id_file(self):
        if path.exists(self.extra_stop_ids_path):
            append_data(self.extra_stop_ids_path, ',' + str(self.id))
        else:
            write_data(self.extra_stop_ids_path, self.id)

    def update_id_number(self):
        self.id += 1
        write_data(self.extra_stop_id_path, self.id)

    # methods for inputting data
    def input_location(self):
        return write_data(self.location_path, input_data(
            f"\n{'Extra stop location:'}\n", str,
            f"\n{'Is this correct?'}         {'[y/n]'}\n", str,
            ('y', 'Y'), ('n', 'Y')))

    def input_miles_traveled(self):
        return write_data(self.miles_path, input_data(
            f"\n{'Extra stop miles traveled:'} {'#.#'}\n", float,
            ' miles\n'
            f"{'Is this correct?'}         {'[y/n]'}\n", str,
            ('y', 'Y'), ('n', 'Y')))

    def input_reason(self):
        return write_data(self.reason_path, input_data(
            '\nReason for extra stop?\n', str,
            f"\n{'Is this correct?'}         {'[y/n]'}\n", str,
            ('y', 'Y'), ('n', 'Y')))

    # methods for continuing tracking if program ends
    def load_current(self):
        if isinstance(self.parent, type(parent_type(self.parent, 'shift'))):
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
        # return parent object with updateded lists
        return self

    def resume(self):
        while True:
            if isinstance(self.parent, type(parent_type(self.parent, 'shift'))):
                if not path.exists(self.start_time_path):
                    self.start_time = write_data(self.start_time_path, now())
            if not path.exists(self.location_path):
                # input extra stop location
                self.location = self.input_location()
            elif not path.exists(self.reason_path):
                # input extra stop reason
                self.reason = self.input_reason()
            elif not path.exists(self.miles_path):
                # input extra stop miles traveled
                self.miles_traveled = self.input_miles_traveled()
            elif not path.exists(self.end_time_path):
                # save the time at the end of the extra stop
                self.end_time = write_data(self.end_time_path, now())
            else:
                break
        # consolidate extra stop data into one file
        self.consolidate()
        # display the amount of time since the delivery was started
        if isinstance(self.parent, type(parent_type(self.parent, 'shift'))):
            time_taken(self.start_time, self.end_time,
                       'Extra stop completed in:\t')
        elif isinstance(self.parent, type(parent_type(self.parent, 'delivery'))):
            time_taken(self.parent.start_time, self.end_time,
                       'Extra stop completed in:\t')
        return self
