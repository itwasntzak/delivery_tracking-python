
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

    def card_tips(self):
        card_tips = []
        for order in self.orders:
            if order.tip.has_card:
                card_tips.append(order.tip.card)
        return card_tips

    def cash_tips(self):
        cash_tips = []
        for order in self.orders:
            if order.tip.has_cash:
                cash_tips.append(order.tip.cash)
        return cash_tips

    def total_tips(self):
        tips = []
        for order in self.orders:
            if order.tip.has_card:
                tips.append(order.tip.card)
            if order.tip.has_cash:
                tips.append(order.tip.cash)
            if order.tip.has_unknown:
                tips.append(order.tip.unknown)
        return tips

# todo: write methods to change data when a delivery is in progress as well as completed
# todo: write method that allows the user selecte data to change
# todo: write method that allows user to change data specific to a delivery
