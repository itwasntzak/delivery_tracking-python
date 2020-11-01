# todo: current issue is if user chooses to add new object and the program
#           ends, there is no way to detect and continue adding the object

class Revise_Shift:
    # todo: if in progress, dont present the option to add a delivery

    # 1 = start time
    # 2 = end time
    # 3 = total hours
    # 4 = distance
    # 5 = fuel economy
    # 6 = vehical compensation
    # 7 = device compensation
    # 8 = extra tips claimed
    # 9 = total cash in hand
    # d = add/revise/select delivery
    # e = revise/select extra stop
    # c = revise carry out tip
    # v = view current shift data
    # b = back menu

    def __init__(self, shift, test=False):
        from objects import Shift
        if not isinstance(shift, Shift):
            raise TypeError
        else:
            from resources.strings import shift__revise__text

            self.original_shift = shift
            self.shift = shift
            self.file_list = shift.file_list()
            self.text = shift__revise__text
            self.loop_condition = True
            self.changed = False

            if test is False:
                self.main()
                while self.loop_condition:
                    self.main()

    def build_confirmation_text(self):
        # start time
        if self.user_selection == '1':
            if self.shift.start_time is None:
                self.confirmation_text = self.text['start_time'][1]
            else:
                self.confirmation_text = self.text['start_time'][0]
        # end time
        elif self.user_selection == '2':
            if self.shift.end_time is None:
                self.confirmation_text = self.text['end_time'][1]
            else:
                self.confirmation_text = self.text['end_time'][0]
        # total hours
        elif self.user_selection == '3':
            if self.shift.total_hours is None:
                self.confirmation_text = self.text['total_hours'][1]
            else:
                self.confirmation_text = self.text['total_hours'][0]
        # distance
        elif self.user_selection == '4':
            if self.shift.distance is None:
                self.confirmation_text = self.text['distance'][1]
            else:
                self.confirmation_text = self.text['distance'][0]
        # fuel economy
        elif self.user_selection == '5':
            if self.shift.fuel_economy is None:
                self.confirmation_text = self.text['fuel_economy'][1]
            else:
                self.confirmation_text = self.text['fuel_economy'][0]
        # vehicle comp
        elif self.user_selection == '6':
            if self.shift.vehical_compensation is None:
                self.confirmation_text = self.text['vehicle_comp'][1]
            else:
                self.confirmation_text = self.text['vehicle_comp'][0]
        # device comp
        elif self.user_selection == '7':
            if self.shift.device_compensation is None:
                self.confirmation_text = self.text['device_comp'][1]
            else:
                self.confirmation_text = self.text['device_comp'][0]
        # extra tips claimed
        elif self.user_selection == '8':
            if self.shift.extra_tips_claimed is None:
                self.confirmation_text = self.text['extra_tips'][1]
            else:
                self.confirmation_text = self.text['extra_tips'][0]
        # delivery
        elif self.user_selection.lower() == 'd':
            if len(self.shift.deliveries) > 1:
                self.confirmation_text = self.text['delivery'][0]
            elif len(self.shift.deliveries) == 1:
                self.confirmation_text = self.text['delivery'][1]
            elif len(self.shift.deliveries) == 0:
                self.confirmation_text = self.text['delivery'][2]
        # extra stop
        elif self.user_selection.lower() == 'e':
            if len(self.shift.extra_stops) > 1:
                self.confirmation_text = self.text['extra_stop'][0]
            elif len(self.shift.extra_stops) == 1:
                self.confirmation_text = self.text['extra_stop'][1]
        # carry out tips
        elif self.user_selection.lower() == 'c':
            self.confirmation_text = self.text['tips']
        # split
        elif self.user_selection.lower() == 's':
            self.confirmation_text = self.text['split']

    def build_prompt(self):
        # initial
        self.prompt = f"\n{self.text['initial']}\n"
        # start time
        start_time_condition = 0
        if self.shift.start_time is None:
            start_time_condition = 1
        self.prompt += f'1. {self.text["start_time"][start_time_condition]}\n'

        if not self.shift.in_progress:
            # end time
            end_time_condition = 0
            if self.shift.end_time is None:
                end_time_condition = 1
            self.prompt += f'2. {self.text["end_time"][end_time_condition]}\n'
            # total hours
            total_hours_condition = 0
            if self.shift.total_hours is None:
                total_hours_condition = 1
            self.prompt +=\
                f'3. {self.text["total_hours"][total_hours_condition]}\n'
            # distance
            distance_condition = 0
            if self.shift.distance is None:
                distance_condition = 1
            self.prompt +=\
                f'4. {self.text["distance"][distance_condition]}\n'
            # fuel economy
            fuel_economy_condition = 0
            if self.shift.fuel_economy is None:
                fuel_economy_condition = 1
            self.prompt +=\
                f'5. {self.text["fuel_economy"][fuel_economy_condition]}\n'
            # vehicle comp
            vehicle_comp_condition = 0
            if self.shift.vehicle_compensation is None:
                vehicle_comp_condition = 1
            self.prompt +=\
                f'6. {self.text["vehicle_comp"][vehicle_comp_condition]}\n'
            # device comp
            device_comp_condition = 0
            if self.shift.device_compensation is None:
                device_comp_condition = 1
            self.prompt +=\
                f'7. {self.text["device_comp"][device_comp_condition]}\n'
            # extra tips claimed
            extra_tips_condition = 0
            if self.shift.extra_tips_claimed is None:
                extra_tips_condition = 1
            self.prompt +=\
                f'8. {self.text["extra_tips"][extra_tips_condition]}\n'

        # delivery
        delivery_condition = 2
        if len(self.shift.deliveries) == 1:
            delivery_condition = 1
        elif len(self.shift.deliveries) > 1:
            delivery_condition = 0
        self.prompt += f'D. {self.text["delivery"][delivery_condition]}\n'

        # extra stop
        if len(self.shift.extra_stops) == 1:
            self.prompt += f'E. {self.text["extra_stop"][1]}\n'
        elif len(self.shift.extra_stops) > 1:
            self.prompt += f'E. {self.text["extra_stop"][0]}\n'

        # carry out tips
        if len(self.shift.carry_out_tips) > 0:
            self.prompt += f'C. {self.text["tips"]}\n'

        # split
        if self.shift.split is not None:
            self.prompt += f'S. {self.text["split"]}\n'

        # back
        self.prompt += f'B. Go back\n'

    def main(self):
        from utility.user_input import confirm

        self.user_choice()
        while self.user_selection.lower() not in ('v', 'b') and\
                not confirm(self.confirmation_text):
            self.user_choice()
        self.result()

    def user_choice(self):
        from utility.user_input import check_match, user_input

        pattern = '^[1'
        if not self.shift.in_progress:
            pattern += '-8'
        if len(self.shift.carry_out_tips) > 0:
            pattern += 'c'
        if self.shift.split is not None:
            pattern += 's'
        pattern += 'devb]$'

        self.build_prompt()
        self.user_selection = user_input(self.prompt)
        while not check_match(pattern, self.user_selection):
            self.user_selection = user_input(self.prompt)
        self.build_confirmation_text()

    def result(self):
        # start time
        if self.user_selection == '1':
            self.shift.change_start_time()
        # end time
        elif self.user_selection == '2':
            self.shift.change_end_time()
        # total hours
        elif self.user_selection == '3':
            self.shift.change_total_hours()
        # distance
        elif self.user_selection == '4':
            self.shift.change_distance()
        # fuel economy
        elif self.user_selection == '5':
            self.shift.change_fuel_economy()
        # vehicle comp
        elif self.user_selection == '6':
            self.shift.change_vehicle_compensation()
        # device comp
        elif self.user_selection == '7':
            self.shift.change_device_compensation()
        # extra tips claimed
        elif self.user_selection == '8':
            self.shift.change_extra_tips_claimed()
        # delivery
        elif self.user_selection.lower() == 'd':
            delivery_option = Delivery_Option(self.shift)
            self.shift = delivery_option.shift
        # extra stop
        elif self.user_selection.lower() == 'e':
            self.shift = extra_stop_option(self.shift)
        # carry out tip
        elif self.user_selection.lower() == 'c':
            from processes.select import Select_Carry_Out_Tip
            from utility.file import write
            # user select a carry out tip to revise
            select_tip = Select_Carry_Out_Tip(self.shift)
            # get tip index
            tip_index = select_tip.get_index()
            if isinstance(tip_index, int):
                # user revises tip
                revise_tip = Revise_Tip(self.shift.carry_out_tips[tip_index])
                # update shift carry out tips list
                self.shift.carry_out_tips[tip_index] = revise_tip.tip
                # make string to update carry out tips file
                data = ''
                for tip in self.shift.carry_out_tips:
                    data += f'{tip.csv()}\n'
                # remove trailing newline
                if data[-1] == '\n':
                    data = data[:-1]
                # rewrite file with revised carry out tip
                write(data, self.shift.file_list()['tips'])
        # split
        elif self.user_selection.lower() == 's':
            revise_split = Revise_Split(self.shift.split)
            self.shift.split = revise_split.split
        # view
        elif self.user_selection.lower() == 'v':
            from processes.view import View_Shift
            print(View_Shift(self.shift).main())
        # back
        elif self.user_selection.lower() == 'b':
            self.loop_condition = False


class Revise_Delivery:
    # todo: if in progress, dont present the option to add a order

    # 1 = start time
    # 2 = distance
    # 3 = average speed
    # 4 = end time
    # o = order selection/revision
    # e = extra stop selection/revision
    # v = view current values of delivery
    # b = go back

    def __init__(self, delivery, test=False):
        from objects import Delivery
        if not isinstance(delivery, Delivery):
            raise TypeError

        from resources.strings import delivery__revise

        self.original_delivery = delivery
        self.delivery = delivery
        self.display_text = delivery__revise
        self.loop_condition = True
        self.changed = False

        if test is False:
            self.main()
            while self.loop_condition:
                self.main()

    def build_confirmation_text(self):
        # todo: need to finish writting unittest for this method
        from datetime import datetime
        # start time
        if self.user_selection == '1':
            if isinstance(self.delivery.start_time, datetime):
                self.confirmation_text = self.display_text['start_time'][0]
            elif self.delivery.start_time is None:
                self.confirmation_text = self.display_text['start_time'][1]
        # distance
        elif self.user_selection == '2':
            if isinstance(self.delivery.distance, float):
                self.confirmation_text = self.display_text['distance'][0]
            elif self.delivery.distance is None:
                self.confirmation_text = self.display_text['distance'][1]
        # average speed
        elif self.user_selection == '3':
            if isinstance(self.delivery.average_speed, int):
                self.confirmation_text = self.display_text['average_speed'][0]
            elif self.delivery.average_speed is None:
                self.confirmation_text = self.display_text['average_speed'][1]
        # end time
        elif self.user_selection == '4':
            if isinstance(self.delivery.end_time, datetime):
                self.confirmation_text = self.display_text['end_time'][0]
            elif self.delivery.end_time is None:
                self.confirmation_text = self.display_text['end_time'][1]
        # order
        elif self.user_selection.lower() == 'o':
            if len(self.delivery.orders) > 1:
                self.confirmation_text = f'{self.display_text["order"][0]}/'\
                                         f'{self.display_text["order"][2]}'
            elif len(self.delivery.orders) == 1:
                self.confirmation_text = f'{self.display_text["order"][1]}/'\
                                         f'{self.display_text["order"][2]}'
            elif len(self.delivery.orders) == 0:
                self.confirmation_text = self.display_text['order'][2]
        # extra stop
        elif self.user_selection.lower() == 'e':
            if len(self.delivery.extra_stops) > 1:
                self.confirmation_text = self.display_text['extra_stop'][0]
            elif len(self.delivery.extra_stops) == 1:
                self.confirmation_text = self.display_text['extra_stop'][1]

    def build_prompt(self):
        from datetime import datetime

        # initial
        self.prompt = f'\n{self.display_text["initial"]}\n'

        # start time
        if isinstance(self.delivery.start_time, datetime):
            start_time_condition = 0
        elif self.delivery.start_time is None:
            start_time_condition = 1
        self.prompt +=\
            f'1. {self.display_text["start_time"][start_time_condition]}\n'

        if not self.delivery.in_progress:
            # distance
            if isinstance(self.delivery.distance, float):
                distance_condition = 0
            elif self.delivery.distance is None:
                distance_condition = 1
            self.prompt +=\
                f'2. {self.display_text["distance"][distance_condition]}\n'

            # average speed
            if isinstance(self.delivery.average_speed, int):
                average_speed_condition = 0
            elif self.delivery.average_speed is None:
                average_speed_condition = 1
            self.prompt +=\
                f'3. {self.display_text["average_speed"][average_speed_condition]}\n'

            # end time
            if isinstance(self.delivery.end_time, datetime):
                end_time_condition = 0
            elif self.delivery.end_time is None:
                end_time_condition = 1
            self.prompt +=\
                f'4. {self.display_text["end_time"][end_time_condition]}\n'

        # order
        self.prompt += 'O. '
        if len(self.delivery.orders) > 1:
            self.prompt += f'{self.display_text["order"][0]}/'\
                            f'{self.display_text["order"][2]}\n'
        elif len(self.delivery.orders) == 1:
            self.prompt += f'{self.display_text["order"][1]}/'\
                            f'{self.display_text["order"][2]}\n'
        elif len(self.delivery.orders) == 0:
            self.prompt += f'{self.display_text["order"][2]}\n'

        # extra stop
        if len(self.delivery.extra_stops) == 1:
            self.prompt += f'E. {self.display_text["extra_stop"][1]}\n'
        elif len(self.delivery.extra_stops) > 1:
            self.prompt += f'E. {self.display_text["extra_stop"][0]}\n'

        # view
        self.prompt += f'V. {self.display_text["view"]}\n'
        # back
        self.prompt += f'B. {self.display_text["back"]}\n'

    def main(self):
        from utility.user_input import confirm
        self.user_choice()
        while self.user_selection.lower() not in ('v', 'b') and\
                not confirm(self.confirmation_text):
            self.user_choice()
        self.result()

    def user_choice(self):
        from utility.user_input import check_match, user_input

        pattern = '^[1oevb]$'
        if not self.delivery.in_progress:
            pattern = '^[1-4oevb]$'

        self.build_prompt()
        self.user_selection = user_input(self.prompt)
        while not check_match(pattern, self.user_selection):
            self.user_selection = user_input(self.prompt)
        self.build_confirmation_text()

    def result(self):
        # start time
        if self.user_selection == '1':
            self.delivery.change_start_time()
        # distance
        elif self.user_selection == '2':
            self.delivery.change_distance()
        # average speed
        elif self.user_selection == '3':
            self.delivery.change_average_speed()
        # end time
        elif self.user_selection == '4':
            self.delivery.change_end_time()
        # orders
        elif self.user_selection.lower() == 'o':
            order_option = Order_Option(self.delivery)
            self.delivery = order_option.delivery
        # extra stop
        elif self.user_selection.lower() == 'e':
            self.delivery = extra_stop_option(self.delivery)
        # view
        elif self.user_selection.lower() == 'v':
            # todo: create view function or class to allow user to view sub parts
            from processes.view import View_Delivery
            print(View_Delivery(self.delivery).main())
        # back
        elif self.user_selection.lower() == 'b':
            self.loop_condition = False


class Revise_Order:
    # 1 = id
    # 2 = tip
    # 3 = miles traveled
    # 4 = end time
    # v = view current tip values
    # b = go back

    def __init__(self, order, test=False):
        # todo: Edit_Order first thing, display the current order data to the user
        # todo: then resent the user with the option to select what data of the order to edit
        from objects import Order
        if not isinstance(order, Order):
            raise TypeError

        self.original_order =  order
        self.order = order
        self.loop_condition = True
        self.changed = False

        if test is False:
            self.main()
            while self.loop_condition:
                self.main()

    def build_confirmation_text(self):
        # todo: need to add conditional text generation
        # id
        if self.user_selection == '1':
            self.confirmation_text = 'Change order id'
        # tip
        elif self.user_selection == '2':
            self.confirmation_text = 'Change the tip'
        # miles traveled
        elif self.user_selection == '3':
            self.confirmation_text = 'Change miles traveled'
        # end time
        elif self.user_selection == '4':
            self.confirmation_text = 'Change end time'

    def build_prompt(self):
        # todo: need to add conditional prompt generation
        self.prompt =\
            '\n- Revise Order -\n'\
            '1. Add/edit I.D.\n'\
            '2. Add/edit tip\n'\
            '3. Add/edit miles traveled\n'\
            '4. Add/edit end time\n'\
            'V. View current order values\n'\
            'B. Go back\n'

    def main(self):
        from utility.user_input import confirm
        self.user_choice()
        while self.user_selection.lower() not in ('v', 'b') and\
                not confirm(self.confirmation_text):
            self.user_choice()
        self.result()

    def user_choice(self):
        from utility.user_input import check_match, user_input

        self.build_prompt()
        self.user_selection = user_input(self.prompt)
        while not check_match('^[1-4vb]$', self.user_selection):
            self.user_selection = user_input(self.prompt)
        self.build_confirmation_text()
    
    def result(self):
        # id
        if self.user_selection == '1':
            self.order.change_id()
        # tip
        elif self.user_selection == '2':
            self.order.change_tip()
        # miles traveled
        elif self.user_selection == '3':
            self.order.change_distance()
        # end time
        elif self.user_selection == '4':
            self.order.change_end_time()
        # view
        elif self.user_selection.lower() == 'v':
            from processes.view import view_order
            print(view_order(self.order))
        # back
        elif self.user_selection.lower() == 'b':
            # todo: if order has been changed but not saved, need to add warning
            self.loop_condition = False


class Revise_Tip:
    # 1 = card
    # 2 = cash
    # 3 = both
    # u = unknown
    # v = view
    # b = back

    def __init__(self, tip, test=False):
        from objects import Tip
        if not isinstance(tip, Tip):
            raise TypeError

        from resources.strings import tip_revise_text

        self.original_tip = tip
        self.tip = tip
        self.text = tip_revise_text
        self.menu_condition = True
        self.save_condition = False

        if test is False:
            self.main()
            while self.menu_condition:
                self.main()
    
    def main(self):
        from utility.user_input import confirm
        self.user_choice()
        while self.user_selection.lower() not in ('v', 'b') and\
                not confirm(self.confirmation):
            self.user_choice()
        self.result()
    
    def build_prompt(self):
        from utility.utility import add_newlines
        # initial
        self.prompt = add_newlines(self.text['initial'])
        # card
        card_condition = 0
        if self.tip.card != 0.0:
            card_condition = 1
        self.prompt += f'1. {self.text["card"][card_condition]}\n'
        # cash
        cash_condition = 0
        if self.tip.cash != 0.0:
            cash_condition = 1
        self.prompt += f'2. {self.text["cash"][cash_condition]}\n'
        # card and cash
        self.prompt += f'3. {self.text["both"]}\n'
        # unknown
        unknown_condition = 0
        if self.tip.unknown != 0.0:
            unknown_condition = 1
        self.prompt += f'U. {self.text["unknown"][unknown_condition]}\n'
        # view
        self.prompt += f'V. {self.text["view"]}\n'
        # back
        self.prompt += f'B. {self.text["back"]}\n'

    def build_confirmation(self):
        # card
        if self.user_selection == '1':
            card_condition = 0
            if self.tip.card != 0.0:
                card_condition = 1
            self.confirmation = f"{self.text['card'][card_condition]}"
        # cash
        elif self.user_selection == '2':
            cash_condition = 0
            if self.tip.cash != 0.0:
                cash_condition = 1
            self.confirmation = f"{self.text['cash'][cash_condition]}"
        # card and cash
        elif self.user_selection == '3':
            self.confirmation = f"{self.text['both']}"
        # unknown
        elif self.user_selection.lower() == 'u':
            unknown_condition = 0
            if self.tip.unknown != 0.0:
                unknown_condition = 1
            self.confirmation = f"{self.text['unknown'][unknown_condition]}"
        
    def user_choice(self):
        from utility.user_input import check_match, user_input

        self.build_prompt()

        self.user_selection = user_input(self.prompt)
        while not check_match('^[123uvb]$', self.user_selection):
            print('Error: Please enter one of the presented options')
            self.user_selection = user_input(self.prompt)

        self.build_confirmation()

    def result(self):
        from utility.utility import to_money
        # card
        if self.user_selection == '1':
            print(f'\nCurrent card tip: {to_money(self.tip.card)}')
            self.tip.input_card()
        # cash
        elif self.user_selection == '2':
            print(f'\nCurrent cash tip: {to_money(self.tip.cash)}')
            self.tip.input_cash()
        # card and cash
        elif self.user_selection == '3':
            print(f'\nCurrent card tip: {to_money(self.tip.card)}')
            print(f'\nCurrent cash tip: {to_money(self.tip.cash)}')
            self.tip.input_both()
        # unknown
        elif self.user_selection.lower() == 'u':
            # todo: need to add part to check if card and/or cash are not 
            #   zero, and then present the user with the apropeate options
            print(f'\nCurrent unknown tip: {to_money(self.tip.unknonw)}')
            self.tip.input_unknown()
        # view
        elif self.user_selection.lower() == 'v':
            from processes.view import view_tip
            print(view_tip(self.tip))
        # back
        elif self.user_selection.lower() == 'b':
            # todo: need to add warning if changes have been made but not saved
            self.menu_condition = False


class Revise_Split:
    # 1 = start time
    # 2 = distance
    # 3 = end time
    # v = view
    # b = back

    def __init__(self, split, test=False):
        from objects import Split
        if not isinstance(split, Split):
            raise TypeError

        self.original_split = split
        self.split = split
        self.loop_condition = True
        self.changed = False

        if test is False:
            self.main()
            while self.loop_condition:
                self.main()
    
    def main(self):
        from utility.user_input import confirm

        self.user_choice()
        while self.user_selection not in ('v', 'b') and\
                not confirm(self.confirmation_text):
            self.user_choice()
        self.result()

    def build_confirmation_text(self):
        # start time
        if self.user_selection == '1':
            self.confirmation_text = 'Change start time'
        # distance
        elif self.user_selection == '2':
            self.confirmation_text = 'Change miles traveled'
        # end time
        elif self.user_selection == '3':
            self.confirmation_text = 'Change end time'

    def build_prompt(self):
        self.prompt =\
            '\n- Revise Split -\n'\
            'Please select an option:\n'\
            '1. Change start time\n'\
            '2. Change miles traveled\n'\
            '3. Change end time\n'\
            'V. View current split values\n'\
            'B. Go back\n'

    def user_choice(self):
        from utility.user_input import check_match, user_input
        self.build_prompt()

        self.user_selection = user_input(self.prompt)
        while not check_match('^[123vb]$', self.user_selection):
            self.user_selection = user_input(self.prompt)

        self.build_confirmation_text()

    def result(self):
        # start time
        if self.user_selection == '1':
            self.split.change_start_time()
        # distance
        elif self.user_selection == '2':
            self.split.change_distance()
        # end time
        elif self.user_selection == '3':
            self.split.change_end_time()
        # view
        elif self.user_selection.lower() == 'v':
            from processes.view import view_split
            print(view_split(self.split))
        # back
        elif self.user_selection.lower() == 'b':
            self.loop_condition = False


class Revise_Extra_Stop:
    # 1 = location
    # 2 = reason
    # 3 = distance
    # 4 = end time
    # 5 = start time (if parent is shift)
    # v = view
    # b = back

    def __init__(self, extra_stop, test=False):
        from objects import Extra_Stop
        if not isinstance(extra_stop, Extra_Stop):
            raise TypeError

        self.original_extra_stop = extra_stop
        self.extra_stop = extra_stop
        self.loop_condition = True
        self.changed = False

        if test is False:
            self.main()
            while self.loop_condition:
                self.main()

    def main(self):
        from utility.user_input import confirm

        self.user_choice()
        while self.user_selection not in ('b', 'v') and\
                not confirm(self.confirmation_text):
            self.user_choice()
        self.result()

    def build_confirmation_text(self):
        # location
        if self.user_selection == '1':
            self.confirmation_text = 'Change location'
        # reason
        elif self.user_selection == '2':
            self.confirmation_text = 'Change reason'
        # distance
        elif self.user_selection == '3':
            self.confirmation_text = 'Change miles traveled'
        # end time
        elif self.user_selection == '4':
            self.confirmation_text = 'Change end time'
        # start time
        elif self.user_selection == '5':
            self.confirmation_text = 'Change start time'

    def build_prompt(self):
        # todo: need to write conditional prompt generation
        self.prompt =\
            '\n- Revise Extra Stop -\n'\
            'Please select an option:\n'\
            '1. Change location\n'\
            '2. Change reason\n'\
            '3. Change miles traveled\n'\
            '4. Change end time\n'\
            '5. Change start time\n'\
            'V. View current extra stop values\n'\
            'B. Go back\n'

    def user_choice(self):
        from objects import Shift
        from utility.user_input import check_match, user_input

        pattern = '^[1-4vb]$'
        if isinstance(self.extra_stop.parent, Shift):
            pattern = '^[1-5vb]$'

        self.build_prompt()
        self.user_selection = user_input(self.prompt)
        while not check_match(pattern, self.user_selection):
            self.user_selection = user_input(self.prompt)

        self.build_confirmation_text()

    def result(self):
        # location
        if self.user_selection == '1':
            self.extra_stop.change_location()
        # reason
        elif self.user_selection == '2':
            self.extra_stop.change_reason()
        # distance
        elif self.user_selection == '3':
            self.extra_stop.change_distance()
        # end time
        elif self.user_selection == '4':
            self.extra_stop.change_end_time()
        # start time
        elif self.user_selection == '5':
            self.extra_stop.change_start_time()
        # view
        elif self.user_selection.lower() == 'v':
            from processes.view import view_extra_stop
            print(view_extra_stop(self.extra_stop))
        # back
        elif self.user_selection.lower() == 'b':
            self.loop_condition = False
        
        if self.extra_stop.collection() != self.original_extra_stop.collection():
            self.changed = True


class Delivery_Option:
    # r = revise
    # s = select
    # a = add
    # b = back

    def __init__(self, shift, test=False):
        from objects import Shift
        if not isinstance(shift, Shift):
            raise TypeError

        self.shift = shift
        self.loop_condition = True

        if test is False:
            self.main()
            while self.loop_condition:
                self.main()

    def build_confirmation_text(self):
        # revise
        if self.user_selection.lower() == 'r':
            self.confirmation_text = 'Revise delivery'
        # select
        elif self.user_selection.lower() == 's':
            self.confirmation_text = 'Select a delivery'
        # add
        elif self.user_selection.lower() == 'a':
            self.confirmation_text = 'Add delivery'

    def build_prompt(self):
        # initial
        self.prompt = '\nPlease select an option:\n'
        # one delivery
        if len(self.shift.deliveries) == 1:
            self.prompt += 'R. Revise delivery\n'
        # more then one delivery
        elif len(self.shift.deliveries) > 1:
            self.prompt += 'S. Select a delivery\n'
        # add delivery
        self.prompt += 'A. Add delivery\n'
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

        pattern = '^[ab]$'
        if len(self.shift.deliveries) == 1:
            pattern = '^[rab]$'
        elif len(self.shift.deliveries) > 1:
            pattern = '^[sab]$'

        self.build_prompt()
        self.user_selection = user_input(self.prompt)
        while not check_match(pattern, self.user_selection):
            self.user_selection = user_input(self.prompt)
        self.build_confirmation_text()

    def result(self):
        # revise
        if self.user_selection.lower() == 'r':
            # revise delivery
            revise_delivery = Revise_Delivery(self.shift.deliveries[0])
            # update shift
            self.shift.deliveries[0] = revise_delivery.delivery
        # select
        elif self.user_selection.lower() == 's':
            from processes.select import Select_Delivery
            # user selects delivery
            select_delivery = Select_Delivery(self.shift)
            # get delivery index in shift list
            delivery_index = select_delivery.get_index()
            # revise delivery
            revise_delivery =\
                Revise_Delivery(self.shift.deliveries[delivery_index])
            # update shift
            self.shift.deliveries[delivery_index] = revise_delivery.delivery
        # add
        elif self.user_selection.lower() == 'a':
            from objects import Delivery
            # delivery
            delivery = Delivery(self.shift)
            # start delivery
            delivery.start()
            # end and add delivery
            self.shift.add_delivery(delivery.end())
        # back
        elif self.user_selection.lower() == 'b':
            self.loop_condition = False


class Order_Option:
    # r = revise
    # s = select
    # a = add
    # b = back

    def __init__(self, delivery, test=False):
        from objects import Delivery
        if not isinstance(delivery, Delivery):
            raise TypeError

        self.delivery = delivery
        self.loop_condition = True

        if test is False:
            self.main()
            while self.loop_condition:
                self.main()

    def build_confirmation_text(self):
        # revise
        if self.user_selection.lower() == 'r':
            self.confirmation_text = 'Revise only order'
        # select
        if self.user_selection.lower() == 's':
            self.confirmation_text = 'Select order to revise'
        # add
        elif self.user_selection.lower() == 'a':
            self.confirmation_text = 'Add order'

    def build_prompt(self):
        # initial
        self.prompt = '\nPlease make a selection:\n'
        # revise order
        if len(self.delivery.orders) == 1:
            self.prompt += 'R. Revise only order\n'
        # select an order
        elif len(self.delivery.orders) > 1:
            self.prompt += 'S. Select order to revise\n'
        # add order
        self.prompt += 'A. Add order\n'
        # back
        self.prompt += 'B. Go back\n'

    def main(self):
        from utility.user_input import confirm

        self.user_choice()
        while self.user_selection.lower() != 'b' and\
                not confirm(self.confirmation_text):
            self.user_choice()
        self.result()

    def  user_choice(self):
        from utility.user_input import check_match, user_input

        pattern = '^[ab]$'
        if len(self.delivery.orders) == 1:
            pattern = '^[rab]$'
        elif len(self.delivery.orders) > 1:
            pattern = '^[sab]$'
        
        self.build_prompt()
        self.user_selection = user_input(self.prompt)
        while not check_match(pattern, self.user_selection):
            self.user_selection = user_input(self.prompt)
        self.build_confirmation_text()

    def result(self):
        # revise
        if self.user_selection.lower() == 'r':
            revise_order = Revise_Order(self.delivery.orders[0])
            if revise_order.changed is True:
                self.delivery.orders[0] = revise_order.order
                if revise_order.order.id != revise_order.original_order.id:
                    self.delivery.order_ids[0] = revise_order.order.id
        # select
        if self.user_selection.lower() == 's':
            from processes.select import Select_Order
            # select order
            order_index = Select_Order(self.delivery).get_index()
            # revise order
            revise_order = Revise_Order(self.delivery.orders[order_index])
            # update changed order to delivery orders list
            self.delivery.orders[order_index] = revise_order.order
            # if order id was changed update the delivery order ids list
            if revise_order.order.id != revise_order.original_order.id:
                self.delivery.order_id[order_index] = revise_order.order.id
        # add
        elif self.user_selection.lower() == 'a':
            from processes.track import track_order
            self.delivery.add_order(track_order(self.delivery))
        # back
        elif self.user_selection.lower() == 'b':
            self.loop_condition = False


def extra_stop_option(parent):
    # revise
    if len(parent.extra_stops) == 1:
        # revise extra stop
        revise_extra_stop = Revise_Extra_Stop(parent.extra_stops[0])
        # update parent list with revised extra stop
        parent.extra_stops[0] = revise_extra_stop.extra_stop
    # select
    elif len(parent.extra_stops) > 1:
        from processes.select import Select_Extra_Stop
        # user selects extra stop
        select_extra_stop = Select_Extra_Stop(parent)
        # get index of extra stop
        extra_stop_index = select_extra_stop.get_index()
        if isinstance(extra_stop_index, int):
            # revise extra stop
            revise_extra_stop =\
                Revise_Extra_Stop(parent.extra_stops[extra_stop_index])
            # update parent list with revised extra stop
            parent.extra_stops[extra_stop_index] = revise_extra_stop.extra_stop

    return parent
