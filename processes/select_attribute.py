
class Delivery:
    # todo: probably need to have two different attribute selection classes for delivery, completed & in progress
    '''
    first program will display the current data for the delivery
    then it will ask the user to select a piece of data they want to change
    if the data already exists it will simply allow the user to input the data
    if the data is missing it and the user still selects to change it, ask for confirmation to add missing data
    if the delivery is still in progress distance and miles trav should be unavailable options
    '''

    def __init__(self, shift, delivery):
        import re
        from resources.strings import delivery__select_attribute__prompt as\
            prompt
        from utility.user_input import confirmation, match_input

        self.shift = shift
        self.delivery = delivery

        self.build_prompt()

        self.option_selection()
        if not re.match('[vVbBqQ]{1,1}', self.user_choice):
            while not confirmation(self.confirmation_text):
                self.option_selection()

        self.result()
    
    def option_selection(self):
        import re
        from datetime import datetime

        self.user_choice = match_input(self.prompt, '[1234vVsSbBqQ]{1,1}')

        # todo: have to figure out how to allow user to add missing data if any is blank

        if re.match('[1]{1,1}', self.user_choice) and\
                isinstance(self.delivery.start_time, datetime):
            confirmation_text = 'Revise start time'
        elif re.match('[1]{1,1}', self.user_choice):
            confirmation_text = 'There is no start time recorded for this delivery'

        if re.match('[2]{1,1}', self.user_choice) and\
                isinstance(self.delivery.miles_traveled, float):
            confirmation_text = 'Revise miles traveled'
        elif re.match('[2]{1,1}', self.user_choice):
            confirmation_text = 'There is no miles traveled recorded for this delivery'

        if re.match('[3]{1,1}', self.user_choice) and\
                isinstance(self.delivery.average_speed, int):
            confirmation_text = 'Revise average speed'
        elif re.match('[3]{1,1}', self.user_choice):
            confirmation_text = 'There is no average speed recorded for this delivery'

        if re.match('[4]{1,1}', self.user_choice) and\
                isinstance(self.delivery.end_time, datetime):
            confirmation_text = 'Revise end time'
        elif re.match('[4]{1,1}', self.user_choice):
            confirmation_text = 'There is no end time recorded for this delivery'

        if re.match('[sS]{1,1}', self.user_choice):
            confirmation_text = f"Save delivery #{self.delivery.id}'s current state"

    def result(self):
        # todo: to handle uncompleted delivery, tell user if data isnt avilable to change
        import re
        from datetime import datetime

        if re.match('[1]{1,1}', self.user_choice)\
                and isinstance(self.delivery.start_time, datetime):
            # print current value, then ask user if they are sure they want to change it
            pass
        elif re.match('[2]{1,1}', self.user_choice)\
                and isinstance(self.delivery.miles_traveled, float):
            pass
        elif re.match('[3]{1,1}', self.user_choice):
            pass
        elif re.match('[4]{1,1}', self.user_choice):
            pass
        elif re.match('[vV]{1,1}', self.user_choice):
            pass
        elif re.match('[sS]{1,1}', self.user_choice):
            pass
        elif re.match('[bB]{1,1}', self.user_choice):
            pass
        elif re.match('[qQ]{1,1}', self.user_choice):
            pass

        return self
