
# first the user enters their selection
#   based on the selection and the state of the passed in object, confirmation text will be returned
# after the user confirms thier selection it will handle the indavidual result

# i think there should be one class for the actual revision/manipulation of deliveries
# and then another class that is the menu the user interacts with, that uses the revision class

import processes.input


class Revise_Ongoing_Shift(input_data.Input_Shift):
    # todo: think it would be best to have ongoing and completed in one menu
    #           have different methods for both

    # options
    # 1 = start time
    # 2 = end time
    # 3 = total hours
    # 4 = distance
    # 5 = fuel economy
    # 6 = vehical compensation
    # 7 = device compensation
    # 8 = extra tips claimed
    # 9 = total cash in hand
    # dD = add/revise/select delivery
    # eE = add/revise/select extra stop
    # vV = view current shift data
    # bB = back menu

    def __init__(self, shift):
        from objects.shift import Shift
        if not isinstance(shift, Shift):
            raise TypeError
        else:
            from resources.strings import shift__revise__text
            self.condition = True
            self.shift = shift
            self.file_list = shift.file_list()
            self.display_text = shift__revise__text

    def completed(self):
        import re
        from utility.user_input import confirmation

        def build_confirmation_text(self):
            from datetime import datetime
            # start time
            if re.match('[1]', self.user_choice):
                if isinstance(self.shift.start_time, datetime):
                    self.confirmation_text = self.display_text['start_time'][0]
                elif self.shift.start_time is None:
                    self.confirmation_text = self.display_text['start_time'][1]
            # end time
            elif re.match('[2]', self.user_choice):
                if isinstance(self.shift.end_time, datetime):
                    self.confirmation_text = self.display_text['end_time'][0]
                elif self.shift.end_time is None:
                    self.confirmation_text = self.display_text['end_time'][1]
            # total hours
            elif re.match('[3]', self.user_choice):
                if isinstance(self.shift.total_hours, float):
                    self.confirmation_text = self.display_text['total_hours'][0]
                elif self.shift.total_hours is None:
                    self.confirmation_text = self.display_text['total_hours'][1]
            # distance
            elif re.match('[4]', self.user_choice):
                if isinstance(self.shift.distance, datetime):
                    self.confirmation_text = self.display_text['distance'][0]
                elif self.shift.distance is None:
                    self.confirmation_text = self.display_text['distance'][1]
            # fuel economy
            elif re.match('[5]', self.user_choice):
                self.confirmation_text = self.display_text['start_time'][0]
            # vehical comp
            elif re.match('[6]', self.user_choice):
                self.confirmation_text = self.display_text['start_time'][0]
            # device comp
            elif re.match('[7]', self.user_choice):
                self.confirmation_text = self.display_text['start_time'][0]
            # extra tips claimed
            elif re.match('[8]', self.user_choice):
                self.confirmation_text = self.display_text['start_time'][0]
            # total in hand
            elif re.match('[9]', self.user_choice):
                self.confirmation_text = self.display_text['start_time'][0]
            # delivery
            elif re.match('[d]', self.user_choice, flags=re.IGNORECASE):
                if len(self.shift.deliveries) > 1:
                    self.confirmation_text = self.display_text['delivery'][0]
                elif len(self.shift.deliveries) == 1:
                    self.confirmation_text = self.display_text['delivery'][1]
            # extra stop
            elif re.match('[e]', self.user_choice, flags=re.IGNORECASE):
                if len(self.shift.extra_stops) > 1:
                    self.confirmation_text = self.display_text['extra_stop'][0]
                elif len(self.shift.extra_stops) == 1:
                    self.confirmation_text = self.display_text['extra_stop'][1]

        def build_prompt(self):
            from datetime import datetime
            # initial
            self.prompt = self.display_text['initial']
            # start time
            self.prompt += '1. '
            if isinstance(self.shift.start_time, datetime):
                self.prompt += self.display_text['start_time'][0]
            elif self.shift.start_time is None:
                self.prompt += self.display_text['start_time'][1]
            # delivery
            self.prompt += 'D. '
            if len(self.shift.deliveries) > 1:
                self.prompt += self.display_text['delivery'][0]
            elif len(self.shift.deliveries) == 1:
                self.prompt += self.display_text['delivery'][1]
            elif len(self.shift.deliveries) == 0:
                self.prompt += self.display_text['delivery'][2]
            # extra stop
            self.prompt += 'E. '
            if len(self.shift.extra_stops) > 1:
                self.prompt += self.display_text['extra_stop'][0]
            elif len(self.shift.extra_stops) == 1:
                self.prompt += self.display_text['extra_stop'][1]
            # view
            self.prompt += f'V. {self.display_text["view"]}'
            # back
            self.prompt += f'B. {self.display_text["back"]}'

        def option_selection(self):
            from utility.user_input import match_input
            build_prompt()
            self.user_choice = match_input(self.prompt, '^[1devb]$')
            build_confirmation_text()
        
        def result(self):
            import re
            from processes.input import Input_Shift

            # start time
            if re.match('[1]', self.user_choice, flags=re.IGNORECASE):
                # todo: update with datetime edit class when written
                pass
            # end time
            elif re.match('[2]', self.user_choice, flags=re.IGNORECASE):
                # todo: update with datetime edit class when written
                pass
            # total hours
            elif re.match('[3]', self.user_choice, flags=re.IGNORECASE):
                self.shift.total_hours = Input_Shift().total_hours()
            # distance
            elif re.match('[4]', self.user_choice, flags=re.IGNORECASE):
                self.shift.distance - Input_Shift().miles_traveled()
            # fuel economy
            elif re.match('[5]', self.user_choice, flags=re.IGNORECASE):
                self.shift.fuel_economy = Input_Shift().fuel_economy()
            # vehical compensation
            elif re.match('[6]', self.user_choice, flags=re.IGNORECASE):
                self.shift.vehical_compensation =\
                    Input_Shift().vehical_compensation()
            # device compensation
            elif re.match('[7]', self.user_choice, flags=re.IGNORECASE):
                self.shift.device_compensation =\
                    Input_Shift().device_compensation()
            # extra tips claimed
            elif re.match('[8]', self.user_choice, flags=re.IGNORECASE):
                self.shift.extra_tips_claimed =\
                    Input_Shift().extra_tips_claimed()
            # total cash in hand
            elif re.match('[9]', self.user_choice, flags=re.IGNORECASE):
                pass
            # delivery
            elif re.match('[d]', self.user_choice, flags=re.IGNORECASE):
                if len(self.shift.deliveries) == 1:
                    delivery = self.shift.deliveries[0]
                    revised = Revise_Delivery(delivery).completed()
                    while revised.condition:
                        revised = Revise_Delivery(delivery).completed()
                    self.shift.deliveries[delivery_id] = revised.delivery
                elif len(self.shift.deliveries) > 1:
                    from processes.select import Select_Delivery
                    delivery_id = Select_Delivery(self.shift).get_id()
                    if delivery_id is int:
                        delivery = self.shift.deliveries[delivery_id]
                        revised = Revise_Delivery(delivery).completed()
                        while revised.condition:
                            revised = Revise_Delivery(delivery).completed()
                        self.shift.deliveries[delivery_id] = revised.delivery
            # extra stop
            elif re.match('[e]', self.user_choice, flags=re.IGNORECASE):
                # todo: update with select extra stop once written
                # todo: update with revise extra stop once written
                pass
            # view
            elif re.match('[v]', self.user_choice, flags=re.IGNORECASE):
                # todo: need to update view.shift to a class and add more functionality
                pass
            # back
            elif re.match('[b]', self.user_choice, flags=re.IGNORECASE):
                self.condition = False

            # update file with any changes
            if re.match('[1-9]', self.user_choice):
                from utility.file import write
                write(self.shift.csv(), self.file_list['info'])

        option_selection()
        while not re.match('[vb]', self.user_choice, flags=re.IGNORECASE)\
                and not confirmation(self.confirmation_text):
            option_selection()
        result()
        return self

    def ongoing(self):
        import re
        from utility.user_input import confirmation

        def build_confirmation_text(self):
            # start time
            if re.match('[1]', self.user_choice):
                self.confirmation_text = self.display_text['start_time'][0]
            # delivery
            elif re.match('[d]', self.user_choice, flags=re.IGNORECASE):
                if len(self.shift.deliveries) > 1:
                    self.confirmation_text = self.display_text['delivery'][0]
                elif len(self.shift.deliveries) == 1:
                    self.confirmation_text = self.display_text['delivery'][1]
            # extra stop
            elif re.match('[e]', self.user_choice, flags=re.IGNORECASE):
                if len(self.shift.extra_stops) > 1:
                    self.confirmation_text = self.display_text['extra_stop'][0]
                elif len(self.shift.extra_stops) == 1:
                    self.confirmation_text = self.display_text['extra_stop'][1]

        def build_prompt(self):
            from datetime import datetime
            # initial
            self.prompt = self.display_text['initial']
            # start time
            self.prompt += '1. '
            if isinstance(self.shift.start_time, datetime):
                self.prompt += self.display_text['start_time'][0]
            elif self.shift.start_time is None:
                self.prompt += self.display_text['start_time'][1]
            # delivery
            self.prompt += 'D. '
            if len(self.shift.deliveries) > 1:
                self.prompt += self.display_text['delivery'][0]
            elif len(self.shift.deliveries) == 1:
                self.prompt += self.display_text['delivery'][1]
            elif len(self.shift.deliveries) == 0:
                self.prompt += self.display_text['delivery'][2]
            # extra stop
            self.prompt += 'E. '
            if len(self.shift.extra_stops) > 1:
                self.prompt += self.display_text['extra_stop'][0]
            elif len(self.shift.extra_stops) == 1:
                self.prompt += self.display_text['extra_stop'][1]
            # view
            self.prompt += f'V. {self.display_text["view"]}'
            # back
            self.prompt += f'B. {self.display_text["back"]}'

        def option_selection(self):
            from utility.user_input import match_input
            build_prompt()
            self.user_choice = match_input(self.prompt, '^[1devb]$')
            build_confirmation_text()
        
        def result(self):
            import re
            # start time
            if re.match('[1]', self.user_choice, flags=re.IGNORECASE):
                # todo: update with datetime edit class when written
                pass
            # delivery
            elif re.match('[d]', self.user_choice, flags=re.IGNORECASE):
                if len(self.shift.deliveries) == 1:
                    delivery = self.shift.deliveries[0]
                    revised = Revise_Delivery(delivery).completed()
                    while revised.condition:
                        revised = Revise_Delivery(delivery).completed()
                    self.shift.deliveries[delivery_id] = revised.delivery
                elif len(self.shift.deliveries) > 1:
                    from processes.select import Select_Delivery
                    delivery_id = Select_Delivery(self.shift).get_id()
                    if delivery_id is int:
                        delivery = self.shift.deliveries[delivery_id]
                        revised = Revise_Delivery(delivery).completed()
                        while revised.condition:
                            revised = Revise_Delivery(delivery).completed()
                        self.shift.deliveries[delivery_id] = revised.delivery
            # extra stop
            elif re.match('[e]', self.user_choice, flags=re.IGNORECASE):
                # todo: update with select extra stop once written
                # todo: update with revise extra stop once written
                pass
            # view
            elif re.match('[v]', self.user_choice, flags=re.IGNORECASE):
                # todo: need to update view.shift to a class and add more functionality
                pass
            # back
            elif re.match('[b]', self.user_choice, flags=re.IGNORECASE):
                self.condition = False

        option_selection()
        while not re.match('[vb]', self.user_choice, flags=re.IGNORECASE)\
                and not confirmation(self.confirmation_text):
            option_selection()
        result()
        return self


class Revise_Delivery(input_data.Input_Delivery):
    # this class will be accessed but ongoing shift menu and completed shift menu

    # options
    # 1 = start time
    # 2 = distance
    # 3 = average speed
    # 4 = end time
    # oO = order selection/revision
    # eE = extra stop selection/revision
    # vV = view current values of delivery
    # bB = back a menu

    def __init__(self, delivery):
        from objects.delivery import Delivery
        if not isinstance(delivery, Delivery):
            raise TypeError

        from resources.strings import delivery__revise__text
        self.condition = True
        self.delivery = delivery
        self.file_list = delivery.file_list
        self.display_text = delivery__revise__text
    
    def completed(self):
        import re
        from utility.user_input import confirmation

        def build_confirmation_text(self):
            from datetime import datetime

            if re.match('[1]', self.user_choice):
                if isinstance(self.delivery.start_time, datetime):
                    self.confirmation_text = self.display_text['start_time'][0]
                elif self.delivery.start_time is None:
                    self.confirmation_text = self.display_text['start_time'][1]
            
            elif re.match('[2]', self.user_choice):
                if isinstance(self.delivery.miles_traveled, float):
                    self.confirmation_text = self.display_text['miles_traveled'][0]
                elif self.delivery.miles_traveled is None:
                    self.confirmation_text = self.display_text['miles_traveled'][1]
            
            elif re.match('[3]', self.user_choice):
                if isinstance(self.delivery.average_speed, int):
                    self.confirmation_text = self.display_text['average_speed'][0]
                elif self.delivery.average_speed is None:
                    self.confirmation_text = self.display_text['average_speed'][1]

            elif re.match('[4]', self.user_choice):
                if isinstance(self.delivery.end_time, datetime):
                    self.confirmation_text = self.display_text['end_time'][0]
                elif self.delivery.end_time is None:
                    self.confirmation_text = self.display_text['end_time'][1]

            elif re.match('[o]', self.user_choice, flags=re.IGNORECASE):
                if len(self.delivery.orders) > 1:
                    self.confirmation_text =\
                        f'{self.display_text["order"][0]}/{self.display_text["order"][2]}'
                elif len(self.delivery.orders) == 1:
                    self.confirmation_text =\
                        f'{self.display_text["order"][1]}/{self.display_text["order"][2]}'
                elif len(self.delivery.orders) == 0:
                    self.confirmation_text = self.display_text['order'][2]

            elif re.match('[e]', self.user_choice, flags=re.IGNORECASE):
                if len(self.delivery.extra_stops) > 1:
                    self.confirmation_text = self.display_text['extra_stop'][0]
                elif len(self.delivery.extra_stops) == 1:
                    self.confirmation_text = self.display_text['extra_stop'][1]

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
                self.prompt +=\
                    f'{self.display_text["order"][0]}/{self.display_text["order"][2]}'
            elif len(self.delivery.orders) == 1:
                self.prompt +=\
                    f'{self.display_text["order"][1]}/{self.display_text["order"][2]}'
            elif len(self.delivery.orders) == 0:
                self.prompt += self.display_text['order'][2]
            
            self.prompt += 'E. '
            if len(self.delivery.extra_stop) >= 1:
                self.prompt += self.display_text['extra_stop']
            
            self.prompt += 'V. ' + self.display_text['view']
            self.prompt += 'B. ' + self.display_text['back']

        def option_selection(self):
            from utility.user_input import match_input

            build_prompt()
            self.user_choice = match_input(self.prompt, '^[1-4oevb]$')
            build_confirmation_text()

        def order_option(self):
            # todo: this is a mess
            if len(self.delivery.orders) == 0:
                from processes.input import order as input_order
                self.delivery.add_order(input_order(self.delivery))

            elif len(self.delivery.orders) == 1:
                # rR = revise order
                # aA = add order
                # bB = back

                from utility.user_input import match_input

                # todo: move prompt to string file
                prompt = 'Please make a selection:\n'\
                        'R. Revise only order\n'\
                        'A. Add order\n'\
                        'B. Go back'
                user_choice = match_input(prompt, '^[rab]$')
                if re.match('[r]', user_choice):
                    # todo: update after writing revise order class
                    pass
                elif re.match('[a]', user_choice):
                    from processes.input import order as input_order
                    self.delivery.add_order(input_order(self.delivery))
                elif re.match('[b]', user_choice):
                    pass

            elif len(self.delivery.orders) > 1:
                # sS = select order
                # aA = add order
                # bB = back

                from utility.user_input import match_input

                # todo: move prompt to string file
                prompt = 'Please make a selection:\n'\
                        'S. Select order to revise\n'\
                        'A. Add order\n'\
                        'B. Go back'
                user_choice = match_input(prompt, '^[sab]$')
                if re.match('[s]', user_choice):
                    from processes.select import Select_Order
                    order_id = Select_Order(self.delivery)
                    # todo: update once revise order is written
                elif re.match('[a]', user_choice):
                    from processes.input import order as input_order
                    self.delivery.add_order(input_order(self.delivery))
                elif re.match('[b]', user_choice):
                    pass

        def result(self):
            from processes.revise import Revise_Delivery

            if re.match('[1]', self.user_choice):
                # todo: update with datetime change class once written
                pass

            elif re.match('[2]', self.user_choice):
                self.delivery.miles_traveled = self.distance()

            elif re.match('[3]', self.user_choice):
                self.delivery.average_speed = self.average_speed()

            elif re.match('[4]', self.user_choice):
                # todo: update with datetime change class once written
                pass

            elif re.match('[o]', self.user_choice, flags=re.IGNORECASE):
                self.order_option()

            elif re.match('[e]', self.user_choice, flags=re.IGNORECASE):
                self.extra_stop_option()

            elif re.match('[v]', self.user_choice, flags=re.IGNORECASE):
                # todo: create view function or class to allow user to view sub parts
                from processes.view import delivery as view_delivery
                print(view_delivery(self.delivery))

            elif re.match('[b]', self.user_choice, flags=re.IGNORECASE):
                self.condition = False
            
            # update file with any changes
            if re.match('[1-4]', self.user_choice):
                from utility.file import write
                write(self.delivery.csv(), self.file_list['info'])
            
        option_selection()
        while not re.match('[vb]', self.user_choice, flags=re.IGNORECASE)\
                and not confirmation(self.confirmation_text):
            option_selection()
        result()
        return self

    def extra_stop_option(self):
        # todo: need to finish writting write delivery revise extra stop option
        # todo: need to write function to select extra stop
        if len(self.delivery.extra_stops) == 1:
            # todo: offer to revise
            pass
        elif len(self.delivery.extra_stops) > 1:
            # todo: offer to select
            pass

    def ongoing(self):
        import re
        from utility.user_input import confirmation

        def build_confirmation_text(self):
            from datetime import datetime

            if re.match('[1]', self.user_choice):
                    self.confirmation_text = self.display_text['start_time'][0]

            elif re.match('[o]', self.user_choice, flags=re.IGNORECASE):
                if len(self.delivery.orders) > 1:
                    self.confirmation_text = self.display_text['order'][0]
                elif len(self.delivery.orders) == 1:
                    self.confirmation_text = self.display_text['order'][1]

            elif re.match('[e]', self.user_choice, flags=re.IGNORECASE):
                if len(self.delivery.extra_stops) > 1:
                    self.confirmation_text = self.display_text['extra_stop'][0]
                elif len(self.delivery.extra_stops) == 1:
                    self.confirmation_text = self.display_text['extra_stop'][1]

        def build_prompt(self):
            from datetime import datetime

            self.prompt = self.display_text['initial']

            self.prompt += f'1. {self.display_text["start_time"][0]}'
            
            self.prompt += 'O. '
            if len(self.delivery.orders) > 1:
                self.prompt += self.display_text['order'][0]
            elif len(self.delivery.orders) == 1:
                self.prompt += self.display_text['order'][1]
            
            self.prompt += 'E. '
            if len(self.delivery.extra_stop) >= 1:
                self.prompt += self.display_text['extra_stop']
            
            self.prompt += 'V. ' + self.display_text['view']
            self.prompt += 'B. ' + self.display_text['back']

        def option_selection(self):
            from utility.user_input import match_input

            self.build_prompt()
            self.user_choice = match_input(self.prompt, '^[1oevb]$')
            self.build_confirmation_text()

        def result(self):
            from processes.revise import Revise_Delivery

            if re.match('[1]', self.user_choice):
                # todo: update with datetime change class once written
                pass

            elif re.match('[o]', self.user_choice, flags=re.IGNORECASE):
                if len(self.delivery.orders) == 1:
                    # todo: update after writing revise order class
                    pass

                elif len(self.delivery.orders) > 1:
                    from processes.select import Select_Order
                    order_id = Select_Order(self.delivery)
                    # todo: add revise order once its written

            elif re.match('[e]', self.user_choice, flags=re.IGNORECASE):
                self.extra_stop_option()

            elif re.match('[v]', self.user_choice, flags=re.IGNORECASE):
                # todo: create view function or class to allow user to view sub parts
                from processes.view import delivery as view_delivery
                print(view_delivery(self.tracking.delivery))

            elif re.match('[b]', self.user_choice, flags=re.IGNORECASE):
                self.condition = False
            
            
        option_selection()
        while not re.match('[vb]', self.user_choice, flags=re.IGNORECASE)\
                and not confirmation(self.confirmation_text):
            option_selection()
        result()
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


