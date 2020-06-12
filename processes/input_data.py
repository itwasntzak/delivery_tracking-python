'''
todo: thinking should change to storing indavidual data in dir namd after
      class (order or extra stop) it is storing until consolidated, use
      those dirs to tell when in progress. shift and deliveries should stay
      in dirs named after thire ids, because those are also checkable
'''


def order(order):
    from os import mkdir, path
    from processes.consolidate import order as consolidate_order
    from resources.strings import\
        Order__input_miles_traveled__prompt as miles_traveled_prompt,\
        Order__time_taken__display as order_ended
    from utility.file import write
    from utility.user_input import User_Input
    from utility.utility import now, time_taken

    # get list of files for order input
    order_files = order.file_list()
    # make directory to store order files
    mkdir(order_files['directory'])
    # input tip
    order.tip = tip(order_files['tip'])
    # input miles traveled
    order.miles_traveled = User_Input(miles_traveled_prompt).miles_traveled()
    # save order miles traveled to file
    write(order.miles_traveled, order_files['miles'])
    # set order end time as currunt time
    order.end_time = now()
    # save order end time to file
    write(order.end_time, order_files['end_time'])
    # consolidate order files into one file
    consolidate_order(order)
    # display time taken since delivery was started
    time_taken(order.parent_start_time(), order.end_time, order_ended)

    return order


def tip(file_path):
    from objects.tip import Tip
    from resources.strings import\
        Tip__input_card__prompt as card_prompt,\
        Tip__input_cash__prompt as cash_prompt
    from utility.file import write
    from utility.user_input import User_Input

    # input tip
    tip = Tip(card=User_Input(card_prompt).card_tip(),
              cash=User_Input(cash_prompt).cash_tip())
    # save tip to file
    write(tip.csv(), file_path)

    return tip
