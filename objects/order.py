from tip import Tip
from utility.user_input import User_Input


class Order:
    # list of attributes
    id = None
    parent = None
    tip = Tip()
    miles_traveled = None
    end_time = None

    def __init__(self, delivery=None, id=None):
        from objects.delivery import Delivery
        if isinstance(delivery, Delivery):
            self.parent = delivery
        elif delivery:
            error_message =\
                f"parent of Order must be Delivery not '{type(delivery)}'"
            raise TypeError(error_message)

        if isinstance(id, int):
            self.id = id
        elif id:
            raise TypeError

    def directory(self):
        from objects.delivery import Delivery
        try:
            from os import path
            return self.parent.directory()
        except AttributeError:
            from resources.error_messages import\
                Order__directory__no_parent as error_message
            print(error_message)

    def csv(self):
        return f'{self.tip.csv()},{self.miles_traveled},{self.end_time}'

    def file_list(self):
        from os import path
        from resources.system_names import\
            end_time, miles_traveled, Order__completed_ids as completed_ids,\
            order_directory, Order__id as order_id, Tip__info as tip

        directory = path.join(self.directory(), order_directory)

        return {
            'completed_ids': path.join(self.directory(), completed_ids),
            'end_time': path.join(directory, end_time),
            'id': path.join(directory, order_id),
            'miles_traveled': path.join(directory, miles_traveled),
            'tip': path.join(directory, tip)
        }

    def info_file(self):
        try:
            from os import path
            return path.join(self.directory(), f'{self.id}.txt')
        except AttributeError:
            from resources.error_messages import\
                Order__info_file__missing_id as error_message
            print(error_message)

    def view(self):
        from resources.strings import Order__time_taken__display as\
            time_display
        from utility.utility import time_taken

        return f'Order Id:\t#{self.id}\n'\
               f'{self.tip.view()}\n'\
               f'Miles to this order:\t{self.miles_traveled} miles\n'\
               f'Time order was completed:\t{self.end_time}\n' +\
               time_taken(self.parent.start_time, self.end_time, time_display)
