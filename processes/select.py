
class Select_Delivery:
    def __init__(self, shift, test=False):
        from objects import Shift
        if not isinstance(shift, Shift):
            raise TypeError

        self.shift = shift

        if test is False:
            self.main()

    def build_prompt(self):
        from resources.strings import delivery__select

        initial = delivery__select['initial'].format(len(self.shift.deliveries))
        self.prompt = f'\n{initial}\n'
        for delivery in self.shift.deliveries:
            self.prompt += f'Delivery #{delivery.id + 1}\n'
            order_id_strings = [str(id) for id in delivery.order_ids]
            self.prompt += f"\tOrder I.D.'s: {', '.join(order_id_strings)}\n"
        self.prompt += f"\n{delivery__select['prompt']}\n"

    def get_index(self):
        if self.user_selection.lower() != 'b':
            return int(self.user_selection) - 1

    def main(self):
        from utility.user_input import confirm

        self.user_choice()
        while self.user_selection.lower() != 'b' and\
                not confirm(f'Delivery #{self.user_selection}'):
            self.user_choice()

    def match_check(self):
        if type(self.user_selection) is str:
            if self.user_selection in ('b', 'B'):
                return True
        elif (self.user_selection - 1) in self.shift.delivery_ids:
            return True
        else:
            return False

    def user_choice(self):
        from utility.user_input import check_match, user_input

        self.build_prompt()
        self.user_selection = user_input(self.prompt)
        while not check_match(r'[\d]|^[b]$', self.user_selection)\
                and not self.match_check():
            self.user_selection = user_input(self.prompt)


class Select_Order:
    def __init__(self, delivery, test=False):
        from objects import Delivery
        if not isinstance(delivery, Delivery):
            raise TypeError

        from resources.strings import order__select

        self.text = order__select
        self.delivery = delivery

        if test is False:
            self.confirm()

    def build_prompt(self):
        self.prompt = '\n' + self.text['initial']
        order_id_string = [str(id) for id in self.delivery.order_ids]
        self.prompt += '\n'.join(order_id_string)
        if self.prompt[-1] != '\n':
            self.prompt += '\n'
        self.prompt += self.text['prompt'][0]

    def confirm(self):
        from utility.user_input import confirm

        self.user_choice()
        while not confirm(self.user_choice, self.text['confrimation']):
            self.user_choice()
    
    def get_index(self):
        if not self.user_choice in ('b', 'B'):
            return self.delivery.order_ids.index(self.user_choice)

    def match_check(self):
        if type(self.user_choice) is str:
            if self.user_choice in ('b', 'B'):
                return True
        elif self.user_choice in self.delivery.order_ids:
            return True
        else:
            return False

    def user_choice(self):
        from utility.user_input import check_match, user_input

        self.build_prompt()
        self.user_choice = user_input(self.prompt)
        while not check_match(r'[\d]|^[b]$', self.user_choice)\
                and not self.match_check():
            self.user_choice = user_input(self.prompt)


class Quick_Select_Order:
    def __init__(self, shift, test=False):
        from objects import Shift
        if not isinstance(shift, Shift):
            raise TypeError

        from resources.strings import order__select

        self.text = order__select
        self.shift = shift

        if test is False:
            self.confirm()
    
    def confirm(self):
        from utility.user_input import confirm

        self.user_choice()
        while not confirm(self.user_choice, self.text['confrimation']):
            self.user_choice()

    def get_delivery_id(self):
        for delivery in self.shift.deliveries:
                for id in delivery.order_ids:
                    if self.user_choice is id:
                        return delivery.id
    
    def get_order_index(self):
        for delivery in self.shift.deliveries:
                for id in delivery.order_ids:
                    if self.user_choice is id:
                        return delivery.order_ids.index(self.user_choice)

    def match_check(self):
        if self.user_choice in ('b', 'B'):
            return True
        else:
            for delivery in self.shift.deliveries:
                for id in delivery.order_ids:
                    if self.user_choice is id:
                        return True

        return False

    def user_choice(self):
        from utility.user_input import check_match, user_input

        pattern = r'[\d]|^[b]$'
        prompt = self.text['prompt'][1]
        self.user_choice = user_input(prompt, pattern)
        while not check_match(pattern, self.user_choice)\
                and not self.match_check():
            self.user_choice = user_input(prompt, pattern)


class Select_Carry_Out_Tip:
    def __init__(self, shift, test=False):
        from objects import Shift
        if not isinstance(shift, Shift):
            raise TypeError

        from resources.strings import carry_out_tip__select

        self.shift = shift
        self.text = carry_out_tip__select

        if test is False:
            if len(shift.carry_out_tips) > 0:
                self.main()
            else:
                print(carry_out_tip__select['no_option'])
        
    def build_prompt(self):
        from utility.utility import to_money

        self.prompt = f"\n{self.text['initial']}\n"

        count = 1
        for tip in self.shift.carry_out_tips:
            self.prompt += f'\t{count}. '
            
            if tip.has_card and tip.has_cash:
                self.prompt +=\
                    f'Card: ${to_money(tip.card)}, Cash: ${to_money(tip.cash)}\n'
            elif tip.has_card:
                self.prompt += f'Card: ${to_money(tip.card)}\n'
            elif tip.has_cash:
                self.prompt += f'Cash: ${to_money(tip.cash)}\n'
            
            count += 1
        
        self.prompt += f"\n{self.text['prompt']}\n"

    def main(self):
        from utility.user_input import confirm

        self.user_choice()
        while self.user_selection.lower() != 'b' and not\
                confirm(self.text['confirmation'].format(self.user_selection)):
            self.user_choice()

    def get_index(self):
        if self.user_selection.lower() != 'b':
            return int(self.user_selection) - 1
    
    def match_check(self):
        if self.user_selection.lower() == 'b':
            return True
        elif (int(self.user_selection) - 1) in\
                range(len(self.shift.carry_out_tips)):
            return True

        return False
    
    def user_choice(self):
        from utility.user_input import check_match, user_input

        self.build_prompt()
        self.user_selection = user_input(self.prompt)
        while not check_match(r'[\d]|^[b]$', self.user_selection)\
                and not self.match_check():
            self.user_selection = user_input(self.prompt)


class Select_Extra_Stop:
    def __init__(self, parent, test=False):
        from objects import Shift
        from objects import Delivery
        if not isinstance(parent, (Shift, Delivery)):
            raise TypeError

        from resources.strings import extra_stop__select

        self.parent = parent
        self.text = extra_stop__select

        if test is False:
            if len(parent.extra_stops) > 0:
                self.main()
            else:
                if isinstance(parent, Shift):
                    parent_type = 'shift'
                elif isinstance(parent, Delivery):
                    parent_type = 'delivery'

                print(extra_stop__select['no_option'].format(parent_type))
    
    def build_prompt(self):
        self.prompt = f"\n{self.text['initial']}\n"

        count = 1
        for extra_stop in self.parent.extra_stops:
            self.prompt +=\
                self.text['display'].format(count, extra_stop.location) + '\n'
            count += 1
        self.prompt += f"\n{self.text['prompt']}\n"

    def get_index(self):
        if self.user_selection.lower() != 'b':
            return int(self.user_selection) - 1

    def main(self):
        from utility.user_input import confirm

        self.user_choice()
        while self.user_selection.lower() != 'b' and\
                not confirm(self.user_selection):
            self.user_choice()

    def match_check(self):
        if type(self.user_selection) is str:
            if self.user_selection.lower() == 'b':
                return True
        elif (int(self.user_selection) - 1) in\
                range(len(self.parent.extra_stop_ids)):
            return True
        
        return False

    def user_choice(self):
        from utility.user_input import check_match, user_input

        pattern = r'[\d]|^[b]$'
        self.build_prompt()
        self.user_selection = user_input(self.prompt)
        while not check_match(pattern, self.user_selection)\
                and not self.match_check():
            self.user_selection = user_input(self.prompt)
