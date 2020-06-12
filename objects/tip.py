
class Tip:
    card = 0.0
    cash = 0.0
    unknown = 0.0
    has_card = False
    has_cash = False
    has_unknown = False

    def __init__(self, card=0.0, cash=0.0, unknown=0.0):
        try:
            if card != 0.0:
                self.has_card = True
                self.card = float(card)

            if cash != 0.0:
                self.has_cash = True
                self.cash = float(cash)

            if unknown != 0.0:
                self.has_unknown = True
                self.unknown = float(unknown)
        except ValueError:
            print("ERROR:\tUse a number value for tip amounts.")

    def csv(self):
        return f'{self.card},{self.cash},{self.unknown}'

    def has_both(self):
        if self.has_card and self.has_cash:
            return True
        else:
            return False

    def view(self):
        display_text = ''
        if self.has_card:
            display_text += f'Card tip amount:\t${self.card}\n'
        if self.has_cash:
            display_text += f'Cash tip amount:\t${self.cash}\n'
        if self.has_unknown:
            display_text += f'Unknown tip amount:\t${self.unknown}\n'
        return display_text
