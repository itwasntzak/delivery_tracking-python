# //TODO: write functions to be able to undo ending shift and split on accident
# //TODO: make way to be able take multipule deliveries on one trip
# //TODO: add option to be able to start a second shift for the day (dif store)

from os import path, chdir

from delivery import Delivery
from extra_stop import Extra_Stop
from order import Order
from shift import shift_menu, Shift
from split import end_split
from utility import driving




chdir('delivery_tracking')
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
        else:
            delivery_object.resume()
    # check if split has been started
    elif path.exists(path.join('shift', 'split_start_time.txt')):
        end_split()
    else:
        shift_menu(shift_object)
