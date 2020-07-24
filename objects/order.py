
class Order:
    def __init__(self, delivery, id=None):
        from objects.delivery import Delivery
        if not isinstance(delivery, Delivery):
            from resources.error_messages import\
                Order__class__wrong_parent_type as error_message
            raise TypeError(error_message.format(type(delivery)))

        self.parent = delivery

        if isinstance(id, int):
            self.id = id
        elif id is None:
            self.id = 0
        elif id:
            from resources.error_messages import\
                Order__class__wrong_id_type as error_message
            raise TypeError(error_message.format(type(id)))

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
        formated_time = self.end_time.strftime('%I:%M:%S %p')

        view_parts = {
            'id': f'Order I.D. #:\t{self.id}',
            'distance': f'Distance to address:\t{self.miles_traveled} miles',
            'end_time': f'Completed at:\t{formated_time}'
        }

        tip_parts = self.tip.view()

        if 'card' in tip_parts.keys() and self.tip.card != 0.0:
            view_parts['card'] = f'Card tip:\t${self.tip.card}'
        if 'cash' in tip_parts.keys() and self.tip.cash != 0.0:
            view_parts['cash'] = f'Cash tip:\t${self.tip.cash}'
        if 'unknown' in tip_parts.keys() and self.tip.unknown != 0.0:
            view_parts['unknown'] = f'Unknown tip:\t${self.tip.unknown}'

        return view_parts
