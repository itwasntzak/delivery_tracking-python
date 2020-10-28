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
            from utility.user_input import enter_to_continue
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

    # o = order
    # e = extra stop
    # c = complete delivery
    # v = view delivery
    # r = revise delivery
    # b = back a menu

    def __init__(self, delivery, test=False):
        from objects import Delivery
        if not isinstance(delivery, Delivery):
            raise TypeError

        from resources.strings import delivery__menu__texts

        self.delivery = delivery.load_current()
        self.display_text = delivery__menu__texts
        self.complete = False
        self.loop_condition = True

        if test is False:
            self.main()
            while self.loop_condition:
                self.main()

    def build_confirmation_text(self):
        import re
        from os import path

        # delivery
        if self.user_selection.lower() == 'o':
            from objects import Order
            if not path.exists(Order(self.delivery).file_list()['directory']):
                self.confirmation_text = self.display_text['order'][0]
            else:
                self.confirmation_text = self.display_text['order'][1]
        # extra stop
        elif self.user_selection.lower() == 'e':
            from objects import Extra_Stop
            extra_stop_directory =\
                Extra_Stop(self.delivery).file_list()['directory']
            if not path.exists(extra_stop_directory):
                self.confirmation_text = self.display_text['extra_stop'][0]
            else:
                self.confirmation_text = self.display_text['extra_stop'][1]
        # complete
        elif self.user_selection.lower() == 'c':
            self.confirmation_text = self.display_text['end']
        # revise
        elif self.user_selection.lower() == 'r':
            self.confirmation_text = self.display_text['revise']
    
    def build_prompt(self):
        from objects import Extra_Stop, Order
        from os import path
        from utility.utility import add_newlines

        # initial
        self.prompt = self.display_text['initial'] + '\n'
        # order
        order_index = 0
        if path.exists(Order(self.delivery).file_list()['directory']):
            order_index = 1
        self.prompt += f'O. {self.display_text["order"][order_index]}\n'
        # extra stop
        extra_stop_index = 0
        if path.exists(Extra_Stop(self.delivery).file_list()['directory']):
            extra_stop_index = 1
        self.prompt +=\
            f'E. {self.display_text["extra_stop"][extra_stop_index]}\n'
        # complete
        self.prompt += f'C. {self.display_text["end"]}\n'
        # view
        self.prompt += f'V. {self.display_text["view"]}\n'
        # revise
        self.prompt += f'R. {self.display_text["revise"]}\n'
        # back
        self.prompt += f'B. {self.display_text["back"]}\n'

        self.prompt = add_newlines(self.prompt)

    def main(self):
        from utility.user_input import confirm

        self.user_choice()
        while not self.user_selection.lower() in ('v', 'b') and\
                not confirm(self.confirmation_text):
            self.user_choice()
        self.result()

    def user_choice(self):
        from utility.user_input import check_match
        from utility.user_input import user_input

        self.build_prompt()
        self.user_selection = user_input(self.prompt)
        while not check_match('^[oecrvb]$', self.user_selection):
            self.user_selection = user_input(self.prompt)
        self.build_confirmation_text()

    def result(self):
        # order
        if self.user_selection.lower() == 'o':
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
        # extra stop
        elif self.user_selection.lower() == 'e':
            from objects import Extra_Stop
            import os
            from processes.consolidate import consolidate_extra_stop
            from processes.track import track_extra_stop

            extra_stop = Extra_Stop(self.delivery).load_current()
            extra_stop = track_extra_stop(extra_stop)
            consolidate_extra_stop(extra_stop)
            self.delivery.add_extra_stop(extra_stop)
        # complete
        elif self.user_selection.lower() == 'c':
            from processes.consolidate import consolidate_delivery
            from processes.track import end_delivery

            self.delivery = end_delivery(self.delivery)
            consolidate_delivery(self.delivery)
            self.loop_condition = False
            self.complete = True
        # view
        elif self.user_selection.lower() == 'v':
            View_Delivery_Menu(self.delivery)
        # revise
        elif self.user_selection.lower() == 'r':
            from processes.revise import Revise_Delivery
            revise_delivery = Revise_Delivery(self.delivery)
            self.delivery = revise_delivery.delivery
        # back
        elif self.user_selection.lower() == 'b':
            self.loop_condition = False


class Shift_Tracking_Menu: 
    # d = delivery
    # e = extra stop
    # c = carry out tip
    # s = split
    # x = end shift
    # r = revise
    # v = view shift
    # q = quit program

    def __init__(self, shift, test=False):
        from objects import Shift
        if not isinstance(shift, Shift):
            raise TypeError(f'{type(shift)}')

        from resources.strings import shift__menu__texts

        self.shift = shift
        self.display_text = shift__menu__texts
        self.loop_condition = True

        if test is False:
            self.main()
            while self.loop_condition:
                self.main()

    def build_confirmation_text(self):
        from os import path

        # delivery
        if self.user_selection.lower() == 'd':
            from objects import Delivery
            if not path.exists(Delivery(self.shift).file_list()['directory']):
                self.confirmation_text = self.display_text['delivery'][0]
            else:
                self.confirmation_text = self.display_text['delivery'][1]
        # extra stop
        elif self.user_selection.lower() == 'e':
            from objects import Extra_Stop
            if not path.exists(Extra_Stop(self.shift).file_list()['directory']):
                self.confirmation_text = self.display_text['extra_stop'][0]
            else:
                self.confirmation_text = self.display_text['extra_stop'][1]
        # carry out tip
        elif self.user_selection.lower() == 'c':
            self.confirmation_text = self.display_text['tip']
        # split
        elif self.user_selection.lower() == 's':
            from objects import Split
            if not path.exists(Split(self.shift).file_list()['directory']):
                self.confirmation_text = self.display_text['split'][0]
            else:
                self.confirmation_text = self.display_text['split'][1]
        # end
        elif self.user_selection.lower() == 'x':
            if not path.exists(self.shift.file_list()['end_time']):
                self.confirmation_text = self.display_text['end'][0]
            else:
                self.confirmation_text = self.display_text['end'][1]
        # revise
        elif self.user_selection.lower() == 'r':
            self.confirmation_text = self.display_text['revise']

    def build_prompt(self):
        from objects import Delivery, Extra_Stop, Split
        from os import path
        from utility.utility import add_newlines

        # initial
        self.prompt = f"\n{self.display_text['initial']}\n"
        # delivery
        delivery_index = 0
        if path.exists(Delivery(self.shift).file_list()['directory']):
            delivery_index = 1
        self.prompt += f'D. {self.display_text["delivery"][delivery_index]}\n'
        # extra stop
        extra_stop_index = 0
        if path.exists(Extra_Stop(self.shift).file_list()['directory']):
           extra_stop_index = 1
        self.prompt +=\
            f'E. {self.display_text["extra_stop"][extra_stop_index]}\n'
        # carry out tip
        self.prompt += f'C. {self.display_text["tip"]}\n'
        # split
        split_index = 0
        if path.exists(Split(self.shift).file_list()['directory']):
            split_index = 1
        self.prompt += f'S. {self.display_text["split"][split_index]}\n'
        # end shift
        end_index = 0
        if path.exists(self.shift.file_list()['end_time']):
            end_index = 1
        self.prompt += f'X. {self.display_text["end"][end_index]}\n'
        # view
        self.prompt += f'V. {self.display_text["view"]}\n'
        # revise
        self.prompt += f'R. {self.display_text["revise"]}\n'
        # quit
        self.prompt += f'Q. {self.display_text["quit"]}\n'

        self.prompt = add_newlines(self.prompt)

    def main(self):
        from utility.user_input import confirm

        self.user_choice()
        while not self.user_selection.lower() in ('v', 'q') and\
                not confirm(self.confirmation_text):
            self.user_choice()
        self.result()

    def user_choice(self):
        from utility.user_input import check_match, user_input

        self.build_prompt()
        self.user_selection = user_input(self.prompt)
        while not check_match('^[decsxrvq]$', self.user_selection):
            self.user_selection = user_input(self.prompt)
        self.build_confirmation_text()

    def result(self):
        # delivery
        if self.user_selection.lower() == 'd':
            from objects import Delivery
            import os
            from processes.track import start_delivery

            delivery = start_delivery(Delivery(self.shift))

            delivery_menu = Delivery_Tracking_Menu(delivery)

            if delivery_menu.complete is True:
                self.shift.add_delivery(delivery_menu.delivery)
        # extra stop
        elif self.user_selection.lower() == 'e':
            from objects import Extra_Stop
            import os
            from processes.consolidate import consolidate_extra_stop
            from processes.load import load_extra_stop
            from processes.track import track_extra_stop

            extra_stop = Extra_Stop(self.shift).load_current()
            extra_stop = track_extra_stop(extra_stop)
            consolidate_extra_stop(extra_stop)
            self.shift.add_extra_stop(extra_stop)
        # carry out tip
        elif self.user_selection.lower() == 'c':
            from objects import Tip
            from utility.file import save

            tip = Tip().input_both()
            save(tip.csv(), self.shift.file_list()['tips'], '\n')
            self.shift.carry_out_tips.append(tip)
        # split
        elif self.user_selection.lower() == 's':
            from objects import Split
            from os import path
            from processes.consolidate import consolidate_split

            if not path.exists(Split(self.shift).file_list()['start_time']):
                self.shift.split = Split(self.shift).start()
                self.loop_condition = False
            else:
                self.shift.split.end()
                consolidate_split(self.shift.split)
        # end shift
        elif self.user_selection.lower() == 'x':
            from processes.consolidate import consolidate_shift
            from processes.track import end_shift

            self.shift = end_shift(self.shift)
            consolidate_shift(self.shift)
            self.loop_condition = False
        # view
        elif self.user_selection.lower() == 'v':
            View_Shift_Menu(self.shift)
        # revise
        elif self.user_selection.lower() == 'r':
            from processes.revise import Revise_Shift
            revise_shift = Revise_Shift(self.shift)
            self.shift = revise_shift.shift
        # quit
        elif self.user_selection.lower() == 'q':
            self.loop_condition = False

        return self


class View_Shift_Menu:
    # f = full
    # m = main
    # q = quick
    # s = select
    # b = back

    def __init__(self, shift):
        from objects import Shift
        if not isinstance(shift, Shift):
            raise TypeError

        from processes.view import View_Shift

        self.shift = shift
        self.view = View_Shift(shift)
        self.prompt =\
            '\n- View Shift -\n'\
            'F. Full view\n'\
            'M. Main view\n'\
            'Q. Quick view\n'\
            'S. Select sub-part to view\n'\
            'B. Go back\n'
        
        self.loop_condition = True
        self.main()
        while self.loop_condition:
            self.main()
    
    def main(self):
        from utility.user_input import check_match, user_input

        self.user_selection = user_input(self.prompt)
        while not check_match('^[fmqsb]$', self.user_selection):
            self.user_selection = user_input(self.prompt)
        self.result()

    def result(self):
        # full
        if self.user_selection.lower() == 'f':
            print(self.view.full())
        # main
        elif self.user_selection.lower() == 'm':
            print(self.view.main())
        # quick
        elif self.user_selection.lower() == 'q':
            print(self.view.quick())
        # sub-parts
        elif self.user_selection.lower() == 's':
            View_Shift_Select_Option(self.shift)
        # back
        elif self.user_selection.lower() == 'b':
            self.loop_condition = False


class View_Shift_Select_Option:
    # d = deliveries
    # e = extra stops
    # s = split
    # t = carry out tips
    # b = back

    def __init__(self, shift):
        from objects import Shift
        if not isinstance(shift, Shift):
            raise TypeError

        self.shift = shift
        self.loop_condition = True

        self.main()
        while self.loop_condition:
            self.main()
    
    def build_confirmation_text(self):
        # deliveries
        if self.user_selection.lower() == 'd':
            self.confirmation_text = 'Select a delivery'
        # extra stops
        elif self.user_selection.lower() == 'e':
            self.confirmation_text = 'Select a extra stop'
        # split
        elif self.user_selection.lower() == 's':
            self.confirmation_text = 'View split'
        # carry out tips
        elif self.user_selection.lower() == 't':
            self.confirmation_text = 'View carry out tips'

    def build_prompt(self):
        # todo: add conditional generation
        self.prompt = '\n- Shift Sub-select -\n'
        if len(self.shift.deliveries) >= 1:
            self.prompt += 'D. Select delivery to view\n'
        if len(self.shift.extra_stops) >= 1:
            self.prompt += 'E. Select extra stop to view\n'
        if self.shift.split is not None:
            self.prompt += 'S. View split\n'
        if len(self.shift.carry_out_tips) >= 1:
            self.prompt += 'T. View carry out tips\n'
        
        self.prompt += 'B. Go back\n'

    def main(self):
        from utility.user_input import confirm

        self.user_choice()
        while self.user_selection.lower() != 'b' and\
                not confirm(self.confirmation_text):
            self.user_choice()
        self.result()

    def user_choice(self):
        from utility.user_input import check_match, user_input
        # build pattern
        pattern = '^['
        if len(self.shift.deliveries) >= 1:
            pattern += 'd'
        if len(self.shift.extra_stops) >= 1:
            pattern += 'e'
        if self.shift.split is not None:
            pattern += 's'
        if len(self.shift.carry_out_tips) >= 1:
            pattern += 't'
        pattern += 'b]$'
        # user input
        self.build_prompt()
        self.user_selection = user_input(self.prompt)
        while not check_match(pattern, self.user_selection):
            self.user_selection = user_input(self.prompt)
        self.build_confirmation_text()

    def result(self):
        # delivery
        if self.user_selection.lower() == 'd':
            if len(self.shift.deliveries) == 1:
                View_Delivery_Menu(self.shift.deliveries[0])
                self.loop_condition = False
            elif len(self.shift.deliveries) > 1:
                from processes.select import Select_Delivery
                select_delivery = Select_Delivery(self.shift)
                delivery_index = select_delivery.get_index()
                if isinstance(delivery_index, int):
                    delivery = self.shift.deliveries[delivery_index]
                    View_Delivery_Menu(delivery)
        # extra stop
        elif self.user_selection.lower() == 'e':
            from processes.view import view_extra_stop
            # 1 extra stop
            if len(self.shift.extra_stops) == 1:
                # display extra stop to user
                print(view_extra_stop(self.shift.extra_stops[0]))
                self.loop_condition = False
            # more then 1 extra stop
            elif len(self.shift.extra_stops) > 1:
                from processes.select import Select_Extra_Stop
                # user select extra stop
                select_extra_stop = Select_Extra_Stop(self.shift)
                # get index
                extra_stop_index = select_extra_stop.get_index()
                # display extra stop to user
                if isinstance(extra_stop_index, int):
                    extra_stop = self.shift.extra_stops[extra_stop_index]
                    print(view_extra_stop(extra_stop))
        # split
        elif self.user_selection.lower() == 's':
            from processes.view import view_split
            print(view_split(self.shift.split))
        # carry out tip
        elif self.user_selection.lower() == 't':
            from processes.view import view_tip
            if len(self.shift.carry_out_tips) == 1:
                print(view_tip(self.shift.carry_out_tips[0]))
            elif len(self.shift.carry_out_tips) > 1:
                from processes.select import Select_Carry_Out_Tip
                select_tip = Select_Carry_Out_Tip(self.shift)
                tip_index = select_tip.get_index()
                if isinstance(tip_index, int):
                    print(view_tip(self.shift.carry_out_tips[tip_index]))
        # back
        elif self.user_selection.lower() == 'b':
            self.loop_condition = False


class View_Delivery_Menu:
    # f = full
    # m = main
    # q = quick
    # s = select
    # b = back
    
    def __init__(self, delivery):
        from objects import Delivery
        if not isinstance(delivery, Delivery):
            raise TypeError

        from processes.view import View_Delivery

        self.delivery = delivery
        self.view = View_Delivery(delivery)
        self.prompt =\
            '\n- View Delivery -\n'\
            'F. Full view\n'\
            'M. Main view\n'\
            'Q. Quick view\n'\
            'S. Select sub-part to view\n'\
            'B. Go back\n'

        self.loop_condition = True
        self.main()
        while self.loop_condition:
            self.main()
    
    def main(self):
        from utility.user_input import check_match, user_input

        self.user_selection = user_input(self.prompt)
        while not check_match('^[fmqsb]$', self.user_selection):
            self.user_selection = user_input(self.prompt)
        self.result()

    def result(self):
        # full
        if self.user_selection.lower() == 'f':
            print(self.view.full())
        # main
        elif self.user_selection.lower() == 'm':
            print(self.view.main())
        # quick
        elif self.user_selection.lower() == 'q':
            print(self.view.quick())
        # sub-parts
        elif self.user_selection.lower() == 's':
            View_Delivery_Select_Option(self.delivery)
        # back
        elif self.user_selection.lower() == 'b':
            self.loop_condition = False


class View_Delivery_Select_Option:
    # o = orders
    # e = extra stops
    # b = back

    def __init__(self, delivery):
        from objects import Delivery
        if not isinstance(delivery, Delivery):
            raise TypeError

        self.delivery = delivery
        self.loop_condition = True

        self.main()
        while self.loop_condition:
            self.main()
    
    def build_confirmation_text(self):
        # orders
        if self.user_selection.lower() == 'o':
            self.confirmation_text = 'Select a delivery'
        # extra stops
        elif self.user_selection.lower() == 'e':
            self.confirmation_text = 'Select a extra stop'

    def build_prompt(self):
        # inital
        self.prompt = '\n- Delivery Sub-select -\n'
        # orders
        if len(self.delivery.orders) >= 1:
            self.prompt += 'O. Select order to view\n'
        # extra stops
        if len(self.delivery.extra_stops) >= 1:
            self.prompt += 'E. Select extra stop to view\n'
        # back
        self.prompt += 'B. Go back\n'

    def main(self):
        from utility.user_input import confirm

        self.user_choice()
        while self.user_selection.lower() != 'b' and\
                not confirm(self.confirmation_text):
            self.user_choice()
        self.result()

    def user_choice(self):
        from utility.user_input import check_match, user_input
        # build pattern
        pattern = '^['
        if len(self.delivery.orders) >= 1:
            pattern += 'o'
        if len(self.delivery.extra_stops) >= 1:
            pattern += 'e'
        pattern += 'b]$'
        # user input
        self.build_prompt()
        self.user_selection = user_input(self.prompt)
        while not check_match(pattern, self.user_selection):
            self.user_selection = user_input(self.prompt)
        self.build_confirmation_text()

    def result(self):
        # orders
        if self.user_selection.lower() == 'o':
            from processes.view import view_order
            # 1 order
            if len(self.delivery.orders) == 1:
                from utility.utility import add_newlines
                print(add_newlines(view_order(self.delivery.orders[0])))
                self.loop_condition = False
            # more then 1 order
            elif len(self.delivery.orders) > 1:
                from processes.select import Select_Order
                select_order = Select_Order(self.delivery)
                order_index = select_order.get_index()
                if isinstance(order_index, int):
                    print(view_order(self.delivery.orders[order_index]))
        # extra stops
        elif self.user_selection.lower() == 'e':
            from processes.view import view_extra_stop
            # 1 extra stop
            if len(self.delivery.extra_stops) == 1:
                # display extra stop to user
                print(view_extra_stop(self.delivery.extra_stops[0]))
                self.loop_condition = False
            # more then 1 extra stop
            elif len(self.delivery.extra_stops) > 1:
                from processes.select import Select_Extra_Stop
                # user select extra stop
                select_extra_stop = Select_Extra_Stop(self.delivery)
                # get index
                extra_stop_index = select_extra_stop.get_index()
                if isinstance(extra_stop_index, int):
                    extra_stop = self.delivery.extra_stops[extra_stop_index]
                    # display extra stop to user
                    print(view_extra_stop(extra_stop))
        # back
        elif self.user_selection.lower() == 'b':
            self.loop_condition = False
