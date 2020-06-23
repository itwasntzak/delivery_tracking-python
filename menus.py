

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


def delivery(delivery):
    # todo: this is next need todo to get everything back to functional
    import re
    from utility.user_input import text
    # todo: need to move this prompt to resources
    prompt = 'Please select an option:\n'\
             'O. Add new order\n'\
             'E. Take extra stop\n'\
             'T. View current time since start of delivery\n'\
             'Q. To quit the program'
    user_choice = text(prompt, permit='[oOeEtTqQ]{1,1}')

    if re.match('[oO]{1,1}', user_choice):
        from processes.input_data import order
        delivery.add_order(order(delivery))

    elif re.match('[eE]{1,1}', user_choice):
        from processes.input_data import delivery_extra_stop as extra_stop
        delivery.add_extra_stop(extra_stop(delivery))

    elif re.match('[tT]{1,1}', user_choice):
        # todo: need to write a display text for time taken in delivery menu
        from utility.utility import now, time_taken
        time_taken(delivery.start_time, now(), )

    elif re.match('[qQ]{1,1}', user_choice):
        pass


def daily_tracking(shift):
    import re
    from utility.user_input import confirmation, text

    def build_prompt(shift):
        from objects.delivery import Delivery
        from objects.extra_stop import Extra_Stop
        from os import path
        from resources.strings import daily_tracking__prompts as prompts

        prompt = prompts['initial']

        delivery = Delivery(shift)
        if not path.exists(delivery.file_list()['directory']):
            prompt += prompts['delivery'][0]
        else:
            prompt += prompts['delivery'][1]

        extra_stop = Extra_Stop(shift)
        if not path.exists(extra_stop.file_list()['directory']):
            prompt += prompts['extra_stop'][0]
        else:
            prompt += prompts['extra_stop'][1]

        prompt += prompts['carry_out_tip']
        prompt += prompts['split']

        if not path.exists(shift.file_list()['end_time']):
            prompt += prompts['end'][0]
        else:
            prompt += prompts['end'][1]

        prompt += prompts['info']
        prompt += prompts['quit']

        return prompt

    def option_selection(prompt):
        user_choice = text(prompt, permit='[dDeEcCsSxXiIqQ]{1,1}')

        if re.match('[dD]{1,1}', user_choice):
            data = 'Start/continue delivery'
        elif re.match('[eE]{1,1}', user_choice):
            data = 'Start/continue extra stop'
        elif re.match('[cC]{1,1}', user_choice):
            data = 'Input carry out tip'
        elif re.match('[sS]{1,1}', user_choice):
            data = 'Start a split'
        elif re.match('[xX]{1,1}', user_choice):
            data = 'End shift'
        elif re.match('[iI]{1,1}', user_choice):
            data = 'Check shift info'
        elif re.match('[qQ]{1,1}', user_choice):
            data = 'Quit the program'

        return user_choice, data

    prompt = build_prompt(shift)

    user_choice, data = option_selection(prompt)
    while not confirmation(data):
        user_choice, data = option_selection(prompt)
    else:
        if re.match('[dD]{1,1}', user_choice):
            from processes.input_data import delivery as input_delivery
            shift.add_delivery(input_delivery(shift))

        elif re.match('[eE]{1,1}', user_choice):
            from processes.input_data import shift_extra_stop as\
                input_extra_stop
            shift.add_extra_stop(input_extra_stop(shift))

        elif re.match('[cC]{1,1}', user_choice):
            from processes.input_data import tip as input_tip
            from utility.file import save
            tip = input_tip()
            shift.add_carry_out_tip(tip)
            save(tip.csv(), shift.file_list()['carry_out_tips'],
                 separator='\n')

        elif re.match('[sS]{1,1}', user_choice):
            from processes.input_data import start_split
            shift.split = start_split(shift)
            return shift, False

        elif re.match('[xX]{1,1}', user_choice):
            from processes.input_data import end_shift
            shift = end_shift(shift)
            return shift, False

        elif re.match('[iI]{1,1}', user_choice):
            # todo: add method call once written
            pass

        elif re.match('[qQ]{1,1}', user_choice):
            return shift, False

        return shift, True


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
