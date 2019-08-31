<<<<<<< HEAD
import os

import utilFunc

def orderNumb():
    while True:
        print('\nenter order number:    ' + utilFunc.beginOrdNumb('number') + '###\n' + utilFunc.beginOrdNumb('number'), end='')
        try:
            orderNumb = int(input())

            areYouSure = utilFunc.areYouSure(utilFunc.beginOrdNumb('number') + str(orderNumb))

            if areYouSure == True:
                utilFunc.writeData("deliveryTracking", "delivery", utilFunc.beginOrdNumb('number') + str(orderNumb) + "OrderNumb.txt", utilFunc.beginOrdNumb('number') + str(orderNumb))

                return utilFunc.beginOrdNumb('number') + str(orderNumb)

            elif areYouSure == False:
                continue

        except ValueError:
            print('\ninvalid input...')

def tip(orderNumber):
    while True:
        print('\ntip?\n1 for yes | 2 for no')
        try:
            tipOption = int(input())

            if tipOption == 1:
                    print('\nenter tip amount: $#.##')
                    try:
                        tipAmount = float(input())

                        areYouSure = utilFunc.areYouSure('$' + str(tipAmount))

                        if areYouSure == True:
                            utilFunc.writeData("deliveryTracking", "delivery", str(orderNumber) + "Tip.txt", [tipAmount, tipType()])
                            break

                        elif areYouSure == False:
                            continue

                    except ValueError:
                        print('\ninvalid input...')

            elif tipOption == 2:
                utilFunc.writeData("deliveryTracking", "delivery", str(orderNumber) + "Tip.txt", '"N/A"')
                break

        except ValueError:
            print('\ninvalid input...')

=======
import util_func
import input_data


def order_number():
    order_number = input_data.input_data(
        prompt1='\nEnter order number:    '
                + util_func.begin_order_number('number')
                + '###\n' + util_func.begin_order_number('number'),
        input_type1=int,
        prompt2='\nIs this correct? [y/n]\n',
        input_type2=str,
        option_yes='y',
        option_no='n',
        symbol=util_func.begin_order_number('number')
    )
    full_order_number = util_func.begin_order_number('number') + str(order_number)
    util_func.write_data(
        path='delivery',
        file=full_order_number
             + "_order_number.txt",
        data=full_order_number
    )
    return full_order_number


def tip(var_path):
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
            util_func.write_data(
                path='delivery',
                file=str(var_path) + '_tip.txt',
                data=[
                    input_data.input_data(
                        prompt1='\nenter tip amount: $#.##\n',
                        input_type1 = float,
                        prompt2='\nIs this correct?    [y/n]\n',
                        input_type2= str,
                        option_yes='y',
                        option_no='n',
                        symbol='$'
                    ),
                    tip_type()
                ]
            )
            break
        elif tip_option == 'n':
            util_func.write_data(
                path='delivery',
                file=str(var_path) + '_tip.txt',
                data="'N/A'")
            break
>>>>>>> master
        else:
            print('\nInvalid input...')


def tip_type():
   while True:
<<<<<<< HEAD
      print('\ntype of tip:\n1 for card, 2 for cash')
      try:
         tipTypeOption = int(input())
         if tipTypeOption == 1:
            return "card"

         elif tipTypeOption == 2:
            return "cash"

      except ValueError:
         print('\ninvalid input...')

      else:
         print('\ninvalid input...')
=======
       tip_type_option = input_data.get_input(
           prompt='\nType of tip?'
                  '\n1 for card '
                  '| 2 for cash\n',
           kind=int
       )
       if tip_type_option == 1:
           print('Card')
           check_correct = input_data.get_input(
               prompt='\nIs this correct?    [y/n]\n',
               kind=str
           )
           if check_correct == 'y':
               return 'card'
           elif check_correct == 'n':
               continue
           else:
               print('\nInvalid input...')
       elif tip_type_option == 2:
           print('Cash')
           check_correct = input_data.get_input(
               prompt='\nIs this correct?    [y/n]\n',
               kind=str
           )
           if check_correct == 'y':
               return 'cash'
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
>>>>>>> master
