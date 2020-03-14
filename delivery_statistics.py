from os import chdir

import input_data
import shift


def select_shifts():
    while True:
        user_choice = input_data.get_input(
            '\n\nSelect a time range to calculate:\n'
            'A. All shifts\n'
            'M. Current month\n'
            'W. Current week\n\n', str)
        if user_choice in ('a', 'A'):
            return shift.load_all_shifts()
        elif user_choice in ('m', 'M'):
            return shift.load_current_month()
        elif user_choice in ('w', 'W'):
            return shift.load_current_week()
        else:
            print('\nInvalid input...\n\n')


def select_statistic(shifts_list):
    while True:
        user_choice = input_data.get_input(
            '\n\nSelect the statistic you would like to see:\n'
            '1. Average deliveries per shift\n'
            '2. Average orders per shift\n'
            '3. Average orders per delivery\n'
            '4. Average tip per shift\n'
            '5. Average tip per delivery\n'
            '6. Average tip per order\n'
            '7. Average total tips per shift\n'
            '8. Average total in hand per shift\n'
            '9. All statistics at once\n'
            '0. Make new time range selection\n'
            '69. Quit the program\n\n', int)
        if user_choice == 1:
            print('\nAverage deliveries per shift:\n'
                  + str(shift.average_deliveries_per_shift(shifts_list)))
        elif user_choice == 2:
            print('\nAverage orders per shift:\n'
                  + str(shift.average_orders_per_shift(shifts_list)))
        elif user_choice == 3:
            print('\nAverage orders per delivery:\n'
                  + str(shift.average_orders_per_delivery(shifts_list)))
        elif user_choice == 4:
            print('\nAverage tip per shift:\n$'
                  + str(shift.average_tip_per_shift(shifts_list)))
        elif user_choice == 5:
            print('\nAverage tip per delivery:\n$'
                  + str(shift.average_tip_per_delivery(shifts_list)))
        elif user_choice == 6:
            print('\nAverage tip per order:\n$'
                  + str(shift.average_tip_per_order(shifts_list)))
        elif user_choice == 7:
            print('\nAverage total tips per shift:\n$'
                  + str(shift.average_total_tips_per_shift(shifts_list)))
        elif user_choice == 8:
            print('\nAverage total in hand per shift:\n$'
                  + str(shift.avereage_total_in_hand_per_shift(shifts_list)))
        elif user_choice == 9:
            print('\n\nAverage deliveries per shift:\t'
                  + str(shift.average_deliveries_per_shift(shifts_list)))
            print('Average orders per shift:\t'
                  + str(shift.average_orders_per_shift(shifts_list)))
            print('Average orders per delivery:\t'
                  + str(shift.average_orders_per_delivery(shifts_list)))
            print('Average tip per shift:\t$'
                  + str(shift.average_tip_per_shift(shifts_list)))
            print('Average tip per delivery:\t$'
                  + str(shift.average_tip_per_delivery(shifts_list)))
            print('Average tip per order:\t$'
                  + str(shift.average_tip_per_order(shifts_list)))
            print('Average total tips per shift:\t$'
                  + str(shift.average_total_tips_per_shift(shifts_list)))
            print('Average total in hand per shift:\t$'
                  + str(shift.avereage_total_in_hand_per_shift(shifts_list)))
        elif user_choice == 0:
            shifts_list = select_shifts()
        elif user_choice == 69:
            exit()
        else:
            print('\nInvalid input...\n\n')


chdir('delivery_tracking')
select_statistic(select_shifts())
