
class Shift:
    def __init__(self, id):
        from datetime import datetime
        if isinstance(id, type(datetime.now().date())):
            self.id = id
        elif not isinstance(id, type(datetime.now().date())):
            raise TypeError

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

    # add a carry out tip
    def add_carry_out_tip(self, tip):
        self.carry_out_tips.append(tip)

    # add a delivery to the delivery lists
    def add_delivery(self, delivery):
        self.delivery_ids.append(delivery.id)
        self.deliveries.append(delivery)

    # add a extra stop to the extra stop lists
    def add_extra_stop(self, extra_stop):
        self.extra_stop_ids.append(extra_stop.id)
        self.extra_stops.append(extra_stop)

    def csv(self):
        '{0},{1},{2},{3},{4},{5},{6},{7}'.format(
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
            user_data_directory as data_directory

        directory = path.join(data_directory, shifts_directory, f'{self.id}')

        return {
            'carry_out_tips': path.join(directory, carry_out_tip),
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
        # todo: this needs to be rewritten, either with regex or the new file.Read class
        temp_id_list = read(self.shift_ids_path).split(',')
        id_list = []
        for id in id_list:
            if id != str(self.id):
                id_list.append(id)
        comma_number = len(id_list) - 1
        new_ids_list = ""
        for value in range(comma_number):
            new_ids_list += id_list[value] + ','
        new_ids_list += id_list[comma_number + 1]
        if len(id_list) == 0:
            remove(self.shift_ids_path)
        elif len(id_list) > 0:
            write_data(self.shift_ids_path, new_ids_list)

    # methods for analyzing data
    def all_orders(self):
        all_orders = []
        for delivery in self.deliveries:
            for order in delivery.orders:
                all_orders.append(order)
        return all_orders

    def all_tips(self):
        tips = []
        for delivery in self.deliveries:
            for order in delivery.orders:
                try:
                    for tip in order.tip:
                        tips.append(tip)
                except TypeError:
                    tips.append(order.tip)
        for tip in self.carry_out_tips:
            tips.append(tip[0])
        return tips

    def card_tips(self):
        card_tips = []
        for delivery in self.deliveries:
            for order in delivery.orders:
                try:
                    index_counter = 0
                    for tip in order.tip:
                        if order.tip_type[index_counter] == 1:
                            card_tips.append(tip)
                        elif order.tip_type in (0, 2):
                            pass
                        index_counter += 1
                except TypeError:
                    if order.tip_type == 1:
                        card_tips.append(order.tip)
                    elif order.tip_type in (0, 2):
                        pass
        for tip in self.carry_out_tips:
            if tip[1] == 1:
                card_tips.append(tip[0])
            elif tip[1] == 2:
                pass
        return card_tips

    def cash_tips(self):
        cash_tips = []
        for delivery in self.deliveries:
            for order in delivery.orders:
                try:
                    index_counter = 0
                    for tip in order.tip:
                        if order.tip_type[index_counter] == 2:
                            cash_tips.append(tip)
                        elif order.tip_type in (0, 1):
                            pass
                        index_counter += 1
                except TypeError:
                    if order.tip_type == 2:
                        cash_tips.append(order.tip)
                    elif order.tip_type in (0, 1):
                        pass
        for tip in self.carry_out_tips:
            if tip[1] == 2:
                cash_tips.append(tip[0])
            elif tip[1] == 1:
                pass
        return cash_tips

# todo: need to write function that allows the user to change data
