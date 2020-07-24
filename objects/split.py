
class Split:
    def __init__(self, shift):
        from objects.shift import Shift
        if isinstance(shift, Shift):
            self.parent = shift
        else:
            raise TypeError

        self.start_time = None
        self.end_time = None
        self.miles_traveled = None

    def csv(self):
        return f'{self.miles_traveled},{self.start_time},{self.end_time}'

    def file_list(self):
        from os import path
        from resources.system_names import\
            end_time, miles_traveled, split_directory, start_time, Split__info

        parent_directory = self.parent.file_list()['directory']
        directory = path.join(parent_directory, split_directory)

        return {
            'directory': directory,
            'end_time': path.join(directory, end_time),
            'info': path.join(parent_directory, Split__info),
            'miles_traveled': path.join(directory, miles_traveled),
            'start_time': path.join(directory, start_time)
        }

    def view(self):
        from datetime import datetime

        start_time = self.start_time.strftime('%I:%M:%S %p')
        view_parts = {'start_time': f'Split was started at:\t{start_time}'}

        if isinstance(self.miles_traveled, float):
            view_parts['distance'] =\
                f'Miles traveled on split:\t{self.miles_traveled} miles'

        if isinstance(self.end_time, datetime):
            end_time = self.end_time.strftime('%I:%M:%S %p')
            view_parts['end_time'] = f'Split was ended at:\t{end_time}'
        
        return view_parts
