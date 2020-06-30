

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


class Delivery_Menu:
    '''
    todo: think there should be a check before completing delivery if any
          orders have been entered. ask user if they really want to end
          delivery without order, or if they want to delete the order
    '''
    # todo: add an options menu option to let user edit data for the delivery
    def __init__(self, shift):
        from objects.shift import Shift
        if not isinstance(shift, Shift):
            raise TypeError

        from processes.input_data import start_delivery
        from utility.user_input import confirmation

        self.shift = shift
        self.shift.delivery_menu_condition = True
        self.delivery = start_delivery(self.shift)

        self.option_selection()
        while not confirmation(self.display_text):
            self.option_selection()

        self.result()

    def option_selection(self):
        import re
        from resources.strings import delivery__prompt as prompt
        from utility.user_input import text
        # todo: need to add build_prompt that makes a prompted based on if things have started
        self.user_choice = text(prompt, permit='[oOeEcCtTqQ]{1,1}')

        if re.match('[oO]{1,1}', self.user_choice):
            self.display_text = 'Enter a new order'
        elif re.match('[eE]{1,1}', self.user_choice):
            self.display_text = 'Take an extra stop'
        elif re.match('[cC]{1,1}', self.user_choice):
            self.display_text = 'Complete this delivery'
        elif re.match('[tT]{1,1}', self.user_choice):
            self.display_text = 'View current time since start of delivery'
        elif re.match('[qQ]{1,1}', self.user_choice):
            self.display_text = 'Quit the program'

    def return_shift(self):
        return self.shift

    def result(self):
        import re

        if re.match('[oO]{1,1}', self.user_choice):
            from processes.input_data import order
            self.delivery.add_order(order(self.delivery))

        elif re.match('[eE]{1,1}', self.user_choice):
            from processes.input_data import delivery_extra_stop as extra_stop
            self.delivery.add_extra_stop(extra_stop(self.delivery))

        elif re.match('[cC]{1,1}', self.user_choice):
            from processes.input_data import end_delivery
            self.shift.add_delivery(end_delivery(self.delivery))
            self.shift.delivery_menu_condition = False

        elif re.match('[tT]{1,1}', self.user_choice):
            # todo: need to write a display text for time taken in delivery menu
            from utility.utility import now, time_taken
            time_taken(self.delivery.start_time, now(), 'time taken:')

        elif re.match('[qQ]{1,1}', self.user_choice):
            self.shift.delivery_menu_condition = False
            self.shift.shift_menu_condition = False


class Shift_Menu:
    def __init__(self, shift):
        from objects.shift import Shift
        if not isinstance(shift, Shift):
            raise TypeError(f'{type(shift)}')

        from utility.user_input import confirmation

        self.shift = shift
        self.shift.shift_menu_condition = True

        self.build_prompt()
        self.option_selection()
        while not confirmation(self.display_text):
            self.build_prompt()
            self.option_selection()

        self.result()

    def build_prompt(self):
        from objects.delivery import Delivery
        from objects.extra_stop import Extra_Stop
        from os import path
        from resources.strings import shift__prompts as prompts

        self.prompt = prompts['initial']

        if not path.exists(Delivery(self.shift).file_list()['directory']):
            self.prompt += prompts['delivery'][0]
        else:
            self.prompt += prompts['delivery'][1]

        if not path.exists(Extra_Stop(self.shift, 0).file_list()['directory']):
            self.prompt += prompts['extra_stop'][0]
        else:
            self.prompt += prompts['extra_stop'][1]

        self.prompt += prompts['carry_out_tip']
        self.prompt += prompts['split']

        if not path.exists(self.shift.file_list()['end_time']):
            self.prompt += prompts['end'][0]
        else:
            self.prompt += prompts['end'][1]

        self.prompt += prompts['info']
        self.prompt += prompts['quit']

        return self

    def option_selection(self):
        import re
        from utility.user_input import text

        self.user_choice = text(self.prompt, permit='[dDeEcCsSxXiIqQ]{1,1}')

        if re.match('[dD]{1,1}', self.user_choice):
            # todo: add assessment to desplay start or continue
            self.display_text = 'Start/continue delivery'
        elif re.match('[eE]{1,1}', self.user_choice):
            self.display_text = 'Start/continue extra stop'
        elif re.match('[cC]{1,1}', self.user_choice):
            self.display_text = 'Input carry out tip'
        elif re.match('[sS]{1,1}', self.user_choice):
            self.display_text = 'Start a split'
        elif re.match('[xX]{1,1}', self.user_choice):
            self.display_text = 'End shift'
        elif re.match('[iI]{1,1}', self.user_choice):
            self.display_text = 'Check shift info'
        elif re.match('[qQ]{1,1}', self.user_choice):
            self.display_text = 'Quit the program'

        return self

    def return_shift(self):
        return self.shift

    def result(self):
        import re

        if re.match('[dD]{1,1}', self.user_choice):
            delivery_menu = Delivery_Menu(self.shift)
            self.shift = delivery_menu.return_shift()
            while self.shift.delivery_menu_condition:
                delivery_menu = Delivery_Menu(self.shift)
                self.shift = delivery_menu.return_shift()

        elif re.match('[eE]{1,1}', self.user_choice):
            from processes.input_data import shift_extra_stop as\
                input_extra_stop
            self.shift.add_extra_stop(input_extra_stop(self.shift))

        elif re.match('[cC]{1,1}', self.user_choice):
            from processes.input_data import tip as input_tip
            from utility.file import save
            tip = input_tip()
            self.shift.add_carry_out_tip(tip)
            save(tip.csv(), self.shift.file_list()['carry_out_tips'],
                 separator='\n')

        elif re.match('[sS]{1,1}', self.user_choice):
            from processes.input_data import start_split
            self.shift = start_split(self.shift)
            self.shift.shift_menu_condition = False

        elif re.match('[xX]{1,1}', self.user_choice):
            from processes.input_data import end_shift
            self.shift = end_shift(self.shift)
            self.shift.shift_menu_condition = False

        elif re.match('[iI]{1,1}', self.user_choice):
            # todo: add method call once written
            print(self.shift.start_time)
            print(self.shift.delivery_ids)
            print(self.shift.deliveries)
            for delivery_id in self.shift.delivery_ids:
                print(delivery_id)
                print(self.shift.deliveries[delivery_id].order_ids)
                print(self.shift.deliveries[delivery_id].orders)
                for index in range(len(self.shift.deliveries[delivery_id].order_ids)):
                    print(self.shift.deliveries[delivery_id].orders[index])
                    print(self.shift.deliveries[delivery_id].orders[index].id)
                    print(self.shift.deliveries[delivery_id].orders[index].tip.csv())
                    print(self.shift.deliveries[delivery_id].orders[index].miles_traveled)
                    print(self.shift.deliveries[delivery_id].orders[index].end_time)

        elif re.match('[qQ]{1,1}', self.user_choice):
            self.shift.shift_menu_condition = False

        return self


def edit_order(order):
    import re
    from utility.user_input import confirmation

    def attribute_selection():
        from resources.strings import Order__change_data__prompt as prompt
        from utility.user_input import text

        user_choice = text(prompt, permit='[iItTmMeEvVsSqQbB]{1,1}')

        if re.match('[iI]{1,1}', user_choice):
            confirm_text = 'Change order id'
        elif re.match('[tT]{1,1}', user_choice):
            confirm_text = 'Change the tip'
        elif re.match('[mM]{1,1}', user_choice):
            confirm_text = 'Change miles traveled'
        elif re.match('[eE]{1,1}', user_choice):
            confirm_text = 'Change end time'
        elif re.match('[vV]{1,1}', user_choice):
            confirm_text = 'View order info'
        elif re.match('[sS]{1,1}', user_choice):
            confirm_text = 'Save any changes'
        elif re.match('[qQ]{1,1}', user_choice):
            confirm_text = 'Quit without saving'
        elif re.match('[bB]{1,1}', user_choice):
            confirm_text = 'Go back to delivery'

        return user_choice, confirm_text

    user_choice, confirm_text = attribute_selection()
    while not confirmation(confirm_text):
        user_choice, confirm_text = attribute_selection()
    else:
        from processes.change_data import order as order_edit
        return order_edit(order, user_choice)
