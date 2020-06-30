
class Order:
    def __init__(self, delivery, id=None):
        from objects.delivery import Delivery
        if not isinstance(delivery, Delivery):
            # todo: move this error message to resources, use %s in place of {}
            error_message =\
                f"parent of Order must be Delivery not '{type(delivery)}'"
            raise TypeError(error_message)

        self.parent = delivery

        if isinstance(id, int):
            self.id = id
        elif id is None:
            self.id = id
        elif id:
            raise TypeError(f'{id} is of type {type(id)}')

        self.tip = None
        self.miles_traveled = None
        self.end_time = None

    def csv(self):
        return f'{self.tip.csv()},{self.miles_traveled},{self.end_time}'

    def file_list(self):
        from os import path
        from resources.system_names import\
            end_time, miles_traveled, Order__completed_ids as completed_ids,\
            order_directory, Order__id as order_id, Tip__info as tip

        parent_directory = self.parent.file_list()['directory']
        directory = path.join(parent_directory, order_directory)

        return {
            'completed_ids': path.join(parent_directory, completed_ids),
            'info': path.join(parent_directory, f'{self.id}.txt'),
            'directory': directory,
            'end_time': path.join(directory, end_time),
            'id': path.join(directory, order_id),
            'miles_traveled': path.join(directory, miles_traveled),
            'tip': path.join(directory, tip)
        }

    def view(self):
        from resources.strings import Order__time_taken__display as\
            time_display
        from utility.utility import time_taken

        return f'Order Id:\t#{self.id}\n'\
               f'{self.tip.view()}\n'\
               f'Miles to this order:\t{self.miles_traveled} miles\n'\
               f'Time order was completed:\t{self.end_time}\n' +\
               time_taken(self.parent.start_time, self.end_time, time_display)
