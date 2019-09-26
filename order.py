import os

import utility_function
import input_data


def order_number():
    return utility_function.write_data(
        path='delivery',
        file='order_number.txt',
        data=utility_function.begin_order_number('number')
             + str(input_data.input_data(
                 prompt1='\nEnter order number:    '
                         + utility_function.begin_order_number('number') + '###\n'
                         + utility_function.begin_order_number('number'),
                 input_type1=int,
                 prompt2='\nIs this correct? [y/n]\n',
                 input_type2=str,
                 option_yes='y',
                 option_no='n',
                 symbol=utility_function.begin_order_number('number')
             )
        )
    )


def tip():
    while True:
        tip_option = input_data.input_data(
            prompt1='\nDid they tip?    [y/n]\n',
            input_type1=str,
            prompt2='\nIs this correct?    [y/n]\n',
            input_type2=str,
            option_yes='y',
            option_no='n'
        )
        if tip_option == 'y':
            return utility_function.write_data(
                path='delivery',
                file='tip.txt',
                data=input_data.input_data(
                    prompt1='\nEnter tip amount:    $#.##\n',
                    input_type1 = float,
                    prompt2='\nIs this correct?    [y/n]\n',
                    input_type2= str,
                    option_yes='y',
                    option_no='n',
                    symbol='$'
                )
            )
            break
        elif tip_option == 'n':
            return utility_function.write_data(
                path='delivery',
                file='tip.txt',
                data='n/a'
            )
            break
        else:
            print('\nInvalid input...')


def tip_type():
    while True:
        tip_type_option = input_data.get_input(
           prompt='\nType of tip?'
                  '\n1 for card '
                  '| 2 for cash\n',
           kind=int
        )
        if tip_type_option == 1:
            print('\nCard')
            check_correct = input_data.get_input(
               prompt='\nIs this correct?    [y/n]\n',
               kind=str
            )
            if check_correct == 'y':
                return utility_function.write_data(
                    path='delivery',
                    file='tip_type.txt',
                    data='card'
                )
            elif check_correct == 'n':
                continue
            else:
                print('\nInvalid input...')

        elif tip_type_option == 2:
            print('\nCash')
            check_correct = input_data.get_input(
               prompt='\nIs this correct?    [y/n]\n',
               kind=str
            )
            if check_correct == 'y':
                return utility_function.write_data(
                    path='delivery',
                    file='tip_type.txt',
                    data='cash'
                )
            elif check_correct == 'n':
                continue
            else:
                print('\nInvalid input...')
        else:
            print('\nInvalid input...')


def get_order_data(path, file):
    order_data = utility_function.read_data(
        path=path,
        file=file
    )
    return order_data.split(',')


class Order:

    def __init__(self,
                 order_number='n/a',
                 tip='n/a', tip_type='n/a',
                 miles_traveled='n/a',
                 order_end_time='n/a'
                 ):
        self.order_number = order_number
        self.tip = tip
        self.tip_type = tip_type
        self.miles_traveled = miles_traveled
        self.order_end_time = order_end_time
