from os import path, remove

from utility import enter_to_continue, miles_traveled, now, read_data,\
    to_datetime, write_data


class Split:
    def __init__(self, shift):
        self.parent = shift
        self.path = shift.path
        # list of all paths
        self.miles_path = path.join(self.path, 'split_miles_traveled.txt')
        self.start_time_path = path.join(self.path, 'split_start_time.txt')
        self.end_time_path = path.join(self.path, 'split_end_time.txt')
        self.split_info_path = path.join(self.path, 'split_info.txt')

    def consolidate(self):
        data = str(self.miles_traveled) + ','\
            + str(self.start_time) + ','\
            + str(self.end_time)
        write_data(self.split_info_path, data)
        # remove files that are no longer needed
        remove(self.miles_path)
        remove(self.start_time_path)
        remove(self.end_time_path)

    # todo: add user confirmation before completing
    def end(self):
        self.start_time = to_datetime(read_data(self.start_time_path))
        if path.exists(self.miles_traveled_path):
            self.miles_traveled = float(read_data(self.miles_traveled_path))
        else:
            self.miles_traveled = write_data(
                self.miles_traveled_path, miles_traveled(
                    'Split miles traveled:    #.#'))
        if path.exists(self.end_time_path):
            self.end_time = to_datetime(read_data(self.end_time_path))
        else:
            self.end_time = write_data(self.end_time_path, now())
        self.consolidate()
        return self

    def load(self):
        split_info = read_data(self.split_info_path).split(',')
        self.miles_traveled = split_info[0]
        self.start_time = split_info[1]
        self.end_time = split_info[2]
        return self

    # todo: add user confirmation before starting
    def start(self):
        write_data(self.start_time_path, now())
        enter_to_continue()
        exit()
