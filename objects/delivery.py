
class Delivery:
    # cnsd: use commas to split delivery data, use newline to split multi-delv
    def __init__(self, shift, id=None):
        from objects.shift import Shift
        if not isinstance(shift, Shift):
            raise TypeError
        self.parent = shift

        if isinstance(id, int):
            self.id = id
        elif id is None:
            self.id = len(shift.deliveries)
        elif id:
            raise TypeError

        self.start_time = None
        self.end_time = None
        self.miles_traveled = None
        self.average_speed = None
        self.order_ids = []
        self.orders = []
        self.extra_stop_ids = []
        self.extra_stops = []

    def add_extra_stop(self, extra_stop):
        from objects.extra_stop import Extra_Stop

        if isinstance(extra_stop, Extra_Stop):
            self.extra_stop_ids.append(extra_stop.id)
            self.extra_stops.append(extra_stop)
        else:
            raise TypeError

    def add_order(self, order):
        from objects.order import Order
        if not isinstance(order, Order):
            raise TypeError(f'{order} is of type {type(order)}')

        self.order_ids.append(order.id)
        self.orders.append(order)

    def csv(self):
        return f'{self.miles_traveled},{self.average_speed},'\
               f'{self.start_time},{self.end_time}'

    def file_list(self):
        from os import path
        from resources.system_names import\
            Delivery__completed_ids as completed_ids,\
            delivery_directory, end_time as end_time,\
            Delivery__average_speed as average_speed,\
            Delivery__info as info_file,\
            miles_traveled as miles_traveled,\
            start_time as start_time

        parent_directory = self.parent.file_list()['directory']
        directory = path.join(parent_directory, f'{self.id}')

        return {
            'completed_ids': path.join(parent_directory, completed_ids),
            'directory': directory,
            'average_speed': path.join(directory, average_speed),
            'end_time': path.join(directory, end_time),
            'info': path.join(directory, info_file),
            'miles_traveled': path.join(directory, miles_traveled),
            'start_time': path.join(directory, start_time)
        }
    
    def view(self):
        from datetime import datetime

        view_parts = {'id': f'Delivery #:\t{self.id + 1}'}

        if isinstance(self.start_time, datetime) and\
                isinstance(self.end_time, datetime):
            from utility.utility import time_taken
            view_parts['time_taken'] =\
                time_taken(self.start_time, self.end_time,
                           'Total time taken:\t')

        if isinstance(self.start_time, datetime):
            start_time = self.start_time.strftime('%I:%M:%S %p')
            view_parts['start_time'] = f'Started at:\t{start_time}'

        view_parts['order_quantity'] = f'Number of orders:\t{len(self.orders)}'

        temp_string = 'Order I.D. #{}:\t'
        if len(self.order_ids) == 1:
            temp_string = temp_string.format('')
            temp_string += f'{self.order_ids[0]}'
            view_parts['order_ids'] = temp_string
        elif len(self.order_ids) > 1:
            temp_string = temp_string.format("'s")
            for value in range(len(self.order_ids) - 1):
                    index = value
                    id = self.order_ids[index]
                    temp_string += f'{id}, '
            index += 1
            id = self.order_ids[index]
            temp_string += f'{id}'
            view_parts['order_ids'] = temp_string

        if isinstance(self.miles_traveled, float)\
                  and self.miles_traveled > 0.0:
            view_parts['distance'] =\
                f'Total distance traveled for delivery:\t{self.miles_traveled} miles'

        if isinstance(self.average_speed, int) and self.average_speed > 0:
            view_parts['average_speed'] = f'Average speed for delivery:\t{self.average_speed} mph'

        if isinstance(self.end_time, datetime):
            end_time = self.end_time.strftime('%I:%M:%S %p')
            view_parts['end_time'] = f'Completed at:\t{end_time}'
        
        if len(self.extra_stops) > 0:
            view_parts['extra_stops'] = f'Number of extra stops:\t{len(self.extra_stops)}'
        
        return view_parts

# todo: write methods to change data when a delivery is in progress as well as completed
# todo: write method that allows the user selecte data to change
# todo: write method that allows user to change data specific to a delivery
