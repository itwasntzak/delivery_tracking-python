
class Split:
    parent = None
    start_time = None
    end_time = None
    miles_traveled = None

    def __init__(self, shift):
        from objects.shift import Shift
        if isinstance(shift, Shift):
            self.parent = shift
        else:
            raise TypeError

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
