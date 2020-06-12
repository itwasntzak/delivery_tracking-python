"""
resource legend:
    file/class_name__function/method_name__resource_occurrence
    file/class_name__resource_occurrence
"""
# objects
#   shift

#   delivery

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

#   split

# utility
#   user input
User_Input__card_tip__succeed = ' card tip'
User_Input__cash_tip__succeed = ' cash tip'
User_Input__unknown_tip__succeed = ' unknown tip amount'
User_Input__miles_traveled__succeed = ' miles'
