# todo: move all of these function to thier own file


def load_all_shifts():
    shift_numbers_list = read('shift_ids.txt').split(',')
    shifts_list = []
    for shift_id in shift_numbers_list:
        shifts_list.append(Shift(to_datetime(shift_id + ' 00:00:00.0')).load())
    return shifts_list


def load_current_month():
    current_month = now().month
    shifts_list = load_all_shifts()
    current_month_shifts = []
    for shift in shifts_list:
        if shift.id.month == current_month:
            current_month_shifts.append(shift)
        else:
            pass
    return current_month_shifts


def load_current_week():
    current_week = now().isocalendar()[1]
    shifts_list = load_all_shifts()
    current_week_shifts = []
    for shift in shifts_list:
        if shift.id.isocalendar()[1] == current_week:
            current_week_shifts.append(shift)
        else:
            pass
    return current_week_shifts


def average_deliveries_per_shift(shifts_list):
    deliveries = []
    for shift in shifts_list:
        deliveries.append(len(shift.deliveries))
    return round(sum(deliveries)/len(shifts_list), 3)


def average_orders_per_delivery(shifts_list):
    deliveries = []
    orders = []
    for shift in shifts_list:
        deliveries.append(len(shift.deliveries))
        for delivery in shift.deliveries:
            orders.append(len(delivery.orders))
    return round(sum(orders)/sum(deliveries), 3)


def average_orders_per_shift(shifts_list):
    orders = []
    for shift in shifts_list:
        orders.append(len(shift.all_orders()))
    return round(sum(orders)/len(shifts_list), 3)


def average_tip_per_delivery(shifts_list):
    deliveries = []
    for shift in shifts_list:
        for delivery in shift.deliveries:
            deliveries.append(delivery)
    return round(total_tips(shifts_list)/len(deliveries), 2)


def average_tip_per_order(shifts_list):
    orders = []
    for shift in shifts_list:
        orders.append(len(shift.all_orders()))
    return round(total_tips(shifts_list)/sum(orders), 2)


def average_tip_per_shift(shifts_list):
    average_tips = []
    for shift in shifts_list:
        average_tips.append(shift.average_tip_per_delivery())
    return round(sum(average_tips)/len(shifts_list), 2)


def avereage_total_in_hand_per_shift(shifts_list):
    return round(total_in_hand(shifts_list)/len(shifts_list), 2)


def average_total_tips_per_shift(shifts_list):
    return round(total_tips(shifts_list)/len(shifts_list), 2)


def card_tips(shifts_list):
    tips = []
    for shift in shifts_list:
        tips.append(shift.card_tips())
    return round(sum(tips), 2)


def cash_tips(shifts_list):
    tips = []
    for shift in shifts_list:
        tips.append(shift.cash_tips())
    return round(sum(tips), 2)


def total_in_hand(shifts_list):
    tips = []
    vehicle = []
    for shift in shifts_list:
        tips.append(sum(shift.all_tips()))
        vehicle.append(shift.vehicle_compensation)
    money = round(round(sum(tips), 2) + round(sum(vehicle), 2), 2)
    return money


def total_tips(shifts_list):
    tips = []
    for shift in shifts_list:
        tips.append(sum(shift.all_tips()))
    return round(sum(tips), 2)


# todo: make average shifts per month function
# todo: make average miles per delivery function
# todo: make avereage speed per delviery function
# todo: make average delivery per hour function


class Shift:
    id = None
    start_time = None
    end_time = None
    delivery_ids = []
    deliveries = []
    extra_stop_ids = []
    extra_stops = []
    carry_out_tips = []
    split = None
    device_compensation = None
    extra_tips_claimed = None
    fuel_economy = None
    miles_traveled = None
    total_hours = None
    vehicle_compensation = None

    # todo: write function to load current shift data before going to menu

    def __init__(self, id):
        from datetime import datetime
        if isinstance(id, type(datetime.now().date())):
            self.id = id
        elif not isinstance(id, type(datetime.now().date())):
            raise TypeError

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

    # methods for getting statistics on shift's data
    def average_miles_per_delivery(self):
        miles = []
        for delivery in self.deliveries:
            miles.append(delivery.miles_traveled)
        return round(sum(miles)/len(self.deliveries), 1)

    def average_speed_per_delivery(self):
        average_speeds = []
        for delivery in self.deliveries:
            average_speeds.append(delivery.average_speed)
        return round(sum(average_speeds)/len(self.deliveries))

    def average_tip_per_delivery(self):
        return sum(self.all_tips())/len(self.deliveries)

    def average_tip_per_order(self):
        return sum(self.all_tips())/len(self.all_orders())

    def view_statistics(self):
        try:
            data = [len(self.deliveries), len(self.all_orders()),
                    to_money(sum(self.all_tips())),
                    to_money(sum(self.card_tips())),
                    to_money(sum(self.cash_tips())),
                    to_money(self.average_tip_per_delivery()),
                    to_money(self.average_tip_per_order())]
            print(f"\n{'Number of deliveries:'}{data[0]:>9}\n"
                  f"{'Number of orders:'}{data[1]:>13}\n"
                  '\n'
                  f"{'Total tips:':<15}{data[2]:>15}\n"
                  f"{'Card tips:':<15}{data[3]:>15}\n"
                  f"{'Cash tips:':<15}{data[4]:>15}\n"
                  'Average tip per:\n'
                  f"{'Delivery:':^15}{data[5]:>15}\n"
                  f"{'Order:':^13}{data[6]:>17}\n")
            enter_to_continue()
        except ZeroDivisionError:
            print('\n\nNothing has yet to be tracked\n\n')

# todo: need to write function that allows the user to change data
