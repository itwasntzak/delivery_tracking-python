
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
        self.device_compensation = None
        self.extra_tips_claimed = None
        self.fuel_economy = None
        self.miles_traveled = None
        self.total_hours = None
        self.vehicle_compensation = None
        self.split = None

    # add a delivery to the delivery lists
    def add_delivery(self, delivery):
        self.delivery_ids.append(delivery.id)
        self.deliveries.append(delivery)

    # add a extra stop to the extra stop lists
    def add_extra_stop(self, extra_stop):
        self.extra_stop_ids.append(extra_stop.id)
        self.extra_stops.append(extra_stop)

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
            Shift__vehical_compensation as vehical_compensation,\
            data_directory

        directory = path.join(data_directory, shifts_directory, f'{self.id}')

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
            'vehical_compensation': path.join(directory, vehical_compensation)
        }

    def remove_id_from_file(self):
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
                tips.append(order.tip.total_amount())
        
        for tip in self.carry_out_tips:
            tips.append(tip.total_amount())

        return tips
    
    def card_tips(self):
        tips = []
        for delivery in self.deliveries:
            for order in delivery.orders:
                tips.append(order.tip.card)
        
        for tip in self.carry_out_tips:
            tips.append(tip.card)

        return tips
    
    def cash_tips(self):
        tips = []
        for delivery in self.deliveries:
            for order in delivery.orders:
                tips.append(order.tip.cash)
        
        for tip in self.carry_out_tips:
            tips.append(tip.cash)

        return tips

# todo: need to write function that allows the user to change data
