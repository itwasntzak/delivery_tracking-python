

def input_data(prompt1, input_type1,
               prompt2, input_type2,
               option_yes, option_no,
               symbol=''):
    while True:
        data = get_input(
            prompt=prompt1, kind=input_type1)
        while True:
            data2 = get_input(
                prompt='\n' + symbol + str(data) + prompt2,
                kind=input_type2
            )
            if data2 == option_yes:
                return data
            elif data2 == option_no:
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
