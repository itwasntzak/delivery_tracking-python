
class Shift:
    def __init__(self, id):
        from datetime import datetime
        if not isinstance(id, type(datetime.now().date())):
            raise TypeError

        self.id = id

        self.delivery_ids = []
        self.deliveries = []
        self.extra_stop_ids = []
        self.extra_stops = []
        self.carry_out_tips = []
        self.start_time = None
        self.end_time = None
        self.distance = None
        self.fuel_economy = None
        self.vehicle_compensation = None
        self.device_compensation = None
        self.total_hours = None
        self.extra_tips_claimed = None
        self.split = None
        self.in_progress = True

    # retrieving tips methods
    def all_tips(self):
        # get order tips
        order_tips = [order.tip
                      for delivery in self.deliveries
                      for order in delivery.orders]
        # get carry out tips
        carry_out_tips = [tip for tip in self.carry_out_tips]
        # combine and return the two lists
        return order_tips + carry_out_tips
    
    def card_tips(self):
        # get order tips
        order_tips = [order.tip
                      for delivery in self.deliveries
                      for order in delivery.orders
                      if order.tip.card != 0.0]
        # get carry out tips
        carry_out_tips = [tip for tip in self.carry_out_tips if tip.card != 0.0]
        # combine and return the two lists
        return order_tips + carry_out_tips
    
    def cash_tips(self):
        # get order tips
        order_tips = [order.tip
                      for delivery in self.deliveries
                      for order in delivery.orders
                      if order.tip.cash != 0.0]
        # get carry out tips
        carry_out_tips = [tip for tip in self.carry_out_tips if tip.cash != 0.0]
        # combine and return the two lists
        return order_tips + carry_out_tips

    # add child objects methods
    def add_delivery(self, delivery):
        if not isinstance(delivery, Delivery):
            raise TypeError

        self.delivery_ids.append(delivery.id)
        self.deliveries.append(delivery)

    def add_extra_stop(self, extra_stop):
        if not isinstance(extra_stop, Extra_Stop):
            raise TypeError

        self.extra_stop_ids.append(extra_stop.id)
        self.extra_stops.append(extra_stop)

    # data changing methods
    def change_device_compensation(self):
        # todo: need to move string
        import os
        from utility.utility import to_money

        # get old value
        old_value = self.device_compensation
        # display old value to user
        print(f'\nCurrent device compensation amount: {to_money(old_value)}')
        # user inputs new value
        self.input_device_compensation()

        # save change
        # shift has been completed
        if os.path.exists(self.file_list()['info']):
            self.save()
        # shift is in progress
        elif os.path.exists(self.file_list()['device_comp']):
            from utility.file import write
            write(self.device_compensation, self.file_list()['device_comp'])

    def change_end_time(self):
        import os
        from utility.utility import Change_Datetime

        change_time = Change_Datetime(self.end_time).time()
        self.end_time = change_time.datetime

        # save change
        # shift has been completed
        if os.path.exists(self.file_list()['info']):
            self.save()
        # shift is in progress
        elif os.path.exists(self.file_list()['end_time']):
            from utility.file import write
            write(self.end_time, self.file_list()['end_time'])

    def change_extra_tips_claimed(self):
        # todo: need to move string
        import os

        # get old value
        old_value = self.extra_tips_claimed
        # display old value to user
        print(f'\nCurrent amount of extra tips claimed: {old_value}')
        # user inputs new value
        self.input_extra_tips_claimed()

        # save change
        # shift has been completed
        if os.path.exists(self.file_list()['info']):
            self.save()
        # shift is in progress
        elif os.path.exists(self.file_list()['extra_tips']):
            from utility.file import write
            write(self.extra_tips_claimed, self.file_list()['extra_tips'])

    def change_fuel_economy(self):
        # todo: need to move string
        import os

        # get old value
        old_value = self.fuel_economy
        # display old value to user
        print(f'\nCurrent amount fuel economy: {old_value}')
        # user inputs new value
        self.input_fuel_economy()

        # save change
        # shift has been completed
        if os.path.exists(self.file_list()['info']):
            self.save()
        # shift is in progress
        elif os.path.exists(self.file_list()['fuel_economy']):
            from utility.file import write
            write(self.fuel_economy, self.file_list()['fuel_economy'])

    def change_distance(self):
        # todo: need to move string
        import os

        # get old value
        old_value = self.distance
        # display old value to user
        print(f'\nCurrent amount miles traveled: {old_value}')
        # user inputs new value
        self.input_distance()

        # save change
        # shift has been completed
        if os.path.exists(self.file_list()['info']):
            self.save()
        # shift is in progress
        elif os.path.exists(self.file_list()['distance']):
            from utility.file import write
            write(self.distance, self.file_list()['distance'])

    def change_start_time(self):
        # todo: need to move string
        import os
        from utility.utility import Change_Datetime

        change_time = Change_Datetime(self.start_time).time()
        self.start_time = change_time.datetime

        # save change
        # shift has been completed
        if os.path.exists(self.file_list()['info']):
            self.save()
        # shift is in progress
        elif os.path.exists(self.file_list()['start_time']):
            from utility.file import write
            write(self.start_time, self.file_list()['start_time'])

    def change_total_hours(self):
        # todo: need to move string
        import os

        # get old value
        old_value = self.total_hours
        # display old value to user
        print(f'\nCurrent amount of total hours: {old_value}')
        # user inputs new value
        self.input_total_hours()

        # save change
        # shift has been completed
        if os.path.exists(self.file_list()['info']):
            self.save()
        # shift is in progress
        elif os.path.exists(self.file_list()['total_hours']):
            from utility.file import write
            write(self.total_hours, self.file_list()['total_hours'])

    def change_vehicle_compensation(self):
        # todo: need to move string
        import os

        # get old value
        old_value = self.vehicle_compensation
        # display old value to user
        print(f'\nCurrent amount of vehicle compensation: {old_value}')
        # user inputs new value
        self.input_vehicle_compensation()

        # save change
        # shift has been completed
        if os.path.exists(self.file_list()['info']):
            self.save()
        # shift is in progress
        elif os.path.exists(self.file_list()['vehicle_comp']):
            from utility.file import write
            write(self.vehicle_compensation, self.file_list()['vehicle_comp'])

    # data input methods
    def input_device_compensation(self):
        # todo: need to move string
        from resources.strings import Shift__device_compensation__prompt
        from utility.user_input import User_Input
        from utility.utility import add_newlines

        prompt = add_newlines(Shift__device_compensation__prompt)
        confirm_text = ' device compensation'
        self.device_compensation = User_Input(prompt).money(confirm_text)
    
    def input_extra_tips_claimed(self):
        # todo: need to move string
        from resources.strings import Shift__extra_tips_claimed__prompt
        from utility.user_input import User_Input
        from utility.utility import add_newlines

        prompt = add_newlines(Shift__extra_tips_claimed__prompt)
        confirm_text = ' extra claimed for taxes'
        self.extra_tips_claimed = User_Input(prompt).money(confirm_text)

    def input_fuel_economy(self):
        # todo: need to move string
        from resources.strings import Shift__fuel_economy__prompt
        from utility.user_input import User_Input
        from utility.utility import add_newlines

        prompt = add_newlines(Shift__fuel_economy__prompt)
        self.fuel_economy = User_Input(prompt).fuel_economy()

    def input_distance(self):
        # todo: need to move string
        from resources.strings import Shift__miles_traveled__prompt
        from utility.user_input import User_Input
        from utility.utility import add_newlines

        prompt = add_newlines(Shift__miles_traveled__prompt)
        self.distance = User_Input(prompt).distance()
    
    def input_total_hours(self):
        # todo: need to move string
        from resources.strings import Shift__total_hours__prompt
        from utility.user_input import User_Input
        from utility.utility import add_newlines

        prompt = add_newlines(Shift__total_hours__prompt)
        self.total_hours = User_Input(prompt).total_hours()
    
    def input_vehicle_compensation(self):
        # todo: need to move string
        from resources.strings import Shift__vehicle_compensation__prompt
        from utility.user_input import User_Input
        from utility.utility import add_newlines

        prompt = add_newlines(Shift__vehicle_compensation__prompt)
        confirm_text = ' vehicle compensation'
        self.vehicle_compensation = User_Input(prompt).money(confirm_text)

    # time setting methods
    def set_end_time(self):
        from datetime import datetime
        self.end_time = datetime.now()

    def set_start_time(self):
        from datetime import datetime
        self.start_time = datetime.now()

    # object loading/saving methods
    def load_completed(self):
        from processes.load import load_shift, load_carry_out_tips,\
            load_shift_deliveries, load_parent_extra_stops, load_split
        from os import path

        self.in_progress = False
        # load shift data
        self = load_shift(self)
        # load carry out tips
        if path.exists(self.file_list()['tips']):
            self = load_carry_out_tips(self)
        # load deliveries
        if path.exists(Delivery(self).file_list()['completed_ids']):
            self = load_shift_deliveries(self)
        # load extra stops
        if path.exists(Extra_Stop(self).file_list()['completed_ids']):
            self = load_parent_extra_stops(self)
        # load split
        if path.exists(Split(self).file_list()['info']):
            self.split = load_split(Split(self))
        return self

    def load_current(self):
        from processes.load import load_shift, load_carry_out_tips,\
            load_shift_deliveries, load_parent_extra_stops, load_split
        from os import path

        # load shift data
        self = load_shift(self)
        # load carry out tips
        if path.exists(self.file_list()['tips']):
            self = load_carry_out_tips(self)
        # load deliveries
        if path.exists(Delivery(self).file_list()['completed_ids']):
            self = load_shift_deliveries(self)
        # load extra stops
        if path.exists(Extra_Stop(self).file_list()['completed_ids']):
            self = load_parent_extra_stops(self)
        # load split
        if path.exists(Split(self).file_list()['info']):
            self.split = Split(self).load_completed()
        # load split start time
        elif path.exists(Split(self).file_list()['start_time']):
            self.split = Split(self).load_current()

        return self
    
    def save(self):
        from utility.file import write
        write(self.csv(), self.file_list()['info'])

    # utility methods
    def csv(self):
        return '{0},{1},{2},{3},{4},{5},{6},{7}'.format(
            self.distance, self.fuel_economy, self.vehicle_compensation,
            self.device_compensation, self.extra_tips_claimed,
            self.total_hours, self.start_time, self.end_time)

    def end(self):
        from processes.track import end_shift
        self = end_shift(self)
        return self

    def file_list(self):
        from os import path
        from resources.system_names import\
            end_time as end_time, start_time as start_time, distance,\
            Shift__carry_out_tips as carry_out_tip,\
            Shift__completed_ids as completed_ids,\
            Shift__completed_info as info_file,\
            Shift__device_compensation as device_compensation,\
            shifts_directory,\
            Shift__extra_tips_claimed as extra_claimed,\
            Shift__fuel_economy as fuel_economy,\
            Shift__total_hours as total_hours,\
            Shift__vehicle_compensation as vehicle_compensation,\
            data_directory

        directory =\
            path.join(data_directory, shifts_directory, f'{self.id}')

        return {
            'tips': path.join(directory, carry_out_tip),
            'completed_ids': path.join(data_directory, completed_ids),
            'device_compensation': path.join(directory, device_compensation),
            'directory': directory,
            'end_time': path.join(directory, end_time),
            'extra_tips_claimed': path.join(directory, extra_claimed),
            'fuel_economy': path.join(directory, fuel_economy),
            'info': path.join(directory, info_file),
            'distance': path.join(directory, distance),
            'start_time': path.join(directory, start_time),
            'total_hours': path.join(directory, total_hours),
            'vehicle_compensation': path.join(directory, vehicle_compensation)
        }

    def remove_id_from_file(self):
        from utility.file import Read, write
        from utility.utility import To_Datetime

        # get file path
        ids_file  = self.file_list()['completed_ids']
        # get list of shift ids
        id_list = [To_Datetime(id).from_date() for id in Read(ids_file).comma()]
        # create new list without current shifts id
        new_ids_list = [str(id.date()) for id in id_list if id != self.id]

        # check if any shift ids are left
        if len(new_ids_list) == 0:
            from os import remove
            remove(ids_file)
        elif len(new_ids_list) > 0:
            from utility.file import write
            write(','.join(new_ids_list), ids_file)

    def start(self):
        from processes.track import start_shift
        self = start_shift(self)
        return self

    def view(self):
        # todo: this isnt very readable, need to rethink this
        from datetime import datetime
        from utility.utility import to_money

        start_time = self.start_time.strftime('%I:%M:%S %p')

        # id, start time, # of deliveries
        view_parts = {
            'id': f'Date: {self.id}',
            'start_time': f'Started at: {start_time}',
            'deliveries': f'Number of deliveries: {len(self.deliveries)}'
        }

        # end time
        if isinstance(self.end_time, datetime):
            end_time = self.end_time.strftime('%I:%M:%S %p')
            view_parts['end_time'] = f'Ended at: {end_time}'

        # device compensation
        if isinstance(self.device_compensation, float)\
                  and self.device_compensation > 0.0:
            view_parts['device_comp'] =\
                f'Compensation for use of device: {to_money(self.device_compensation)}'

        # extra tips claimed
        if isinstance(self.extra_tips_claimed, float)\
                  and self.extra_tips_claimed > 0.0:
            view_parts['extra_tips_claimed'] =\
                f'Extra tips reported for taxes: {to_money(self.extra_tips_claimed)}'

        # fuel economy
        if isinstance(self.fuel_economy, float) and self.fuel_economy > 0.0:
            view_parts['fuel_economy'] =\
                f'Average fuel economy: {self.fuel_economy} mpg'

        # distance
        if isinstance(self.distance, float)\
                  and self.distance > 0.0:
            view_parts['distance']  =\
                f'Total miles traveled: {self.distance} miles'

        # total hours
        if isinstance(self.total_hours, float) and self.total_hours > 0.0:
            view_parts['total_hours'] =\
                f'Work recorded hours: {self.total_hours} hours'

        # vehicle compensation
        if isinstance(self.vehicle_compensation, float)\
                  and self.vehicle_compensation > 0.0:
            view_parts['vehicle_comp'] = 'Amount paid for vehicle usage: '\
                f'{to_money(self.vehicle_compensation)}'

        # carry out tips
        if len(self.carry_out_tips) > 0:
            tips_list = [tip.total_amount() for tip in self.carry_out_tips]
            view_parts['carry_out_tips'] =\
                f'Total made in carry out tips: {to_money(sum(tips_list))}'
        
        # total tips
        all_tips = [tip.total_amount() for tip in self.all_tips()]
        view_parts['total_tips'] = f'Total tips: {to_money(sum(all_tips))}'

        # card tips
        card_tips = [tip.card for tip in self.card_tips()]
        view_parts['card_tips'] = f'Card tips: {to_money(sum(card_tips))}'

        # cash tips
        cash_tips = [tip.cash for tip in self.cash_tips()]
        view_parts['cash_tips'] = f'Cash tips: {to_money(sum(cash_tips))}'

        # unknown tips

        # number of extra stops
        if len(self.extra_stops) > 0:
            view_parts['extra_stops'] =\
                f'Number of extra stops: {len(self.extra_stops)}'
        
        return view_parts


class Delivery:
    def __init__(self, shift, id=None):
        if not isinstance(shift, Shift):
            raise TypeError
        self.parent = shift

        if isinstance(id, int):
            self.id = id
        elif id is None:
            self.id = len(shift.deliveries)
        elif id:
            raise TypeError

        self.date = shift.id
        self.start_time = None
        self.end_time = None
        self.distance = None
        self.average_speed = None
        self.order_ids = []
        self.orders = []
        self.extra_stop_ids = []
        self.extra_stops = []
        self.in_progress = True

    # adding children methods
    def add_extra_stop(self, extra_stop):
        if not isinstance(extra_stop, Extra_Stop):
            raise TypeError

        self.extra_stop_ids.append(extra_stop.id)
        self.extra_stops.append(extra_stop)

    def add_order(self, order):
        if not isinstance(order, Order):
            raise TypeError(f'{order} is of type {type(order)}')

        self.order_ids.append(order.id)
        self.orders.append(order)

    # data changing methods
    def change_average_speed(self):
        # todo: need to move string
        import os

        # display current value to user
        if self.average_speed is not None:
            print(f'\nCurrent average speed: {self.average_speed} mph')
        # user inputs new value
        self.input_average_speed()

        # save change
        # completed delivery
        if os.path.exists(self.file_list()['info']):
            self.save()
        # delivery in progress
        elif os.path.exists(self.file_list()['average_speed']):
            from utility.file import write
            write(self.average_speed, self.file_list()['average_speed'])

    def change_end_time(self):
        import os
        from utility.utility import Change_Datetime

        change_time = Change_Datetime(self.end_time).time()
        self.end_time = change_time.datetime

        # save change
        # completed delivery
        if os.path.exists(self.file_list()['info']):
            self.save()
        # delivery is in progress
        elif os.path.exists(self.file_list()['end_time']):
            from utility.file import write
            write(self.end_time, self.file_list()['end_time'])

    def change_distance(self):
        # todo: need to moved string
        import os

        # display current value to user
        if self.average_speed is not None:
            print(f'\nCurrent miles traveled: {self.distance} miles')
        # user inputs new value
        self.input_distance()

        # save change
        # completed delivery
        if os.path.exists(self.file_list()['info']):
            self.save()
        # delivery in progress
        elif os.path.exists(self.file_list()['distance']):
            from utility.file import write
            write(self.distance, self.file_list()['distance'])

    def change_start_time(self):
        import os
        from utility.utility import Change_Datetime

        change_time = Change_Datetime(self.start_time).time()
        self.start_time = change_time.datetime

        # save change
        # completed delivery
        if os.path.exists(self.file_list()['info']):
            self.save()
        # delivery is in progress
        elif os.path.exists(self.file_list()['start_time']):
            from utility.file import write
            write(self.start_time, self.file_list()['start_time'])

    # data imput methods
    def input_average_speed(self):
        from resources.strings import Delivery__average_speed__prompt
        from utility.user_input import User_Input
        from utility.utility import add_newlines

        prompt = add_newlines(Delivery__average_speed__prompt)
        self.average_speed = User_Input(prompt).average_speed()

    def input_distance(self):
        from resources.strings import Delivery__miles_traveled_prompt
        from utility.user_input import User_Input
        from utility.utility import add_newlines

        prompt = add_newlines(Delivery__miles_traveled_prompt)
        self.distance = User_Input(prompt).distance()

    # time setting methods
    def set_end_time(self):
        from utility.utility import now
        self.end_time = now()

    def set_start_time(self):
        from utility.utility import now
        self.start_time = now()

    # object loading/saving methods
    def load_completed(self):
        from processes.load import\
            load_delivery,\
            load_delivery_orders,\
            load_parent_extra_stops
        from os import path

        self.in_progress = False
        # load delivery data
        self = load_delivery(self)
        # load orders
        if path.exists(Order(self).file_list()['completed_ids']):
            self = load_delivery_orders(self)
        # load extra stops
        if path.exists(Extra_Stop(self).file_list()['completed_ids']):
            self = load_parent_extra_stops(self)
        return self

    def load_current(self):
        from processes.load import\
            load_delivery,\
            load_delivery_orders,\
            load_parent_extra_stops
        from os import path

        # load delivery data
        self = load_delivery(self)
        # load orders
        if path.exists(Order(self).file_list()['completed_ids']):
            self = load_delivery_orders(self)
        # load extra stops
        if path.exists(Extra_Stop(self).file_list()['completed_ids']):
            self = load_parent_extra_stops(self)
        return self

    def save(self):
        from os import path
        from utility.file import write
        write(self.csv(), self.file_list()['info'])

    # utility methods
    def collection(self):
        return (self.distance, self.average_speed,
                self.start_time, self.end_time)

    def csv(self):
        return f'{self.distance},{self.average_speed},'\
               f'{self.start_time},{self.end_time}'

    def delete(self):
        # todo: should add confirmation before deleting everything
        from processes.delete import delete_delivery
        delete_delivery(self)

    def end(self):
        from processes.track import end_delivery
        self = end_delivery(self)

    def file_list(self):
        from os import path
        from resources.system_names import distance, start_time,\
            Delivery__completed_ids as completed_ids,\
            delivery_directory, end_time as end_time,\
            Delivery__average_speed as average_speed,\
            Delivery__info as info_file

        parent_directory = self.parent.file_list()['directory']
        directory = path.join(parent_directory, f'{self.id}')

        return {
            'completed_ids': path.join(parent_directory, completed_ids),
            'directory': directory,
            'average_speed': path.join(directory, average_speed),
            'end_time': path.join(directory, end_time),
            'info': path.join(directory, info_file),
            'distance': path.join(directory, distance),
            'start_time': path.join(directory, start_time)
        }

    def remove_id_from_file(self):
        import os

        # get file
        id_file = self.file_list()['completed_ids']

        if os.path.exists(id_file):
            from utility.file import Read, write
            # load delivery ids list
            delivery_ids = Read(id_file).integer_list()
            # remove id from list
            if self.id in delivery_ids:
                delivery_ids.pop(delivery_ids.index(self.id))
                # update ids file
                write(','.join([str(id) for id in delivery_ids]), id_file)

    def start(self):
        from processes.track import start_delivery
        self = start_delivery(self)

    def view(self):
        # todo: this is a big mess, need to rethink this
        from datetime import datetime

        view_parts = {'id': f'Delivery #: {self.id + 1}'}

        # total duration
        if isinstance(self.start_time, datetime) and\
                isinstance(self.end_time, datetime):
            from resources.strings import delivery__menu__texts as display_text
            view_parts['total_duration'] =\
                f"{display_text['total_duration']} {self.end_time - self.start_time}"

        # start time
        if isinstance(self.start_time, datetime):
            start_time = self.start_time.strftime('%I:%M:%S %p')
            view_parts['start_time'] = f'Started at: {start_time}'

        # number of orders
        view_parts['order_quantity'] = f'Number of orders: {len(self.orders)}'

        # order ids
        temp_string = 'Order I.D. #{}: '
        if len(self.order_ids) == 1:
            temp_string = temp_string.format('')
            temp_string += f'{self.order_ids[0]}'
            view_parts['order_ids'] = temp_string
        elif len(self.order_ids) > 1:
            temp_string = temp_string.format("'s")
            for value in range(len(self.order_ids) - 1):
                index = value
                id = self.order_ids[index]
                temp_string += f'{id}, '
            index += 1
            id = self.order_ids[index]
            temp_string += f'{id}'
            view_parts['order_ids'] = temp_string

        # distance
        if isinstance(self.distance, float)\
                  and self.distance > 0.0:
            view_parts['distance'] =\
                f'Total distance traveled for delivery: {self.distance} miles'

        # average speed
        if isinstance(self.average_speed, int) and self.average_speed > 0:
            view_parts['average_speed'] = f'Average speed for delivery: {self.average_speed} mph'

        # end time
        if isinstance(self.end_time, datetime):
            end_time = self.end_time.strftime('%I:%M:%S %p')
            view_parts['end_time'] = f'Completed at: {end_time}'

        # extra stops
        if len(self.extra_stops) > 0:
            view_parts['extra_stops'] =\
                f'Number of extra stops: {len(self.extra_stops)}'
        
        return view_parts


class Order:
    def __init__(self, delivery, id=None):
        if not isinstance(delivery, Delivery):
            from resources.error_messages import Order__class__wrong_parent_type
            message = Order__class__wrong_parent_type.format(type(delivery))
            raise TypeError(message)

        self.parent = delivery

        if isinstance(id, int):
            self.id = id
        elif id is None:
            self.id = 0
        elif id:
            from resources.error_messages import Order__class__wrong_id_type
            raise TypeError(Order__class__wrong_id_type.format(type(id)))

        self.date = delivery.date
        self.tip = Tip()
        self.distance = None
        self.end_time = None
        self.in_progress = True

    # data changing methods
    def change_id(self):
        # todo: need to write unittest for this
        import os
        from utility.file import Read, write

        # get old id
        original_order_id = self.id

        # user input new id
        print(f'\nCurrent I.D. #:{self.id}')
        self.input_id()

        # update completed ids file
        if os.path.exists(self.file_list()['completed_ids']):
            # get order id(s) currently in file
            order_ids = Read(self.file_list()['completed_ids']).integer_list()
            # check if old order id is in list, if so remove it
            if original_order_id in order_ids:
                order_ids[order_ids.index(original_order_id)] = self.id
            # write updated list to completed ids file
            write(','.join([str(id) for id in order_ids]),
                  self.file_list()['completed_ids'])

        # remove file
        if os.path.exists(self.file_list()['info']):
            os.remove(self.file_list()['info'])
        elif os.path.exists(self.file_list()['id']):
            os.remove(self.file_list()['id'])
        # rewrite file
        if self.in_progress is False:
            write(self.csv(), self.file_list()['info'])
        else:
            write(self.id, self.file_list()['id'])
        
        return original_order_id

    def change_distance(self):
        import os

        # display current value
        if self.distance is not None:
            print(f'Current distance traveled: {self.distance} miles')
        # user inputs new value
        self.input_distance()

        # save change
        # completed order
        if os.path.exists(self.file_list()['info']):
            self.save()
        # order in progress
        elif os.path.exists(self.file_list()['distance']):
            from utility.file import write
            write(self.distance, self.file_list()['distance'])

    def change_tip(self):
        import os
        from processes.revise import Revise_Tip

        # user revise's tip
        revise_tip = Revise_Tip(self.tip)
        # change current tip values to new tip values
        self.tip = revise_tip.tip

        # save change
        # completed order
        if os.path.exists(self.file_list()['info']):
            self.save()
        # order in progress
        elif os.path.exists(self.file_list()['tip']):
            from utility.file import write
            write(self.tip.csv(), self.file_list()['tip'])

    def change_end_time(self):
        import os
        from utility.utility import Change_Datetime

        change_time = Change_Datetime(self.end_time).time()
        self.end_time = change_time.datetime

        # save change
        # completed order
        if os.path.exists(self.file_list()['info']):
            self.save()
        # order in progress
        elif os.path.exists(self.file_list()['end_time']):
            from utility.file import write
            write(self.end_time, self.file_list()['end_time'])

    # data input methods
    def input_id(self):
        from resources.strings import Order__input_id__prompt
        from utility.user_input import User_Input
        from utility.utility import add_newlines

        self.id = User_Input(add_newlines(Order__input_id__prompt)).id()

    def input_distance(self):
        from resources.strings import Order__input_miles_traveled__prompt
        from utility.user_input import User_Input
        from utility.utility import add_newlines

        prompt = add_newlines(Order__input_miles_traveled__prompt)
        self.distance = User_Input(prompt).distance()

    def input_tip(self):
        self.tip = Tip().input_both()

    # time setting methods
    def set_end_time(self):
        from utility.utility import now
        self.end_time = now()

    def set_start_time(self):
        from utility.utility import now
        self.start_time = now()

    # object loading/saving methods
    def load_completed(self):
        from processes.load import load_order
        self.in_progress = False
        self = load_order(self)
        return self
    
    def load_current(self):
        from processes.load import load_order
        self = load_order(self)
        return self

    def save(self):
        from utility.file import write
        write(self.csv(), self.file_list()['info'])

    # utility methods
    def collection(self):
        return (self.tip.card, self.tip.cash, self.tip.unknown,
                self.distance, self.end_time)

    def csv(self):
        return f'{self.tip.csv()},{self.distance},{self.end_time}'

    def delete(self):
        from processes.delete import delete_order
        delete_order(self.order)

    def file_list(self):
        from os import path
        from resources.system_names import\
            end_time, distance, Order__completed_ids as completed_ids,\
            order_directory, Order__id as order_id, Tip__info as tip

        parent_directory = self.parent.file_list()['directory']
        directory = path.join(parent_directory, order_directory)

        return {
            'completed_ids': path.join(parent_directory, completed_ids),
            'info': path.join(parent_directory, f'{self.id}.txt'),
            'directory': directory,
            'end_time': path.join(directory, end_time),
            'id': path.join(directory, order_id),
            'distance': path.join(directory, distance),
            'tip': path.join(directory, tip)
        }

    def view(self):
        # id
        view_parts = {'id': f'Order I.D. #: {self.id}'}
        if self.distance:
            view_parts['distance'] =\
                f'Distance to address: {self.distance} miles'
        if self.end_time:
            formated_time = self.end_time.strftime('%I:%M:%S %p')
            view_parts['end_time'] = f'Completed at: {formated_time}'
        # tip
        tip_parts = self.tip.view()
        # total
        if 'total'in tip_parts.keys():
            view_parts['total'] = tip_parts['total']
        # card
        if 'card' in tip_parts.keys():
            view_parts['card'] = tip_parts['card']
        # cash
        if 'cash' in tip_parts.keys():
            view_parts['cash'] = tip_parts['cash']
        # unknown
        if 'unknown' in tip_parts.keys():
            view_parts['unknown'] = tip_parts['unknown']
        

        return view_parts

    def remove_id_from_file(self):
        import os

        id_file = self.file_list()['completed_ids']

        if os.path.exists(id_file):
            from utility.file import Read, write
            # load order ids list
            id_list = Read(id_file).integer()
            # remove id from list
            if self.id in id_list:
                id_list.pop(id_list.index(self.id))
                # update file without id
                write(','.join([str(id) for id in id_list]), id_file)

    def track(self):
        from processes.track import track_order
        self = track_order(self)


class Tip:
    def __init__(self, card=0.0, cash=0.0, unknown=0.0):
        try:
            self.card = float(card)
            self.cash = float(cash)
            self.unknown = float(unknown)
        except ValueError:
            print("ERROR:\tUse a number value for tip amounts.")
        
        self.evaluate()

    # data input methods
    def input_both(self):
        from resources.strings import\
            Tip__input_card__prompt as card_prompt,\
            Tip__input_cash__prompt as cash_prompt
        from utility.user_input import User_Input

        self.card = User_Input(card_prompt).card_tip()
        self.cash = User_Input(cash_prompt).cash_tip()
        self.evaluate()
        return self

    def input_card(self):
        from resources.strings import Tip__input_card__prompt as card_prompt
        from utility.user_input import User_Input

        self.card = User_Input(card_prompt).card_tip()
        self.evaluate()
        return self

    def input_cash(self):
        from resources.strings import Tip__input_cash__prompt as cash_prompt
        from utility.user_input import User_Input

        self.cash = User_Input(cash_prompt).cash_tip()
        self.evaluate()
        return self

    def input_unknown(self):
        from resources.strings import Tip__input_unknown__prompt as unknown_prompt
        from utility.user_input import User_Input

        self.unknown = User_Input(unknown_prompt).unknown_tip()
        self.evaluate()
        return self

    # utility methods
    def csv(self):
        return f'{self.card},{self.cash},{self.unknown}'

    def collection(self):
        return (self.card, self.cash, self.unknown)

    def evaluate(self):
        if self.card != 0.0:
            self.has_card = True
        else:
            self.has_card = False

        if self.cash != 0.0:
            self.has_cash = True
        else:
            self.has_cash = False

        if self.unknown != 0.0:
            self.has_unknown = True
        else:
            self.has_unknown = False

    def total_amount(self):
        return self.card + self.cash + self.unknown

    def view(self):
        from utility.utility import to_money
        view_parts = {}

        view_parts['total'] = f'Total tip: {to_money(self.total_amount())}'
        view_parts['card'] = f'Card tip: {to_money(self.card)}'
        view_parts['cash'] = f'Cash tip: {to_money(self.cash)}'
        view_parts['unknown'] = f'Unknown tip: {to_money(self.unknown)}'

        return view_parts


class Split:
    def __init__(self, shift):
        if not isinstance(shift, Shift):
            raise TypeError

        self.parent = shift
        self.date = shift.id
        self.start_time = None
        self.end_time = None
        self.distance = None
        self.in_progress = True

    # data changing methods
    def change_end_time(self):
        import os
        from utility.utility import Change_Datetime

        change_time = Change_Datetime(self.end_time).time()
        self.end_time = change_time.datetime

        # save change
        # completed
        if os.path.exists(self.file_list()['info']):
            self.save()
        # in progress
        elif os.path.exists(self.file_list()['end_time']):
            from utility.file import write
            write(self.end_time, self.file_list()['end_time'])

    def change_distance(self):
        import os

        # get old value
        old_value = self.distance
        # display old value to user
        print(f'\nCurrent miles traveled: {self.distance}')
        # user inputs new value
        self.input_distance()

        # save change
        # completed
        if os.path.exists(self.file_list()['info']):
            self.save()
        # in progress
        elif os.path.exists(self.file_list()['distance']):
            from utility.file import write
            write(self.distance, self.file_list()['distance'])

    def change_start_time(self):
        import os
        from utility.utility import Change_Datetime

        change_time = Change_Datetime(self.start_time).time()
        self.start_time = change_time.datetime

        # save change
        # completed
        if os.path.exists(self.file_list()['info']):
            self.save()
        # in progress
        elif os.path.exists(self.file_list()['start_time']):
            from utility.file import write
            write(self.start_time, self.file_list()['start_time'])

    # data input methods
    def input_distance(self):
        from utility.user_input import User_Input
        from utility.utility import add_newlines
        # todo: need to write prompt for distance and put it in resoursces file
        prompt = add_newlines('enter miles traveled')
        self.distance = User_Input(prompt).distance()

    # time setting methods
    def set_end_time(self):
        from utility.utility import now
        self.end_time = now()

    def set_start_time(self):
        from utility.utility import now
        self.start_time = now()

    # object loading/saving methods
    def load_completed(self):
        from processes.load import load_split
        self.in_progress = False
        self = load_split(self)
        return self

    def load_current(self):
        from processes.load import load_split
        self = load_split(self)
        return self

    def save(self):
        from utility.file import write
        write(self.csv(), self.file_list()['info'])

    # utility methods
    def csv(self):
        return f'{self.distance},{self.start_time},{self.end_time}'

    def end(self):
        from processes.track import end_split
        self = end_split(self)

    def file_list(self):
        from os import path
        from resources.system_names import\
            end_time, distance, split_directory, start_time, Split__info

        parent_directory = self.parent.file_list()['directory']
        directory = path.join(parent_directory, split_directory)

        return {
            'directory': directory,
            'end_time': path.join(directory, end_time),
            'info': path.join(parent_directory, Split__info),
            'distance': path.join(directory, distance),
            'start_time': path.join(directory, start_time)
        }

    def start(self):
        from processes.track import start_split
        self = start_split(self)
        return self

    def view(self):
        from datetime import datetime

        start_time = self.start_time.strftime('%I:%M:%S %p')
        view_parts = {'start_time': f'Started at: {start_time}'}

        if isinstance(self.distance, float):
            view_parts['distance'] =\
                f'Miles traveled: {self.distance} miles'

        if isinstance(self.end_time, datetime):
            end_time = self.end_time.strftime('%I:%M:%S %p')
            view_parts['end_time'] = f'Ended at: {end_time}'
        
        return view_parts


class Extra_Stop:
    def __init__(self, parent, id=None):
        if not isinstance(parent, (Shift, Delivery)):
            raise TypeError

        self.parent = parent

        if isinstance(parent, Shift):
            self.date = parent.id
        elif isinstance(parent, Delivery):
            self.date = parent.date


        if isinstance(id, int):
            self.id = id
        elif id is None:
            self.assign_id()
        else:
            raise TypeError

        self.location = None
        self.reason = None
        self.distance = None
        self.start_time = None
        self.end_time = None
        self.in_progress = True

    # data changing methods
    def change_end_time(self):
        import os
        from utility.utility import Change_Datetime

        change_time = Change_Datetime(self.end_time).time()
        self.end_time = change_time.datetime

        # save change
        # completed
        if os.path.exists(self.file_list()['info']):
            self.save()
        # in progress
        elif os.path.exists(self.file_list()['end_time']):
            from utility.file import write
            write(self.end_time, self.file_list()['end_time'])

    def change_location(self):
        import os

        # get old location
        old_location = self.location
        # display old location to user
        print(f'\nCurrent location: {self.location}')
        # user inputs new location
        self.input_location()

        # save change
        # completed
        if os.path.exists(self.file_list()['info']):
            self.save()
        # in progress
        elif os.path.exists(self.file_list()['location']):
            from utility.file import write
            write(self.location, self.file_list()['location'])

    def change_distance(self):
        import os

        # get old distance
        old_reason = self.distance
        # display old distance to user
        print(f'\nCurrent miles traveled: {self.distance}')
        # user inputs new distance
        self.input_distance()

        # save change
        # completed
        if os.path.exists(self.file_list()['info']):
            self.save()
        # in progress
        elif os.path.exists(self.file_list()['distance']):
            from utility.file import write
            write(self.distance, self.file_list()['distance'])

    def change_reason(self):
        import os

        # get old reason
        old_reason = self.reason
        # display old reason to user
        print(f'\nCurrent reason: {self.reason}')
        # user inputs new reason
        self.input_reason()

        # save change
        # completed
        if os.path.exists(self.file_list()['info']):
            self.save()
        # in progress
        elif os.path.exists(self.file_list()['reason']):
            from utility.file import write
            write(self.reason, self.file_list()['reason'])

    def change_start_time(self):
        import os
        from utility.utility import Change_Datetime

        change_time = Change_Datetime(self.start_time).time()
        self.start_time = change_time.datetime

        # save change
        # completed
        if os.path.exists(self.file_list()['info']):
            self.save()
        # in progress
        elif os.path.exists(self.file_list()['start_time']):
            from utility.file import write
            write(self.start_time, self.file_list()['start_time'])

    # data input methods
    def input_location(self):
        from resources.strings import Extra_Stop__location__prompt
        from utility.user_input import User_Input
        from utility.utility import add_newlines

        prompt = add_newlines(Extra_Stop__location__prompt)
        self.location = User_Input(prompt).location()

    def input_distance(self):
        from resources.strings import Extra_Stop__miles_traveled__prompt
        from utility.user_input import User_Input
        from utility.utility import add_newlines

        prompt = add_newlines(Extra_Stop__miles_traveled__prompt)
        self.distance = User_Input(prompt).distance()

    def input_reason(self):
        from resources.strings import Extra_Stop__reason__prompt
        from utility.user_input import User_Input
        from utility.utility import add_newlines

        prompt = add_newlines(Extra_Stop__reason__prompt)
        self.reason = User_Input(prompt).reason()

    # time setting methods
    def set_end_time(self):
        from utility.utility import now
        self.end_time = now()

    def set_start_time(self):
        from utility.utility import now
        self.start_time = now()

    # object loading/saving methods
    def load_completed(self):
        from processes.load import load_extra_stop
        self.in_progress = False
        self = load_extra_stop(self)
        return self

    def load_current(self):
        from processes.load import load_extra_stop
        self = load_extra_stop(self)
        return self

    def save(self):
        from utility.file import write
        write(self.nlsv(), self.file_list()['info'])

    # utility methods
    def assign_id(self):
        from os import path

        self.id = 0

        if path.exists(self.file_list()['running_id']):
            from utility.file import Read
            self.id = Read(self.file_list()['running_id']).integer()

        return self

    def collection(self):
        from objects import Shift

        if isinstance(self.parent, Shift):
            return (self.location, self.reason, self.distance,
                    self.end_time, self.start_time)

        return (self.location, self.reason, self.distance, self.end_time)

    def csv(self):
        # shift parent
        if isinstance(self.parent, Shift):
            return f'{self.location},{self.reason},{self.distance},'\
                   f'{self.start_time},{self.end_time}'
        # delivery parent
        elif isinstance(self.parent, Delivery):
            return f'{self.location},{self.reason},{self.distance},'\
                   f'{self.end_time}'

    def file_list(self):
        from os import path
        from resources.system_names import\
            end_time, extra_stop_directory, distance, start_time,\
            Extra_Stop__completed_ids as completed_ids,\
            Extra_Stop__info as info_file,\
            Extra_Stop__location as location, Extra_Stop__reason as reason,\
            Extra_Stop__running_id as running_id,\
            shifts_directory, data_directory
        from utility.utility import now

        parent_directory = self.parent.file_list()['directory']
        shift_directory =\
            path.join(data_directory, shifts_directory, f'{now().date()}')

        directory = path.join(parent_directory, extra_stop_directory)

        return {
            'running_id': path.join(shift_directory, running_id),
            'completed_ids': path.join(parent_directory, completed_ids),
            'info': path.join(parent_directory, info_file.format(self.id)),
            'directory': directory,
            'end_time': path.join(directory, end_time),
            'location': path.join(directory, location),
            'distance': path.join(directory, distance),
            'reason': path.join(directory, reason),
            'start_time': path.join(directory, start_time)
        }

    def nlsv(self):
        # shift parent
        if isinstance(self.parent, Shift):
            return f'{self.location}\n'\
                   f'{self.reason}\n'\
                   f'{self.distance}\n'\
                   f'{self.start_time}\n'\
                   f'{self.end_time}'
        # delivery parent
        elif isinstance(self.parent, Delivery):
            return f'{self.location}\n'\
                   f'{self.reason}\n'\
                   f'{self.distance}\n'\
                   f'{self.end_time}'

    def track(self):
        from processes.track import track_extra_stop
        self = track_extra_stop(self)

    def view(self):
        from datetime import datetime

        end_time = self.end_time.strftime('%I:%M:%S %p')

        view_parts = {
            'id': f'Extra stop id #: {self.id + 1}',
            'location': f'Location: {self.location.capitalize()}',
            'reason': f'Reason: {self.reason.capitalize()}',
            'distance': f'Distance to extra stop: {self.distance} miles',
            'end_time': f'Extra stop was completed at: {end_time}'
        }

        # shift parent
        if isinstance(self.start_time, datetime):
            view_parts['start_time'] = self.start_time.strftime('%I:%M:%S %p')
        
        return view_parts
