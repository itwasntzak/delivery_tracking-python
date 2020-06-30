# todo: these all need to be updated because they wont work with new system

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


class Shift_Statistics:
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
