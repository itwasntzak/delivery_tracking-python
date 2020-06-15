from os import mkdir, path, remove
from shutil import move

from objects.extra_stop import Extra_Stop
from utility.user_input import get_input, input_data
from objects.order import Order
from utility import append_data, now, read_data, time_taken,\
    to_datetime, write_data


class Delivery:
    id = None
    parent = None
    miles_traveled = None
    average_speed = None
    order_ids = []
    orders = []
    extra_stop_ids = []
    extra_stops = []

    # cnsd: use commas to split delivery data, use newline to split multi-delv
    def __init__(self, shift=None, id=None):
        from objects.shift import Shift
        if isinstance(shift, Shift):
            self.parent = shift
        elif shift:
            raise TypeError

        if isinstance(id, int):
            self.id = id
        elif id:
            raise TypeError

    def add_extra_stop(self, extra_stop):
        self.extra_stop_ids.append(extra_stop.id)
        self.extra_stops.append(extra_stop)

    def add_order(self, order):
        self.order_ids.append(order.id)
        self.orders.append(order)

    def csv(self):
        return f'{self.miles_traveled},{self.average_speed},'\
               f'{self.start_time},{self.end_time}'

    def directory(self):
        from objects.shift import Shift
        if isinstance(self.parent, Shift):
            return self.parent.directory()
        elif self.parent:
            raise TypeError

    def file_list(self):
        from os import path
        from resources.strings import Delivery__info, Delivery__order_quantity
        # todo: need to finish making paths for delivery
        return {
            'average_speed': None,
            'completed_ids': None,
            'directory': None,
            'extra_stop_ids': None,
            'end_time': None,
            'info_file': None,
            'miles_traveled': None,
            'order_ids': None,
            'order_quantity': None,
            'start_time': None
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
