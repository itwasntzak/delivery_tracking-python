
class Extra_Stop:
    id = None
    parent = None
    location = None
    reason = None
    miles_traveled = None
    start_time = None
    end_time = None

    def __init__(self, parent, id=None):
        self.parent = parent

        if isinstance(id, int):
            self.id = id
        elif id is None:
            pass
        else:
            raise TypeError

    def assign_id(self):
        from os import path

        if not path.exists(self.file_list()['running_id']):
            self.id = 0
        else:
            from utility.file import Read
            self.id = Read(self.file_list()['running_id']).integers()

    def csv(self):
        from objects.delivery import Delivery
        from objects.shift import Shift
        if isinstance(self.parent, Shift):
            return f'{self.location},{self.reason},{self.miles_traveled},'\
                   f'{self.start_time},{self.end_time}'
        elif isinstance(self.parent, Delivery):
            return f'{self.location},{self.reason},{self.miles_traveled},'\
                   f'{self.end_time}'

    def file_list(self):
        from os import path
        from resources.system_names import\
            end_time, extra_stop_directory, miles_traveled, start_time,\
            Extra_Stop__completed_ids as completed_ids,\
            Extra_Stop__info as info_file,\
            Extra_Stop__location as location, Extra_Stop__reason as reason,\
            Extra_Stop__running_id as running_id,\
            shifts_directory, user_data_directory as data_directory
        from utility.utility import now

        parent_directory = self.parent.file_list()['directory']
        shift_directory =\
            path.join(data_directory, shifts_directory, f'{now().date()}')

        directory = path.join(parent_directory, extra_stop_directory)

        return {
            'completed_ids': path.join(parent_directory, completed_ids),
            'directory': directory,
            'end_time': path.join(directory, end_time),
            'info': path.join(parent_directory, info_file),
            'location': path.join(directory, location),
            'miles_traveled': path.join(directory, miles_traveled),
            'reason': path.join(directory, reason),
            'running_id': path.join(shift_directory, running_id),
            'start_time': path.join(directory, start_time)
        }

    def nlsv(self):
        from objects.delivery import Delivery
        from objects.shift import Shift
        if isinstance(self.parent, Shift):
            return f'{self.location}\n'\
                   f'{self.reason}\n'\
                   f'{self.miles_traveled}\n'\
                   f'{self.start_time}\n'\
                   f'{self.end_time}'
        elif isinstance(self.parent, Delivery):
            return f'{self.location}\n'\
                   f'{self.reason}\n'\
                   f'{self.miles_traveled}\n'\
                   f'{self.end_time}'

    def update_running_id(self):
        from utility.file import write

        write(self.id + 1, self.file_list()['running_id'])

# todo: change extra stops from comma seperated to newline seperated
# todo: need to write function that allows the user to change data
# todo: need to write function that saves changes to data
