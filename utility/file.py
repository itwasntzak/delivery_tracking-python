
def append(file_path, data, separator):
    with open(file_path, 'a') as file:
        file.write(f'{separator}{data}')


def save(data, file_path, separator=None):
    if separator and not isinstance(separator, str):
        raise TypeError

    from os import path

    if path.exists(file_path) and separator:
        append(file_path, data, separator)
    elif not path.exists(file_path) or not separator:
        write(data, file_path)


def write(data, file_path):
    with open(file_path, 'w') as file:
        file.write(f'{data}')


class Read():
    def __init__(self, file_path):
        with open(file_path, 'r') as file:
            self.data = file.read()

    def newline(self):
        return self.data.split('\n')

    def comma(self):
        return self.data.split(',')

    def integer(self):
        integer_list = self.integer_list()
        if len(integer_list) == 1:
            return integer_list[0]
        elif len(integer_list) > 1:
            return integer_list

    def integer_list(self):
        return [int(data) for data in self.comma()]

    def decimal(self):
        decimal_list = self.decimal_list()
        if len(decimal_list) == 1:
            return decimal_list[0]
        elif len(decimal_list) > 1:
            return decimal_list

    def decimal_list(self):
        return [float(data) for data in self.comma()]

    def date(self):
        date_list = self.date_list()
        if len(date_list) == 1:
            return date_list[0]
        elif len(date_list) > 1:
            return date_list
    
    def date_list(self):
        from utility.utility import To_Datetime
        return [To_Datetime(data).from_date() for data in self.comma()]

    def datetime(self):
        datetime_list = self.datetime_list()
        if len(datetime_list) == 1:
            return datetime_list[0]
        elif len(datetime_list) > 1:
            return datetime_list
    
    def datetime_list(self):
        from utility.utility import To_Datetime
        return [To_Datetime(data).from_datetime() for data in self.comma()]
