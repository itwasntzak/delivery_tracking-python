from processes.input_data import Input_Delivery

class Track_Delivery(Input_Delivery):
    def __init__(self, shift):
        from objects.shift import Shift
        if not isinstance(shift, Shift):
            # todo: need to write error message
            raise TypeError

        from objects.delivery import Delivery

        self.delivery = Delivery(shift)
        # get list of files and directory for delivery
        self.file_list = self.delivery.file_list()

    def end(self):
        from os import path

        # miles traveled
        if not path.exists(self.file_list['miles_traveled']):
            from utility.file import write
            # input and save miles traveled
            self.delivery.miles_traveled = self.distance()
            write(self.delivery.miles_traveled, self.file_list['miles_traveled'])
        else:
            from utility.file import Read
            # load miles traveled
            self.delivery.miles_traveled = Read(self.file_list['miles_traveled']).floats()

        # average speed
        if not path.exists(self.file_list['average_speed']):
            from utility.file import write
            # input and save average speed
            self.delivery.average_speed = self.average_speed()
            write(self.delivery.average_speed, self.file_list['average_speed'])
        else:
            from utility.file import Read
            # load average speed
            self.delivery.average_speed = Read(self.file_list['average_speed']).integer()

        # end time
        if not path.exists(self.file_list['end_time']):
            from utility.file import write
            from utility.utility import now
            # set and save end time
            self.delivery.end_time = self.time()
            write(self.delivery.end_time, self.file_list['end_time'])
        else:
            from utility.file import Read
            # load end time
            self.delivery.end_time = Read(self.file_list['end_time']).datetimes()

        # consolidate all delivery data to one file
        from processes.consolidate import delivery as\
            consolidate_delivery
        consolidate_delivery(self.delivery)

        # display time taken since starting delivery
        from resources.strings import Delivery__time_taken__display as\
            time_take_display
        from utility.utility import time_taken
        print(time_taken(
            self.delivery.start_time, self.delivery.end_time, time_take_display
            ))

        return self

    def start(self):
        from os import path

        # create directory to store files
        if not path.exists(self.file_list['directory']):
            from os import mkdir
            mkdir(self.file_list['directory'])

        # start time
        if not path.exists(self.file_list['start_time']):
            from utility.file import write
            from utility.utility import now
            # set and save start time for delivery
            self.delivery.start_time = self.time()
            write(self.delivery.start_time, self.file_list['start_time'])
        else:
            from utility.file import Read
            # load start time
            self.delivery.start_time = Read(self.file_list['start_time']).datetimes()

        # load orders
        from objects.order import Order
        if path.exists(Order(self.delivery).file_list()['completed_ids']):
            from processes.load import order as load_order
            from utility.file import Read
            self.delivery.order_ids =\
                Read(Order(self.delivery).file_list()['completed_ids']).integers()
            self.delivery.orders =\
                [load_order(self.delivery, id) for id in self.delivery.order_ids]

        # load extra stops
        from objects.extra_stop import Extra_Stop
        if path.exists(Extra_Stop(self.delivery, 0).file_list()['completed_ids']):
            from processes.load import delivery_extra_stop as load_extra_stop
            from utility.file import Read
            self.delivery.extra_stop_ids =\
                Read(Extra_Stop(self.delivery).file_list()['completed_ids']).integers()
            self.delivery.extra_stops = [load_extra_stop(self.delivery, id)
                for id in self.delivery.extra_stop_ids]

        return self
