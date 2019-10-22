import datetime
import os

import input_data
import utility_function


# //TODO: read order function still needs to be writen
def read_order():
    pass


# //TODO: read extra stops function still needs to be writen
def read_extras_stop():
    on_extra_stop_path = os.path.join('delivery', 'extra_stop')
    if os.path.exists(on_extra_stop_path):
        pass


# //TODO: work out how to read in different deliveries, depending on request
def read_delivery(order_number='', file=''):
    delivery_path = os.path.join('delivery')
    on_delivery_path = os.path.join('delivery', 'on_delivery')

    if os.path.exists(delivery_path):
        if os.path.exists(on_delivery_path):
            while True:
                try:
                    user_choice = input_data.get_input(
                        prompt='Currently on delivery, '
                               'what would you like to do?\n'
                               '1 to continue action | '
                               '2 to continue delivery | '
                               '3 to delete the delivery',
                        kind=int)
                    if user_choice == 1:
                        pass
                    elif user_choice == 2:
                        pass
                    elif user_choice == 3:
                        pass
                else:
                    print('Invalid input...')


def read_past_delivery():
    pass


def read_split():
    split_start_time_path = os.path.join('shift', 'split_start_time.txt')
    split_info_path = os.path.join('shift', 'split_info.txt')

    if os.path.exists(split_start_time_path):
        return datetime.datetime.strptime(utility_function.read_data(
            split_start_time_path), '%Y-%m-%d %H:%M:%S.%f')
    elif os.path.exists(split_info_path):
        return utility_function.read_data(split_info_path).split(',')
    else:
        return None


def read_shift():
    shift_path = os.path.join('shift')
    todays_date_path = os.path.join(
        'shift_storage', str(utility_function.now().today()))

    if os.path.exists(shift_path):
        number_of_deliveries_path = os.path.join(
            'shift', 'number_of_deliveries.txt')
        number_of_extra_stops_path = os.path.join(
            'shift', 'number_of_extra_stops.txt')
        shift_start_time_path = os.path.join('shift', 'shift_start_time.txt')

        shift_start_time = datetime.datetime.strptime(
            utility_function.read_data(shift_start_time_path),
            '%Y-%m-%d %H:%M:%S.%f')
        if os.path.exists(number_of_deliveries_path):
            number_of_deliveries = int(utility_function.read_data(
                number_of_deliveries_path))
        if os.path.exists(number_of_extra_stops_path):
            number_of_extra_stops = int(utility_function.read_data(
                number_of_extra_stops_path))

        if number_of_deliveries and number_of_extra_stops:
            return [number_of_deliveries, number_of_extra_stops,
                    shift_start_time]
        elif number_of_deliveries:
            return [number_of_deliveries, shift_start_time]
        elif number_of_extra_stops:
            return [number_of_extra_stops, shift_start_time]
        else:
            return shift_start_time
    elif os.path.exists(todays_date_path):
        shift_info_path = os.path.join(todays_date_path, 'shift_info.txt')
        return utility_function.read_data(shift_info_path).split(',')
    else:
        return None


def read_past_shift(date):
    shift_path = os.path.join('shift_storage', date)
    if os.path.exists(shift_path):
        shift_info_path = os.path.join(shift_path, 'shift_info.txt')
        return utility_function.read_data(shift_info_path).split(',')
    else:
        return None
