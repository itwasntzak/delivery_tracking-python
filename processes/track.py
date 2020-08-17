
class Track_Shift:
    def __init__(self):
        from objects import Shift
        from utility.utility import now

        self.shift = Shift(now().date())
        self.file_list = self.shift.file_list()
    
    def end(self):
        from os import path
        from processes.consolidate import shift as consolidate_shift
        from resources.strings import Shift__end___enter_to_continue__display as\
            shift_ended
        from utility.utility import enter_to_continue
        from utility.file import Read, write

        # end time
        if not path.exists(self.file_list['end_time']):
            # set
            self.shift.input_end_time()
            # save
            write(self.shift.end_time, self.file_list['end_time'])
        else:
            # load
            self.shift.end_time = Read(self.file_list['end_time']).datetimes()

        # miles traveled
        if not path.exists(self.file_list['miles_traveled']):
            # input
            self.shift.input_miles_traveled()
            # save
            write(self.shift.miles_traveled, self.file_list['miles_traveled'])
        else:
            # load
            self.shift.miles_traveled = Read(self.file_list['miles_traveled']).floats()

        # fuel economy
        if not path.exists(self.file_list['fuel_economy']):
            # input
            self.shift.input_fuel_economy()
            # save
            write(self.shift.fuel_economy, self.file_list['fuel_economy'])
        else:
            # load
            self.shift.fuel_economy = Read(self.file_list['fuel_economy']).floats()

        # vehical compensation
        if not path.exists(self.file_list['vehical_compensation']):
            # input
            self.shift.input_vehical_complensation()
            # save
            write(self.shift.vehical_complensation,
                  self.file_list['vehical_compensation'])
        else:
            # load
            self.shift.vehical_compensation =\
                Read(self.file_list['vehical_compensation']).floats()

        # device compensation
        if not path.exists(self.file_list['device_compensation']):
            # input
            self.shift.input_device_compensation()
            # save
            write(self.shift.device_compensation, self.file_list['device_compensation'])
        else:
            # load
            self.shift.device_compensation =\
                Read(self.file_list['device_compensation']).floats()

        # total hours
        if not path.exists(self.file_list['total_hours']):
            # input
            self.shift.input_total_hours()
            # save
            write(self.shift.total_hours, self.file_list['total_hours'])
        else:
            # load
            self.shift.total_hours = Read(self.file_list['total_hours']).floats()

        # extra tips claimed
        if not path.exists(self.file_list['extra_tips_claimed']):
            # input
            self.shift.input_extra_tips_claimed()
            # save
            write(self.shift.extra_tips_claimed, self.file_list['extra_tips_claimed'])
        else:
            # load
            self.shift.extra_tips_claimed =\
                Read(self.file_list['extra_tips_claimed']).floats()

        # consolidate indavidual files into one
        consolidate_shift(shift)
        # inform user shift was successfully
        enter_to_continue(shift_ended)
        return self
    
    def start(self):
        from os import mkdir
        from resources.strings import Shift__start__enter_to_continue__display as\
            shift_started
        from utility.file import write
        from utility.utility import enter_to_continue, now

        self.shift.input_start_time()
        mkdir(self.file_list['directory'])
        write(self.shift.start_time, self.file_list['start_time'])
        enter_to_continue(shift_started)
        return self


class Track_Delivery:
    def __init__(self, shift):
        from objects import Shift
        if not isinstance(shift, Shift):
            # todo: need to write error message
            raise TypeError

        from objects import Delivery

        self.delivery = Delivery(shift)
        # get list of files and directory for delivery
        self.file_list = self.file_list()

    def end(self):
        from os import path
        from processes.consolidate import delivery as consolidate_delivery
        from resources.strings import Delivery__time_taken__display as\
            time_take_display
        from utility.file import Read, write
        from utility.utility import time_taken

        # miles traveled
        if not path.exists(self.file_list['miles_traveled']):
            # input
            self.delivery.input_distance()
            # save
            write(self.delivery.miles_traveled, self.file_list['miles_traveled'])
        else:
            # load
            self.delivery.miles_traveled = Read(self.file_list['miles_traveled']).floats()

        # average speed
        if not path.exists(self.file_list['average_speed']):
            # input
            self.delivery.input_average_speed()
            # save
            write(self.delivery.average_speed, self.file_list['average_speed'])
        else:
            # load
            self.delivery.average_speed = Read(self.file_list['average_speed']).integer()

        # end time
        if not path.exists(self.file_list['end_time']):
            # set
            self.end_time()
            # save
            write(self.delivery.end_time, self.file_list['end_time'])
        else:
            # load
            self.delivery.end_time = Read(self.file_list['end_time']).datetimes()

        # consolidate all delivery data to one file
        consolidate_delivery(self)
        # display time taken since starting delivery
        print(time_taken(self.start_time, self.end_time, time_take_display))

        return self

    def start(self):
        from objects import Extra_Stop, Order
        from os import path
        from utility.file import Read, write

        # create directory to store files
        if not path.exists(self.file_list['directory']):
            from os import mkdir
            mkdir(self.file_list['directory'])

        # start time
        if not path.exists(self.file_list['start_time']):
            # set
            self.delivery.input_start_time()
            # save
            write(self.delivery.start_time, self.file_list['start_time'])
        else:
            # load
            self.delivery.start_time = Read(self.file_list['start_time']).datetimes()

        # orders
        if path.exists(Order(self).file_list()['completed_ids']):
            from processes.load import order as load_order
            # load order ids
            self.delivery.order_ids =\
                Read(Order(self).file_list()['completed_ids']).integers()
            # load order objects
            self.delivery.orders = [load_order(self, id) for id in self.delivery.order_ids]

        # extra stops
        if path.exists(Extra_Stop(self, 0).file_list()['completed_ids']):
            from processes.load import delivery_extra_stop as load_extra_stop
            # load extra stop ids
            self.delivery.extra_stop_ids =\
                Read(Extra_Stop(self).file_list()['completed_ids']).integers()
            # load extra stop objects
            self.delivery.extra_stops =\
                [load_extra_stop(self, id) for id in self.delivery.extra_stop_ids]

        return self


class Track_Order:
    def __init__(self, delivery):
        from objects import Delivery
        if not isinstance(delivery, Delivery):
            # todo: need to write error message
            raise TypeError

        self.order = Order(delivery)
        # get list of files for order input
        self.file_list = self.order.file_list()
    
    def start(self):
        from objects import Order
        from os import mkdir, path
        from processes.consolidate import order as consolidate_order
        from resources.strings import\
            Order__time_taken__display as order_ended
        from utility.file import Read, write
        from utility.utility import time_taken

        # make directory to store order files
        if not path.exists(order_files['directory']):
            mkdir(order_files['directory'])

        # id
        if not path.exists(order_files['id']):
            # input
            self.order.input_id()
            # save
            write(self.order.id, order_files['id'])
        else:
            # load
            self.order.id = Read(order_files['id']).integer()

        # tip
        if not path.exists(order_files['tip']):
            # input 
            self.order.input_tip()
            # save
            write(self.order.tip.csv(), order_files['tip'])
        else:
            # load
            from processes.load import tip as load_tip
            self.order.tip = load_tip(order_files['tip'])

        # miles traveled
        if not path.exists(order_files['miles_traveled']):
            # input
            self.order.input_miles_traveled()
            # save
            write(self.order.miles_traveled, order_files['miles_traveled'])
        else:
            # load
            self.order.miles_traveled = Read(order_files['miles_traveled']).floats()

        # end time
        if not path.exists(order_files['end_time']):
            # set
            self.order.input_end_time()
            # save
            write(self.end_time, order_files['end_time'])
        else:
            # load
            self.end_time = Read(order_files['end_time']).datetimes()

        # consolidate order files into one file
        consolidate_order(self.order)
        # display time taken since delivery was started
        time_taken(self.order.parent.start_time, self.order.end_time, order_ended)
        # return completed order
        return self.order


class Track_Split:
    def __init__(self, shift):
        from objects import Shift
        if not isinstance(shift, Shift):
            # todo: need to write this error message
            raise TypeError

        from objects import Split
        self.split = Split(shift)
        self.file_list = self.split.file_list()

    def end(self):
        from os import path
        from processes.consolidate import split as consolidate_split
        from utility.file import Read, write

        # load start time
        self.split.start_time = Read(self.file_list['start_time']).datetimes()

        # miles traveled
        if not path.exists(self.file_list['miles_traveled']):
            # input
            self.split.input_miles_traveled()
            # save
            write(self.split.miles_traveled, self.file_list['miles_traveled'])
        else:
            # load
            self.split.miles_traveled = Read(self.file_list['miles_traveled']).floats()

        # end time
        if not path.exists(self.file_list['end_time']):
            # set
            self.split.input_end_time()
            # save
            write(self.split.end_time, self.file_list['end_time'])
        else:
            # load
            self.split.end_time = Read(self.file_list['end_time']).datetimes()

        # consolidate individual files into one file
        consolidate_split(self.split)
        return self

    def start(self):
        from os import path
        from resources.strings import Split__start__enter_to_continue as prompt
        from utility.utility import enter_to_continue

        # directory
        if not path.exists(self.file_list()['directory']):
            from os import mkdir
            # create directory
            mkdir(self.file_list()['directory'])
        # start time
        if not path.exists(self..file_list()['start_time']):
            from utility.file import write
            # set and save
            self.split.input_start_time()
            write(self.split.start_time,  self.file_list()['start_time'])

        enter_to_continue(prompt)
        return self


class Track_Extra_Stop:
    def __init__(self, parent):
        from objects import Extra_Stop

        self.extra_stop = Extra_Stop(parent)
        self.file_list = extra_stop.file_list()

    def main(self):
        from os import path
        from utility.file import Read, write
        from utility.user_input import User_Input

        # id
        self.extra_stop.assign_id()

        # location
        if not path.exists(self.file_list['location']):
            # input
            self.extra_stop.input_location()
            # save
            write(self.extra_stop.location, self.file_list['location'])
        else:
            # load
            self.extra_stop.location = Read(self.file_list['location'])

        # reason
        if not path.exists(self.file_list['reason']):
            # input
            self.extra_stop.input_reason()
            # save
            write(self.extra_stop.reason, self.file_list['reason'])
        else:
            # load
            self.extra_stop.reason = Read(self.file_list['reason'])

        # miles traveled
        if not path.exists(self.file_list['miles_traveled']):
            # input
            self.extra_stop.input_miles_traveled()
            # save
            write(self.extra_stop.miles_traveled, self.file_list['miles_traveled'])
        else:
            # load
            self.extra_stop.miles_traveled = Read(self.file_list['miles_traveled']).floats()

        # end time
        if not path.exists(self.file_list['end_time']):
            # set
            self.extra_stop.input_end_time()
            # save
            write(self.extra_stop.end_time, self.file_list['end_time'])
        else:
            # load
            self.extra_stop.end_time = Read(self.file_list['end_time']).datetimes()

        return self

    def shift(self):
        from os import path
        from processes.consolidate import shift_extra_stop as\
            consolidate_extra_stop
        from resources.strings import Extra_Stop__time_taken__display as\
            time_taken_display
        from utility.file import Read, write
        from utility.utility import time_taken


        # directory
        if not path.exists(self.file_list['directory']):
            from os import mkdir
            mkdir(self.file_list['directory'])

        # start time
        if not path.exists(self.file_list['start_time']):
            # set
            self.extra_stop.input_start_time()
            # save
            write(self.extra_stop.start_time, self.file_list['start_time'])
        else:
            # load
            self.extra_stop.start_time = Read(self.file_list['start_time']).datetimes()

        self.main()

        # consolidate all files into one
        consolidate_extra_stop(self.extra_stop)
        # display time since starting delivery
        time_taken(self.extra_stop.start_time, self.extra_stop.end_time,
            time_taken_display)

        return self

    def delivery(self):
        from os import path
        from processes.consolidate import delivery_extra_stop as\
            consolidate_extra_stop
        from resources.strings import Extra_Stop__time_taken__display as\
            time_taken_display
        from utility.utility import time_taken

        # directory
        if not path.exists(file_list['directory']):
            from os import mkdir
            mkdir(file_list['directory'])

        self.main()

        # consolidate all files into one
        consolidate_extra_stop(self.extra_stop)
        # display time since starting delivery
        time_taken(self.extra_stop.parent.start_time, self.extra_stop.end_time,
            time_taken_display)

        return self
