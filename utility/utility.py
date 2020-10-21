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


class Change_Datetime:
    def __init__(self, my_datetime):
        import datetime
        if not isinstance(my_datetime, datetime.datetime):
            raise TypeError(f'not the type {datetime}')

        self.original_datetime = my_datetime
        self.datetime = my_datetime
        self.loop_condition = True
        self.date_condition = False
        self.time_condition = False
    
    def build_confirmation_text(self):
        # day
        if self.user_selection.lower() == 'd':
            self.confirmation_text = 'Change the day'
        # minute/month
        elif self.user_selection.lower() == 'm':
            # date, month
            if self.date_condition:
                self.confirmation_text = 'Change the month'
            # time, minute
            elif self.time_condition:
                self.confirmation_text = 'Change the minute'
        # year
        elif self.user_selection.lower() == 'y':
            self.confirmation_text = 'Change the year'
        # hour
        elif self.user_selection.lower() == 'h':
            self.confirmation_text = 'Change the hour'
        # seconds
        elif self.user_selection.lower() == 's':
            self.confirmation_text = 'Change the second'

    def build_prompt(self):
        # date
        if self.date_condition:
            self.prompt =\
                '\nPlease select an option:\n'\
                'D. Change the day\n'\
                'M. Change the month\n'\
                'Y. Change the year\n'\
                'V. View current date\n'\
                'B. Go back\n'
        # time
        elif self.time_condition:
            self.prompt =\
                '\nPlease select an option:\n'\
                'H. Change the hour\n'\
                'M. Change the minute\n'\
                'S. Change the second\n'\
                'V. View current time\n'\
                'B. Go back\n'

    def change_day(self):
        from utility.user_input import confirm

        pattern = '^(3[01]|[12][0-9]|[1-9])$'
        prompt = 'Please enter the new day:\n'
        error_message = 'Error: please enter a number 1 - 31'
        # display current value to user
        print(f'\nCurrent day is {self.datetime.day}')
        # user inputs new day
        new_day = self.validate_user_input(pattern, prompt, error_message)
        # user confirms what they have entered
        while not confirm(f'New day is: {new_day}'):
            new_day = self.validate_user_input(pattern, prompt, error_message)
        # update datetime object with changes
        self.datetime = self.datetime.replace(day=int(new_day))

    def change_minute(self):
        from utility.user_input import confirm

        pattern = '^[1-5]?[0-9]$'
        prompt = 'Please enter the new minute:\n'
        error_message = 'Error: please enter a number 0 - 59'
        # display current value to user
        print(f'\nCurrent minute is {self.datetime.minute}')
        # user inputs new minute
        new_minute = self.validate_user_input(pattern, prompt, error_message)
        # user confirms what they have entered
        while not confirm(f'New minute is: {new_minute}'):
            new_minute = self.validate_user_input(pattern, prompt, error_message)
        # update datetime object with changes
        self.datetime = self.datetime.replace(minute=int(new_minute))

    def change_month(self):
        from utility.user_input import confirm

        pattern = '^(1[0-2]|[1-9])$'
        prompt = 'Please enter the new month:\n'
        error_message = 'Error: please enter a number 1 - 12'
        # display current value to user
        print(f'\nCurrent month is {self.datetime.month}')
        # user inputs new month
        new_month = self.validate_user_input(pattern, prompt, error_message)
        # user confirms what they have entered
        while not confirm(f'New month is: {new_month}'):
            new_month = self.validate_user_input(pattern, prompt, error_message)
        # update datetime object with changes
        self.datetime = self.datetime.replace(month=int(new_month))

    def change_hour(self):
        from utility.user_input import confirm

        pattern = '^(2[0-4]|1[0-9]|[1-9])$'
        prompt = 'Please enter the new hour:\n'
        error_message = 'Error: please enter a number 1 - 24'
        # display current value to user
        print(f'\nCurrent hour is {self.datetime.hour}')
        # user inputs new hour
        new_hour = self.validate_user_input(pattern, prompt, error_message)
        # user confirms what they have entered
        while not confirm(f'New hour is: {new_hour}'):
            new_hour = self.validate_user_input(pattern, prompt, error_message)
        # update datetime object with changes
        self.datetime = self.datetime.replace(hour=int(new_hour))

    def change_second(self):
        from utility.user_input import confirm

        pattern = '^[1-5]?[0-9]$'
        prompt = 'Please enter the new second:\n'
        error_message = 'Error: please enter a number 0 - 59'
        # display current value to user
        print(f'\nCurrent second is {self.datetime.second}')
        # user inputs new second
        new_second = self.validate_user_input(pattern, prompt, error_message)
        # user confirms what they have entered
        while not confirm(f'New second is: {new_second}'):
            new_second = self.validate_user_input(pattern, prompt, error_message)
        # update datetime object with changes
        self.datetime = self.datetime.replace(second=int(new_second))

    def change_year(self):
        from utility.user_input import confirm

        pattern = '^[1-2][0-9][0-9][0-9]$'
        prompt = 'Please enter the new year:\n'
        error_message = 'Error: please enter a number 1000 - 2999'
        # display current value to user
        print(f'\nCurrent year is {self.datetime.year}')
        # user inputs new year
        new_year = self.validate_user_input(pattern, prompt, error_message)
        # user confirms what they have entered
        while not confirm(f'New year is: {new_year}'):
            new_year = self.validate_user_input(pattern, prompt, error_message)
        # update datetime object with changes
        self.datetime = self.datetime.replace(year=int(new_year))

    def validate_user_input(self, pattern, prompt, error_message):
        from utility.user_input import check_match, confirm, user_input

        new_value = user_input(prompt)
        while not check_match(pattern, new_value):
            print(error_message)
            new_value = user_input(prompt)
        
        return new_value

    def main(self):
        from utility.user_input import confirm

        self.user_choice()
        while self.user_selection.lower() not in ('b', 'v') and\
                not confirm(self.confirmation_text):
            self.user_choice()
        self.result()

    def user_choice(self):
        from utility.user_input import check_match, user_input

        # date
        if self.date_condition:
            pattern = '^[dmyvb]$'
        # time
        elif self.time_condition:
            pattern = '^[hmsvb]$'

        self.build_prompt()
        self.user_selection = user_input(self.prompt)
        while not check_match(pattern, self.user_selection):
            self.user_selection = user_input(self.prompt)
        self.build_confirmation_text()
    
    def result(self):
        # day
        if self.user_selection.lower() == 'd':
            self.change_day()
        # minute/month
        elif self.user_selection.lower() == 'm':
            # date, month
            if self.date_condition:
                self.change_month()
            # time, minute
            elif self.time_condition:
                self.change_minute()
        # year
        elif self.user_selection.lower() == 'y':
            self.change_year()
        # second
        elif self.user_selection.lower() == 's':
            self.change_second()
        # hour
        elif self.user_selection.lower() == 'h':
            self.change_hour()
        # view
        elif self.user_selection.lower() == 'v':
            from datetime import datetime

            # date
            if self.date_condition:
                string =\
                    f'\nCurrent date is: {self.datetime.strftime("%d-%m-%Y")}'
            # time
            elif self.time_condition:
                string =\
                    f'\nCurrent time is: {self.datetime.strftime("%I:%M:%S %p")}'
            print(string)
        # back
        elif self.user_selection.lower() == 'b':
            self.loop_condition = False

    def date(self):
        self.date_condition = True
        self.main()
        while self.loop_condition:
            self.main()
        return self

    def time(self):
        self.time_condition = True
        self.main()
        while self.loop_condition:
            self.main()
        return self


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
    if value < 0:
        return '-${:.2f}'.format(round(abs(value), 2))
    return '${:.2f}'.format(round(value, 2))
