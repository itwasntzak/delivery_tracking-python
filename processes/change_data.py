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


# todo:  after editing a parent, childern must have the changed parent reassigned


# todo: probably need to make a special function for changing time


def order(order, user_choice):
    import re

    order_files = order.file_list()

    if re.match('[iI]{1,1}', user_choice):
        from resources.strings import Order__input_id__prompt as prompt
        from utility.user_input import User_Input
        order.id = User_Input(prompt).id()
    elif re.match('[tT]{1,1}', user_choice):
        from processes.input_data import tip
        order.tip = tip(order_files['tip'])
    elif re.match('[mM]{1,1}', user_choice):
        from resources.strings import\
            Order__input_miles_traveled__prompt as prompt
        from utility.user_input import User_Input
        order.miles_traveled = User_Input(prompt).miles_traveled()
    elif re.match('[eE]{1,1}', user_choice):
        # todo: need to make function to change datetime/date/time
        pass
    elif re.match('[vV]{1,1}', user_choice):
        print(f'\n{order.view()}')
    elif re.match('[sS]{1,1}', user_choice):
        from utility.file import write
        write(order.csv(), order_files['info_file'])
    elif re.match('[qQ]{1,1}', user_choice):
        quit()
    elif re.match('[bB]{1,1}', user_choice):
        # todo: probably return the edit_delivery function
        pass


# todo: thinking should keep the remove id from file func in the shift class
#       have the function search the list after it is read in for a match of
#       todays id after finding it then remove it and rewrite the file
def overwrite_shift():
    from objects.shift import Shift
    from os import mkdir, remove
    from resources.strings import Shift__overwritten__confirmation as\
        confirmation
    from utility.file import write
    from utility.user_input import text
    from utility.utility import enter_to_continue, now

    shift = Shift(now().date())

    # delete directory that contains all files
    remove(shift.directory())
    # recreate the directory to store new files
    mkdir(shift.directory())
    # recreate shift instance
    shift = Shift(now().date())
    # set and save start time
    shift.start_time = now()
    write(shift.start_time, shift.file_list()['start_time'])
    # remove id from completed ids file
    shift.remove_id_from_file()
    # confirm to user the shift was overwritten
    enter_to_continue(confirmation)

    return shift


def resume_shift():
    from objects.shift import Shift
    from os import remove
    from processes.load import shift as load_shift
    from utility.file import write
    from utility.utility import enter_to_continue, now

    shift = Shift(now().date())

    # load shift data
    shift = load_shift(shift)
    # get shift start time
    start_time = shift.start_time
    # delete shift info file
    remove(shift.file_list()['info_file'])
    # save start time
    write(start_time, shift.file_list()['start_time'])
    # remove id from completed ids file
    shift.remove_id_from_file()
    # reinitialize shift object
    shift = Shift(now().date())
    # set start time for new shift instance
    shift.start_time = start_time
    # confirm to user that shift was resumed
    # todo: need to add a prompt for enter to continue in resume shift
    enter_to_continue()

    return shift
