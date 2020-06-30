"""
resource legend:
    file/class_name__function/method_name__resource_occurrence
    file/class_name__resource_occurrence
"""
# objects
#   shift
Shift__completed__menu =\
    'You have already completed a shift for today.\n'\
    'Please select an option:\n'\
    "R: Resume today's shift\n"\
    'O: Overwrite shift\n'\
    'Q: Quit program\n'
Shift__device_compensation__prompt = 'Amount of device compensation paid:\t$#.##'
Shift__end___enter_to_continue__display = 'Shift has been ended!'
Shift__extra_tips_claimed__prompt = 'Extra tips claimed for shift:\t$#.##'
Shift__fuel_economy__prompt = 'Enter fuel economy:\t##.#'
Shift__miles_traveled__prompt = 'Total miles traveled for this shift:\t#.#'
Shift__overwritten__confirmation = 'Shift has been overwriten!'
Shift__overwrite__prompt = 'Are you sure you want to overwrite the completed shift?'
Shift__start__enter_to_continue__display = 'Shift has been started!'
Shift__total_hours__prompt = 'Enter total hours worked:\t#.##'
Shift__vehical_compensation__prompt = 'Amount of vehicle compensation paid:\t$#.##'

#   delivery
Delivery__average_speed__prompt = 'Enter the average speed for this delivery:\t##'
Delivery__miles_traveled_prompt = 'Delivery miles traveled:\t#.#'
Delivery__order_quantity__prompt = 'Number of orders?'
Delivery__time_taken__display = 'Delivery completed in:\t'

#   order
Order__change_data__prompt =\
    'Please select an option:\n'\
    'I. Change Id\n'\
    'T. Change Tip amounts\n'\
    'M. Change Miles Traveled\n'\
    'E. Change End Time\n'\
    'V. View current Order data\n'\
    'S. Save any changes\n'\
    'Q. Quit the program\n'\
    'B. Go back to delivery options'
Order__input_id__prompt = 'Enter order number:\t#-####'
Order__input_miles_traveled__prompt = 'Order miles traveled:\t#.#'
Order__time_taken__display = 'Order completed in:\t'

#   tip
Tip__input_card__prompt = 'Enter card tip amount:\t$#.##\n(0 for no tip)'
Tip__input_cash__prompt  = 'Enter cash tip amount:\t$#.##\n(0 for no tip)'

#   extra stop
Extra_Stop__location__prompt = 'Extra stop location:'
Extra_Stop__miles_traveled__prompt = 'Extra stop miles traveled:\t#.#'
Extra_Stop__reason__prompt = 'Reason for extra stop?'
Extra_Stop__time_taken__display = 'Extra stop completed in:\t'

#   split
Split__end__confirmation = 'Are you sure you want to end the split?'
Split__start__enter_to_continue = 'Split has been started.'
Split__start__confirmation = 'Are you sure you want to start a split?'


# menus
shift__prompts = {
            'initial': 'What would you like to do?\n',
            'delivery': ['D: Start a delivery\n', 'D: Continue delivery\n'],
            'extra_stop': ['E: Start an extra stop\n', 'E: Continue extra stop\n'],
            'carry_out_tip': 'C: Enter carry out tip\n',
            'split': 'S: Start split\n',
            'end': ['X: End shift\n', 'X: Continue ending shift\n'],
            'info': 'I: Information on shift\n',
            'quit': 'Q: Quit program'
        }
delivery__prompt =\
    'Please select an option:\n'\
    'O. Add new order\n'\
    'E. Take extra stop\n'\
    'T. View current time since start of delivery\n'\
    'C. To complete the delivery\n'\
    'Q. To quit the program'


# utility
#   user input
User_Input__average_speed__succeed = ' mph'
User_Input__card_tip__succeed = ' card tip'
User_Input__cash_tip__succeed = ' cash tip'
User_Input__unknown_tip__succeed = ' unknown tip amount'
User_Input__miles_traveled__succeed = ' miles'
