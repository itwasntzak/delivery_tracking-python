from os import path, remove

import utility


def start_split():
    utility.write_data(
        path.join('shift', 'split_start_time.txt'), utility.now())
    exit()


def end_split():
    split_object = Split()
    split_object.start_time = utility.to_datetime(utility.read_data(
        path.join('shift', 'split_start_time.txt')))
    split_object.miles_traveled = utility.write_data(
        path.join('shift', 'split_miles_traveled.txt'),
        utility.miles_traveled('Split miles traveled:    #.#'))
    split_object.end_time = utility.write_data(
        path.join('shift', 'split_end_time.txt'), utility.now())
    split_object.consolidate()
    exit()


class Split():
    def get_miles_traveled(self):
        return self.miles_traveled

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    def consolidate(self):
        # list of all paths
        # pre consolidation paths
        split_miles_path = path.join('shift', 'split_miles_traveled.txt')
        split_start_time_path = path.join('shift', 'split_start_time.txt')
        split_end_time_path = path.join('shift', 'split_end_time.txt')
        # post consolidation paths
        split_info_path = path.join('shift', 'split_info.txt')

        # assign data to variables
        split_miles = str(self.miles_traveled)
        split_start_time = str(self.start_time)
        split_end_time = str(self.end_time)

        data = split_miles + ',' + split_start_time + ',' + split_end_time
        utility.write_data(split_info_path, data)

        # remove files that are no longer needed
        remove(split_miles_path)
        remove(split_start_time_path)
        remove(split_end_time_path)
