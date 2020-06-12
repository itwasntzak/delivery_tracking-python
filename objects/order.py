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
        from delivery import Delivery
        if isinstance(delivery, Delivery):
            self.parent = delivery
        elif delivery:
            error_message =\
                f"parent of Order must be Delivery not '{type(delivery)}'"
            raise TypeError(error_message)

        if id:
            try:
                self.id = int(id)
            except TypeError:
                print('An order id must be numbers (base 10)')
            except ValueError:
                print('An order id must be numbers (base 10)')
            else:
                self.info_file()

    def csv(self):
        return f'{self.tip.csv()},{self.miles_traveled},{self.end_time}'

    def directory(self):
        from delivery import Delivery
        from error_messages import\
            Order__directory__wrong_parent as error_message

        if isinstance(self.parent, Delivery):
            return self.parent.directory()
        elif not self.parent:
            pass
        elif self.parent:
            raise TypeError(error_message)

    def file_list(self):
        from os import path
        from resources.system_names import end_time, miles_traveled as miles,\
            Order__completed_ids, order_directory, Order__id, Tip__info

        return {
            'directory': path.join(self.directory(), order_directory),
            'id': path.join(self.directory(), order_directory, Order__id),
            'tip': path.join(self.directory(), order_directory, Tip__info),
            'miles': path.join(self.directory(), order_directory, miles),
            'end_time': path.join(self.directory(), order_directory, end_time),
            'info_file': path.join(self.directory(), self.info_file()),
            'completed_ids': path.join(self.directory(), Order__completed_ids)
        }

    def info_file(self):
        if self.id:
            return f'{self.id}.txt'
        else:
            from resources.error_messages import Order__info_file__missing_id
            raise AttributeError(Order__info_file__missing_id)

    def view(self):
        from resources.strings import Order__time_taken__display as\
            time_display
        from utility.utility import time_taken

        return f'Order Id:\t#{self.id}\n'\
               f'{self.tip.view()}\n'\
               f'Miles to this order:\t{self.miles_traveled} miles\n'\
               f'Time order was completed:\t{self.end_time}\n' +\
               time_taken(self.parent.start_time, self.end_time, time_display)

