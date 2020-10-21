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
Shift__vehicle_compensation__prompt = 'Amount of vehicle compensation paid:\t$#.##'

#   delivery
Delivery__average_speed__prompt = 'Enter the average speed for this delivery:\t##'
Delivery__miles_traveled_prompt = 'Delivery miles traveled:\t#.#'
Delivery__order_quantity__prompt = 'Number of orders?'
Delivery__time_taken__display = 'Delivery completed in:'

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
Order__time_taken__display = 'Order completed in:'

#   tip
Tip__input_card__prompt = 'Enter card tip amount:\t$#.##'
Tip__input_cash__prompt  = 'Enter cash tip amount:\t$#.##'
Tip__input_unknown__prompt  = 'Enter unknown tip amount:\t$#.##'

#   extra stop
Extra_Stop__location__prompt = 'Extra stop location:'
Extra_Stop__miles_traveled__prompt = 'Extra stop miles traveled:\t#.#'
Extra_Stop__reason__prompt = 'Reason for extra stop?'
Extra_Stop__time_taken__display = 'Extra stop completed in:'

#   split
Split__end__confirmation = 'Are you sure you want to end the split?'
Split__start__enter_to_continue = 'Split has been started.'
Split__start__confirmation = 'Are you sure you want to start a split?'


# Shift_Menu
shift__menu__texts = {
    'initial': '- Shift Menu -\nPlease select an option:',
    'delivery': ['Start delivery', 'Continue delivery'],
    'extra_stop': ['Start extra stop', 'Continue extra stop'],
    'tip': 'Enter carry out tip',
    'split': ['Start split', 'End split'],
    'end': ['End shift', 'Continue ending shift'],
    'revise': 'Revise part of shift',
    'view': 'View shift',
    'quit': 'Quit program'
}

shift__revise__text = {
    'initial': '- Revise Shift -\nPlease select an option:',
    'start_time': ['Revise start time', 'Add start time'],
    'end_time': ['Revise end time', 'Add end time'],
    'total_hours': ['Revise total hour', 'Add total hour'],
    'distance': ['Revise miles traveled', 'Add miles traveled'],
    'fuel_economy': ['Revise fuel economy', 'Add fuel economy'],
    'vehicle_comp': ['Revise mileage', 'Add mileage'],
    'device_comp': ['Revise device useage paid', 'Add device useage paid'],
    'extra_tips': ['Revise extra tips claimed', 'Add extra tips claimed'],
    'total_in_hand': ['Revise total money in hand', 'Add total money in hand'],
    'delivery': ['Select a delivery', 'Revise delivery', 'Add a delivery'],
    'extra_stop': ['Select a extra stop', 'Revise extra stop'],
    'tips': 'Revise a carry out tip',
    'split': 'Revise split',
    'view': 'View current shift',
    'back': 'Go back'
}

# Delivery_Menu
delivery__menu__texts = {
    'initial': '- Delivery Menu -\nPlease select an option:',
    'order': ['Add new order', 'Continue entering order'],
    'extra_stop': ['Take extra stop', 'Continue extra stop'],
    'end': 'Complete current delivery',
    'view': 'View current delivery',
    'revise': 'Revise current delivery',
    'back': 'Back a menu',
    'quit': 'Quit program',
    'current_duration': 'Current time on delivery:\t',
    'total_duration': 'Total time on delivery:'
}

delivery__select = {
    'initial': 'There are {} number of deliveries',
    'prompt': 'Enter the ID of the delivery you want to select:\n(B to go back)'
}

delivery__revise = {
    'initial': '- Revise Delivery -\nPlease select an option:',
    'start_time': ['Revise start time', 'Add start time'],
    'distance': ['Revise miles traveled', 'Add miles traveled'],
    'average_speed': ['Revise average speed', 'Add average speed'],
    'end_time': ['Revise end time', 'Add end time'],
    'order': ['Select an order', 'Revise order', 'Add order'],
    'extra_stop': ['Select an extra stop', 'Revise extra stop'],
    'view': 'View current delivery',
    'save': 'Save changes',
    'back': 'Go back'
}

order__select = {
    'initial': 'Order IDs:',
    'prompt': ['Enter an above ID to select an order:\n(B to go back)',
               'Enter the ID of the order you want to select:\n(B to go back)'],
    'no_match': "The entered number doesn't match a order ID",
    'confirmation': 'Select order with ID #'
}

tip_revise_text = {
    'initial': '- Revise Tip -\nPlease select an option:',
    'card': ['Add a card tip', 'Edit card tip'],
    'cash': ['Add a cash tip', 'Edit cash tip'],
    'both': 'Edit/add both card and cash tips',
    'unknown': ['Add a tip of unknown type', 'Edit tip of unknown type'],
    'view': "View tip's current values",
    'save': 'Save changes',
    'back': 'Go back'
}

carry_out_tip__select = {
    'initial': 'Carry out tips:',
    'prompt': 'Enter a number to select a tip:\n(B to go back)',
    'no_option': 'There are no carry out tips',
    'no_match': "That number doesn't match an option",
    'confirmation': 'Tip option: {}'
}

extra_stop__select = {
    'initial': 'Extra Stops:',
    'display': '#{}, Location: {}',
    'prompt': 'Enter an ID number to select an extra stop:\n(B to go back)',
    'no_match': 'Please enter one of the ID numbers above',
    'no_option': 'There are no extra stops for this {}'
}

# utility
#   user input
confirm_text = 'Is this correct?\t[Y/N]'
money_symbol = '$'
average_speed_after_text = ' mph'
card_tip_after_text = ' card tip'
cash_tip_after_text = ' cash tip'
fuel_economy_after_text = ' mpg'
miles_traveled_after_text = ' miles'
total_hours_after_text = ' hours worked'
unknown_tip_after_text = ' unknown tip amount'
