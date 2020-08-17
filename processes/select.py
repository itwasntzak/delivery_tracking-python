
class Select_Delivery(shift):
    def __init__(self, shift):
        from objects.shift import Shift
        if not isinstance(shift, Shift):
            raise TypeError

        from utility.user_input import confirmation

        self.shift = shift
        self.option_selection()
        while not confirmation(f'Delivery #{self.user_choice}'):
            self.option_selection()
    
    def build_prompt(self):
        from resources.strings import delivery__select

        self.prompt = delivery__select['initial'].format(len(shift.deliveries))
        for delivery in self.shift.deliveries:
            self.prompt += f'Delivery #{delivery.id}\n'
            self.prompt += f"\t{', '.join(delivery.orders)}\n"
        self.prompt += delivery__select['prompt']

    def option_selection(self):
        from utility.user_input import match_input

        pattern = '^[\dbB]$'
        self.build_prompt()
        self.user_choice = match_input(self.prompt, pattern)
        while not (self.user_choice - 1) in self.shift.delivery_id\
                or not self.user_choice in ('b', 'B'):
            self.build_prompt()
            self.user_choice = match_input(self.prompt, pattern)
    
    def get_id(self):
        return self.user_choice - 1


class Select_Order:
    def __init__(self, delivery):
        from objects.delivery import Delivery
        if not isinstance(delivery, Delivery):
            raise TypeError

        from resources.strings import order__select
        from utility.user_input import confirmation

        self.text = order__select
        self.delivery = delivery
        self.option_selection()
        while not confirmation(self.user_choice, self.text['confrimation']):
            self.option_selection()

    def build_prompt(self):
        self.prompt = self.text['initial']
        self.prompt += f"{'\n'.join(self.delivery.orders)}\n"
        self.prompt += self.text['prompt'][0]

    def match_check(self):
        if not self.user_choice in self.delivery.order_ids:
            print(self.text['no_match'])
            return False

        return True

    def option_selection(self):
        from utility.user_input import match_input

        pattern = '^[\db]$'
        self.build_prompt()
        self.user_choice = match_input(self.prompt, pattern)
        while not self.match_check() or not self.user_choice in ('b', 'B'):
            self.build_prompt()
            self.user_choice = match_input(self.prompt, pattern)
    
    def get_index(self):
        index = 0
        for id in self.delivery.order_ids:
            if self.user_choice is id:
                return index
            
            index += 1


class Quick_Select_Order:
    def __init__(self, shift):
        from objects.shift import Shift
        if not isinstance(shift, Shift):
            raise TypeError

        from resources.strings import order__select
        from utility.user_input import confirmation

        self.text = order__select
        self.shift = shift
        self.option_selection()
        while not confirmation(self.user_choice, self.text['confrimation']):
            self.option_selection()

    def get_ids(self):
        for delivery in self.shift.deliveries:
            index = 0
            for id in delivery.order_ids:
                if not self.user_choice is id:
                    index += 1

                return [delivery.id, index]

    def match_check(self):
        for delivery in self.shift.deliveries:
            for id in delivery.order_ids:
                if self.user_choice is id:
                    return True

        print(self.text['no_match'])
        return False

    def option_selection(self):
        from utility.user_input import match_input

        pattern = '^[\db]$'
        prompt = self.text['prompt'][1]
        self.user_choice = match_input(prompt, pattern)
        while not match_check() or not self.user_choice in ('b', 'B'):
            self.user_choice = match_input(prompt, pattern)


class Select_Carry_Out_Tip:
    def __init__(self, shift):
        from objects.shift import Shift
        if not isinstance(shift, Shift):
            raise TypeError

        from resources.strings import carry_out_tip__select

        if len(shift.carry_out_tips) < 0:
            from utility.user_input import confirmation

            self.shift = shift
            self.text = carry_out_tip__select
            self.option_selection()
            while not self.user_choice in ('b', 'B') and\
                    not confirmation(self.user_choice, self.text['confirmation']):
                self.option_selection()

        else:
            print(carry_out_tip__select['no_option'])
        
    def build_prompt(self):
        self.prompt = self.text['initial']

        count = 1
        for tip in self.shift.carry_out_tips:
            self.prompt += f'\t{count}. '
            
            if tip.has_card and tip.has_cash:
                self.prompt += f'Card: ${tip.card}, Cash: ${tip.cash}\n'
            elif tip.has_card:
                self.prompt += f'Card: ${tip.card}\n'
            elif tip.has_cash:
                self.prompt += f'Cash: ${tip.cash}\n'
            
            count += 1
    
    def get_index(self):
        return self.user_choice - 1
    
    def match_check(self):
        count = len(self.shift.carry_out_tips) + 1
        if not self.user_choice in range(count):
            return False
        return True
    
    def option_selection(self):
        from utility.user_input import match_input

        pattern = '^[\db]$'
        self.build_prompt()
        self.user_choice = match_input(self.prompt, prompt)
        while not self.match_check() or not self.user_choice in ('b', 'B'):
            self.user_choice = match_input(self.prompt, prompt)


class Select_Extra_Stop:
    def __init__(self, parent):
        from objects.shift import Shift
        from objects.delivery import Delivery
        if not isinstance(parent, (Shift, Delivery)):
            raise TypeError

        from resources.strings import extra_stop__select

        if len(parent.extra_stops) < 0:
            from utility.user_input import confirmation

            self.parent = parent
            self.text = extra_stop__select

            self.option_selection()
            while not self.user_choice in ('b', 'B') or\
                    not confirmation(self.user_choice):
                self.option_selection()
        
        else:
            if isinstance(parent, Shift):
                parent_type = 'shift'
            elif isinstance(parent, Delivery):
                parent_type = 'delivery'

            print(extra_stop__select['no_option'].format(parent_type))
    
    def build_prompt(self):
        self.prompt = self.text['initial']
        for extra_stop in self.parent.extra_stops:
            self.prompt += self.text['display'].format(extra_stop.id, extra_stop.location)
        self.prompt += self.text['prompt']
    
    def get_index(self):
        if self.user_choice in self.parent.extra_stop_ids:
            return self.parent.extra_stop_ids.index(self.user_choice)
    
    def option_selection(self):
        from utility.user_input import match_input

        pattern = '^[\db]$'
        self.build_prompt()
        self.user_choice = match_input(self.prompt, pattern)
        while not self.user_choice in self.parent.extra_stop_ids\
                or not self.user_choice in ('b', 'B'):
            self.user_choice = match_input(self.prompt, pattern)
