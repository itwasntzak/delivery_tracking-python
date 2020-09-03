from os import path, remove


def now():
    import datetime
    return datetime.datetime.now()


class To_Datetime:
    def __init__(self, string):
        self.string = string

    def from_date(self):
        import datetime
        return datetime.datetime.strptime(self.string, '%Y-%m-%d')

    def from_datetime(self):
        # this doesn't work when time ends with .000 because it doesnt write thaat part
        import datetime
        return datetime.datetime.strptime(self.string, '%Y-%m-%d %H:%M:%S.%f')


def to_money(value):
    return '${:.2f}'.format(round(value, 2))


# todo: func cacluates len of strings, force everything to same screen length
def time_taken(start_time, end_time, prompt):
    time_diff = end_time - start_time
    return f"{prompt}{time_diff}"


def enter_to_continue(prompt):
    while True:
        print(prompt + '\n')
        wait_for_user = input('Press enter to continue.\n')
        if wait_for_user == '':
            break
        else:
            continue
