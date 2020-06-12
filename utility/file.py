from utility import to_datetime


def append(data, separator, file_name, directory_path=None):
    if isinstance(directory_path, str):
        from os import path
        with open(path.join(directory_path, file_name), 'a') as file:
            file.write(f'{data}{separator}')
    elif not directory_path:
        with open(file_name, 'a') as file:
            file.write(f'{data}{separator}')
    elif directory_path:
        raise TypeError('directory_path must be a string type')


def save(data, file_name, directory_path=None, separator=None):
    from os import path
    if isinstance(directory_path, str):
        file_path = path.join(directory_path, file_name)
    elif not directory_path:
        file_path = file_name
    elif directory_path:
        raise TypeError('directory_path must be a string, usually a path')

    if path.exists(file_path) and isinstance(separator, str):
        append(data, separator, file_name, directory_path)
    elif not path.exists(file_path):
        write(data, file_name, directory_path)
    elif path.exists(file_path) and separator:
        raise ValueError('seperator perameter must be added to append data')


def write(data, file_name, directory_path=None):
    if isinstance(directory_path, str):
        from os import path
        with open(path.join(directory_path, file_name), 'w') as file:
            file.write(f'{data}')
    elif not directory_path:
        with open(file_name, 'w') as file:
            file.write(f'{data}')
    elif directory_path:
        raise TypeError('directory_path must be a string type')


class Read():
    def __init__(self, file_name, directory_path=None):
        if isinstance(directory_path, str):
            from os import path
            with open(path.join(directory_path, file_name), 'r') as file:
                self.data = file.read()
        elif not directory_path:
            with open(file_name, 'r') as file:
                self.data = file.read()
        elif directory_path:
            raise TypeError('directory_path must be a string type')

    def newline(self):
        return self.data.split('\n')

    def comma(self):
        return self.data.split(',')

    def newline_comma(self):
        data_list = []
        for newline in self.newline():
            data_list.append(newline.split(','))
        if len(data_list) == 0:
            pass
        elif len(data_list) == 1:
            return data_list[0]
        else:
            return data_list

    def integers(self):
        integer_list = []
        for data in self.comma():
            integer_list.append(int(data))
        if len(integer_list) == 0:
            pass
        elif len(integer_list) == 1:
            return integer_list[0]
        else:
            return integer_list

    def floats(self):
        float_list = []
        for data in self.comma():
            float_list.append(float(data))
        if len(float_list) == 0:
            pass
        elif len(float_list) == 1:
            return float_list[0]
        else:
            return float_list

    def datetime(self):
        datetime_list = []
        for data in self.comma():
            datetime_list.append(to_datetime(data))
        if len(datetime_list) == 0:
            pass
        elif len(datetime_list) == 1:
            return datetime_list[0]
        else:
            return datetime_list
