
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
        self.miles_traveled = None
        self.fuel_economy = None
        self.vehicle_compensation = None
        self.device_compensation = None
        self.total_hours = None
        self.extra_tips_claimed = None
        self.split = None

    def csv(self):
        return '{0},{1},{2},{3},{4},{5},{6},{7}'.format(
            self.miles_traveled, self.fuel_economy, self.vehicle_compensation,
            self.device_compensation, self.extra_tips_claimed,
            self.total_hours, self.start_time, self.end_time)

    def file_list(self):
        from os import path
        from resources.system_names import\
            end_time as end_time, start_time as start_time,\
            miles_traveled as miles_traveled,\
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
            'miles_traveled': path.join(directory, miles_traveled),
            'start_time': path.join(directory, start_time),
            'total_hours': path.join(directory, total_hours),
            'vehicle_compensation': path.join(directory, vehicle_compensation)
        }

    def view(self):
        from datetime import datetime

        start_time = self.start_time.strftime('%I:%M:%S %p')

        view_parts = {
            'id': f'Shift date:\t{self.id}',
            'start_time': f'Shift was started at:\t{start_time}',
            'deliveries': f'Number of deliveries:\t{len(self.deliveries)}'
        }

        if isinstance(self.end_time, datetime):
            end_time = self.end_time.strftime('%I:%M:%S %p')
            view_parts['end_time'] = f'Shift was ended at:\t{end_time}'

        if isinstance(self.device_compensation, float)\
                  and self.device_compensation > 0.0:
            view_parts['device_comp'] =\
                f'Compensation for use of device\t${self.device_compensation}'

        if isinstance(self.extra_tips_claimed, float)\
                  and self.extra_tips_claimed > 0.0:
            view_parts['extra_tips_claimed'] =\
                f'Extra tips reported for taxes:\t${self.extra_tips_claimed}'

        if isinstance(self.fuel_economy, float) and self.fuel_economy > 0.0:
            view_parts['fuel_economy'] =\
                f'Average fuel economy:\t{self.fuel_economy} mpg'

        if isinstance(self.miles_traveled, float)\
                  and self.miles_traveled > 0.0:
            view_parts['distance']  =\
                f'Total distance traveled:\t{self.miles_traveled} miles'

        if isinstance(self.total_hours, float) and self.total_hours > 0.0:
            view_parts['total_hours'] =\
                f'Work recorded hours:\t{self.total_hours} hours'

        if isinstance(self.vehicle_compensation, float)\
                  and self.vehicle_compensation > 0.0:
            view_parts['vehicle_comp'] = 'Amount paid for vehicle usage:\t'\
                f'${self.vehicle_compensation}'

        if len(self.carry_out_tips) > 0:
            tips_list = [tip.total_amount() for tip in self.carry_out_tips]
            view_parts['carry_out_tips'] =\
                f'Total made in carry out tips:\t${sum(tips_list)}'

        if len(self.extra_stops) > 0:
            view_parts['extra_stops'] =\
                f'Number of extra stops:\t{len(self.extra_stops)}'
        
        return view_parts

    def all_tips(self):
        tips = []
        for delivery in self.deliveries:
            for order in delivery.orders:
                tips.append(order.tip)
        
        for tip in self.carry_out_tips:
            tips.append(tip)

        return tips
    
    def card_tips(self):
        tips = []
        for delivery in self.deliveries:
            for order in delivery.orders:
                if order.tip.card != 0.0:
                    tips.append(order.tip)
        
        for tip in self.carry_out_tips:
            if tip.card != 0.0:
                tips.append(tip)

        return tips
    
    def cash_tips(self):
        tips = []
        for delivery in self.deliveries:
            for order in delivery.orders:
                if order.tip.cash != 0.0:
                    tips.append(order.tip)
        
        for tip in self.carry_out_tips:
            if tip.cash != 0.0:
                tips.append(tip)

        return tips

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

    def input_device_compensation(self):
        from resources.strings import Shift__device_compensation__prompt as\
                prompt
        from utility.user_input import User_Input
        self.device_compensation = User_Input(prompt).money(' device compensation')
    
    def input_extra_tips_claimed(self):
        from resources.strings import Shift__extra_tips_claimed__prompt as\
                prompt
        from utility.user_input import User_Input
        self.extra_tips_claimed = User_Input(prompt).money(' extra claimed for taxes')

    def input_fuel_economy(self):
        from resources.strings import Shift__fuel_economy__prompt as prompt
        from utility.user_input import User_Input
        self.fuel_economy = User_Input(prompt).fuel_economy()

    def input_miles_traveled(self):
        from resources.strings import Shift__miles_traveled__prompt as prompt
        from utility.user_input import User_Input
        self.miles_traveled = User_Input(prompt).miles_traveled()
    
    def input_total_hours(self):
        from resources.strings import Shift__total_hours__prompt as prompt
        from utility.user_input import User_Input
        self.total_hours = User_Input(prompt).total_hours()
    
    def input_vehicle_compensation(self):
        from resources.strings import Shift__vehicle_compensation__prompt as\
                prompt
        from utility.user_input import User_Input
        self.vehicle_compensation = User_Input(prompt).money(' vehicle compensation')

    def set_end_time(self):
        from datetime import datetime
        self.end_time = datetime.now()

    def set_start_time(self):
        from datetime import datetime
        self.start_time = datetime.now()

    def end(self):
        from processes.track import end_shift
        self = end_shift(self)

    def load_completed(self):
        from processes.load import load_completed_shift
        self = load_completed_shift(self)

    def load_current(self):
        from processes.load import load_current_shift
        self = load_current_shift(self)

    def start(self):
        from processes.track import start_shift
        self = start_shift(self)

    def remove_id_from_file(self):
        # todo: this needs to be tested and reworked
        from os import remove
        from utility.file import Read, write
        from utility.utility import To_Datetime

        ids_file  = self.file_list()['completed_ids']

        id_list = [id for id in Read(ids_file).comma() if id != f'{self.id}']
        comma_number = len(id_list) - 1

        new_ids_list = ''
        for value in range(comma_number):
            new_ids_list += id_list[value] + ','
        new_ids_list += id_list[-1]

        if len(id_list) == 0:
            remove(ids_file)
        elif len(id_list) > 0:
            write(new_ids_list, ids_file)


class Delivery:
    # cnsd: use commas to split delivery data, use newline to split multi-delv
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

        self.start_time = None
        self.end_time = None
        self.miles_traveled = None
        self.average_speed = None
        self.order_ids = []
        self.orders = []
        self.extra_stop_ids = []
        self.extra_stops = []

    def csv(self):
        return f'{self.miles_traveled},{self.average_speed},'\
               f'{self.start_time},{self.end_time}'

    def file_list(self):
        from os import path
        from resources.system_names import\
            Delivery__completed_ids as completed_ids,\
            delivery_directory, end_time as end_time,\
            Delivery__average_speed as average_speed,\
            Delivery__info as info_file,\
            miles_traveled as miles_traveled,\
            start_time as start_time

        parent_directory = self.parent.file_list()['directory']
        directory = path.join(parent_directory, f'{self.id}')

        return {
            'completed_ids': path.join(parent_directory, completed_ids),
            'directory': directory,
            'average_speed': path.join(directory, average_speed),
            'end_time': path.join(directory, end_time),
            'info': path.join(directory, info_file),
            'miles_traveled': path.join(directory, miles_traveled),
            'start_time': path.join(directory, start_time)
        }

    def view(self):
        from datetime import datetime

        view_parts = {'id': f'Delivery #:\t{self.id + 1}'}

        if isinstance(self.start_time, datetime) and\
                isinstance(self.end_time, datetime):
            from resources.strings import delivery__menu__texts as display_text
            from utility.utility import time_taken
            view_parts['time_taken'] =\
                time_taken(self.start_time,
                           self.end_time,
                           display_text['total_duration'])

        if isinstance(self.start_time, datetime):
            start_time = self.start_time.strftime('%I:%M:%S %p')
            view_parts['start_time'] = f'Started at:\t{start_time}'

        view_parts['order_quantity'] = f'Number of orders:\t{len(self.orders)}'

        temp_string = 'Order I.D. #{}:\t'
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

        if isinstance(self.miles_traveled, float)\
                  and self.miles_traveled > 0.0:
            view_parts['distance'] =\
                f'Total distance traveled for delivery:\t{self.miles_traveled} miles'

        if isinstance(self.average_speed, int) and self.average_speed > 0:
            view_parts['average_speed'] = f'Average speed for delivery:\t{self.average_speed} mph'

        if isinstance(self.end_time, datetime):
            end_time = self.end_time.strftime('%I:%M:%S %p')
            view_parts['end_time'] = f'Completed at:\t{end_time}'
        
        if len(self.extra_stops) > 0:
            view_parts['extra_stops'] = f'Number of extra stops:\t{len(self.extra_stops)}'
        
        return view_parts

    def add_extra_stop(self, extra_stop):
        if isinstance(extra_stop, Extra_Stop):
            self.extra_stop_ids.append(extra_stop.id)
            self.extra_stops.append(extra_stop)
        else:
            raise TypeError

    def add_order(self, order):
        if not isinstance(order, Order):
            raise TypeError(f'{order} is of type {type(order)}')

        self.order_ids.append(order.id)
        self.orders.append(order)

    def input_average_speed(self):
        from resources.strings import Delivery__average_speed__prompt as\
            prompt
        from utility.user_input import User_Input
        self.average_speed = User_Input(prompt).average_speed()

    def input_distance(self):
        from resources.strings import Delivery__miles_traveled_prompt as\
            prompt
        from utility.user_input import User_Input
        self.miles_traveled = User_Input(prompt).miles_traveled()

    def set_end_time(self):
        from utility.utility import now
        self.end_time = now()

    def set_start_time(self):
        from utility.utility import now
        self.start_time = now()

    def end(self):
        from processes.track import end_delivery
        self = end_delivery(self)

    def start(self):
        from processes.track import start_delivery
        self = start_delivery(self)


class Order:
    def __init__(self, delivery, id=None):
        if not isinstance(delivery, Delivery):
            from resources.error_messages import Order__class__wrong_parent_type
            raise TypeError(Order__class__wrong_parent_type.format(type(delivery)))

        self.parent = delivery

        if isinstance(id, int):
            self.id = id
        elif id is None:
            self.id = 0
        elif id:
            from resources.error_messages import Order__class__wrong_id_type
            raise TypeError(Order__class__wrong_id_type.format(type(id)))

        self.tip = None
        self.miles_traveled = None
        self.end_time = None

    def csv(self):
        return f'{self.tip.csv()},{self.miles_traveled},{self.end_time}'

    def file_list(self):
        from os import path
        from resources.system_names import\
            end_time, miles_traveled, Order__completed_ids as completed_ids,\
            order_directory, Order__id as order_id, Tip__info as tip

        parent_directory = self.parent.file_list()['directory']
        directory = path.join(parent_directory, order_directory)

        return {
            'completed_ids': path.join(parent_directory, completed_ids),
            'info': path.join(parent_directory, f'{self.id}.txt'),
            'directory': directory,
            'end_time': path.join(directory, end_time),
            'id': path.join(directory, order_id),
            'miles_traveled': path.join(directory, miles_traveled),
            'tip': path.join(directory, tip)
        }

    def view(self):
        formated_time = self.end_time.strftime('%I:%M:%S %p')

        view_parts = {
            'id': f'Order I.D. #:\t{self.id}',
            'distance': f'Distance to address:\t{self.miles_traveled} miles',
            'end_time': f'Completed at:\t{formated_time}'
        }

        tip_parts = self.tip.view()

        if 'card' in tip_parts.keys() and self.tip.card != 0.0:
            view_parts['card'] = f'Card tip:\t${self.tip.card}'
        if 'cash' in tip_parts.keys() and self.tip.cash != 0.0:
            view_parts['cash'] = f'Cash tip:\t${self.tip.cash}'
        if 'unknown' in tip_parts.keys() and self.tip.unknown != 0.0:
            view_parts['unknown'] = f'Unknown tip:\t${self.tip.unknown}'

        return view_parts

    def input_id(self):
        from resources.strings import Order__input_id__prompt as prompt
        from utility.user_input import User_Input
        self.id = User_Input(prompt).id()

    def input_miles_traveled(self):
        from resources.strings import Order__input_miles_traveled__prompt as\
            prompt
        from utility.user_input import User_Input
        self.miles_traveled = User_Input(prompt).miles_traveled()

    def input_tip(self):
        self.tip = Tip().input()

    def set_end_time(self):
        from utility.utility import now
        self.end_time = now()

    def set_start_time(self):
        from utility.utility import now
        self.start_time = now()

    def load_completed(self):
        from processes.load import load_completed_order
        self = load_completed_order(self)

    def load_current(self):
        from processes.load import load_current_order
        self = load_current_order(self)

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
        
        if card != 0.0:
            self.has_card = True
        else:
            self.has_card = False

        if cash != 0.0:
            self.has_cash = True
        else:
            self.has_cash = False

        if unknown != 0.0:
            self.has_unknown = True
        else:
            self.has_unknown = False

    def csv(self):
        return f'{self.card},{self.cash},{self.unknown}'

    def total_amount(self):
        return self.card + self.cash + self.unknown

    def view(self):
        view_parts = {}

        if self.has_card:
            view_parts['card'] = f'Card tip amount:\t${self.card}'
        if self.has_cash:
            view_parts['cash'] = f'Cash tip amount:\t${self.cash}'
        if self.has_unknown:
            view_parts['unknown'] = f'Unknown tip amount:\t${self.unknown}'

        return view_parts
    
    def input(self):
        from resources.strings import\
            Tip__input_card__prompt as card_prompt,\
            Tip__input_cash__prompt as cash_prompt
        from utility.user_input import User_Input

        self.card = User_Input(card_prompt).card_tip()
        self.cash = User_Input(cash_prompt).cash_tip()


class Split:
    def __init__(self, shift):
        if not isinstance(shift, Shift):
            raise TypeError

        self.parent = shift
        self.start_time = None
        self.end_time = None
        self.miles_traveled = None

    def csv(self):
        return f'{self.miles_traveled},{self.start_time},{self.end_time}'

    def file_list(self):
        from os import path
        from resources.system_names import\
            end_time, miles_traveled, split_directory, start_time, Split__info

        parent_directory = self.parent.file_list()['directory']
        directory = path.join(parent_directory, split_directory)

        return {
            'directory': directory,
            'end_time': path.join(directory, end_time),
            'info': path.join(parent_directory, Split__info),
            'miles_traveled': path.join(directory, miles_traveled),
            'start_time': path.join(directory, start_time)
        }

    def view(self):
        from datetime import datetime

        start_time = self.start_time.strftime('%I:%M:%S %p')
        view_parts = {'start_time': f'Split was started at:\t{start_time}'}

        if isinstance(self.miles_traveled, float):
            view_parts['distance'] =\
                f'Miles traveled on split:\t{self.miles_traveled} miles'

        if isinstance(self.end_time, datetime):
            end_time = self.end_time.strftime('%I:%M:%S %p')
            view_parts['end_time'] = f'Split was ended at:\t{end_time}'
        
        return view_parts

    def input_miles_traveled(self):
        from utility.user_input import User_Input
        # todo: need to write prompt for miles traveled and put it in resoursces file
        self.miles_traveled = User_Input('enter miles traveled').miles_traveled()

    def set_end_time(self):
        from utility.utility import now
        self.end_time = now()

    def set_start_time(self):
        from utility.utility import now
        self.start_time = now()

    def end(self):
        from processes.track import end_split
        self = end_split(self)

    def load_completed(self):
        from processes.load import load_completed_extra_stop
        self = load_completed_extra_stop(self)

    def load_current(self):
        from processes.load import load_current_extra_stop
        self = load_current_extra_stop(self)

    def start(self):
        from processes.track import start_split
        self = start_split(self)


class Extra_Stop:
    def __init__(self, parent, id=None):
        if not isinstance(parent, (Shift, Delivery)):
            raise TypeError

        self.parent = parent

        if isinstance(id, int):
            self.id = id
        elif id is None:
            self.assign_id()
        else:
            raise TypeError

        self.location = None
        self.reason = None
        self.miles_traveled = None
        self.start_time = None
        self.end_time = None

    def csv(self):
        if isinstance(self.parent, Shift):
            return f'{self.location},{self.reason},{self.miles_traveled},'\
                   f'{self.start_time},{self.end_time}'
        elif isinstance(self.parent, Delivery):
            return f'{self.location},{self.reason},{self.miles_traveled},'\
                   f'{self.end_time}'

    def file_list(self):
        from os import path
        from resources.system_names import\
            end_time, extra_stop_directory, miles_traveled, start_time,\
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
            'miles_traveled': path.join(directory, miles_traveled),
            'reason': path.join(directory, reason),
            'start_time': path.join(directory, start_time)
        }

    def nlsv(self):
        if isinstance(self.parent, Shift):
            return f'{self.location}\n'\
                   f'{self.reason}\n'\
                   f'{self.miles_traveled}\n'\
                   f'{self.start_time}\n'\
                   f'{self.end_time}'
        elif isinstance(self.parent, Delivery):
            return f'{self.location}\n'\
                   f'{self.reason}\n'\
                   f'{self.miles_traveled}\n'\
                   f'{self.end_time}'

    def view(self):
        from datetime import datetime

        end_time = self.end_time.strftime('%I:%M:%S %p')

        view_parts = {
            'id': f'Extra stop id #:\t{self.id + 1}',
            'location': f'Location:\t{self.location.capitalize()}',
            'reason': f'Reason:\t{self.reason.capitalize()}',
            'distance': f'Distance to extra stop:\t{self.miles_traveled} miles',
            'end_time': f'Extra stop was completed at:\t{end_time}'
        }

        if isinstance(self.start_time, datetime):
            view_parts['start_time'] = self.start_time.strftime('%I:%M:%S %p')
        
        return view_parts

    def assign_id(self):
        from os import path

        self.id = 0

        if path.exists(self.file_list()['running_id']):
            from utility.file import Read
            self.id = Read(self.file_list()['running_id']).integer()

        return self

    def input_location(self):
        from resources.strings import Extra_Stop__location__prompt as prompt
        from utility.user_input import User_Input
        self.location = User_Input(prompt).location()
    
    def input_reason(self):
        from resources.strings import Extra_Stop__reason__prompt as prompt
        from utility.user_input import User_Input
        self.reason = User_Input(prompt).reason()
    
    def input_miles_traveled(self):
        from resources.strings import Extra_Stop__miles_traveled__prompt as\
            prompt
        from utility.user_input import User_Input
        self.miles_traveled = User_Input(prompt).miles_traveled()

    def set_end_time(self):
        from utility.utility import now
        self.end_time = now()

    def set_start_time(self):
        from utility.utility import now
        self.start_time = now()

    def load_completed(self):
        from processes.load import load_completed_extra_stop
        self = load_completed_extra_stop(self)

    def load_current(self):
        from processes.load import load_current_extra_stop
        self = load_current_extra_stop(self)

    def track(self):
        from processes.track import track_extra_stop
        self = track_extra_stop(self)