# todo: in menus i want there to be tracking delivery menu and revise delivery menu
#       there will also be seperate menus for completed vs. ongoing deliveries
#       attribute selection should be apart of the functionality of the revision menu

# i think better to only offer exit program from main menu
#   all other menus/processes should just go back a menu

class Completed_Shift:
    def __init__(self, shift, test=False):
        from objects import Shift
        if not isinstance(shift, Shift):
            raise TypeError

        self.shift = shift

        if test is False:
            from utility.utility import enter_to_continue
            self.user_choice()
            if self.user_choice.lower() == 'r':
                from resources.strings import Shift__resume__confirmation
                self.resume_shift(self.shift)
                enter_to_continue(Shift__resume__confirmation)
            elif self.user_choice.lower() == 'o':
                from resources.strings import Shift__overwritten__confirmation
                self.overwrite_shift(self.shift)
                enter_to_continue(Shift__overwritten__confirmation)
            elif self.user_choice.lower() == 'q':
                pass

    def overwrite_shift(self):
        from objects import Shift
        from os import mkdir
        from shutil import rmtree
        from utility.file import write
        from utility.utility import now

        self.shift = Shift(now().date())

        # delete directory that contains all files
        rmtree(self.shift.file_list()['directory'])
        # recreate the directory to store new files
        mkdir(self.shift.file_list()['directory'])
        # set and save start time
        self.shift.set_start_time()
        write(self.shift.start_time, self.shift.file_list()['start_time'])
        # remove id from completed ids file
        self.shift.remove_id_from_file()

        return self

    def resume_shift(self):
        from objects import Shift
        from os import remove
        from utility.file import write
        from utility.utility import now

        self.shift = Shift(now().date())

        # load completed shift data
        self.shift.load_completed()
        # get shift start time
        start_time = self.shift.start_time
        # delete shift info file
        remove(self.shift.file_list()['info'])
        # save start time
        write(start_time, self.shift.file_list()['start_time'])
        # remove id from completed ids file
        self.shift.remove_id_from_file()
        # load current shift data
        self.shift.load_current()

        return self

    def user_choice(self):
        from resources.strings import Shift__completed__menu as prompt
        from utility.user_input import check_match, user_input

        self.user_choice = user_input(self.prompt)
        while not check_match('^[roq]$', self.user_choice):
            self.user_choice = user_input(self.prompt)
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

    def __init__(self, delivery, test=False):
        from objects import Delivery
        if not isinstance(delivery, Delivery):
            raise TypeError

        from resources.strings import delivery__menu__texts

        self.condition = True
        self.complete = False
        self.display_text = delivery__menu__texts
        self.delivery = delivery

        if test is False:
            from processes.load import load_delivery

            self.delivery.load_current()
            self.confirm()
            self.result()

    def build_confirmation_text(self):
        import re
        from os import path

        if self.user_choice.lower() == 'o':
            from objects import Order
            if not path.exists(Order(self.delivery).file_list()['directory']):
                self.confirmation_text = self.display_text['order'][0]
            else:
                self.confirmation_text = self.display_text['order'][1]

        elif self.user_choice.lower() == 'e':
            from objects import Extra_Stop
            if not path.exists(Extra_Stop(self.delivery).file_list()['directory']):
                self.confirmation_text = self.display_text['extra_stop'][0]
            else:
                self.confirmation_text = self.display_text['extra_stop'][1]

        elif self.user_choice.lower() == 'c':
            self.confirmation_text = self.display_text['end']

        elif self.user_choice.lower() == 'r':
            self.confirmation_text = self.display_text['revise']
    
    def build_prompt(self):
        from objects import Extra_Stop, Order
        from os import path
        from utility.utility import add_newlines

        # initial
        self.prompt = self.display_text['initial']
        # order
        if not path.exists(Order(self.delivery).file_list()['directory']):
            self.prompt += 'O. ' + self.display_text['order'][0]
        else:
            self.prompt += 'O. ' + self.display_text['order'][1]
        # extra stop
        if not path.exists(Extra_Stop(self.delivery).file_list()['directory']):
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

        self.prompt = add_newlines(self.prompt)

        return self

    def confirm(self):
        from utility.user_input import confirm

        self.user_choice()
        while not self.user_choice.lower() in ('v', 'b') and\
                not confirm(self.confirmation_text):
            self.user_choice()

    def user_choice(self):
        from utility.user_input import check_match
        from utility.user_input import user_input

        self.build_prompt()
        self.user_choice = user_input(self.prompt)
        while not check_match('^[oecvb]$', self.user_choice):
            self.user_choice = user_input(self.prompt)

        self.build_confirmation_text()

    def result(self):
        if self.user_choice.lower() == 'o':
            from objects import Order
            import os
            from processes.consolidate import consolidate_order
            from processes.track import track_order

            order = Order(self.delivery)
            if os.path.exists(order.file_list()['directory']):
                order.load_current()
            order = track_order(order)
            consolidate_order(order)
            self.delivery.add_order(order)

        elif self.user_choice.lower() == 'e':
            from objects import Extra_Stop
            import os
            from processes.consolidate import consolidate_extra_stop
            from processes.track import track_extra_stop

            extra_stop = Extra_Stop(self.delivery)
            if os.path.exists(extra_stop.file_list()['start_time']):
                from processes.load import load_extra_stop
                extra_stop = load_extra_stop(extra_stop, current=True)
            extra_stop = track_extra_stop(extra_stop)
            consolidate_extra_stop(extra_stop)
            self.delivery.add_extra_stop(extra_stop)

        elif self.user_choice.lower() == 'c':
            from processes.consolidate import consolidate_delivery
            from processes.track import end_delivery

            self.delivery = end_delivery(self.delivery)
            consolidate_delivery(self.delivery)
            self.condition = False
            self.complete = True

        elif self.user_choice.lower() == 'v':
            # todo: should ask if user wants to view sub parts
            from utility.utility import now, add_newlines
            from processes.view import view_delivery

            duration = now() - self.delivery.start_time
            print(f"{add_newlines(self.display_text['current_duration'] + str(duration))}")
            print(view_delivery(self.delivery))
        
        elif self.user_choice.lower() == 'r':
            # todo: need to write functions that allow user to edit data having to do with delivery
            # parts to make this happen:
            # the first part is allowing the user to select what part of the extisting delivery to edit
            # if that is start time, or select from any of the entered orders for the delivery to edit
            # if the user wants to edit the order, other selection must be made of what data or the order to edit
            pass

        elif self.user_choice.lower() == 'b':
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

    def __init__(self, shift, test=False):
        from objects import Shift
        if not isinstance(shift, Shift):
            raise TypeError(f'{type(shift)}')

        from resources.strings import shift__menu__texts

        self.condition = True
        self.display_text = shift__menu__texts
        self.shift = shift

        if test is False:
            from processes.load import load_shift

            self.confirm()
            self.result()

    def build_confirmation_text(self):
        from os import path
        import re

        if self.user_choice.lower() == 'd':
            from objects import Delivery
            if not path.exists(Delivery(self.shift).file_list()['directory']):
                self.confirmation_text = self.display_text['delivery'][0]
            else:
                self.confirmation_text = self.display_text['delivery'][1]

        elif self.user_choice.lower() == 'e':
            from objects import Extra_Stop
            if not path.exists(Extra_Stop(self.shift).file_list()['directory']):
                self.confirmation_text = self.display_text['extra_stop'][0]
            else:
                self.confirmation_text = self.display_text['extra_stop'][1]

        elif self.user_choice.lower() == 'c':
            self.confirmation_text = self.display_text['tip']

        elif self.user_choice.lower() == 's':
            from objects import Split
            if not path.exists(Split(self.shift).file_list()['directory']):
                self.confirmation_text = self.display_text['split'][0]
            else:
                self.confirmation_text = self.display_text['split'][1]

        elif self.user_choice.lower() == 'x':
            if not path.exists(self.shift.file_list()['end_time']):
                self.confirmation_text = self.display_text['end'][0]
            else:
                self.confirmation_text = self.display_text['end'][1]

        return self

    def build_prompt(self):
        from objects import Delivery, Extra_Stop, Split
        from os import path
        from utility.utility import add_newlines

        # initial
        self.prompt = self.display_text['initial']
        # delivery
        self.prompt += 'D. '
        if not path.exists(Delivery(self.shift).file_list()['directory']):
            self.prompt += self.display_text['delivery'][0]
        else:
            self.prompt += self.display_text['delivery'][1]
        # extra stop
        self.prompt += 'E. '
        if not path.exists(Extra_Stop(self.shift).file_list()['directory']):
            self.prompt += self.display_text['extra_stop'][0]
        else:
            self.prompt += self.display_text['extra_stop'][1]
        # carry out tip
        self.prompt += 'C. ' + self.display_text['tip']
        # split
        self.prompt += 'S. '
        if not path.exists(Split(self.shift).file_list()['directory']):
            self.prompt += self.display_text['split'][0]
        else:
            self.prompt += self.display_text['split'][1]
        # end shift
        self.prompt += 'X. '
        if not path.exists(self.shift.file_list()['end_time']):
            self.prompt += self.display_text['end'][0]
        else:
            self.prompt += self.display_text['end'][1]
        # view
        self.prompt += 'V. ' + self.display_text['view']

        # todo: add revise as a menu option one revise shift is written

        # quit
        self.prompt += 'Q. ' + self.display_text['quit']

        self.prompt = add_newlines(self.prompt)

        return self

    def confirm(self):
        from utility.user_input import confirm

        self.user_action()
        while not self.user_choice.lower() in ('v', 'q') and\
                not confirm(self.confirmation_text):
            self.user_action()

    def user_action(self):
        from utility.user_input import check_match, user_input

        self.build_prompt()
        self.user_choice = user_input(self.prompt)
        while not check_match('^[decsxvq]$', self.user_choice):
            self.user_choice = user_input(self.prompt)

        self.build_confirmation_text()

    def result(self):
        if self.user_choice.lower() == 'd':
            from objects import Delivery
            import os
            from processes.track import start_delivery

            delivery = start_delivery(Delivery(self.shift))

            menu = Delivery_Tracking_Menu(delivery)
            while menu.condition:
                menu = Delivery_Tracking_Menu(menu.delivery)

            if menu.complete is True:
                self.shift.add_delivery(menu.delivery)

        elif self.user_choice.lower() == 'e':
            from objects import Extra_Stop
            import os
            from processes.consolidate import consolidate_extra_stop
            from processes.load import load_extra_stop
            from processes.track import track_extra_stop

            extra_stop = Extra_Stop(self.shift)
            if os.path.exists(extra_stop.file_list()['start_time']):
                extra_stop = load_extra_stop(extra_stop, current=True)
            extra_stop = track_extra_stop(extra_stop)
            consolidate_extra_stop(extra_stop)
            self.shift.add_extra_stop(extra_stop)

        elif self.user_choice.lower() == 'c':
            from objects import Tip
            from utility.file import save

            tip = Tip().input()
            save(tip.csv(), self.shift.file_list()['tips'], '\n')
            self.shift.carry_out_tips.append(tip)

        elif self.user_choice.lower() == 's':
            from objects import Split
            from os import path
            from processes.consolidate import consolidate_split

            split = Split(self.shift)
            if not path.exists(split.file_list()['start_time']):
                split.start()
                self.condition = False
            else:
                split.load_current()
                split.end()
                consolidate_split(split)
                self.shift.split = split

        elif self.user_choice.lower() == 'x':
            from processes.consolidate import consolidate_shift
            from processes.track import end_shift

            self.shift = end_shift(self.shift)
            consolidate_shift(self.shift)
            self.condition = False

        elif self.user_choice.lower() == 'v':
            # todo: should ask if user wants to view sub parts
            # todo: add averages, average tip per delviery and etc...
            from processes.view import view_shift
            from utility.utility import to_money

            all_tips = [tip.total_amount() for tip in self.shift.all_tips()]
            card_tips = [tip.card for tip in self.shift.card_tips()]
            cash_tips = [tip.cash for tip in self.shift.cash_tips()]


            print(f'\n{view_shift(self.shift)}'
                  f'Total tips:\t{to_money(sum(all_tips))}\n'
                  f'Card tips:\t{to_money(sum(card_tips))}\n'
                  f'Cash tips:\t{to_money(sum(cash_tips))}\n')
        
        # todo: add revise result one revise shift is written

        elif self.user_choice.lower() == 'q':
            self.condition = False

        return self
