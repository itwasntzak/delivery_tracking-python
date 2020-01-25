# //TODO: write functions to be able to undo ending shift and split on accident
# //TODO: make way to be able take multipule deliveries on one trip
# //TODO: add option to be able to start a second shift for the day (dif store)

from os import path, chdir

<<<<<<< HEAD
from continuation import continuation
import extra_stop
import menu_options
import input_data
import shift
import utility


shift_start_time_path = path.join('shift', 'shift_start_time.txt')
shift_end_time_path = path.join('shift', 'shift_end_time.txt')
split_start_time_path = path.join('shift', 'split_start_time.txt')
split_end_time_path = path.join('shift', 'split_end_time.txt')


# //TODO: need to add logic for split_info.txt
def start():
    chdir('delivery_tracking')
    continuation()
    while True:
        # check if shift has started
        if not path.exists(shift_start_time_path):
            menu_options.new_shift()
        # check if shift has ended
        elif path.exists(shift_end_time_path):
            menu_options.ended_shift()
        # check if a split has or has not been started or ended
        elif path.exists(shift_start_time_path)\
                and not path.exists(split_start_time_path)\
                or path.exists(split_end_time_path):
            shift_menu()
            menu_options.continue_shift()
        # check if split has been started
        elif path.exists(shift_start_time_path)\
                and path.exists(split_start_time_path)\
                and not path.exists(split_end_time_path):
            menu_options.end_split()


def shift_menu():
    shift_object = shift.Shift()
    shift_object.start_time = datetime.strptime(
        utility.read_data(
            path.join('shift', 'shift_start_time.txt')),
        '%Y-%m-%d %H:%M:%S.%f')
    while True:
        user_choice = input_data.get_input(
            prompt='\nWhat would you like to do?'
                   '\n1 to start delivery '
                   '| 2 to end shift '
                   '| 3 to start split '
                   '| 4 to start an extra stop '
                   '| 0 for start menu\n',
            kind=int)
        if user_choice == 1:
            menu_options.start_delivery()
        elif user_choice == 2:
            shift.end_shift()
        elif user_choice == 3:
            shift.start_split()
        elif user_choice == 4:
            extra_stop_start_time_path = path.join(
                'shift', 'extra_stop_start_time.txt')
            utility.write_data(extra_stop_start_time_path, utility.now())
            # //TODO: write a menu option function for extra_stop, enter to cont
            extra_stop.extra_stop(shift_object)
        elif user_choice == 0:
            break
=======
from delivery import Delivery
from extra_stop import Extra_Stop
from order import Order
from shift import shift_menu, Shift
from split import end_split
from utility import driving




# chdir('delivery_tracking')
while True:
    shift_object = Shift()
    # check if shift has started
    if not path.exists(path.join('shift', 'shift_start_time.txt')):
        shift_object.start()
    else:
        shift_object.load()
        # check if end shift has been started
        if path.exists(path.join('shift', 'end_shift')):
            shift_object.resume_end_shift()
        # check if an extra stop has been started
        elif path.exists(path.join('shift', 'extra_stop')):
            extra_stop_object = Extra_Stop().load(shift_object)
            extra_stop_object.resume(shift_object)
    # check if delivery directory exist, if so delivery must be completed
    if path.exists(path.join('delivery')):
        delivery_object = Delivery().load(shift_object)
        # check if extra stop has been started while on delivery
        if path.exists(path.join('delivery', 'extra_stop')):
            extra_stop_object = Extra_Stop().load(delivery_object)
            extra_stop_object.resume(delivery_object)
        # check if order has been started
        elif path.exists(path.join('delivery', 'order')):
            order_object = Order().load()
            order_object.resume()
        # check if driving to address is in progress
        elif path.exists(path.join('delivery', 'driving-address')):
            driving(delivery_object, '\nDriving to address...', 'address')
>>>>>>> test
        else:
            delivery_object.resume()
    # check if split has been started
    elif path.exists(path.join('shift', 'split_start_time.txt')):
        end_split()
    else:
        shift_menu(shift_object)
