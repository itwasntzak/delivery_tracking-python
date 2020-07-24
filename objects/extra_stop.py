
class Extra_Stop:
    def __init__(self, parent, id=None):
        from objects.delivery import Delivery
        from objects.shift import Shift
        if not isinstance(parent, (Shift, Delivery)):
            raise TypeError

        self.parent = parent

        if isinstance(id, int):
            self.id = id
        elif id is None:
            self.assign_id()
        else:
            raise TypeError

        self.location = None
        self.reason = None
        self.miles_traveled = None
        self.start_time = None
        self.end_time = None

    def assign_id(self):
        from os import path

        self.id = 0

        if path.exists(self.file_list()['running_id']):
            from utility.file import Read
            self.id = Read(self.file_list()['running_id']).integer()

        return self

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
            shifts_directory, data_directory
        from utility.utility import now

        parent_directory = self.parent.file_list()['directory']
        shift_directory =\
            path.join(data_directory, shifts_directory, f'{now().date()}')

        directory = path.join(parent_directory, extra_stop_directory)

        return {
            'running_id': path.join(shift_directory, running_id),
            'completed_ids': path.join(parent_directory, completed_ids),
            'info': path.join(parent_directory, info_file.format(self.id)),
            'directory': directory,
            'end_time': path.join(directory, end_time),
            'location': path.join(directory, location),
            'miles_traveled': path.join(directory, miles_traveled),
            'reason': path.join(directory, reason),
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

    def view(self):
        from datetime import datetime

        end_time = self.end_time.strftime('%I:%M:%S %p')

        view_parts = {
            'id': f'Extra stop id #:\t{self.id + 1}',
            'location': f'Location:\t{self.location.capitalize()}',
            'reason': f'Reason:\t{self.reason.capitalize()}',
            'distance': f'Distance to extra stop:\t{self.miles_traveled} miles',
            'end_time': f'Extra stop was completed at:\t{end_time}'
        }

        if isinstance(self.start_time, datetime):
            view_parts['start_time'] = self.start_time.strftime('%I:%M:%S %p')
        
        return view_parts

# todo: need to write function that allows the user to change data
# todo: need to write function that saves changes to data
