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

        else:
            print('\ninvalid input...')


def tipType():
   while True:
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
