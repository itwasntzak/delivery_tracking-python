def input_data(prompt1, input_type1, prompt2, input_type2, option_yes, option_no, symbol=''):
    while True:
        try:
            data = get_data(prompt=prompt1, kind=input_type1)
            while True:
                try:
                    data2 = get_data(prompt='\n' + symbol + str(data) + prompt2, kind=input_type2)
                except ValueError:
                    print('\nInvalid input...')
                    continue

                if data2 == option_yes:
                    return data
                elif data2 == option_no:
                    break
                else:
                    print('\nInvalid input...')
        except TypeError:
            print('\nInvalid input...')
        except ValueError:
            print('\nInvalid input...')


def get_data(prompt, kind):
    data = input(prompt)
    if kind == str and (data.isalpha() or ' ' in data or ',' in data or '&' in data or '_' in data):
        return str(data)
    elif kind == int and data.isdecimal():
        return int(data)
    elif kind == float and (data.isdecimal() or '.' in data):
        try:
            return float(data)
        except ValueError:
            pass
    raise ValueError('Invalid input...')


#test = input_data(
#    prompt1='\nEnter the tip amount: $#.##\n$', input_type1=float,
#    prompt2='\nIs this correct? [y/n]\n', input_type2=str, option_yes='y', option_no='n', symbol='$')

#test2 = input_data(
#    prompt1='\nName of extra stop:\n', input_type1=str,
#    prompt2='\nIs this correct?\n1 for yes | 2 for no\n', input_type2=int, option_yes=1, option_no=2)






## would like if depending on the intended input type
##     it will return 'needs to be string' or 'need to be a number'

## if possible to not have a newline before prompt1 the first pass of the function
##     only having a newline before the prompt1 if its coming from an invalid input