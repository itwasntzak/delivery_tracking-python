
class Tip:
    def __init__(self, card=0.0, cash=0.0, unknown=0.0):
        try:
            self.card = float(card)
            self.cash = float(cash)
            self.unknown = float(unknown)
        except ValueError:
            print("ERROR:\tUse a number value for tip amounts.")
        
        if card != 0.0:
            self.has_card = True
        else:
            self.has_card = False

        if cash != 0.0:
            self.has_cash = True
        else:
            self.has_cash = False

        if unknown != 0.0:
            self.has_unknown = True
        else:
            self.has_unknown = False

    def csv(self):
        return f'{self.card},{self.cash},{self.unknown}'
    
    def total_amount(self):
        return self.card + self.cash + self.unknown

    def view(self):
        view_parts = {}

        if self.has_card:
            view_parts['card'] = f'Card tip amount:\t${self.card}'
        if self.has_cash:
            view_parts['cash'] = f'Cash tip amount:\t${self.cash}'
        if self.has_unknown:
            view_parts['unknown'] = f'Unknown tip amount:\t${self.unknown}'

        return view_parts
