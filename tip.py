from os import path

# from file import append, write
# from input_data import input_data


class Tip:
    # list of attributes
    card = 0.0
    cash = 0.0
    unknown = 0.0
    has_card = False
    has_cash = False
    has_unknown = False
    # list of file names
    tip_file = 'tip.txt'
    carry_out_tips_file = 'carry_out_tips.txt'

    def __init__(self, card=card, cash=cash, unknown=unknown):
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

    def has_both(self):
        if self.has_card and self.has_cash:
            return True
        else:
            return False

    # def input_card(self):
        # self.card = input_data(
            # '\nEnter card tip amount:\t$#.##\n(0 for no tip)\n', float,
            # 'Is this correct?\t[y/n]', str,
            # ('y', 'Y'), ('n', 'N'), '$', ' card tip')
        # if self.card != 0.0:
            # self.has_card = True
        # return self

    # def input_cash(self):
        # self.cash = input_data(
            # '\nEnter cash tip amount:\t$#.##\n(0 for no tip)\n', float,
            # 'Is this correct?\t[y/n]', str,
            # ('y', 'Y'), ('n', 'N'), '$', ' cash tip')
        # if self.cash != 0.0:
            # self.has_cash = True
        # return self

    # def input_split(self):
        # self.input_card()
        # self.input_cash()
        # return self

    # def input_unknown(self):
        # self.unknown = input_data(
            # '\nEnter unknown type tip amount:\t$#.##\n(0 for no tip)\n', float,
            # 'Is this correct?\t[y/n]', str,
            # ('y', 'Y'), ('n', 'N'), '$', ' unknown tip type')
        # if self.unknown != 0.0:
            # self.has_unknown = True
        # return self

    # def save(self, file_path):
        # if path.exists(file_path):
            # append(file_path, f'\n{self.string()}')
        # else:
            # write(file_path, f'{self.string()}')

    # utility methods
    def string(self):
        return f'{self.card},{self.cash},{self.unknown}'
