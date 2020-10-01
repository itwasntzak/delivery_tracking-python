from os import path, remove


def add_newlines(string):
    if string[0] != '\n':
        string = f'\n{string}'
    if string[-1] != '\n':
        string += '\n'
    
    return string


def now():
    '''
    convenience to access datetime.datetime.now
    '''
    import datetime
    return datetime.datetime.now()


def prep_data_string(data, before=None, after=None):
    """
    data = must be string or a type that can be converted to a string
    before, after = strings to be displayed respectively around data
    """
    if not before and not after:
        raise ValueError('at that least one of before or after to not be None')

    string = ''
    if before and after:
        string += f'{before}{data}{after}'
    elif before:
        string += f'{before}{data}'
    elif after:
        string += f'{data}{after}'
    
    return string


class To_Datetime:
    def __init__(self, string):
        self.string = string

    def from_date(self):
        import datetime
        return datetime.datetime.strptime(self.string, '%Y-%m-%d')

    def from_datetime(self):
        import datetime
        import re

        if not re.search(r'[\d]+:+[\d]+:+[\d]+.+[\d]', self.string):
            return datetime.datetime.strptime(self.string, '%Y-%m-%d %H:%M:%S')

        return datetime.datetime.strptime(self.string, '%Y-%m-%d %H:%M:%S.%f')

    def from_time(self):
        import datetime
        import re

        if not re.search(r'[\d]+:+[\d]+:+[\d]+.+[\d]', self.string):
            return datetime.datetime.strptime(self.string, '%H:%M:%S')

        return datetime.datetime.strptime(self.string, '%H:%M:%S.%f')


def to_money(value):
    return '${:.2f}'.format(round(value, 2))
