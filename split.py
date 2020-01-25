from os import path, remove

import utility


class Split():
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

    def end(self):
        start_time_path = path.join('shift', 'split_start_time.txt')
        miles_traveled_path = path.join('shift', 'split_miles_traveled.txt')
        end_time_path = path.join('shift', 'split_end_time.txt')
        self.start_time = utility.to_datetime(utility.read_data(
            start_time_path))
        self.miles_traveled = utility.write_data(
            miles_traveled_path,
            utility.miles_traveled('Split miles traveled:    #.#'))
        self.end_time = utility.write_data(end_time_path, utility.now())
        self.consolidate()
        utility.enter_to_continue()
        exit()

    def start(self):
        utility.write_data(
            path.join('shift', 'split_start_time.txt'), utility.now())
        utility.enter_to_continue()
        exit()
