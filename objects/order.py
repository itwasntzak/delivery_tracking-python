
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
            self.id = 0
        elif id:
            raise TypeError(f'{id} is of type {type(id)}')

        self.tip = None
        self.miles_traveled = None
        self.end_time = None

    def csv(self):
        return f'{self.tip.csv()},{self.miles_traveled},{self.end_time}'

    def display_text(self):
        display_text = {}

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
