'''
 todo: before changing data, must assess if todays shift exists
       if it does, ask the user if they want to change data about todays shift
       or about a past shift

 todo: once user has selected what shift to edit data on, have them select
       if they want to edit the shifts data or a sub object
       do this continualy until the user ariaves at the subobject they to edit

 todo: then present them with the option to select what data of that object
       they want to edit. also present options, to go back a subobject or
       to select a different instance of a subobject. also options for exiting
       without saving and saving the object with or without exiting
'''

# todo: probably need to make a special function for changing time
import re


def order(order):
    from resources.strings import Order__change_data__prompt as prompt
    from utility.user_input import confirmation, text, User_Input

    user_choice = text(prompt, permit='[iItTmMeEvVsSqQbB]{1,1}')
    if re.match('[iI]{1,1}', user_choice):
        data = 'Change order id'
    elif re.match('[tT]{1,1}', user_choice):
        data = 'Change the tip'
    elif re.match('[mM]{1,1}', user_choice):
        data = 'Change Miles Traveled'
    elif re.match('[eE]{1,1}', user_choice):
        data = 'Change end time'
    elif re.match('[vV]{1,1}', user_choice):
        data = 'View order info'
    elif re.match('[sS]{1,1}', user_choice):
        data = 'Save any changes'
    elif re.match('[qQ]{1,1}', user_choice):
        data = 'Quit without saving'
    elif re.match('[bB]{1,1}', user_choice):
        data = 'Go back to delivery'

    while not confirmation(data):
        user_choice = text(prompt, permit='[iItTmMeEvVsSqQbB]{1,1}')

    else:
        order_files = order.file_list()
        if re.match('[iI]{1,1}', user_choice):
            from resources.strings import Order__input_id__prompt as prompt
            order.id = User_Input(prompt).id()
        elif re.match('[tT]{1,1}', user_choice):
            from processes.input_data import tip
            order.tip = tip(order_files['tip'])
        elif re.match('[mM]{1,1}', user_choice):
            from resources.strings import Order__input_miles_traveled__prompt\
                as prompt
            order.miles_traveled = User_Input(prompt).miles_traveled()
        elif re.match('[eE]{1,1}', user_choice):
            # todo: need to make function to change datetime/date/time
            pass
        elif re.match('[vV]{1,1}', user_choice):
            print(f'\n{order.view()}')
        elif re.match('[sS]{1,1}', user_choice):
            from utility.file import save
            save(order.csv(), order_files['info_file'])
        elif re.match('[qQ]{1,1}', user_choice):
            quit()
        elif re.match('[bB]{1,1}', user_choice):
            pass
