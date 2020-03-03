from os import mkdir, path, remove
from shutil import move

from extra_stop import check_id_number as extra_stop_id_check, Extra_Stop
import input_data
from order import check_id_number as order_id_check, input_id_number, Order
from utility import append_data, driving, miles_traveled, now, read_data,\
    time_taken, to_datetime, write_data


class Delivery:
    def __init__(self, shift, delivery_path):
        self.parent = shift
        self.path = delivery_path
        self.order_numbers = []
        self.orders = []
        self.extra_stop_numbers = []
        self.extra_stops = []
        # list of all paths
        self.order_quantity_path = path.join(self.path, 'order_quantity.txt')
        self.miles_path = path.join(self.path, 'delivery_miles_traveled.txt')
        self.average_speed_path =\
            path.join(self.path, 'delivery_average_speed.txt')
        self.start_time_path = path.join(self.path, 'delivery_start_time.txt')
        self.end_time_path = path.join(self.path, 'delivery_end_time.txt')
        self.order_numbers_path = path.join(self.path, 'order_numbers.txt')
        self.extra_stop_numbers_path =\
            path.join(self.path, 'extra_stop_numbers.txt')
        self.delivery_info_path = path.join(self.path, 'delivery_info.txt')

    def consolidate(self):
        data = str(self.miles_traveled) + ','\
            + str(self.average_speed) + ','\
            + str(self.start_time) + ','\
            + str(self.end_time)
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
        # assign data to variable and convert to intended types
        self.miles_traveled = float(delivery_data[0])
        self.average_speed = int(delivery_data[1])
        self.start_time = to_datetime(delivery_data[2])
        self.end_time = to_datetime(delivery_data[3])
        # read any order numbers, convert to list
        order_numbers = read_data(self.order_numbers_path).split(',')
        self.order_numbers = [int(item) for item in order_numbers]
        # append orders list with order classes
        for value in range(len(self.order_numbers)):
            order_id = self.order_numbers[len(self.orders)]
            self.orders.append(Order(self, order_id).load())
        # check if any extra stops have been completed
        if path.exists(self.extra_stop_numbers_path):
            extra_stop_numbers =\
                read_data(self.extra_stop_numbers_path).split(',')
            self.extra_stop_numbers =\
                [int(item) for item in extra_stop_numbers]
            for value in range(len(self.extra_stop_numbers)):
                extra_stop_id = self.extra_stop_numbers[len(self.extra_stops)]
                self.extra_stops.append(Extra_Stop(self, extra_stop_id).load())
        return self

    def load_current(self):
        # create varieable contaning a delivery start time
        if path.exists(self.start_time_path):
            self.start_time = to_datetime(read_data(self.start_time_path))
        else:
            self.start_time = write_data(self.start_time_path, now())
        self.id = len(self.parent.delivery_numbers)
        # read and set order quantity for delivery object
        if path.exists(self.order_quantity_path):
            self.order_quantity = int(read_data(self.order_quantity_path))
        else:
            # save number of order per delivery, add it to the delivery object
            self.order_quantity = write_data(
                self.order_quantity_path, input_data.input_data(
                    '\nNumber of orders?\n', int,
                    '\nIs this correct? [y/n]\n', str, 'y', 'n'))
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
        if path.exists(self.order_numbers_path):
            order_numbers = read_data(self.order_numbers_path).split(',')
            self.order_numbers = [int(item) for item in order_numbers]
            # append orders list with order classes
            for value in range(len(self.order_numbers)):
                order_id = self.order_numbers[len(self.orders)]
                order = Order(self, order_id).load()
                self.orders.append(order)
        # check if any extra stops have been completed
        if path.exists(self.extra_stop_numbers_path):
            extra_stop_numbers =\
                read_data(self.extra_stop_numbers_path).split(',')
            self.extra_stop_numbers =\
                [int(item) for item in extra_stop_numbers]
            for value in range(len(self.extra_stop_numbers)):
                extra_stop_id = self.extra_stop_numbers[len(self.extra_stops)]
                self.extra_stops.append(Extra_Stop(self, extra_stop_id).load())
        while True:
            # check if extra stop has been started while on delivery
            # todo: still need to work how to update shift extra stop id & parent lists
            if path.exists(path.join(self.path, 'extra_stop')):
                # assign a extra stop id number
                extra_stop_id = extra_stop_id_check(self)
                extra_stop = Extra_Stop(self, extra_stop_id).load_current()
                self.extra_stop_numbers.append(extra_stop.id)
                self.extra_stops.append(extra_stop)
            # check if order has been started
            elif path.exists(path.join(self.path, 'order')):
                order_id = order_id_check(self)
                order = Order(self, order_id).load_current()
                self.order_numbers.append(order.id)
                self.orders.append(order)
            # check if driving to address is in progress
            elif path.exists(path.join(self.path, 'driving-address')):
                driving(self, '\nDriving to address...', 'address')
            else:
                self.resume()
                break
        return self

    def resume(self):
        while True:
            orders_remaining = self.order_quantity - len(self.order_numbers)
            # loop through these functions for all of order quantity
            for value in range(orders_remaining):
                # user input after completing order or take extra stop
                driving(self, '\nDriving to address...', 'address')
                # enter data for orders
                order_id = order_id_check(self)
                order = Order(self, order_id).start()
                self.order_numbers.append(order.id_number)
                self.order.append(order)
            break
        # driving back to store
        driving(self, 'Driving back to store...', 'store')
        while True:
            # save the start time of the delivery and add it to the delivery
            if not path.exists(self.miles_path):
                # input/save/set total miles traveled to delivery object
                self.miles_traveled = write_data(
                    self.miles_path,
                    miles_traveled('Delivery miles traveled:    #.#'))
            elif not path.exists(self.average_speed_path):
                # input/save/set average speed to delivery object
                self.average_speed = write_data(
                    self.average_speed_path, input_data.input_data(
                        '\nEnter the average speed for this delivery:\n', int,
                        '\nIs this correct? [y/n]\n', str, 'y', 'n'))
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

    def start(self):
        # make folder to store data
        mkdir(self.path)
        # save the start time of the delivery and add it to the delivery object
        self.start_time = write_data(self.start_time_path, now())
        # assign delivery an id number
        self.id = len(self.parent.delivery_numbers)
        # save number of order per delivery, add it to the delivedy object
        self.order_quantity = write_data(
            self.order_quantity_path, input_data.input_data(
                '\nNumber of orders?\n', int,
                '\nIs this correct? [y/n]\n', str, 'y', 'n'))
        for value in range(self.order_quantity):
            # wait for user input after completing order or taking extra stop
            driving(self, '\nDriving to address...', 'address')
            # enter data for orders
            order_id = input_id_number(self)
            order = Order(self, order_id).start()
            self.order_numbers.append(order.id)
            self.orders.append(order)
        # driving back to store
        driving(self, 'Driving back to store...', 'store')
        # input/save/set total miles traveled to delivery object
        self.miles_traveled = write_data(
            self.miles_path, miles_traveled('Delivery miles traveled:    #.#'))
        # input/save/set average speed to delivery object
        self.average_speed = write_data(
            self.average_speed_path, input_data.input_data(
                '\nEnter the average speed for this delivery:\n', int,
                '\nIs this correct? [y/n]\n', str, 'y', 'n'))
        # save/set current time for end time of delivery object
        self.end_time = write_data(self.end_time_path, now())
        # consolidate files relating to delivery into one file
        self.consolidate()
        # display the total time taken on delivery
        time_taken(self.start_time, self.end_time, 'Delivery completed in:\t')
        return self

    def update_id_file(self):
        if path.exists(self.parent.delivery_numbers_path):
            return append_data(
                self.parent.delivery_numbers_path, ',' + str(self.id))
        else:
            return write_data(self.parent.delivery_numbers_path, self.id)
