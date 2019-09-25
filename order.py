import os

import utility_function
import input_data


delivery_path = os.path.join(
    'delivery'
)


def order_number():
    return utility_function.write_data(
        path=delivery_path,
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
                path=delivery_path,
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
                path=delivery_path,
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
                    path=delivery_path,
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
                    path=delivery_path,
                    file='tip_type.txt',
                    data='cash'
                )
            elif check_correct == 'n':
                continue
            else:
                print('\nInvalid input...')
        else:
            print('\nInvalid input...')






'''class order:

    def __init__(self, orderNumberFirstHalf, orderNumberLastHalf, tip, tipType, milesTraveled, endTime):
        self.orderNumber = str(orderNumberFirstHalf) + str(orderNumberLastHalf)
        self.tip = tip
        self.tipType = tipType
        self.milesTraveled = milesTraveled
        self.endTime = endTime

    def getOrderNumber(self):
        return int(self.orderNumber)

    def getTip(self):
        return int(self.tip)

    def getMilesTraveled(self):
        return int(self.milesTraveled)

    def saveOrder(self, folder, subfoler, fileName):
        with open(os.path.join(folder, subfoler, fileName), 'w') as orderFile:
            orderFile.write()'''
