# todo: in menus i want there to be tracking delivery menu and revise delivery menu
#       there will also be seperate menus for completed vs. ongoing deliveries
#       attribute selection should be apart of the functionality of the revision menu


def completed_shift(shift):
    import re
    from resources.strings import Shift__completed__menu as prompt
    from utility.user_input import confirmation, text

    def option_selection(prompt):
        user_choice = text(prompt, permit='[rRoOqQ]{1,1}')

        # todo: need to finish writing this
        if re.match('[rR]{1,1}', user_choice):
            pass
        elif re.match('[oO]{1,1}', user_choice):
            pass
        elif re.match('[qQ]{1,1}', user_choice):
            pass

        return user_choice, data

    user_choice, data = option_selection(prompt)
    while not confirmation(data):
        user_choice, data = option_selection(prompt)
    else:
        if re.match('[rR]{1,1}', user_choice):
            from processes.change_data import resume_shift
            resume_shift(shift)
        elif re.match('[oO]{1,1}', user_choice):
            from processes.change_data import overwrite_shift
            overwrite_shift(shift)
        elif re.match('[qQ]{1,1}', user_choice):
            pass


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
    # qQ = quit program

    def __init__(self, shift_menu):
        import re
        from processes.track_object import Track_Delivery
        from utility.user_input import confirmation
        from resources.strings import delivery__menu__texts

        self.condition = True
        self.tracking = Track_Delivery(shift_menu.shift).start()

        self.display_text = delivery__menu__texts
        self.shift_menu = shift_menu

        self.option_selection()
        while not re.match('[vVbBqQ]{1,1}', self.user_choice) and\
                not confirmation(self.confirmation_text):
            self.option_selection()

        self.result()

    def build_confirmation_text(self):
        import re
        from os import path

        if re.match('[oO]{1,1}', self.user_choice):
            from objects.order import Order
            if not path.exists(Order(self.tracking.delivery).file_list()['directory']):
                self.confirmation_text = self.display_text['order'][0]
            else:
                self.confirmation_text = self.display_text['order'][1]

        elif re.match('[eE]{1,1}', self.user_choice):
            from objects.extra_stop import Extra_Stop
            if not path.exists(Extra_Stop(self.tracking.delivery).file_list()['directory']):
                self.confirmation_text = self.display_text['extra_stop'][0]
            else:
                self.confirmation_text = self.display_text['extra_stop'][1]

        elif re.match('[cC]{1,1}', self.user_choice):
            self.confirmation_text = self.display_text['end']

        elif re.match('[rR]{1,1}', self.user_choice):
            self.confirmation_text = self.display_text['revise']
    
    def build_prompt(self):
        from objects.extra_stop import Extra_Stop
        from objects.order import Order
        from os import path
        # initial
        self.prompt = self.display_text['initial']
        # order
        if not path.exists(Order(self.tracking.delivery).file_list()['directory']):
            self.prompt += 'O. ' + self.display_text['order'][0]
        else:
            self.prompt += 'O. ' + self.display_text['order'][1]
        # extra stop
        if not path.exists(Extra_Stop(self.tracking.delivery).file_list()['directory']):
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
        # quiit
        self.prompt += 'Q. ' + self.display_text['quit']
    
    def option_selection(self):
        from utility.user_input import text

        self.build_prompt()
        self.user_choice = text(self.prompt, permit='[oOeEcCvVrRbBqQ]{1,1}')
        self.build_confirmation_text()

    def result(self):
        import re

        if re.match('[oO]{1,1}', self.user_choice):
            from processes.input_data import order
            self.tracking.delivery.add_order(order(self.tracking.delivery))

        elif re.match('[eE]{1,1}', self.user_choice):
            from processes.input_data import delivery_extra_stop as extra_stop
            self.tracking.delivery.add_extra_stop(extra_stop(self.tracking.delivery))

        elif re.match('[cC]{1,1}', self.user_choice):
            from processes.track_object import Track_Delivery
            self.tracking.end()
            self.shift_menu.shift.add_delivery(self.tracking.delivery)
            self.condition = False

        elif re.match('[vV]{1,1}', self.user_choice):
            # todo: should ask if user wants to view sub parts
            from utility.utility import now, time_taken
            from view_objects import delivery as view_delivery
            print(time_taken(self.tracking.delivery.start_time, now(),
                             self.display_text['time_taken']))
            print(view_delivery(self.tracking.delivery))
        
        elif re.match('[rR]{1,1}', self.user_choice):
            # todo: need to write functions that allow user to edit data having to do with delivery
            # parts to make this happen:
            # the first part is allowing the user to select what part of the extisting delivery to edit
            # if that is start time, or select from any of the entered orders for the delivery to edit
            # if the user wants to edit the order, other selection must be made of what data or the order to edit
            pass

        elif re.match('[bB]{1,1}', self.user_choice):
            # todo: update prompt with this option
            self.condition = False

        elif re.match('[qQ]{1,1}', self.user_choice):
            self.condition = False
            self.shift_menu.condition = False


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
        while not re.match('[vVqQ]', self.user_choice) and\
                not confirmation(self.confirmation_text):
            self.option_selection()

        self.result()

    def build_confirmation_text(self):
        from os import path
        import re
        from resources.strings import shift__menu__texts as confirm_text

        if re.match('[dD]{1,1}', self.user_choice):
            from objects.delivery import Delivery
            if not path.exists(Delivery(self.shift).file_list()['directory']):
                self.confirmation_text = confirm_text['delivery'][0]
            else:
                self.confirmation_text = confirm_text['delivery'][1]

        elif re.match('[eE]{1,1}', self.user_choice):
            from objects.extra_stop import Extra_Stop
            if not path.exists(Extra_Stop(self.shift).file_list()['directory']):
                self.confirmation_text = confirm_text['extra_stop'][0]
            else:
                self.confirmation_text = confirm_text['extra_stop'][1]

        elif re.match('[cC]{1,1}', self.user_choice):
            self.confirmation_text = confirm_text['tip']

        elif re.match('[sS]{1,1}', self.user_choice):
            from objects.split import Split
            if not path.exists(Split(self.shift).file_list()['directory']):
                self.confirmation_text = confirm_text['split'][0]
            else:
                self.confirmation_text = confirm_text['split'][1]

        elif re.match('[xX]{1,1}', self.user_choice):
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
        self.user_choice = text(self.prompt, permit='[dDeEcCsSxXvVqQ]{1,1}')
        self.build_confirmation_text()

        return self

    def result(self):
        import re

        if re.match('[dD]{1,1}', self.user_choice):
            delivery_menu = Delivery_Tracking_Menu(self)
            while delivery_menu.condition:
                delivery_menu = Delivery_Tracking_Menu(self)
            
            self = delivery_menu.shift_menu

        elif re.match('[eE]{1,1}', self.user_choice):
            from processes.input_data import shift_extra_stop as\
                input_extra_stop
            self.shift.add_extra_stop(input_extra_stop(self.shift))

        elif re.match('[cC]{1,1}', self.user_choice):
            from processes.input_data import tip as input_tip
            from utility.file import save
            tip = input_tip()
            self.shift.carry_out_tips.append(tip)
            save(tip.csv(), self.shift.file_list()['tips'], separator='\n')

        elif re.match('[sS]{1,1}', self.user_choice):
            from processes.input_data import start_split
            start_split(self.shift)
            self.condition = False

        elif re.match('[xX]{1,1}', self.user_choice):
            from processes.input_data import end_shift
            end_shift(self.shift)
            self.condition = False

        elif re.match('[vV]{1,1}', self.user_choice):
            # todo: should ask if user wants to view sub parts
            # todo: add averages, average tip per delviery and etc...
            from view_objects import shift as view_shift
            print(f'\n{view_shift(self.shift)}'
                  f'Total tips:\t${sum(self.shift.all_tips())}\n'\
                  f'Card tips:\t${sum(self.shift.card_tips())}\n'\
                  f'Cash tips:\t${sum(self.shift.cash_tips())}\n')
        
        # todo: add revise result one revise shift is written

        elif re.match('[qQ]{1,1}', self.user_choice):
            self.condition = False

        return self


class Revise_Completed_Delivery:
    # this class will be accessed but ongoing shift menu and completed shift menu

    # options
    # 1 = start time
    # 2 = distance
    # 3 = average speed
    # 4 = end time
    # oO = order selection/revision
    # eE = extra stop selection/revision
    # vV = view current values of delivery
    # sS = save current values of delivery
    # bB = back a menu
    # qQ = quit program

    def __init__(self, shift_menu, delivery_id):
        import re
        from resources.strings import delivery__revise__text
        from utility.user_input import confirmation

        self.condition = True
        self.shift_menu = shift_menu
        self.delivery = shift_menu.shift.deliveries[delivery_id]
        self.display_text = delivery__revise__text

        self.option_selection()
        if not re.match('[vVbBqQ]{1,1}', self.user_choice):
            while not confirmation(self.confirmation_text):
                self.option_selection()

        self.result()
    
    def build_confirmation_text(self):
        from datetime import datetime
        import re

        if re.match('[1]{1,1}', self.user_chioce):
            if isinstance(self.delivery.start_time, datetime):
                self.confirmation_text = self.display_text['start_time'][0]
            elif self.delivery.start_time is None:
                self.confirmation_text = self.display_text['start_time'][1]
        
        elif re.match('[2]{1,1}', self.user_chioce):
            if isinstance(self.delivery.miles_traveled, float):
                self.confirmation_text = self.display_text['miles_traveled'][0]
            elif self.delivery.miles_traveled is None:
                self.confirmation_text = self.display_text['miles_traveled'][1]
        
        elif re.match('[3]{1,1}', self.user_chioce):
            if isinstance(self.delivery.average_speed, int):
                self.confirmation_text = self.display_text['average_speed'][0]
            elif self.delivery.average_speed is None:
                self.confirmation_text = self.display_text['average_speed'][1]

        elif re.match('[4]{1,1}', self.user_chioce):
            if isinstance(self.delivery.end_time, datetime):
                self.confirmation_text = self.display_text['end_time'][0]
            elif self.delivery.end_time is None:
                self.confirmation_text = self.display_text['end_time'][1]

        elif re.match('[oO]{1,1}', self.user_choice):
            if len(self.delivery.orders) > 1:
                self.confirmation_text = self.display_text['order'][0]
            elif len(self.delivery.orders) == 1:
                self.confirmation_text = self.display_text['order'][1]
            elif len(self.delivery.orders) == 0:
                self.confirmation_text = self.display_text['order'][2]

        elif re.match('[eE]{1,1}', self.user_chioce):
            if len(self.delivery.extra_stops) > 1:
                self.confirmation_text = self.display_text['extra_stop'][0]
            elif len(self.delivery.extra_stops) == 1:
                self.confirmation_text = self.display_text['extra_stop'][1]

        elif re.match('[sS]{1,1}', self.user_choice):
            self.confirmation_text = self.display_text['save']

    def build_prompt(self):
        from datetime import datetime

        self.prompt = self.display_text['initial']

        self.prompt += '1. '
        if isinstance(self.delivery.start_time, datetime):
            self.prompt += self.display_text['start_time'][0]
        elif self.delivery.start_time is None:
            self.prompt += self.display_text['start_time'][1]
        
        self.prompt += '2. '
        if isinstance(self.delivery.miles_traveled, float):
            self.prompt += self.display_text['miles_traveled'][0]
        elif self.delivery.miles_traveled is None:
            self.prompt += self.display_text['miles_traveled'][1]
        
        self.prompt += '3. '
        if isinstance(self.delivery.average_speed, int):
            self.prompt += self.display_text['average_speed'][0]
        elif self.delivery.average_speed is None:
            self.prompt += self.display_text['average_speed'][1]

        self.prompt += '4. '
        if isinstance(self.delivery.end_time, datetime):
            self.prompt += self.display_text['end_time'][0]
        elif self.delivery.end_time is None:
            self.prompt += self.display_text['end_time'][1]
        
        self.prompt += 'O. '
        if len(self.delivery.orders) > 1:
            self.prompt += self.display_text['order'][0]
        elif len(self.delivery.orders) == 1:
            self.prompt += self.display_text['order'][1]
        elif len(self.delivery.orders) == 0:
            self.prompt += self.display_text['order'][2]
        
        self.prompt += 'E. '
        if len(self.delivery.extra_stop) >= 1:
            self.prompt += self.display_text['extra_stop']
        
        self.prompt += 'V. ' + self.display_text['view']
        self.prompt += 'S. ' + self.display_text['save']
        self.prompt += 'B. ' + self.display_text['back']
        self.prompt += 'Q. ' + self.display_text['quit']

        return self

    def option_selection(self):
        from utility.user_input import match_input

        self.build_prompt()
        self.user_choice = match_input(self.prompt, '[1234oOeEvVsSbBqQ]{1,1}')
        self.build_confirmation_text()

    def result(self):
        import re
        from processes.revise_object import Revise_Delivery

        if re.match('[1]{1,1}', self.user_choice):
            pass

        elif re.match('[2]{1,1}', self.user_choice):
            pass

        elif re.match('[3]{1,1}', self.user_choice):
            pass

        elif re.match('[4]{1,1}', self.user_choice):
            pass

        elif re.match('[oO]{1,1}', self.user_choice):
            pass

        elif re.match('[eE]{1,1}', self.user_choice):
            # todo: need to write extra stop delivery select function
            pass

        elif re.match('[vV]{1,1}', self.user_choice):
            from view_objects import delivery as view_delivery
            print(view_delivery(self.tracking.delivery))

        elif re.match('[bB]{1,1}', self.user_choice):
            pass

        elif re.match('[qQ]{1,1}', self.user_choice):
            self.condition = False
            self.shift_menu.condition = False
        
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

        if re.match('[iI]{1,1}', user_choice):
            self.confirmation_text = 'Change order id'
        elif re.match('[tT]{1,1}', user_choice):
            self.confirmation_text = 'Change the tip'
        elif re.match('[mM]{1,1}', user_choice):
            self.confirmation_text = 'Change miles traveled'
        elif re.match('[eE]{1,1}', user_choice):
            self.confirmation_text = 'Change end time'
        elif re.match('[vV]{1,1}', user_choice):
            self.confirmation_text = 'View order info'
        elif re.match('[sS]{1,1}', user_choice):
            self.confirmation_text = 'Save any changes'
        elif re.match('[qQ]{1,1}', user_choice):
            self.confirmation_text = 'Quit without saving'
        elif re.match('[bB]{1,1}', user_choice):
            self.confirmation_text = 'Go back to delivery'

        return self

    def build_prompt(self):
        # todo: need to write build prompt for the revise order menu
        pass

    def option_selection(self):
        from resources.strings import Order__change_data__prompt as prompt
        from utility.user_input import text

        self.build_prompt()
        self.user_choice = text(prompt, permit='[iItTmMeEvVsSqQbB]{1,1}')
        self.build_confirmation_text()
    
    def result(self):
        # todo: write result method for revise order menu
        pass

