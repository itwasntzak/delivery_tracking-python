

def order(order):
    from os import path

    order_files = order.file_list()

    # check if order tip file exists
    if path.exists(order_files['tip']):
        from utility.load import tip as load_tip
        order.tip = load_tip(order_files['tip'])
    else:
        from objects.tip import Tip
        from utility.start import tip as start_tip
        tip = Tip()
        tip.file_path = order_files['tip']
        order.tip = start_tip()

    # check if order miles traveled file exists
    if path.exists(order_files['miles']):
        from utility.file import Read
        self.miles_traveled = Read(order_files['miles']).floats()
    else:
        from resources.strings import Order__input_miles_traveled__prompt as\
            prompt
        from utility.file import write
        from utility.user_input import User_Input
        # input miles traveled
        order.miles_traveled = User_Input(prompt).miles_traveled()
        # save miles traveled data to file
        write(order.miles_traveled, order_files['miles'])

    # check if the end time file exists
    if path.exists(order_files['end_times']):
        from utility.file import Read
        order.end_time = Read(order_files['end_time']).datetimes()
    else:
        from utility.file import write
        from utility.utility import now
        # set current time as end time for order
        order.end_time = now()
        # save end time data to file
        write(order.end_time, order_files['end_times'])

    from utility.consolidate import order as consolidate_order
    consolidate_order()
    # display amount of time since delivery
    from resources.strings import Order__time_taken__display as display_text
    from utility.utility import time_taken
    time_taken(order.parent.start_time, order.end_time, display_text)
    return order
