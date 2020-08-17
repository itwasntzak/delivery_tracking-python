# todo: change the way things are orgonized
#           use comments to show file names, first name for class or function
"""
resource legend:
    file/class_name__function/method_name__resource_occurrence
    file/class_name__resource_occurrence
thoughts on new ways
    group by files,
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
Shift__fuel_economy__prompt = 'Enter fuel economy:\t##.# mpg'
Shift__miles_traveled__prompt = 'Total miles traveled for this shift:\t#.# miles'
Shift__overwritten__confirmation = 'Shift has been overwriten!'
Shift__overwrite__prompt = 'Are you sure you want to overwrite the completed shift?'
Shift__start__enter_to_continue__display = 'Shift has been started!'
Shift__total_hours__prompt = 'Enter total hours worked:\t#.## hours'
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
Extra_Stop__location__prompt = 'Extra stop location:\n'
Extra_Stop__miles_traveled__prompt = 'Extra stop miles traveled:\t#.#\n'
Extra_Stop__reason__prompt = 'Reason for extra stop?\n'
Extra_Stop__time_taken__display = 'Extra stop completed in:\t'

#   split
Split__end__confirmation = 'Are you sure you want to end the split?'
Split__start__enter_to_continue = 'Split has been started.'
Split__start__confirmation = 'Are you sure you want to start a split?'


# Shift_Menu
shift__menu__texts = {
            'initial': '- Shift Menu -\nPlease select an option:\n',
            'delivery': ['Start delivery\n', 'Continue delivery\n'],
            'extra_stop': ['Start extra stop\n', 'Continue extra stop\n'],
            'tip': 'Enter carry out tip\n',
            'split': ['Start split\n', 'End split\n'],
            'end': ['End shift\n', 'Continue ending shift\n'],
            'view': 'View shift\n',
            'quit': 'Quit program\n'
}

shift__revise__text = {
    'initial': 'Select part of the shfit to revise:\n',
    'start_time': ['Revise start time\n', 'Add start time\n'],
    'end_time': ['Revise end time\n', 'Add end time\n'],
    'total_hours': ['Revise total hour\n', 'Add total hour\n'],
    'distance': ['Revise miles traveled\n', 'Add miles traveled\n'],
    'fuel_economy': ['Revise fuel economy\n', 'Add fuel economy\n'],
    'vehical_comp': ['Revise mileage\n', 'Add mileage\n'],
    'device_comp': ['Revise device useage paid\n', 'Add device useage paid\n'],
    'extra_tips': ['Revise extra tips claimed\n', 'Add extra tips claimed\n'],
    'total_in_hand': ['Revise total money in hand\n', 'Add total money in hand\n'],
    'delivery': ['Select a delivery\n', 'Revise delivery\n', 'Add a delivery\n'],
    'extra_stop': ['Select a extra stop\n', 'Revise extra stop\n'],
    'view': 'View current shift\n',
    'back': 'Go back a menu\n'
}

# Delivery_Menu
delivery__menu = {
    'initial': '- Delivery Menu -\nPlease select an option:\n',
    'order': ['Add new order\n', 'Continue entering order\n'],
    'extra_stop': ['Take extra stop\n', 'Continue extra stop\n'],
    'end': 'Complete current delivery\n',
    'view': 'View current delivery\n',
    'revise': 'Revise current delivery\n',
    'back': 'Back a menu\n',
    'quit': 'Quit program\n',
    'current_duration': 'Current time on delivery:\t',
    'total_duration': 'Total time on delivery:\t'
}

delivery__select = {
    'initial': 'There are {} number of deliveries\n',
    'prompt': 'Enter the ID of the delivery you want to select:\n'\
              '(B to go back)\n'
}

delivery__revise = {
    'initial': 'Select part of the delivery to revise:\n',
    'start_time': ['Revise start time\n', 'Add start time\n'],
    'miles_traveled': ['Revise miles traveled\n', 'Add miles traveled\n'],
    'average_speed': ['Revise average speed\n', 'Add average speed\n'],
    'end_time': ['Revise end time\n', 'Add end time\n'],
    'order': ['Select an order\n', 'Revise order\n', 'Add order\n'],
    'extra_stop': ['Select an extra stop\n', 'Revise extra stop\n'],
    'view': 'View current delivery\n',
    'back': 'Go back a menu\n',
}

order__select = {
    'initial': 'Order IDs:\n',
    'prompt': ['Enter an above ID to select an order:\n'\
               '(B to go back)\n',
               'Enter the ID of the order you want to select:\n'\
               '(B to go back)\n'],
    'no_match': "The entered number doesn't match a order ID\n",
    'confirmation': 'Select order with ID #\n'
}

carry_out_tip__select = {
    'initial': 'Carry out tips:\n',
    'prompt': 'Enter a number to select a tip:\n'\
              '(B to go back)\n',
    'no_option': 'There are no carry out tips\n',
    'no_match': "That number doesn't match an option\n",
    'confirmation': 'Tip option: {}\n'
}

extra_stop__select = {
    'initial': 'Extra Stops:\n',
    'display': 'Extra stop #{}, Location: {}\n',
    'prmopt': 'Enter an ID number to select an extra stop:\n'\
              '(B to go back)\n',
    'no_match': 'Please enter one of the ID numbers above\n',
    'no_option': 'There are no extra stops for this {}\n'
}

# utility
#   user input
User_Input__average_speed__succeed = ' mph'
User_Input__card_tip__succeed = ' card tip'
User_Input__cash_tip__succeed = ' cash tip'
User_Input__fuel_economy__succeed = ' mpg'
User_Input__miles_traveled__succeed = ' miles'
User_Input__total_hours__succeed = ' hours worked'
User_Input__unknown_tip__succeed = ' unknown tip amount'
