from os import path, remove

import delivery
import id_number
import input_data
import shift
import utility


class Extra_Stop():
    def consolidate(self):
        # list of all paths
        # pre consolidation paths
        extra_stop_number_path =\
            path.join(self.directory, 'extra_stop_number.txt')
        extra_stop_location_path =\
            path.join(self.directory, 'extra_stop_location.txt')
        extra_stop_reason_path =\
            path.join(self.directory, 'extra_stop_reason.txt')
        extra_stop_miles_path =\
            path.join(self.directory, 'extra_stop_miles.txt')
        extra_stop_start_time_path =\
            path.join(self.directory, 'extra_stop_start_time.txt')
        extra_stop_end_time_path =\
            path.join(self.directory, 'extra_stop_end_time.txt')
        # post consolidation paths
        extra_stop_number_file_path =\
            path.join(self.directory, str(self.id_number) + '.txt')

        data = str(self.location) + ',' + str(self.reason) + ','\
            + str(self.miles_traveled) + ',' + str(self.end_time)
        utility.write_data(extra_stop_number_file_path, data)
        id_number.id_number_file(self)
        # remove files that are no longer needed
        remove(extra_stop_number_path)
        remove(extra_stop_location_path)
        remove(extra_stop_reason_path)
        remove(extra_stop_miles_path)
        remove(extra_stop_end_time_path)
        if path.exists(extra_stop_start_time_path):
            remove(extra_stop_start_time_path)

    def extra_stop(self, object):
        if isinstance(object, type(delivery.Delivery())):
            # set variable path for files to be written
            self.directory = 'delivery'
        elif isinstance(object, type(shift.Shift())):
            extra_stop_start_time_path =\
                path.join('shift', 'extra_stop_start_time.txt')
            object.start_time = utility.write_data(
                extra_stop_start_time_path, utility.now())
            # set variable path for files to be written
            self.directory = 'shift'
        id_number_path = path.join(self.directory, 'extra_stop_number.txt')
        location_path = path.join(self.directory, 'extra_stop_location.txt')
        reason_path = path.join(self.directory, 'extra_stop_reason.txt')
        miles_path = path.join(self.directory, 'extra_stop_miles.txt')
        end_time_path = path.join(self.directory, 'extra_stop_end_time.txt')
        # indicator to program when extra stop has been started
        utility.write_data(path.join(self.directory, 'extra_stop'), None)
        # assign a extra stop id number
        self.id_number = utility.write_data(
            id_number_path, id_number.assign_id_number(self))
        # input extra stop location
        self.location = utility.write_data(
            location_path, input_data.input_data(
                '\nExtra stop location:\n', str,
                '\nIs this correct? [y/n]\n', str, 'y', 'n'))
        # input extra stop reason
        self.reason = utility.write_data(
            reason_path, input_data.input_data(
                '\nReason for extra stop?\n', str,
                '\nIs this correct? [y/n]\n', str, 'y', 'n'))
        # input extra stop miles traveled
        self.miles_traveled = utility.write_data(
            miles_path,
            utility.miles_traveled('Extra stop miles traveled:    #.#'))
        # save the time at the end of the extra stop
        self.end_time = utility.write_data(end_time_path, utility.now())
        # consolidate extra stop data into one file
        self.consolidate()
        # display the amount of time since the delivery was started
        utility.time_taken(object.start_time, self.end_time, 'Extra stop')
        # remove file telling program that extra stop in progress
        remove(path.join(self.directory, 'extra_stop'))
        # return extra stop object to the function that called it
        return self

    def load(self, object):
        if isinstance(object, type(delivery.Delivery())):
            # set variable path for files to be written
            self.directory = 'delivery'
        elif isinstance(object, type(shift.Shift())):
            extra_stop_start_time_path = path.join(
                'shift', 'extra_stop_start_time.txt')
            # set variable path for files to be written
            self.directory = 'shift'
            object.start_time = utility.to_datetime(utility.read_data(
                extra_stop_start_time_path))
        id_number_path = path.join(self.directory, 'extra_stop_number.txt')
        location_path = path.join(self.directory, 'extra_stop_location.txt')
        reason_path = path.join(self.directory, 'extra_stop_reason.txt')
        miles_path = path.join(self.directory, 'extra_stop_miles.txt')
        end_time_path = path.join(self.directory, 'extra_stop_end_time.txt')

        if path.exists(id_number_path):
            # assign a extra stop id number
            self.id_number = utility.read_data(id_number_path)
        if path.exists(location_path):
            # input extra stop location
            self.location = utility.read_data(location_path)
        if path.exists(reason_path):
            # input extra stop reason
            self.reason = utility.read_data(reason_path)
        if path.exists(miles_path):
            # input extra stop miles traveled
            self.miles_traveled = utility.read_data(miles_path)
        if path.exists(end_time_path):
            # save the time at the end of the extra stop
            self.end_time = utility.read_data(end_time_path)
        return self

    def resume(self, object):
        if isinstance(object, type(delivery.Delivery())):
            # set variable path for files to be written
            self.directory = 'delivery'
        elif isinstance(object, type(shift.Shift())):
            extra_stop_start_time_path = path.join(
                'shift', 'extra_stop_start_time.txt')
            # set variable path for files to be written
            self.directory = 'shift'
            object.start_time = utility.to_datetime(utility.read_data(
                extra_stop_start_time_path))
        id_number_path = path.join(self.directory, 'extra_stop_number.txt')
        location_path = path.join(self.directory, 'extra_stop_location.txt')
        reason_path = path.join(self.directory, 'extra_stop_reason.txt')
        miles_path = path.join(self.directory, 'extra_stop_miles.txt')
        end_time_path = path.join(self.directory, 'extra_stop_end_time.txt')

        while True:
            if not path.exists(id_number_path):
                # assign a extra stop id number
                self.id_number = utility.write_data(
                    id_number_path, id_number.assign_id_number(self))
            elif not path.exists(location_path):
                # input extra stop location
                self.location = utility.write_data(
                    location_path, input_data.input_data(
                        '\nExtra stop location:\n', str,
                        '\nIs this correct? [y/n]\n', str, 'y', 'n'))
            elif not path.exists(reason_path):
                # input extra stop reason
                self.reason = utility.write_data(
                    reason_path, input_data.input_data(
                        '\nReason for extra stop?\n', str,
                        '\nIs this correct? [y/n]\n', str, 'y', 'n'))
            elif not path.exists(miles_path):
                # input extra stop miles traveled
                self.miles_traveled = utility.write_data(
                    miles_path, utility.miles_traveled(
                        'Extra stop miles traveled:    #.#'))
            elif not path.exists(end_time_path):
                # save the time at the end of the extra stop
                self.end_time =\
                    utility.write_data(end_time_path, utility.now())
            else:
                break
        # consolidate extra stop data into one file
        self.consolidate()
        # display the amount of time since the delivery was started
        utility.time_taken(
            object.start_time, self.end_time, 'Extra stop')
        # remove file telling program that on extra stop
        remove(path.join(self.directory, 'extra_stop'))
        return self
