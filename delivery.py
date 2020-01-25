import datetime
from os import mkdir, path, remove
import shutil

import extra_stop
import id_number
import input_data
import order
import utility


class Delivery:
    def consolidate(self):
        # list of all paths
        # pre consolidation paths
        order_quantity_path =\
            path.join('delivery', 'order_quantity.txt')
        miles_traveled_path =\
            path.join('delivery', 'delivery_miles_traveled.txt')
        average_speed_path =\
            path.join('delivery', 'delivery_average_speed.txt')
        start_time_path =\
            path.join('delivery', 'delivery_start_time.txt')
        end_time_path =\
            path.join('delivery', 'delivery_end_time.txt')
        # pre & post consolidation paths
        order_numbers_path =\
            path.join('delivery', 'order_numbers.txt')
        extra_stop_numbers_path =\
            path.join('delivery', 'extra_stop_numbers.txt')
        # post consolidation paths
        delivery_info_path =\
            path.join('delivery', 'delivery_info.txt')

        # assign data to variables
        order_quantity = str(self.order_quantity)
        extra_stop_quantity = str(len(self.extra_stop_numbers))
        miles_traveled = str(self.miles_traveled)
        average_speed = str(self.average_speed)
        delivery_start_time = str(self.start_time)
        delivery_end_time = str(self.end_time)

        data = order_quantity + ',' + extra_stop_quantity + ','\
            + miles_traveled + ',' + average_speed + ','\
            + delivery_start_time + ',' + delivery_end_time
        # write the data to the file
        utility.write_data(delivery_info_path, data)
        # create/update file tracking delivery quantity
        id_number.id_number_file(self)
        # remove files that are no longer needed
        remove(order_quantity_path)
        remove(miles_traveled_path)
        remove(average_speed_path)
        remove(start_time_path)
        remove(end_time_path)
        # mv temp folder to perma folder named the delivery's id number
        shutil.move('delivery', path.join('shift', str(self.id_number)))

    def delivery(self, shift_object):
        # make folder to store data
        mkdir('delivery')
        order_quantity_path =\
            path.join('delivery', 'order_quantity.txt')
        miles_traveled_path =\
            path.join('delivery', 'delivery_miles_traveled.txt')
        average_speed_path =\
            path.join('delivery', 'delivery_average_speed.txt')
        start_time_path =\
            path.join('delivery', 'delivery_start_time.txt')
        end_time_path =\
            path.join('delivery', 'delivery_end_time.txt')
        # save the start time of the delivery and add it to the delivery object
        self.start_time = utility.write_data(start_time_path, utility.now())
        # assign delivery an id number
        self.id_number = len(shift_object.delivery_numbers)
        # save number of order per delivery, add it to the delivedy object
        self.order_quantity = utility.write_data(
            order_quantity_path, input_data.input_data(
                '\nNumber of orders?\n', int,
                '\nIs this correct? [y/n]\n', str, 'y', 'n'))
        self.order_numbers = []
        for value in range(self.order_quantity):
            # wait for user input after completing order or taking extra stop
            utility.driving(self, '\nDriving to address...', 'address')
            order_object = order.Order().order()
            # enter data for orders
            self.order_numbers.append(order_object)
            # display amount of time to complete the order
            utility.time_taken(self.start_time, order_object.end_time, 'Order')
        # driving back to store
        utility.driving(self, 'Driving back to store...', 'store')
        # input/save/set total miles traveled to delivery object
        self.miles_traveled = utility.write_data(
            miles_traveled_path,
            utility.miles_traveled('Delivery miles traveled:    #.#'))
        # input/save/set average speed to delivery object
        self.average_speed = utility.write_data(
            average_speed_path, input_data.input_data(
                '\nEnter the average speed for this delivery:\n', int,
                '\nIs this correct? [y/n]\n', str, 'y', 'n'))
        # save/set current time for end time of delivery object
        self.end_time = utility.write_data(end_time_path, utility.now())
        # consolidate files relating to delivery into one file
        self.consolidate()
        # display the total time taken on delivery
        utility.time_taken(self.start_time, self.end_time, 'Delivery')
        # allow user time to view time taken
        utility.enter_to_continue()
        exit()

    def load(self, shift_object):
        # set all possible paths to varibles
        order_quantity_path =\
            path.join('delivery', 'order_quantity.txt')
        miles_traveled_path =\
            path.join('delivery', 'delivery_miles_traveled.txt')
        average_speed_path =\
            path.join('delivery', 'delivery_average_speed.txt')
        start_time_path =\
            path.join('delivery', 'delivery_start_time.txt')
        end_time_path =\
            path.join('delivery', 'delivery_end_time.txt')
        order_numbers_path =\
            path.join('delivery', 'order_numbers.txt')
        extra_stop_numbers_path =\
            path.join('delivery', 'extra_stop_numbers.txt')

        # assign delivery an id number
        self.id_number = len(shift_object.delivery_numbers)
        # create a varieable contaning a delivery start time
        if path.exists(start_time_path):
            self.start_time = utility.to_datetime(
                utility.read_data(start_time_path))
        else:
            self.start_time =\
                utility.write_data(start_time_path, utility.now())
        # read and set order quantity for delivery object
        if path.exists(order_quantity_path):
            self.order_quantity =\
                int(utility.read_data(order_quantity_path))
        else:
            # save number of order per delivery, add it to the delivedy object
            self.order_quantity = utility.write_data(
                path.join('delivery', 'order_quantity.txt'),
                input_data.input_data(
                    '\nNumber of orders?\n', int,
                    '\nIs this correct? [y/n]\n', str, 'y', 'n'))
        # check if miles traveled file has been created yet
        if path.exists(miles_traveled_path):
            self.miles_traveled =\
                float(utility.read_data(miles_traveled_path))
        if path.exists(average_speed_path):
            self.average_speed =\
                int(utility.read_data(average_speed_path))
        # check if end time file has been created yet
        if path.exists(end_time_path):
            self.end_time = utility.to_datetime(
                utility.read_data(end_time_path))
        if path.exists(order_numbers_path):
            self.order_numbers =\
                utility.read_data(order_numbers_path).split(',')
        else:
            self.order_numbers = []
        if path.exists(extra_stop_numbers_path):
            self.extra_stop_numbers =\
                utility.read_data(extra_stop_numbers_path).split(',')
        else:
            self.extra_stop_numbers = []
        return self

    def resume(self):
        # set all possible paths to varibles
        miles_traveled_path =\
            path.join('delivery', 'delivery_miles_traveled.txt')
        average_speed_path =\
            path.join('delivery', 'delivery_average_speed.txt')
        end_time_path =\
            path.join('delivery', 'delivery_end_time.txt')

        while True:
            orders_remaining =\
                self.order_quantity - len(self.order_numbers)
            # loop through these functions for all of order quantity
            for value in range(orders_remaining):
                # user input after completing order or take extra stop
                utility.driving(self, '\nDriving to address...', 'address')
                # enter data for orders
                order_object = order.Order().order()
                self.order_numbers.append(order_object)
                # display amount of time to complete the order
                utility.time_taken(
                    self.start_time, order_object.end_time, 'Order')
            break
        # driving back to store
        utility.driving(self, 'Driving back to store...', 'store')
        while True:
            # save the start time of the delivery and add it to the delivery
            if not path.exists(miles_traveled_path):
                # input/save/set total miles traveled to delivery object
                self.miles_traveled = utility.write_data(
                    miles_traveled_path,
                    utility.miles_traveled('Delivery miles traveled:    #.#'))
            elif not path.exists(average_speed_path):
                # input/save/set average speed to delivery object
                self.average_speed = utility.write_data(
                    average_speed_path, input_data.input_data(
                        '\nEnter the average speed for this delivery:\n', int,
                        '\nIs this correct? [y/n]\n', str, 'y', 'n'))
            elif not path.exists(end_time_path):
                # save/set current time for end time of delivery object
                self.end_time =\
                    utility.write_data(end_time_path, utility.now())
            else:
                break
        # consolidate files relating to delivery into one file
        self.consolidate()
        # display the total time taken on delivery
        utility.time_taken(
            self.start_time, self.end_time, 'Delivery')
        # allow user time to view time taken
        while True:
            wait_for_user = input('Press enter to continue.\n')
            if wait_for_user == '':
                exit()
            else:
                continue
