# //TODO: write functions to be able to undo ending shift and split on accident
# //TODO: make way to be able take multipule deliveries on one trip
# //TODO: add option to be able to start a second shift for the day (dif store)

from os import path, chdir

from delivery import Delivery
from extra_stop import Extra_Stop
from order import Order
from shift import shift_menu, Shift
from split import Split
from utility import driving




# chdir('delivery_tracking')
while True:
    shift = Shift()
    # check if shift has started
    if not path.exists(path.join('shift', 'shift_start_time.txt')):
        shift.start()
    else:
        shift.load()
        # check if end shift has been started
        if path.exists(path.join('shift', 'end_shift')):
            shift.resume_end()
        # check if an extra stop has been started
        elif path.exists(path.join('shift', 'extra_stop')):
            extra_stop = Extra_Stop().load(shift)
            extra_stop.resume(shift)
    # check if delivery directory exist, if so delivery must be completed
    if path.exists(path.join('delivery')):
        delivery = Delivery().load(shift)
        # check if extra stop has been started while on delivery
        if path.exists(path.join('delivery', 'extra_stop')):
            extra_stop = Extra_Stop().load(delivery)
            extra_stop.resume(delivery)
        # check if order has been started
        elif path.exists(path.join('delivery', 'order')):
            order = Order().load()
            order.resume()
        # check if driving to address is in progress
        elif path.exists(path.join('delivery', 'driving-address')):
            driving(delivery, '\nDriving to address...', 'address')
        else:
            delivery.resume()
    # check if split has been started
    elif path.exists(path.join('shift', 'split_start_time.txt')):
        split = Split().end()
    else:
        shift_menu(shift)
