from os import mkdir, path, remove
from shutil import move

from extra_stop import Extra_Stop
from input_data import get_input, input_data
from order import Order
from utility import append_data, now, read_data, time_taken,\
    to_datetime, write_data


def driving(delivery, prompt, destination):
    from extra_stop import Extra_Stop
    while True:
        if path.exists(path.join(delivery.path, 'driving-' + destination)):
            pass
        else:
            # create file so program knows while in driving process
            write_data(path.join(delivery.path, 'driving-' + destination), None)
        wait_for_user = get_input(
            f'{prompt}\n'
            'C: To complete\n'
            'E: For extra stop\n'
            'T: See current time\n'
            'Q: Quit program\n', str)
        if wait_for_user in ('c', 'C'):
            # remove driving file so code can knows driving has ended
            remove(path.join(delivery.path, 'driving-' + destination))
            break
        # extra stop option
        elif wait_for_user in ('e', 'E'):
            delivery.add_extra_stop(Extra_Stop(delivery).start())
        elif wait_for_user in ('t', 'T'):
            time_taken(delivery.start_time, now(), 'Current time is:\t')
        elif wait_for_user in ('q', 'Q'):
            exit()
        else:
            print('\nInvalid input...\n')
    return delivery


class Delivery:
    order_ids = []
    orders = []
    extra_stop_ids = []
    extra_stops = []

    # 

    # cnsd: use commas to split delivery data, use newline to split multi-delv
    def __init__(self, shift=None, id=None):
        if shift is not None and id is not None:
            self.id = id
            self.parent = shift
            self.path = path.join(shift.path, str(self.id))
        elif shift is not None:
            self.id = len(shift.deliveries)
            self.parent = shift
            self.path = path.join(shift.path, str(self.id))
        # list of all paths
        self.order_quantity_path = path.join(self.path, 'order_quantity.txt')
        self.miles_path = path.join(self.path, 'delivery_miles_traveled.txt')
        self.average_speed_path =\
            path.join(self.path, 'delivery_average_speed.txt')
        self.start_time_path = path.join(self.path, 'delivery_start_time.txt')
        self.end_time_path = path.join(self.path, 'delivery_end_time.txt')
        self.extra_stop_ids_path = path.join(self.path, 'extra_stop_ids.txt')
        self.delivery_info_path = path.join(self.path, 'delivery_info.txt')

    # methods for delivery tracking
    def add_extra_stop(self, extra_stop):
        self.extra_stop_ids.append(extra_stop.id)
        self.extra_stops.append(extra_stop)

    def add_order(self, order):
        self.order_ids.append(order.id)
        self.orders.append(order)

    def consolidate(self):
        self.save()
        # remove files that are no longer needed
        remove(self.order_quantity_path)
        remove(self.miles_path)
        remove(self.average_speed_path)
        remove(self.start_time_path)
        remove(self.end_time_path)
        # move temp folder to perma folder named the delivery's id number
        # todo: name folder to id at all times. check if path.exists(length(shift.delivery_ids) + 1)
        move(self.path, path.join(self.parent.path, str(self.id)))
        # create/update file tracking delivery quantity
        self.update_ids_file()

    def end(self):
        # wait for user to drive back to store
        driving(self, '\nDriving back to store...', 'store')
        if not path.exists(self.miles_path):
            # user inputs miles traveled
            self.input_miles_traveled()
        if not path.exists(self.average_speed_path):
            # user inputs average speed
            self.input_average_speed()
        if not path.exists(self.end_time_path):
            # save/set current time for end time of delivery object
            self.end_time()
        # consolidate data from individual files into one file
        self.consolidate()
        # display the time taken on delivery
        time_taken(self.start_time, self.end_time, 'Delivery completed in:\t')

    def load(self):
        # load data from file, convert to list
        delivery_data = read_data(self.delivery_info_path).split(',')
        #  todo: this it is better to try indaviduly and then handle it
        self.miles_traveled = float(delivery_data[0])
        self.average_speed = int(delivery_data[1])
        self.start_time = to_datetime(delivery_data[2])
        self.end_time = to_datetime(delivery_data[3])
        # load any completed orders
        order_ids = read_data(self.order_ids_path).split(',')
        for order_id in order_ids:
            self.add_order(Order(self, int(order_id)).load())
        # load any completed extra stops
        if path.exists(self.extra_stop_ids_path):
            extra_stop_ids = read_data(self.extra_stop_ids_path).split(',')
            for extra_stop_id in extra_stop_ids:
                self.add_extra_stop(
                    Extra_Stop(self, int(extra_stop_id)).load())
        return self

    def save(self):
        write_data(self.delivery_info_path, self.string())

    def start(self):
        # make directory to store data
        mkdir(self.path)
        # save the start time of the delivery
        self.start_time()
        # save number of order per delivery
        self.input_order_quantity()
        for value in range(self.order_quantity):
            # wait for user to complete order or take extra stop
            driving(self, '\nDriving to address...', 'address')
            # enter data for orders
            self.add_order(Order(self).start())
        self.end()

    def update_ids_file(self):
        if path.exists(self.parent.delivery_ids_path):
            append_data(self.parent.delivery_ids_path, ',' + str(self.id))
        else:
            write_data(self.parent.delivery_ids_path, self.id)

    # methods for saving/inputting data
    def end_time(self):
        self.end_time = now()
        write_data(self.end_time_path, self.end_time)

    def input_average_speed(self):
        self.average_speed = input_data(
            '\nEnter the average speed for this delivery:\t##\n', int,
            'Is this correct?\t[y/n]', str,
            ('y', 'Y'), ('n', 'N'), word='mph')
        write_data(self.average_speed_path, self.average_speed)

    def input_miles_traveled(self):
        self.miles_traveled = input_data(
            '\nDelivery miles traveled:\t#.#\n', float,
            'Is this correct?\t[y/n]', str,
            ('y', 'Y'), ('n', 'N'), word=' miles')
        write_data(self.miles_path, self.miles_traveled)

    def input_order_quantity(self):
        self.order_quantity = input_data(
            '\nNumber of orders?\n', int,
            'Is this correct?\t[y/n]', str,
            ('y', 'Y'), ('n', 'N'))
        write_data(self.order_quantity_path, self.order_quantity)

    def start_time(self):
        self.start_time = now()
        write_data(self.start_time_path, self.start_time)

    # methods for continuing tracking if program ends
    def load_current(self):
        # create varieable contaning a delivery start time
        if path.exists(self.start_time_path):
            self.start_time = to_datetime(read_data(self.start_time_path))
        else:
            self.start_time()
        self.id = len(self.parent.deliveries)
        # load order quantity file if it has been created yet
        if path.exists(self.order_quantity_path):
            self.order_quantity = int(read_data(self.order_quantity_path))
        else:
            # save number of order per delivery
            self.input_order_quantity()
        # load miles traveled file if it has been created yet
        if path.exists(self.miles_path):
            self.miles_traveled = float(read_data(self.miles_path))
        # load average speed file if it has been created yet
        if path.exists(self.average_speed_path):
            self.average_speed = int(read_data(self.average_speed_path))
        # load end time file if it has been created yet
        if path.exists(self.end_time_path):
            self.end_time = to_datetime(read_data(self.end_time_path))
        # load any orders that have been completed
        if path.exists(self.order_ids_path):
            order_ids = read_data(self.order_ids_path).split(',')
            for int(id) in order_ids:
                self.add_order(Order(self, id).load())
        # load any extra stops that have been completed
        if path.exists(self.extra_stop_ids_path):
            extra_stop_ids = read_data(self.extra_stop_ids_path).split(',')
            for extra_stop_id in extra_stop_ids:
                self.extra_stop_ids.append(int(extra_stop_id))
                self.extra_stops.append(Extra_Stop(self, extra_stop_id).load())
        self.resume()
        return self

    def resume(self):
        # check if extra stop has been started while on delivery
        if path.exists(path.join(self.path, 'extra_stop')):
            self.add_extra_stop(Extra_Stop(self).load_current())
        # check if order has been started
        if path.exists(path.join(self.path, 'order')):
            self.add_order(Order(self).load_current())
        while self.order_quantity > len(self.orders):
            # wait for user to complete order or take extra stop
            driving(self, '\nDriving to address...', 'address')
            # enter data for order
            self.add_order(Order(self).start())
        self.end()

    # utility methods
    def string(self):
        return f'{self.miles_traveled},{self.average_speed},{self.start_time},{self.end_time}'

    # methods for analyzing data
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
            if order.tip.has_both():
                tips.append(order.tip.card)
                tips.append(order.tip.cash)
            elif order.tip.has_card:
                tips.append(order.tip.card)
            elif order.tip.has_cash:
                tips.append(order.tip.cash)
            elif order.tip.has_unknown:
                tips.append(order.tip.unknown)
        return tips

# todo: write methods to change data when a delivery is in progress as well as completed
# todo: write method that allows the user selecte data to change
# todo: write method that allows user to change data specific to a delivery
