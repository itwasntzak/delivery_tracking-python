# todo: in menus i want there to be tracking delivery menu and revise delivery menu
#       there will also be seperate menus for completed vs. ongoing deliveries
#       attribute selection should be apart of the functionality of the revision menu

# i think better to only offer exit program from main menu
#   all other menus/processes should just go back a menu

class Completed_Shift:
    # todo: this is just thrown together, no testing done if it works
    def __init__(self, shift):
        import re
        from resources.strings import Shift__completed__menu as prompt
        from utility.user_input import confirmation, text

        self.shift = self.shift

        self.option_selection()
        while not confirmation(self.confirmation_text):
            self.option_selection()
        else:
            if re.match('[rR]{1}', user_choice):
                self.resume_shift(self.shift)
            elif re.match('[oO]{1}', user_choice):
                self.overwrite_shift(self.shift)
            elif re.match('[qQ]{1}', user_choice):
                pass

    def option_selection(self):
        self.user_choice = text(self.prompt, permit='^[rRoOqQ]{1}')

        # todo: need to finish writing this
        if re.match('[rR]{1}', user_choice):
            pass
        elif re.match('[oO]{1}', user_choice):
            pass
        elif re.match('[qQ]{1}', user_choice):
            pass

        return self

    def resume_shift(self):
        from objects.shift import Shift
        from os import remove
        from processes.load import shift as load_shift
        from utility.file import write
        from utility.utility import enter_to_continue, now

        self.shift = Shift(now().date())
        file_list = self.shift.file_list()

        # load shift data
        self.shift = load_shift(self.shift)
        # get shift start time
        start_time = self.shift.start_time
        # delete shift info file
        remove(file_list['info_file'])
        # save start time
        write(start_time, file_list['start_time'])
        # remove id from completed ids file
        self.shift.remove_id_from_file()
        # reinitialize shift object
        self.shift = Shift(now().date())
        # set start time for new shift instance
        self.shift.start_time = start_time
        # confirm to user that shift was resumed
        # todo: need to add a prompt for enter to continue in resume shift
        enter_to_continue()

        return self

    def overwrite_shift(self):
        from objects.shift import Shift
        from os import mkdir, remove
        from resources.strings import Shift__overwritten__confirmation as\
            confirmation
        from utility.file import write
        from utility.user_input import text
        from utility.utility import enter_to_continue, now

        self.shift = Shift(now().date())

        # delete directory that contains all files
        remove(self.shift.directory())
        # recreate the directory to store new files
        mkdir(self.shift.directory())
        # recreate shift instance
        self.shift = Shift(now().date())
        # set and save start time
        self.shift.start_time = now()
        write(self.shift.start_time, shift.file_list()['start_time'])
        # remove id from completed ids file
        self.shift.remove_id_from_file()
        # confirm to user the shift was overwritten
        enter_to_continue(confirmation)

        return self


class Delivery_Tracking_Menu:
    '''
    todo: there should be a check before completing delivery if any
          orders have been entered. ask user if they really want to end
          delivery without order, or if they want to delete the delivery
    '''

    # options
    # oO = order
    # eE = extra stop
    # cC = complete delivery
    # vV = view delivery
    # rR = revise delivery
    # bB = back a menu

    def __init__(self, shift_menu):
        import re
        from processes.tracking import Track_Delivery
        from utility.user_input import confirmation
        from resources.strings import delivery__menu__texts

        self.condition = True
        self.delivery_menu = Track_Delivery(shift_menu.shift).start()

        self.display_text = delivery__menu__texts
        self.shift_menu = shift_menu

        self.option_selection()
        while not re.match('[vb]', self.user_choice, flags=re.IGNORECASE) and\
                not confirmation(self.confirmation_text):
            self.option_selection()

        self.result()

    def build_confirmation_text(self):
        import re
        from os import path

        delivery = self.delivery_menu.delivery

        if re.match('[o]', self.user_choice, flags=re.IGNORECASE):
            from objects.order import Order
            if not path.exists(Order(delivery).file_list()['directory']):
                self.confirmation_text = self.display_text['order'][0]
            else:
                self.confirmation_text = self.display_text['order'][1]

        elif re.match('[e]', self.user_choice, flags=re.IGNORECASE):
            from objects.extra_stop import Extra_Stop
            if not path.exists(Extra_Stop(delivery).file_list()['directory']):
                self.confirmation_text = self.display_text['extra_stop'][0]
            else:
                self.confirmation_text = self.display_text['extra_stop'][1]

        elif re.match('[c]', self.user_choice, flags=re.IGNORECASE):
            self.confirmation_text = self.display_text['end']

        elif re.match('[r]', self.user_choice, flags=re.IGNORECASE):
            self.confirmation_text = self.display_text['revise']
    
    def build_prompt(self):
        from objects.extra_stop import Extra_Stop
        from objects.order import Order
        from os import path

        delivery = self.delivery_menu.delivery

        # initial
        self.prompt = self.display_text['initial']
        # order
        if not path.exists(Order(delivery).file_list()['directory']):
            self.prompt += 'O. ' + self.display_text['order'][0]
        else:
            self.prompt += 'O. ' + self.display_text['order'][1]
        # extra stop
        if not path.exists(Extra_Stop(delivery).file_list()['directory']):
            self.prompt += 'E. ' + self.display_text['extra_stop'][0]
        else:
            self.prompt += 'E. ' + self.display_text['extra_stop'][1]
        # complete
        self.prompt += 'C. ' + self.display_text['end']
        # view
        self.prompt += 'V. ' + self.display_text['view']
        # revise
        self.prompt += 'R. ' + self.display_text['revise']
        # back
        self.prompt += 'B. ' + self.display_text['back']
    
    def option_selection(self):
        from utility.user_input import text

        self.build_prompt()
        self.user_choice = text(self.prompt, permit='^[oecvrb]$')
        self.build_confirmation_text()

    def result(self):
        import re

        if re.match('[o]', self.user_choice, flags=re.IGNORECASE):
            from processes.input import order
            self.delivery_menu.delivery.add_order(order(self.delivery_menu.delivery))

        elif re.match('[e]', self.user_choice, flags=re.IGNORECASE):
            from processes.input import delivery_extra_stop as extra_stop
            self.delivery_menu.delivery.add_extra_stop(extra_stop(self.delivery_menu.delivery))

        elif re.match('[c]', self.user_choice, flags=re.IGNORECASE):
            from processes.tracking import Track_Delivery
            self.delivery_menu.end()
            self.shift_menu.shift.add_delivery(self.delivery_menu.delivery)
            self.condition = False

        elif re.match('[v]', self.user_choice, flags=re.IGNORECASE):
            # todo: should ask if user wants to view sub parts
            from utility.utility import now, time_taken
            from processes.view import delivery as view_delivery
            print(time_taken(self.delivery_menu.delivery.start_time, now(),
                             self.display_text['current_duration']))
            print(view_delivery(self.delivery_menu.delivery))
        
        elif re.match('[r]', self.user_choice, flags=re.IGNORECASE):
            # todo: need to write functions that allow user to edit data having to do with delivery
            # parts to make this happen:
            # the first part is allowing the user to select what part of the extisting delivery to edit
            # if that is start time, or select from any of the entered orders for the delivery to edit
            # if the user wants to edit the order, other selection must be made of what data or the order to edit
            pass

        elif re.match('[b]', self.user_choice, flags=re.IGNORECASE):
            # todo: update prompt with this option
            self.condition = False


class Shift_Tracking_Menu:
    # todo: add rR option to allow shift revision

    # option
    # dD = delivery
    # eE = extra stop
    # cC = carry out tip
    # sS = split
    # xX = end shift
    # vV = view shift
    # qQ = quit program

    def __init__(self, shift):
        from objects.shift import Shift
        if not isinstance(shift, Shift):
            raise TypeError(f'{type(shift)}')

        import re
        from utility.user_input import confirmation

        self.shift = shift
        self.condition = True

        self.option_selection()
        while not re.match('[vq]', self.user_choice, flags=re.IGNORECASE) and\
                not confirmation(self.confirmation_text):
            self.option_selection()

        self.result()

    def build_confirmation_text(self):
        from os import path
        import re
        from resources.strings import shift__menu__texts as confirm_text

        if re.match('[d]', self.user_choice, flags=re.IGNORECASE):
            from objects.delivery import Delivery
            if not path.exists(Delivery(self.shift).file_list()['directory']):
                self.confirmation_text = confirm_text['delivery'][0]
            else:
                self.confirmation_text = confirm_text['delivery'][1]

        elif re.match('[e]', self.user_choice, flags=re.IGNORECASE):
            from objects.extra_stop import Extra_Stop
            if not path.exists(Extra_Stop(self.shift).file_list()['directory']):
                self.confirmation_text = confirm_text['extra_stop'][0]
            else:
                self.confirmation_text = confirm_text['extra_stop'][1]

        elif re.match('[c]', self.user_choice, flags=re.IGNORECASE):
            self.confirmation_text = confirm_text['tip']

        elif re.match('[s]', self.user_choice, flags=re.IGNORECASE):
            from objects.split import Split
            if not path.exists(Split(self.shift).file_list()['directory']):
                self.confirmation_text = confirm_text['split'][0]
            else:
                self.confirmation_text = confirm_text['split'][1]

        elif re.match('[x]', self.user_choice, flags=re.IGNORECASE):
            if not path.exists(self.shift.file_list()['end_time']):
                self.confirmation_text = confirm_text['end'][0]
            else:
                self.confirmation_text = confirm_text['end'][1]

        return self

    def build_prompt(self):
        from objects.delivery import Delivery
        from objects.extra_stop import Extra_Stop
        from objects.split import Split
        from os import path
        from resources.strings import shift__menu__texts as prompts

        # initial
        self.prompt = prompts['initial']
        # delivery
        self.prompt += 'D. '
        if not path.exists(Delivery(self.shift).file_list()['directory']):
            self.prompt += prompts['delivery'][0]
        else:
            self.prompt += prompts['delivery'][1]
        # extra stop
        self.prompt += 'E. '
        if not path.exists(Extra_Stop(self.shift).file_list()['directory']):
            self.prompt += prompts['extra_stop'][0]
        else:
            self.prompt += prompts['extra_stop'][1]
        # carry out tip
        self.prompt += 'C. ' + prompts['tip']
        # split
        self.prompt += 'S. '
        if not path.exists(Split(self.shift).file_list()['directory']):
            self.prompt += prompts['split'][0]
        else:
            self.prompt += prompts['split'][1]
        # end shift
        self.prompt += 'X. '
        if not path.exists(self.shift.file_list()['end_time']):
            self.prompt += prompts['end'][0]
        else:
            self.prompt += prompts['end'][1]
        # view
        self.prompt += 'V. ' + prompts['view']

        # todo: add revise as a menu option one revise shift is written

        # quit
        self.prompt += 'Q. ' + prompts['quit']

        return self

    def option_selection(self):
        from utility.user_input import text

        self.build_prompt()
        self.user_choice = text(self.prompt, permit='^[decsxvq]$')
        self.build_confirmation_text()

        return self

    def result(self):
        import re

        if re.match('[d]', self.user_choice, flags=re.IGNORECASE):
            delivery_menu = Delivery_Tracking_Menu(self)
            while delivery_menu.condition:
                delivery_menu = Delivery_Tracking_Menu(self)
            
            self = delivery_menu.shift_menu

        elif re.match('[e]', self.user_choice, flags=re.IGNORECASE):
            from processes.input import shift_extra_stop as\
                input_extra_stop
            self.shift.add_extra_stop(input_extra_stop(self.shift))

        elif re.match('[c]', self.user_choice, flags=re.IGNORECASE):
            from processes.input import tip as input_tip
            from utility.file import save
            tip = input_tip()
            self.shift.carry_out_tips.append(tip)
            save(tip.csv(), self.shift.file_list()['tips'], separator='\n')

        elif re.match('[s]', self.user_choice, flags=re.IGNORECASE):
            from processes.input import start_split
            start_split(self.shift)
            self.condition = False

        elif re.match('[x]', self.user_choice, flags=re.IGNORECASE):
            from processes.input import end_shift
            end_shift(self.shift)
            self.condition = False

        elif re.match('[v]', self.user_choice, flags=re.IGNORECASE):
            # todo: should ask if user wants to view sub parts
            # todo: add averages, average tip per delviery and etc...
            from processes.view import shift as view_shift
            print(f'\n{view_shift(self.shift)}'
                  f'Total tips:\t${round(sum(self.shift.all_tips()), 2)}\n'\
                  f'Card tips:\t${round(sum(self.shift.card_tips()), 2)}\n'\
                  f'Cash tips:\t${round(sum(self.shift.cash_tips()), 2)}\n')
        
        # todo: add revise result one revise shift is written

        elif re.match('[q]', self.user_choice, flags=re.IGNORECASE):
            self.condition = False

        return self


class Revise_Order:
    # options
    # iI = id
    # tT = tip
    # mM = miles traveled
    # eE = end time
    # vV = view current values of order
    # sS = save current values of order
    # bB = back a menu
    # qQ = quit program

    def __init__(self, shift, order):
        # todo: Edit_Order first thing, display the current order data to the user
        # todo: then resent the user with the option to select what data of the order to edit
        from utility.user_input import confirmation
        
        self.option_selection()
        while not confirmation(self.confirmation_text):
            self.option_selection()
        
        self.result()

    def build_confirmation_text(self):
        import re

        if re.match('[iI]{1}', user_choice):
            self.confirmation_text = 'Change order id'
        elif re.match('[tT]{1}', user_choice):
            self.confirmation_text = 'Change the tip'
        elif re.match('[mM]{1}', user_choice):
            self.confirmation_text = 'Change miles traveled'
        elif re.match('[eE]{1}', user_choice):
            self.confirmation_text = 'Change end time'
        elif re.match('[vV]{1}', user_choice):
            self.confirmation_text = 'View order info'
        elif re.match('[sS]{1}', user_choice):
            self.confirmation_text = 'Save any changes'
        elif re.match('[qQ]{1}', user_choice):
            self.confirmation_text = 'Quit without saving'
        elif re.match('[bB]{1}', user_choice):
            self.confirmation_text = 'Go back to delivery'

        return self

    def build_prompt(self):
        # todo: need to write build prompt for the revise order menu
        pass

    def option_selection(self):
        from resources.strings import Order__change_data__prompt as prompt
        from utility.user_input import text

        self.build_prompt()
        self.user_choice = text(prompt, permit='^[iItTmMeEvVsSqQbB]{1}')
        self.build_confirmation_text()
    
    def result(self):
        # todo: write result method for revise order menu
        pass

