
class Select_Delivery:
    def __init__(self, shift, test=False):
        from objects import Shift
        if not isinstance(shift, Shift):
            raise TypeError

        self.shift = shift

        if test is False:
            self.confirm()

    def build_prompt(self):
        from resources.strings import delivery__select

        self.prompt = delivery__select['initial'].format(len(self.shift.deliveries))
        for delivery in shift.deliveries:
            self.prompt += f'Delivery #{delivery.id + 1}\n'
            self.prompt += f"\t{', '.join(delivery.orders)}\n"
        self.prompt += delivery__select['prompt']

    def confirm(self):
        self.user_choice()
        while not confirmation(f'Delivery #{self.user_choice}'):
            self.user_choice()

    def get_index(self):
        if not self.user_choice in ('b', 'B'):
            return self.user_choice - 1

    def match_check(self):
        if not (self.user_choice - 1) in self.shift.delivery_id\
                or not user_choice in ('b', 'B'):
            return False

        return True

    def user_choice(self):
        from utility.user_input import match_input
        pattern = '^[\db]$'
        self.build_prompt()
        self.user_choice = match_input(self.prompt, pattern)
        while not self.match_check():
            self.user_choice = match_input(self.prompt, pattern)


class Select_Order:
    def __init__(self, delivery, test=False):
        from objects import Delivery
        if not isinstance(delivery, Delivery):
            raise TypeError

        from resources.strings import order__select
        from utility.user_input import confirmation

        self.text = order__select
        self.delivery = delivery

        if test is False:
            self.confirm()

    def build_prompt(self):
        self.prompt = self.text['initial']
        self.prompt += '\n'.join(self.delivery.orders)
        self.prompt += self.text['prompt'][0]

    def confirm(self):
        self.user_choice()
        while not confirmation(self.user_choice, self.text['confrimation']):
            self.user_choice()
    
    def get_index(self):
        if not self.user_choice in ('b', 'B'):
            return self.delivery.order_ids.index(self.user_choice)

    def match_check(self):
        if not self.user_choice in self.delivery.order_ids\
                or not self.user_choice in ('b', 'B'):
            print(self.text['no_match'])
            return False

        return True

    def user_choice(self):
        from utility.user_input import match_input

        pattern = '^[\db]$'
        self.build_prompt()
        self.user_choice = match_input(self.prompt, pattern)
        while not self.match_check():
            self.user_choice = match_input(self.prompt, pattern)


class Quick_Select_Order:
    def __init__(self, shift, test=False):
        from objects import Shift
        if not isinstance(shift, Shift):
            raise TypeError

        from resources.strings import order__select
        from utility.user_input import confirmation

        self.text = order__select
        self.shift = shift

        if test is False:
            self.confirm()
    
    def confirm(self):
        self.user_choice()
        while not confirmation(self.user_choice, self.text['confrimation']):
            self.user_choice()

    def get_delivery_id(self):
        for delivery in self.shift.deliveries:
                for id in delivery.order_ids:
                    if self.user_choice is id:
                        return delivery.id
    
    def get_order_id(self):
        for delivery in self.shift.deliveries:
                for id in delivery.order_ids:
                    if self.user_choice is id:
                        return id

    def match_check(self):
        if self.user_choice in ('b', 'B'):
            return True
        else:
            for delivery in self.shift.deliveries:
                for id in delivery.order_ids:
                    if self.user_choice is id:
                        return True

            print(self.text['no_match'])
            return False

    def user_choice(self):
        from utility.user_input import match_input

        pattern = '^[\db]$'
        prompt = self.text['prompt'][1]
        self.user_choice = match_input(prompt, pattern)
        while not match_check():
            self.user_choice = match_input(prompt, pattern)


class Select_Carry_Out_Tip:
    def __init__(self, shift):
        from objects import Shift
        if not isinstance(shift, Shift):
            raise TypeError

        from resources.strings import carry_out_tip__select
        from utility.user_input import confirmation

        self.shift = shift
        self.text = carry_out_tip__select

        if test is False:
            if len(shift.carry_out_tips) < 0:
                self.confirm()
            else:
                if test is False:
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

    def confirm(self):
        self.user_choice()
        while not self.user_choice in ('b', 'B') and\
                not confirmation(self.user_choice, self.text['confirmation']):
            self.user_choice()

    def get_index(self):
        if not self.user_choice in ('b', 'B'):
            return self.user_choice - 1
    
    def match_check(self):
        if not self.user_choice in range(len(self.shift.carry_out_tips))\
                or not self.user_choice in ('b', 'B'):
            return False

        return True
    
    def user_choice(self):
        from utility.user_input import match_input

        pattern = '^[\db]$'
        self.build_prompt()
        self.user_choice = match_input(self.prompt, prompt)
        while not self.match_check():
            self.user_choice = match_input(self.prompt, prompt)


class Select_Extra_Stop:
    def __init__(self, parent, test=False):
        from objects import Shift
        from objects import Delivery
        if not isinstance(parent, (Shift, Delivery)):
            raise TypeError

        from resources.strings import extra_stop__select
        from utility.user_input import confirmation

        self.parent = parent
        self.text = extra_stop__select

        if test is False:
            if len(parent.extra_stops) < 0:
                self.confirm()
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
    
    def confirm(self):
        self.user_choice()
        while not self.user_choice in ('b', 'B') or\
                not confirmation(self.user_choice):
            self.user_choice()

    def get_index(self):
        if not self.user_choice in ('b', 'B'):
            return self.parent.extra_stop_ids.index(self.user_choice)

    def match_check(self):
        if not self.user_choice in self.parent.extra_stop_ids\
                or not self.user_choice in ('b', 'B'):
            return False
        
        return True

    def user_choice(self):
        from utility.user_input import match_input

        pattern = '^[\db]$'
        self.build_prompt()
        self.user_choice = match_input(self.prompt, pattern)
        while self.match_check():
            self.user_choice = match_input(self.prompt, pattern)
