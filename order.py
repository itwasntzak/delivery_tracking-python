import os

import main
import utilFunc

def order():
   return [orderNumb(), [tip(), utilFunc.milesTrav(), utilFunc.now()]]


def orderNumb():
   while True:
      print('\nenter order number:    ' + utilFunc.beginOrdNumb('whatIs') + '###')
      try:
         orderNumb = int(input())
         return int(utilFunc.beginOrdNumb('whatIs') + str(orderNumb))

      except ValueError:
         print('\ninvalid input...')


def tip():
   while True:
      print('\ndid they tip?\n1 for yes | 2 for no')
      try:
         tipOption = int(input())
         if tipOption == 1:
            while True:
               print('\nenter tip amount: #.##')
               try:
                  tipAmount = float(input())
                  return [tipAmount, tipType()]

               except ValueError:
                  print('\ninvalid input...')

         elif tipOption == 2:
            return 'N/A'

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
            return 'card'

         elif tipTypeOption == 2:
            return 'cash'

      except ValueError:
         print('\ninvalid input...')

      else:
         print('\ninvalid input...')
