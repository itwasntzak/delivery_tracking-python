from os import mkdir, path, remove
from shutil import move

from extra_stop import Extra_Stop
from input_data import input_data
from order import Order
from utility import append_data, driving, now, read_data, time_taken,\
    to_datetime, write_data


class Delivery:
    # todo: use commas to split delivery data, then use newline to seperate if multi-delivery
    def __init__(self, shift='', delivery_path=''):
        if (shift) != '':
            self.parent = shift
        if (delivery_path) != '':
            self.path = delivery_path
        self.order_ids = []
        self.orders = []
        self.extra_stop_ids = []
        self.extra_stops = []
        # list of all paths
        try:
            self.order_quantity_path =\
                path.join(self.path, 'order_quantity.txt')
            self.miles_path =\
                path.join(self.path, 'delivery_miles_traveled.txt')
            self.average_speed_path =\
                path.join(self.path, 'delivery_average_speed.txt')
            self.start_time_path =\
                path.join(self.path, 'delivery_start_time.txt')
            self.end_time_path = path.join(self.path, 'delivery_end_time.txt')
            self.order_ids_path = path.join(self.path, 'order_ids.txt')
            self.extra_stop_ids_path =\
                path.join(self.path, 'extra_stop_ids.txt')
            self.delivery_info_path = path.join(self.path, 'delivery_info.txt')
        except AttributeError:
            pass

    # methods for delivery tracking
    def consolidate(self):
        data = '{0},{1},{2},{3}'.format(
            self.miles_traveled, self.average_speed,
            self.start_time, self.end_time)
        # write the data to the file
        write_data(self.delivery_info_path, data)
        # remove files that are no longer needed
        remove(self.order_quantity_path)
        remove(self.miles_path)
        remove(self.average_speed_path)
        remove(self.start_time_path)
        remove(self.end_time_path)
        # move temp folder to perma folder named the delivery's id number
        move(self.path, path.join(self.parent.path, str(self.id)))
        # create/update file tracking delivery quantity
        self.update_id_file()

    def load(self):
        # load data from file, convert to list
        delivery_data = read_data(self.delivery_info_path).split(',')
        try:
            self.miles_traveled = float(delivery_data[0])
            self.average_speed = int(delivery_data[1])
            self.start_time = to_datetime(delivery_data[2])
            self.end_time = to_datetime(delivery_data[3])
        except ValueError:
            try:
                self.miles_traveled = float(delivery_data[0])
                self.start_time = to_datetime(delivery_data[2])
                self.end_time = to_datetime(delivery_data[3])
            except ValueError:
                self.miles_traveled = float(delivery_data[0])
        order_ids = read_data(self.order_ids_path).split(',')
        for order_id in order_ids:
            self.order_ids.append(int(order_id))
            self.orders.append(Order(self, order_id.rstrip('\n')).load())
        # check if any extra stops have been completed
        if path.exists(self.extra_stop_ids_path):
            extra_stop_ids = read_data(self.extra_stop_ids_path).split(',')
            for extra_stop_id in extra_stop_ids:
                self.extra_stop_ids.append(int(extra_stop_id))
                self.extra_stops.append(Extra_Stop(self, extra_stop_id).load())
        return self

    def start(self):
        # make folder to store data
        mkdir(self.path)
        # save the start time of the delivery and add it to the delivery object
        self.start_time = write_data(self.start_time_path, now())
        # assign delivery an id number
        self.id = len(self.parent.delivery_ids)
        # save number of order per delivery, add it to the delivedy object
        self.order_quantity = self.input_order_quantity()
        for value in range(self.order_quantity):
            # wait for user input after completing order or taking extra stop
            driving(self, '\nDriving to address...', 'address')
            # enter data for orders
            order = Order(self).start()
            self.order_ids.append(order.id)
            self.orders.append(order)
        # driving back to store
        driving(self, 'Driving back to store...', 'store')
        # input/save/set total miles traveled to delivery object
        self.miles_traveled = self.input_miles_traveled()
        # input/save/set average speed to delivery object
        self.average_speed = self.input_average_speed()
        # save/set current time for end time of delivery object
        self.end_time = write_data(self.end_time_path, now())
        # consolidate files relating to delivery into one file
        self.consolidate()
        # display the total time taken on delivery
        time_taken(self.start_time, self.end_time, 'Delivery completed in:')
        return self

    def update_id_file(self):
        if path.exists(self.parent.delivery_ids_path):
            return append_data(
                self.parent.delivery_ids_path, ',' + str(self.id))
        else:
            return write_data(self.parent.delivery_ids_path, self.id)

    # methods for inputting data
    def input_average_speed(self):
        return write_data(self.average_speed_path, input_data(
            '\nEnter the average speed for this delivery:\n', int,
            f"{'Is this correct?'}         {'[y/n]'}\n", str,
            ('y', 'Y'), ('n', 'N'), word='mph'))

    def input_miles_traveled(self):
        return write_data(self.miles_path, input_data(
            f"\n{'Delivery miles traveled:'}   {'#.#'}\n", float,
            f"{'Is this correct?'}         {'[y/n]'}\n", str,
            ('y', 'Y'), ('n', 'N'), word=' miles'))

    def input_order_quantity(self):
        return write_data(self.order_quantity_path, input_data(
            '\nNumber of orders?\n', int,
            f"\n{'Is this correct?'}         {'[y/n]'}\n", str,
            ('y', 'Y'), ('n', 'N')))

    # methods for continuing tracking if program ends
    def load_current(self):
        # create varieable contaning a delivery start time
        if path.exists(self.start_time_path):
            self.start_time = to_datetime(read_data(self.start_time_path))
        else:
            self.start_time = write_data(self.start_time_path, now())
        self.id = len(self.parent.delivery_ids)
        # read and set order quantity for delivery object
        if path.exists(self.order_quantity_path):
            self.order_quantity = int(read_data(self.order_quantity_path))
        else:
            # save number of order per delivery, add it to the delivery object
            self.order_quantity = self.input_order_quantity()
        # check if miles traveled file has been created yet
        if path.exists(self.miles_path):
            self.miles_traveled = float(read_data(self.miles_path))
        # check if average speed file has been created yet
        if path.exists(self.average_speed_path):
            self.average_speed = int(read_data(self.average_speed_path))
        # check if end time file has been created yet
        if path.exists(self.end_time_path):
            self.end_time = to_datetime(read_data(self.end_time_path))
        # check if any orders have been completed
        if path.exists(self.order_ids_path):
            order_ids = read_data(self.order_ids_path).split(',')
            for order_id in order_ids:
                self.order_ids.append(int(order_id))
                self.orders.append(Order(self, order_id).load())
        # check if any extra stops have been completed
        if path.exists(self.extra_stop_ids_path):
            extra_stop_ids = read_data(self.extra_stop_ids_path).split(',')
            for extra_stop_id in extra_stop_ids:
                self.extra_stop_ids.append(int(extra_stop_id))
                self.extra_stops.append(Extra_Stop(self, extra_stop_id).load())
        self.resume()
        return self

    def resume(self):
        while True:
            # check if extra stop has been started while on delivery
            if path.exists(path.join(self.path, 'extra_stop')):
                extra_stop = Extra_Stop(self).load_current()
                self.extra_stop_ids.append(extra_stop.id)
                self.extra_stops.append(extra_stop)
            # check if order has been started
            elif path.exists(path.join(self.path, 'order')):
                order = Order(self).load_current()
                self.order_ids.append(order.id)
                self.orders.append(order)
            # check if driving to address is in progress
            elif path.exists(path.join(self.path, 'driving-address')):
                driving(self, '\nDriving to address...', 'address')
                # enter data for orders
                order = Order(self).start()
                self.order_ids.append(order.id)
                self.orders.append(order)
            else:
                break
        orders_remaining = self.order_quantity - len(self.orders)
        # loop through these functions for all of order quantity
        for value in range(orders_remaining):
            # user input after completing order or take extra stop
            driving(self, '\nDriving to address...', 'address')
            # enter data for orders
            order = Order(self).start()
            self.order_ids.append(order.id)
            self.orders.append(order)
        # driving back to store
        driving(self, '\nDriving back to store...', 'store')
        while True:
            if not path.exists(self.miles_path):
                # input/save/set total miles traveled to delivery object
                self.miles_traveled = self.input_miles_traveled()
            elif not path.exists(self.average_speed_path):
                # input/save/set average speed to delivery object
                self.average_speed = self.input_average_speed()
            elif not path.exists(self.end_time_path):
                # save/set current time for end time of delivery object
                self.end_time = write_data(self.end_time_path, now())
            else:
                break
        # consolidate files relating to delivery into one file
        self.consolidate()
        # display the total time taken on delivery
        time_taken(self.start_time, self.end_time, 'Delivery completed in:\t')
        return self

    # methods for analyzing data
# def card_tips(self):
#     card_tips = []
#     for order in self.orders:
#         if order.tip_type == 1:
#             card_tips.append(order.tip)
#         elif order.tip_type in (0, 2):
#             pass
#     return card_tips

# def cash_tips(self):
#     cash_tips = []
#     for order in self.orders:
#         if order.tip_type == 2:
#             cash_tips.append(order.tip)
#         elif order.tip_type in (0, 1):
#             pass
#     return cash_tips

# def total_tips(self):
#     tips = []
#     for order in self.orders:
#         tips.append(order.tip)
#     return tips
