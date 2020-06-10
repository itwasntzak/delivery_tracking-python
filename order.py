from os import path, remove

from input_data import get_input, input_data
import load
from tip import Tip
from utility import append_data, now, read_data, time_taken,\
    to_datetime, write_data


class Order:
    # list of attributes
    id = None
    parent = None
    tip = Tip()
    miles_traveled = None
    end_time = None
    id_file = 'order_id.txt'

    def __init__(self, delivery=None, id=None):
        if delivery is not None:
            from delivery import Delivery
            if isinstance(delivery, Delivery):
                self.parent = delivery
            else:
                em = f"parent of Order must be Delivery not '{type(delivery)}'"
                raise TypeError(em)
        if id is not None:
            try:
                self.id = int(id)
            except TypeError:
                print(f'an Order id must be a string or a number type')
            except ValueError:
                print(f"string Order id's must contain number characters")
            else:
                self.info_file()

    def info_file(self):
        if self.id is not None:
            return f'{self.id}.txt'
        else:
            raise AttributeError('this Order does not have an assigned id')

    # method to load a completed order
    def load(self):
        if self.parent is not None:
            from delivery import Delivery
            if isinstance(self.parent, Delivery):
                try:
                    self = load.order((parent.directory, self.info_file()))
                except AttributeError:
                    # todo: present user with option to input id
                    # todo: present user with option to cancel order
                    self.input_id()
                    self.load()
                except FileNotFoundError:
                    # todo: present user with the option to change the id
                    # todo: present user with option to enter data for the order
                    # todo: present user with option to remove the order id
                    print('the file was not found, or does not exist')
            else:
                raise TypeError('parent of Order must be Delivery')
        else:
            try:
                self = load.order(self.info_file())
            except AttributeError:
                # todo: present user with option to input id
                # todo: present user with option to cancel order
                self.input_id()
                self.load()
            except FileNotFoundError:
                # todo: present user with the option to change the id
                # todo: present user with option to enter data for the order
                # todo: present user with option to remove the order id
                print('the file was not found, or does not exist')

# todo: everything below is still not fixed

    # methods for order tracking
    def consolidate(self):
        self.save()
        # remove files that are no longer needed
        remove(self.id_path)
        remove(self.tip_path)
        remove(self.miles_path)
        remove(self.end_time_path)
        # update/create order_ids.txt
        self.update_ids_file()
        # remove file telling program, order is in progress
        remove(path.join(self.path, 'order'))

    # method to continue entering data if program ends
    def load_current(self):
        # check if the user has entered the tip yet, if not enter it
        if path.exists(self.tip_path):
            tip = read_data(self.tip_path).split(',')
            self.tip = Tip(tip[0], tip[1], tip[2])
        else:
            self.tip.input_split()
        # check if the user has entered the miles, if not enter it
        if path.exists(self.miles_path):
            self.miles_traveled = float(read_data(self.miles_path))
        else:
            self.input_miles_traveled()
        # check if the end time has been save yet, if not do so
        if path.exists(self.end_time_path):
            self.end_time = to_datetime(read_data(self.end_time_path))
        else:
            self.end_time()
        # bring data from seperate files to a single file
        self.consolidate()
        # display amount of time to complete the order
        time_taken(self.parent.start_time, self.end_time,
                   'Order completed in:\t')
        return self

    # method to save data for order to a file
    def save(self):
        write_data(self.order_file_path, self.string())

    # method to begin entering order data
    def start(self):
        # create file so program knows order was started
        write_data(path.join(self.path, 'order'), None)
        # input tip amount
        self.tip.input_split()
        self.tip.save(self.tip_path)
        # input miles since previous destination
        self.input_miles_traveled()
        # save/assign current time for end of order
        self.end_time()
        # consolidate order files into one file
        self.consolidate()
        # display amount of time to complete the order
        time_taken(self.parent.start_time,
                   self.end_time,
                   'Order completed in:')
        return self

    # create/update a file so program knows what orders exist
    def update_ids_file(self):
        if path.exists(self.parent.order_ids_path):
            append_data(self.parent.order_ids_path, ',' + str(self.id))
        else:
            write_data(self.parent.order_ids_path, self.id)

    # methods for saving/inputting data
    def end_time(self):
        self.end_time = now()
        write_data(self.end_time_path, self.end_time)

    def input_miles_traveled(self):
        self.miles_traveled = input_data(
            '\nOrder miles traveled:\t#.#\n', float,
            'Is this correct?\t[y/n]', str,
            ('y', 'Y'), ('n', 'N'), word=' miles')
        write_data(self.miles_path, self.miles_traveled)

    def input_id_number(self):
        self.id = input_data(
            '\nEnter order number:\t#-####\n', int,
            'Is this correct?\t[y/n]', str,
            ('y', 'Y'), ('n', 'N'))
        write_data(self.id_path, self.id)

    # utility methods
    def string(self):
        return f'{self.tip.string()},{self.miles_traveled},{self.end_time}'
# todo: need to write function that allows the user to change data
