import re


def confirmation(data, preced=None, succeed=None):
    """
    data = type that can be converted to a string
    preced, succeed = strings to be displayed respectively around data
    """
    prompt = ''
    if not re.match('^[\n]{1,1}', f'{data}'):
        prompt += '\n'

    if preced and succeed:
        prompt += f'{preced}{data}{succeed}'
    elif preced:
        prompt += f'{preced}{data}'
    elif succeed:
        prompt += f'{data}{succeed}'
    else:
        prompt += f'{data}'

    if prompt[-1] != '\n':
        prompt += '\n'

    prompt += 'Is this correct?\t[Y/N]'

    user_choice = text(prompt, permit='[yYnN]{1,1}')

    if re.match('[yY]{1,1}', user_choice):
        return True
    elif re.match('[nN]{1,1}', user_choice):
        return False
    else:
        # this should never ever occur, but to be safe
        raise ValueError


def decimal(prompt, preced=None, places=None):
    """
    preced = type that can be converted into string | comes before user input
    places = integer | represents the number of decimal places
    """
    error_message = '\nERROR: Please enter a whole or decimal number (base 10)'
    if places and not isinstance(places, int):
        raise TypeError('places value must be type integer')

    while True:
        try:
            user_input = float(preceded_input(prompt, preced))
        except ValueError:
            print(error_message)
            continue
        else:
            if places:
                return round(user_input, places)
            else:
                return user_input


def integer(prompt, preced=None):
    """
    preced = type that can be converted into string | comes before user input
    """
    error_message = '\nERROR: Please enter a whole number (base 10)'
    while True:
        try:
            user_input = int(preceded_input(prompt, preced))
        except ValueError:
            print(error_message)
            continue
        else:
            return user_input


def text(prompt, preced=None, alpha_only=False, forbid=None, permit=None):
    """
    preced = type that can be converted into string | comes before user input
    alpha_only = True | only accepts alpha characters and no symbols or spaces
    forbid = list/tuple containing strings of a character | to not accept, or\n
    forbid = regex | what not to accept\n
    permit = list/tuple with strings of character | only accept from user or\n
    permit = regex | what to only accept from user
    """
    error = '\nERROR: '
    message1 = 'Please enter something'
    message2 = 'Please enter text characters\n(Not numbers)'
    message3 = 'Please enter text characters\n(Not symbols or spaces)'

    # todo: probably need to make a custom regex class for getting the search
    #       characters as well as getting and building the regex
    message4 = f'These characters are not allowed: {forbid}'
    message5 = f'Please only use any of these characters: {permit}'
    while True:
        user_input = preceded_input(prompt, preced)
        if not user_input or user_input.isspace():
            print(f'{error}{message1}')
            continue

        for character in user_input:
            # check there is no numbers in user input
            if character.isdigit():
                print(f'{error}{message2}')
                break

            # when alpha is switched on, make sure user only enters alpha chars
            if alpha_only and not character.isalpha():
                print(f'{error}{message3}')
                break

            # check for forbidden characters in user input
            if isinstance(forbid, list or tuple) and character in forbid:
                print(f'{error}{message4}')
                break
            elif isinstance(forbid, str) and re.match(forbid, character):
                print(f'{error}{message4}')
                break
            elif forbid:
                raise TypeError('parameter forbid must be a string or list/tuple')

            # check that user has entered only permitted characters
            if isinstance(permit, list or tuple) and character not in permit:
                print(f'{error}{message5}')
                break
            elif isinstance(permit, str) and not re.match(permit, character):
                print(f'{error}{message5}')
                break
            elif isinstance(permit, list or tuple) and character in permit:
                pass
            elif isinstance(permit, str) and re.match(permit, character):
                pass
            elif permit:
                raise TypeError('parameter permit must be a string or list/tuple')
        else:
            break
    return user_input


def match_input(prompt, pattern):
    import re
    user_input = input(prompt)
    while not re.match(pattern, user_input, flags=re.IGNORECASE):
        user_input = input(prompt)
    else:
        return user_input


def preceded_input(prompt, preced=None):
    if not re.match('^[\n]$', prompt):
        prompt = f'\n{prompt}'
    if prompt[-1] != '\n':
        prompt += '\n'

    print(prompt, end='')

    if preced:
        return input(f'{preced}')
    return input()


class User_Input():
    def __init__(self, prompt):
        self.prompt = prompt

    # general
    def miles_traveled(self):
        from resources.strings import User_Input__miles_traveled__succeed as\
            succeed
        miles_traveled = decimal(self.prompt)
        while not confirmation(miles_traveled, succeed=succeed):
            miles_traveled = decimal(self.prompt)
        return miles_traveled

    def money(self, succeed=None):
        money = decimal(self.prompt, '$', 2)
        if isinstance(succeed, str):
            while not confirmation(money, '$', succeed=succeed):
                money = decimal(self.prompt, '$', 2)
        elif not succeed:
            while not confirmation(money, '$'):
                money = decimal(self.prompt, '$', 2)
        elif succeed:
            raise TypeError('succeed must be able to be converted to string')

        return money

    # shift
    def fuel_economy(self):
        from resources.strings import User_Input__fuel_economy__succeed as\
            succeed
        fuel_economy = decimal(self.prompt)
        while not confirmation(fuel_economy, succeed=succeed):
            fuel_economy = decimal(self.prompt)

        return fuel_economy
    
    def total_hours(self):
        from resources.strings import User_Input__total_hours__succeed as\
            succeed
        total_hours = decimal(self.prompt)
        while not confirmation(total_hours, succeed=succeed):
            total_hours = decimal(self.prompt)
        
        return total_hours

    # delivery
    def average_speed(self):
        from resources.strings import User_Input__average_speed__succeed as\
            succeed
        average_speed = integer(self.prompt)
        while not confirmation(average_speed, succeed=succeed):
            average_speed = integer(self.prompt)
        return average_speed

    # order
    def id(self):
        id = integer(self.prompt, '#')
        while not confirmation(id, 'Id is #'):
            id = integer(self.prompt, '#')
        return id


    # tip
    def card_tip(self):
        from resources.strings import User_Input__card_tip__succeed as succeed
        return self.money(succeed)

    def cash_tip(self):
        from resources.strings import User_Input__cash_tip__succeed as succeed
        return self.money(succeed)

    def unknown_tip(self):
        from resources.strings import User_Input__unknown_tip__succeed as\
            succeed
        return self.money(succeed)

    # extra stop
    def location(self):
        location = text(self.prompt)
        while not confirmation(location):
            location = text(self.prompt)

        return location

    def reason(self):
        reason = text(self.prompt)
        while not confirmation(reason):
            reason = text(self.prompt)

        return reason
