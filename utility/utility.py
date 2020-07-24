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
        import datetime
        return datetime.datetime.strptime(self.string, '%Y-%m-%d %H:%M:%S.%f')


def to_money(value):
    return '${:.2f}'.format(round(value, 2))


# todo: func cacluates len of strings, force everything to same screen length
def time_taken(start_time, end_time, prompt):
    time_diff = end_time - start_time
    return f"\n{prompt}\t{time_diff}"


def enter_to_continue(prompt):
    while True:
        print(prompt + '\n')
        wait_for_user = input('Press enter to continue.\n')
        if wait_for_user == '':
            break
        else:
            continue
