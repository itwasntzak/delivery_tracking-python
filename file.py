from os import path

from utility import to_datetime

# list of shared file names
end_time = 'end_time.txt'
miles_traveled = 'miles_traveled.txt'


def write(file_name, data, directory_path=None):
    with open(file_name, 'w') as file:
        file.write(f'{data}')


def append(file_name, data, separator, directory_path=None):
    with open(file_name, 'a') as file:
        file.write(f'{data}{separator}')


class Read():
    def __init__(self, file_name, directory_path=None):
        if directory_path is not None:
            with open(path.join(directory_path, file_name), 'r') as file:
                self.data = file.read()
        else:
            with open(file_name, 'r') as file:
                self.data = file.read()

    def newline(self):
        return self.data.split('\n')

    def comma(self):
        return self.data.split(',')

    def newline_comma(self):
        data_list = []
        for newline in self.newline():
            data_list.append(newline.split(','))
        return data_list

    def integers(self):
        integer_list = []
        for data in self.comma():
            integer_list.append(int(data))
        return integer_list

    def floats(self):
        float_list = []
        for data in self.comma():
            float_list.append(float(data))
        return float_list

    def datetimes(self):
        datetime_list = []
        for data in self.comma():
            datetime_list.append(to_datetime(data))
        return datetime_list
