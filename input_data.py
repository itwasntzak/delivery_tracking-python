

def input_data(prompt_1, input_type_1,
               prompt_2, input_type_2,
               option_1, option_2,
               symbol='', word=''):
    while True:
        data = get_input(
            prompt=prompt_1, kind=input_type_1)
        while True:
            data_2 = get_input(
                prompt=f'\n{symbol}{data}{word}\n'
                       f'{prompt_2}\n',
                kind=input_type_2)
            if data_2 in option_1:
                return data
            elif data_2 in option_2:
                break
            else:
                print('\nInvalid input...')


def get_input(prompt, kind):
    while True:
        try:
            data = input(prompt)
            if kind == str and (data.isalpha()
                                or ' ' in data or ',' in data
                                or '&' in data or '_' in data):
                return str(data)
            elif kind == int and data.isdecimal():
                return int(data)
            elif kind == float and (data.isdecimal() or '.' in data):
                return float(data)
        except TypeError:
            print('\nInvalid input...')
        except ValueError:
            print('\nInvalid input...')
        else:
            print('\nInvalid input...')



# would like if depending on the intended input type
#     it will return 'needs to be string' or 'need to be a number'

# if possible to not have a newline before prompt1 the first pass of the function
#     only having a newline before the prompt1 if its coming from an invalid input
